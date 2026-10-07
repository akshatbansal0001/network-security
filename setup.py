from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """Return the list of requirements from requirements.txt."""
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            for line in file.readlines():
                requirement = line.strip()
                # ignore empty lines, comments, and -e .
                if requirement and not requirement.startswith("#") and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


print(get_requirements())  # temporary test, delete after checking

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Krish Naik",
    author_email="krishnaik06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)