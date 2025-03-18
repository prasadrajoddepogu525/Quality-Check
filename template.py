import os
import logging

from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="Quality Check"

list_of_folder=[
    "setup.py",
    "exception.py"
    ".github/workflows/.gitkeep",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "research/research.ipynb",
    "templates/index.html",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity_config.py",
    f"src/{project_name}/constants/__init__.py",

]


for filepath in list_of_folder:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory {filedir} for the file name {filename}")

    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating empty file {filepath}")

    else:
        logging.info(f"{filename} already exsist")
        