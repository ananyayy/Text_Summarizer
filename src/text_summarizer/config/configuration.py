from text_summarizer.constants import *
from text_summarizer.utils.common import read_yaml,create_directories 
from text_summarizer.entity import (DataIngestionConfig, Datavalidationconfig)


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

#config manager for data_va
class ConfigManager:
    def  __init__(
        self,
        config_fp= CONFIG_PATH,
        params_fp =  PARAMS_PATH):

        self.config = read_yaml(config_fp)
        self.params = read_yaml(params_fp)

        create_directories([self.config.artifacts_root])

    def get_data_validation_config(self)-> Datavalidationconfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        dataValConfig = Datavalidationconfig(
                root_dir= config.root_dir ,
            status_file= config.status_file,
            all_required_files= config.all_required_files, 
        )
        return  dataValConfig