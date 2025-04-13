# GPS Based Toll Collection System

A smart, automated toll collection system using GPS and IoT technologies designed to enhance road transportation infrastructure in India. This project minimizes congestion, increases efficiency, and improves the accuracy and security of toll collection through geo-fencing and real-time vehicle tracking.

## 🚀 Project Overview

The system utilizes GPS to determine the location of a vehicle and automatically deducts the toll amount from the user's account based on geofencing of toll plazas. It aims to replace the manual and semi-automatic systems currently in place, such as FASTag, by offering a more efficient and scalable solution using embedded systems and real-time communication technologies.

## 📌 Features

- 📍 **GPS-Based Tracking**: Detects vehicle presence within geofenced toll areas.
- 💳 **Automatic Toll Deduction**: Charges users based on the actual distance traveled.
- ⚙️ **IoT Integration**: Uses GSM/GPRS for real-time data transmission to the server.
- 🔐 **Secure & Accurate**: Reduces human error, fraud, and toll evasion.
- 🚦 **Reduced Traffic Congestion**: No stopping at toll booths.
- 📈 **Real-Time Monitoring**: Authorities can track usage patterns and collect insights.

## 📷 System Components

- **On-Board Unit** (NodeMCU + GPS + Accelerometer)
- **Power Supply** (Battery + Power Circuit)
- **Central Web Server** (Data receiver & dashboard)
- **Geo-fenced Toll Zones** (Defined by latitude/longitude)

## 🛠️ Technologies Used

### Hardware
- **NodeMCU (ESP8266/ESP32)**
- **GPS Module** (e.g., NEO-6M)
- **Accelerometer Sensor** (e.g., MPU6050)
- **Power Circuit & Battery**

### Software
- **Arduino IDE** (for firmware development)
- **Embedded C/C++** (microcontroller code)
- **HTML/CSS/JavaScript** (web dashboard)
- **GSM/GPRS Library** (for IoT data transmission)
- **Web Server** (e.g., Node.js or Python Flask)

## 📖 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/gps-toll-collection.git
   cd gps-toll-collection
Configure and Upload Firmware

2.Open firmware/VehicleOBU.ino in Arduino IDE.
 In the code, set your Wi‑Fi/GPRS credentials and server URL:

 const char* ssid     = "YOUR_SSID";
 const char* password = "YOUR_WIFI_PASSWORD";
 const char* server   = "http://your.server.ip:5000";
 Select the correct board (ESP8266/ESP32) and port, then Upload.

3.Start the Web Server
Navigate to the web-dashboard folder:
cd web-dashboard
Using Python:
python3 -m http.server 8000
Open http://localhost:8000 in your browser.
#how to setup flask
Link:https://flask.palletsprojects.com/en/stable/

4.Power the On-Board Unit
 Connect the battery/power circuit to the NodeMCU and sensors.
 Ensure the GPS module has a clear view of the sky to achieve satellite lock.

5.Test the System
 Drive the vehicle into a geofenced toll zone.
 Monitor the web dashboard to see entry/exit logs and real-time account deductions.

👨‍💻 Contributors
-Revanthesh C (20CS068)
-S Kushal (20CS069)
-Tushar P Raj TG (20CS090)
-Mithun Gupta H M (20CS121)

🏫 Institution
 Sri Siddhartha Institute of Technology, Tumkur, Karnataka
 Under the guidance of Dr. Channakrishnaraju, Dept. of Computer Science & Engineering.

📆 Academic Year
2023–24

For full project details, please refer to the Project Synopsis PDF.
