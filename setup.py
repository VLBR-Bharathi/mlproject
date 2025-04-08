from setuptools import setup, find_packages
from typing import List

'''
This is the setup file for the ML project.
It contains the package name, version, author information, and a function to read the requirements from a file.
The setup function is called to create the package.
The requirements are read from a file and passed to the setup function.
The package will be created with the specified name, version, author information, and requirements.
'''

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='Ramya',
author_email='mbps2000@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),


)