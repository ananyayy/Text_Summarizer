from text_summarizer.config.configuration import ConfigManager 
from text_summarizer.components.data_validation import validation
from text_summarizer.logging import logger 

class dataValPipeline:
    def __init__(self):
        pass
    try:
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_ingestion = validation(config=data_validation_config)
        data_ingestion.validate_allFiles()

    except Exception as e:
        raise e 