import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from pathlib import Path
from TextSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def dowload_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headres =  request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} descargar! con la siguiente informaicon: \n{headres}")
        else:
            logger.info(f"Archivo ya existe, de size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """ 
        zip_file_path: str
        Devuelve el zip hacia el data directorie
        funcion no devuelve nada

        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile( self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)





