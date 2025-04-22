from setuptools import find_packages , setup 
from typing import List 

def get_requirements()-> List[str]: 
    """ 
    This fuction will return list of requirements
    """ 
    
    requirements_list:List[str]  = [] 
    
    return requirements_list

setup( 
    name="sensor" , 
    author="Prince Raj" , 
    author_email="jarvisraj04@gmail.com" , 
    packages=find_packages() , 
    install_rerequires = get_requirements() ,
    )