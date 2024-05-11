from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f">>>>>> satge {STAGE_NAME} Started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage{STAGE_NAME} completes <<<<<<\n\n x===========x")
except Exception as e:
    logger.exception(e)
    raise e