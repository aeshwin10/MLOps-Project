import logging
import os
from datetime import datetime

# Hardcoded path where you want to store logs
project_root = r"E:\Coding_Career\MLOps-Project\MLOPS-Project"

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory
log_dir = 'logs'

# Construct the full logs path
logs_path = os.path.join(project_root, log_dir)

# Ensure that the log directory exists
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
log_file_path = os.path.join(logs_path, LOG_FILE)

# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler(log_file_path)
console_handler = logging.StreamHandler()

# Set levels for handlers
file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log an example message
logger.info("Logging setup is complete.")
