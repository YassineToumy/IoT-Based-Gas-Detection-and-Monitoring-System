# IoT-Based Gas Detection System

## Overview
Gas leaks pose significant safety risks, and early detection can prevent potential hazards. This project develops an IoT-based gas detection system that uses an Arduino, a gas sensor, and a Flask server to monitor and alert in real-time. The system sends sensor data to a Python Flask server via Wi-Fi, displaying it on a web interface for immediate action.

## Features
- Real-time monitoring of gas levels.
- Automatic data transmission to a Python Flask server.
- Web-based interface to display gas sensor data.
- Immediate alerts for potential gas leaks.

## Components
- **Arduino**: The central microcontroller that reads data from the gas sensor and sends it to the server.
- **Gas Sensor**: Detects the presence of harmful gases and provides real-time data to the Arduino.
- **Buzzer & LED**: Alerts the user in case of a gas leak by sound and light signals.
- **Wi-Fi Module**: Allows the Arduino to communicate with the Python Flask server over the internet.
- **Python Flask Server**: Receives data from the Arduino and displays it on a web interface.
- **Breadboard & Jumper Wires**: For setting up the sensor and other components.

## Setup Instructions

### 1. Hardware Setup
- Connect the gas sensor to the Arduino following the manufacturer's instructions.
- Connect the buzzer and LED to the Arduino to provide alerts when a gas leak is detected.
- Use the Wi-Fi module (e.g., ESP8266) to enable the Arduino to send data to the server.

### 2. Software Setup
- **Arduino IDE**: Install the Arduino IDE and necessary libraries for your gas sensor and Wi-Fi module.
- **Python Flask Server**:
  - Install Python and Flask:
    ```bash
    pip install flask
    ```
  - Clone this repository:
    ```bash
    git clone https://github.com/yourusername/gas-detection-system.git
    ```
  - Navigate to the project directory and run the Flask server:
    ```bash
    python app.py
    ```

### 3. Arduino Code
Upload the code to your Arduino that will:
- Read gas sensor data.
- Send the data over Wi-Fi to the Python Flask server.

### 4. Web Interface
- The server will host a simple web page showing real-time data from the gas sensor.
- Open your browser and go to `http://localhost:5000` to view the data.

## Code Structure

- **app.py**: Main Flask application handling incoming data and displaying it on the web interface.
- **static/**: Contains static assets like CSS and JavaScript for the web interface.
- **templates/**: HTML files that define the structure of the web interface.
- **arduino/**: Contains the Arduino code for setting up the gas sensor and communication with the server.

## Usage
Once the system is set up:
1. The Arduino reads data from the gas sensor and sends it to the Flask server via Wi-Fi.
2. The Flask server processes the data and updates the web interface in real-time.
3. In case of a gas leak, the system activates the buzzer and LED, providing immediate alerts.

## Contributing
Feel free to fork this repository and make improvements or contributions. For any issues or suggestions, please open an issue.
