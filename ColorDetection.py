import serial
import time
import requests
import json
from datetime import datetime

# Initialize serial communication with Arduino
ser = serial.Serial('COM11', 9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize
ser.flush()  # Clear the serial buffer

# Power BI streaming dataset URL (replace with your own URL)
power_bi_url = "https://api.powerbi.com/beta/c7b00d7f-ad99-442a-b12f-c2c912044fdc/datasets/c6f0ff2b-d19b-4785-9dc0-fc58d48f82c6/rows?experience=power-bi&key=woth8pZpJgrbtVhd620WjgHlWVxV1iLWUQ9BEp9NfsaTMjLWH2mePOn97iEF5NfDSOsdQWBvgt%2F8MCL9YrzK4w%3D%3D"

def send_to_power_bi(red, green, blue):
    """Send RGB data with timestamp to Power BI using REST API"""
    try:
        payload = json.dumps([{
            "Red": int(red),
            "Green": int(green),
            "Blue": int(blue),
            "Timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }])
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(power_bi_url, data=payload, headers=headers)
        
        if response.status_code == 200:
            print(f"Successfully sent RGB data to Power BI: R={red}, G={green}, B={blue}")
        else:
            print(f"Failed to send data: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error in sending data to Power BI: {e}")

while True:
    try:
        # Read raw bytes from the Arduino
        raw_data = ser.readline()
        print(f"Raw data: {raw_data}")  # Print raw bytes to see what is received
        
        # Attempt to decode
        try:
            decoded_data = raw_data.decode('utf-8').strip()
            print(f"Decoded data: {decoded_data}")

            # Process the decoded data only if decoding is successful
            if decoded_data:
                try:
                    red_value = int(decoded_data.split('|')[0].split(':')[1].strip())
                    green_value = int(decoded_data.split('|')[1].split(':')[1].strip())
                    blue_value = int(decoded_data.split('|')[2].split(':')[1].strip())
                    print(f"Red: {red_value}, Green: {green_value}, Blue: {blue_value}")
                    send_to_power_bi(red_value, green_value, blue_value)
                except Exception as e:
                    print(f"Error in parsing RGB values: {e}")

        except UnicodeDecodeError as e:
            print(f"Decoding error: {e}")

        time.sleep(1)  # Small delay before reading the next data
    except KeyboardInterrupt:
        print("Exiting program...")
        ser.close()
        break
