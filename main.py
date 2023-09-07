from text_summarizer.pipeline.step1_D1 import DataIngPipeline
from text_summarizer.pipeline.step2_D2 import dataValPipeline
from text_summarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<')
    data_ingestion = DataIngPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<< \n \n x===x')
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<')
    data_ingestion = dataValPipeline()
    data_validation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<< \n \n x===x')
except Exception as e:
    logger.exception(e)
    raise e 


