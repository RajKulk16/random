from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    #  'get_requirements' takes a string parameter called file_path and returns a list of strings.
    '''
    This function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #every package is next line in requirements.txt ='\n'
        #readlines will read '\n' as an object and add it to requrirements.txt
        #Therefore, have to replace '\n' with blank.
        requirements = [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements



setup(
    name='random',
    version='0.0.1',
    author='Raj Kulkarni',
    author_email='rsk132302@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']
)