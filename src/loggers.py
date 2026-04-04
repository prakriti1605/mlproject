import logging
import os
from datetime import datetime
#making a logs folder 
#first gave the path and then used makedirs fucntion 
#exists_ok = true means avoid crash if folder already exists
log_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(log_folder, exist_ok=True)

#create unique log file
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(log_folder, log_file)


# golbal setup of logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
"""1st param: logs go to file not console 
"""

if __name__=="__main__":
    logging.info("logging has started")
     