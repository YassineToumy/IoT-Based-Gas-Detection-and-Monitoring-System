from flask import Flask, render_template, request
import serial
from datetime import datetime

app = Flask(__name__)

# Global variable to hold the serial connection
serialcom = None
threshold = 40  # Example threshold for gas level

# Function to initialize serial connection
def init_serial():
    global serialcom
    if serialcom is None or not serialcom.is_open:
        try:
            serialcom = serial.Serial('COM4', 9600, timeout=1)
        except Exception as e:
            print(f"Error opening serial port: {e}")
            return False
    return True

def close_serial():
    global serialcom
    if serialcom is not None:
        serialcom.close()
        serialcom = None

# Function to read gas level from Arduino
def read_gas_level():
    global serialcom
    try:
        if serialcom is not None and serialcom.in_waiting > 0:
            raw_data = serialcom.readline().decode('utf-8', errors='replace').strip()
            print(f"Raw data received: {raw_data}")  # Debugging
            if raw_data.isdigit():
                
                gas_value = int(raw_data)
                if 0 <= gas_value <= 1023:  # Validate range
                    gas_percentage = (gas_value / 1023) * 100
                    print(f"Gas percentage: {gas_percentage}")  # Debugging
                    return gas_percentage
                else:
                    print("Gas value out of range.")  # Debugging
            else:
                print("Invalid data format.")  # Debugging
    except Exception as e:
        print(f"Error reading gas level: {e}")
    return 0


@app.route('/')
def index():
    # Ensure the serial connection is initialized before reading the gas level
    if not init_serial():
        return "Error: Unable to open serial port", 500

    # Read gas level when the page is accessed
    gas_level = read_gas_level()

    # Set status based on the gas level
    status, status_message = ("safe", "Safe") if gas_level <= threshold else ("danger", "Dangerous Gas Levels!")

    # Get the current timestamp for the last updated time
    last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template('iot_projeth.html', gas_level=gas_level, threshold=threshold, 
                           status=status, status_message=status_message, last_updated=last_updated)

@app.route('/manual', methods=['POST'])
def manual_control():
    mode = request.form['mode']
    
    # Initialize the serial connection if it's not already open
    if not init_serial():
        return "Error: Unable to open serial port", 500

    if mode == 'on':
        serialcom.write(b'1')  # Activate buzzer or LED in manual mode
    elif mode == 'off':
        serialcom.write(b'0')  # Deactivate buzzer or LED in manual mode
    
    gas_level = read_gas_level()  # Get the latest gas level
    return render_template('iot_projeth.html', mode=mode, gas_level=gas_level)

@app.route('/auto', methods=['POST'])
def auto_mode():
    # Initialize the serial connection if it's not already open
    if not init_serial():
        return "Error: Unable to open serial port", 500

    serialcom.write(b'a')  # Switch to automatic mode
    
    gas_level = read_gas_level()  # Get the latest gas level
    return render_template('iot_projeth.html', mode='auto', gas_level=gas_level)

@app.route('/shutdown')
def shutdown():
    close_serial()  # Close the serial connection before shutdown
    return 'Server shutting down...'

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        close_serial()  # Ensure the serial connection is closed when the app stops
