import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="text_summarizer"

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/components/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml", 
    "params.yaml", 
    "app.py",
    "main.py",
    "Dockerfile", 
    "requirements.txt", 
    "setup.py", 
    "research/trials.ipynb"

]

for i in list_files:
    i = Path(i)
    dir,file = os.path.split(i)
    if dir != "":
        os.makedirs(dir,exist_ok=True)
        logging.info(f'creating directory:{dir} for file {file}')

    if (not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open(i,'w') as f:
            pass 
            logging.info(f'Creating empty file:{i}')
    else:
        logging.info(f'{file} already exists')


