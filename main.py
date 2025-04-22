from sensor.exception import SensorException 
from sensor.logger import logging 
import os 
import sys 

if __name__ == "__main__": 
    try: 
        logging.info("logging and exception file successfully execute...")
        a=1/0
    except Exception as e: 
        raise SensorException(e,sys)