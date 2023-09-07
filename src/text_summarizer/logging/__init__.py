import os 
import sys 
import logging 

#handles all ops with

logging_str= "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"
ldir = "logs"
log_fp = os.path.join(ldir,"running_logs.log")
os.makedirs(ldir,exist_ok=True)

logging.basicConfig(
    #sets level above INFO such as WARNING and so on
    level = logging.INFO,
    #sets log format
    format = logging_str,

    handlers=[
        #writes log msgs to file of given path
        logging.FileHandler(log_fp),

        #writes log messages to console
        logging.StreamHandler(sys.stdout)
    ]
    
)
logger = logging.getLogger("textSummarizer")