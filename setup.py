from setuptools import setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME='housing-predictor'
AUTHOR='Arshad Shaikh'
VERSION='0.0.4'
DESCRIPTION='First ML end-to-end Project'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirement.txt'

def get_requirement_list()->List[str]:
     """"
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
     with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(name=PROJECT_NAME,
      version=VERSION,
      author=AUTHOR,
      description=DESCRIPTION,
      packages=PACKAGES,
      install_requires=get_requirement_list()
      )