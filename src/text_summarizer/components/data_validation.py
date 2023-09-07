import os 
from text_summarizer.logging import logger 
from text_summarizer.entity import Datavalidationconfig

class validation:
    def __init__(self,config: Datavalidationconfig):
        self.config=config 

    def validate_allFiles(self)->bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in all_files:
                if file not in all_files:
                    validation_status=False
                    with open(self.config.status_file,'w')as f:
                        f.write(f'validation status: {validation_status}')


                else:
                    validation_status = True 
                    with open(self.config.status_file,'w')as f:
                        f.write(f'validation status:{validation_status}')
            return validation_status 
        
        except Exception as e:
            raise e 