# Project C VPN

**Project C VPN** is a modern and user-friendly virtual private network (VPN) login system designed for secure and streamlined access. It features a clean, contemporary login interface and simplifies user authentication for VPN connections.

## Features

- Modern, intuitive login interface
- Secure user authentication
- Notifications for connection and disconnection

## Requirements

- **Python**: Ensure Python is installed on your system.
- **Flask**: A lightweight WSGI web application framework for Python.
- **win10toast**: A Python library to show toast notifications on Windows 10.

## Installation

1. **Install Python**:
   Download and install Python from [python.org](https://www.python.org/).

2. **Install Flask**:
   Open Command Prompt and run:
   ```bash
   pip install flask
   ```

3. **Install win10toast**:
   Open Command Prompt and run:
   ```bash
   pip install win10toast
   ```

## Configuration

Edit the `app.py` file to set your default credentials:
```python
EMAIL = "root@gmail.com"
USER_PASSWORD = "admin123"
```

## Running the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/coderip321/Project-C-VPN.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Project C VPN 
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Demo

To demonstrate the project:

1. Open the application in your browser.
2. Use the default email and password:
   - **Email**: `root@gmail.com`
   - **Password**: `admin123`

3. Upon successful login, you will receive a notification indicating that the VPN is connected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
