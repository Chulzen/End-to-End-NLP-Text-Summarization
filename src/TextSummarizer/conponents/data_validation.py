import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self)->bool:
        try:
            validation_satus = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_satus= False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {validation_satus}")
                
                else:
                    validation_satus = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Satatus: {validation_satus}")

            return validation_satus

        except Exception as e:
            raise e