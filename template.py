import os 
from pathlib import Path 
import logging 
# logging.baseConfig(Level=logging.INFO, format= '[%(asctime)s]: %(message)s')
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = "cnnClassifier"
list_of_files= [
    ".github/workflows/.gitkeep", # required to perform commit an empty folder on github
    f"src/{project_name}/__init__.py", # constructor file as it this project is a local package. 
    f"src/{project_name}/components/__init__.py", # another constructor file is required as component is a also a local package 
    f"src/{project_name}/utils/__init__.py", # 
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "configuration.py",
    "templates/index.html"
    ]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass 
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")
        