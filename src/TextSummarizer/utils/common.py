#funciones que usaremos en nuestro codigo par apoder utilizarlo

import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox #para poder acceder a los diccionaros de otra manera
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """reads yaml file an returns
    
    Args: 
        path_to_yaml (srtr): path like input

    Raises:
        ValueError if Yaml file is empty
        e: empty file

    Returns:
    ConfigBox ConfigBox Type
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (boll, optional): ignore if multiple dirs is to be created. Defaults to flase
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")

@ensure_annotations
def get_size(path: Path)-> str:
    """path (Path): path of the file

    Returns:
        str: size in KB
    
    """
    size_in_kb = round(os.path.getsize(path/1024))
    return f"~ {size_in_kb} KB"
