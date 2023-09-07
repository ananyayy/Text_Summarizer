from text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml,create_directories 
from text_summarizer.entity import (DataIngestionConfig)

#create configuration manager 
class ConfigManager:
    def  __init__(
         self,
        config_fp= CONFIG_PATH,
        params_fp =  PARAMS_PATH):

        self.config = read_yaml(config_fp)
        self.params = read_yaml(params_fp)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        DI_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL =  config.source_URL,
            local_file= config.local_file,
            unzip_dir= config.unzip_dir
        )
        return DI_config