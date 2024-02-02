from setuptools import find_packages, setup 
from typing import List

def get_requirements(filepath:str)->List[str]:
    """This function will return the list of requiremnts

    Args:
        filepath (str): filepath

    Returns:
        List[str]: function will returns the list of requirements
    """
    requiremnts =[]
    HYPEN_E_DOT='-e .'
    with open(filepath) as file_obj:
        requiremnts = file_obj.readlines()
        requiremnts = [req.replace('\n','') for req in requiremnts]
        
        if HYPEN_E_DOT in requiremnts:
            requiremnts.remove(HYPEN_E_DOT)
            
    return requiremnts
        
setup(
    name='ML_PROJECT',
    version='0.0.1',
    author='rahul',
    author_email='rrp30998@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)