import time
import logging
import socket
from datetime import datetime

logging.basicConfig(
    filename='result/internet_connection.log',
    level=logging.INFO,
    format='%(message)s'
)

def check_internet():
    """Check if the system is connected to the internet."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

def log_internet_status():
    """Log the current internet connection status."""
    is_connected = check_internet()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    logging.info(f"{timestamp} - Internet connection: {is_connected}")

if __name__ == "__main__":
    while True:
        log_internet_status()
        time.sleep(600)
