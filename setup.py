from setuptools import find_packages, setup
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
def get_requirements(file_path: str):
    requirements = []
    with open(file_path) as f:
        requirements = f.read().splitlines()
    return requirements


setup(
    name="Geeta_search_engine_project",
    version="0.0.1",
    author="Navneet Kumar",
    author_email="navneetgautam920@gmail.com",  # Change this
    description="Bhagavad Gita Semantic Search Engine using TF-IDF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/search_engine_project",  # Change this
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/search_engine_project/issues",
        "Source Code": "https://github.com/yourusername/search_engine_project",
    },
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.9",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    include_package_data=True,
    zip_safe=False,
)