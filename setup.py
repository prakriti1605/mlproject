from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''this will return a list of requirements. 
        why are we doing this?
        Because we want only one source of '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="churnproject",
    version="0.0.1",
    author="prakriti",
    author_email="prakritijain1205@gmail.com",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires= get_requirements("requirements.txt")
)

# install_requires=[
#         "pandas",
#         "numpy",
#         "scikit-learn",
#         "dill",
#         "xgboost",
#         "Flask",
#         "gunicorn",
#         "seaborn",
#     ], pahle ye likh rahe thay 