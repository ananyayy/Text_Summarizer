import os 
from box.exceptions import BoxValueError
import yaml 
from text_summarizer.logging import logger
from ensure import ensure_annotations 
from box import ConfigBox 
from pathlib import Path 
from typing import Any 

#this module is used to read yaml files, create directories and get file size
#this includes functions that would be common for all modules and need to be reused 

@ensure_annotations 
# ensure annotations help verfiy that the values passed to a function are 
#according to the preset data types 

def read_yaml(path_to_yaml:Path) :
    #read yaml files 
    try:
        with open(path_to_yaml) as yfl:
            con = yaml.safe_load(yfl)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(con)

    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e 

@ensure_annotations  
def create_directories(path_to_dir:list, verbose=True):
    #create directories 
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at:{path}')

@ensure_annotations
def get_size(path:Path)-> str:
    #returns size of a file in KB
    size = round(os.path.getsize(path)/1024)
    return f'~ {size} KB'
