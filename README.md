#  Smart Energy Consumption Tracker

A Spring Boot-based system to monitor household electricity usage in real-time, detect anomalies and predict future consumption using data analysis.

![Dashboard Preview](https://github.com/user-attachments/assets/12fcc316-71b9-4e74-8e63-4537ee92557c)


## Features

- **Real-time monitoring** of energy/water usage via IoT sensors (MQTT).
- **Anomaly detection** (threshold-based or ML-powered).
- **Predictive analytics** (Linear Regression/LSTM for forecasts).
- **Interactive dashboard** (React.js + Chart.js).
- **Automated alerts** (Email/SMS for abnormal usage).

##  Tech Stack

| Component               | Technology                          |
|-------------------------|-------------------------------------|
| Backend                 | Spring Boot (Java)                  |
| Database                | InfluxDB (Time-series), PostgreSQL  |
| IoT Communication       | MQTT (Eclipse Mosquitto)            |
| Data Analysis           | Python (Pandas, Scikit-learn)       |
| Frontend                | React.js + Chart.js                 |
| Alerts                  | Twilio (SMS), JavaMail (Email)      |
