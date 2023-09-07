#update components 
import os 
from pathlib import Path 
from text_summarizer.entity import DataIngestionConfig
import urllib.request as request 
from text_summarizer.logging import logger 
import zipfile 

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config 
    
    def download_file(self):
        if not os.path.exists(self.config.local_file):
            fname, header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_file
            )
            logger.info(f"{fname} download, with following info: \n {header}")
        else:
            logger.info(f"file already exists")
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_file , 'r') as zipref:
            zipref.extractall(unzip_path)

