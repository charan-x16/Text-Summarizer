import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__version__ = "69.5.1"



REPO_NAME = "Text-Summarization-project"
AUTHOR_USER_NAME = "charan-x16"
SRC_REPO = "textsummarizer" 
AUTHOR_EMAIL = "chsricharan2003@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small pyhton package for NLP app",
    long_description=long_description,
    long_description_content='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
)