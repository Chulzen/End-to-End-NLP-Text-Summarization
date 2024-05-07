import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)]:%(messege)s:')


project_name = "TextSummarizer"

list_of_file = [
    ".github/workflows/.gitkeep", #para poder hacer los push de git
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utilis/__init__.py",
    f"src/{project_name}/utilis/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config//__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/consttants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt"
    'setup.py',
    "research/trails.ipynb"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename =os.path.split(filepath) #hace la separacion de del directorio y path que necesitamos

    if filedir != "":#cheqqueamos si efectivamente esta creado el file
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"create directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creatin empty file:{filepath}")

    else:
        logging.info(f"{filename} already exist")

