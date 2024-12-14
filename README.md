# Flask Application with Virtual Android System Simulation

This project is a Flask-based application that integrates backend development, database management, a virtual Android system simulation, and basic networking functionalities.

## Aim and Problem Statement

### Aim
To develop a versatile Flask-based application that simulates a virtual Android system, integrates RESTful backend development, and demonstrates fundamental networking concepts alongside efficient database management.

### Problem Statement
Modern software projects often require the integration of various components like database management, RESTful APIs, simulation environments, and networking to emulate real-world scenarios. This project addresses the challenge of combining these functionalities into a cohesive system, making it a useful learning and development tool for developers.

## Features

### 1. **Database Management**
- Uses **SQLAlchemy** for ORM to manage app data.
- A SQLite database (`apps.db`) is configured.
- A sample app is preloaded into the database during initialization.

### 2. **Backend Development**
- Provides RESTful APIs to manage app data:
  - **Add an App**: `POST /add-app`
  - **Get App Details**: `GET /get-app/<id>`
  - **Delete an App**: `DELETE /delete-app/<id>`
- Renders a simple HTML page at the root route (`/`).

### 3. **Virtual Android System Simulation**
- Simulates an Android device with:
  - Device Model
  - OS Version
  - Memory Details
- Includes functionalities to:
  - Display system information.
  - Simulate app installations.

### 4. **Basic Networking**
- Provides a `/send-data` endpoint to send mock data from the virtual Android system to a mock server using sockets.

## Advantages and Disadvantages

### Advantages
- **Modular Design**: Combines multiple functionalities, making it a useful tool for developers to learn or prototype.
- **Lightweight**: Utilizes SQLite and Flask, making it easy to set up and run locally.
- **Simulation Features**: The virtual Android system provides an educational simulation of real-world devices.
- **Scalable**: The project structure allows for future expansion.

### Disadvantages
- **Limited Simulation**: The virtual Android system lacks advanced features found in actual devices.
- **Single-User Focus**: SQLite database may not scale well for multi-user scenarios.
- **Networking Dependence**: Requires socket setup, which might not work in restricted network environments.
- 
## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Flask-SQLAlchemy
