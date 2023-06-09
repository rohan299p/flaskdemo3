import logging
import time
current_time = time.strftime( "%Y-%m-%d_%H-%M-%S", time.localtime())
log_filename = f"session_{current_time}.txt"
# Configure logging
logging.basicConfig(filename=f'./logs/{log_filename}', level=logging.INFO, format='%(asctime)s - %(message)s')
def log(input,result):
    # Function to log input and return result
    # Log input and result
    logging.info(f"Input: {input},\n Result: {result}")