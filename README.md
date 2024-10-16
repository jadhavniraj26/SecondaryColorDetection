# Arduino RGB and Secondary Color Detection with TCS3200
This project explores the capabilities of the Arduino Uno Mini and the TCS3200 sensor for detecting and identifying RGB and secondary colors. The TCS3200 sensor measures the intensity of red, green, and blue light, allowing us to determine the color of objects placed in front of it. The system interprets RGB values to identify secondary colors such as yellow, cyan, and magenta by comparing their respective RGB components. For example, yellow is recognized when both red and green values are prominent, while cyan and magenta are identified based on their specific RGB combinations.

Features:
Real-Time Color Detection: The system uses LED indicators to represent detected colors, where:
A single LED (red, green, or blue) lights up for primary colors.
Two LEDs activate for secondary colors, visually mimicking the resulting color combination.
Data Transmission: Detected RGB values are transmitted to Power BI for analysis and visualization. Although the system lacks a direct internet connection, a Python script running on a PC serves as an intermediary to send color data from the Arduino to the Power BI online platform.
Benefits:
Visual Insights: Users can visualize and analyze color data in real-time, enabling deeper insights into the detected colors.
Affordable Setup: This project provides a comprehensive solution for detecting, displaying, and analyzing color information using an accessible and cost-effective setup.
Installation and Usage:
Follow the instructions in the repository to set up the Arduino and TCS3200 sensor, run the Python script, and connect to Power BI for real-time data visualization.
