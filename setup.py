import setuptools

with open('README.md','r',encoding='utf-8')as f:
    long_desc = f.read()

__version__ = "0.0.0"

REPO="Text_Summarizer"
AUTHOR ="ananyayy"
SRC ="text_summarizer"
EMAIL="ananyaa1003@gmail.com"

setuptools.setup(
    name='SRC',
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description='small python package',
    long_description=long_desc,
    long_description_content = 'text/markdown',
    url="https://github.com/{AUTHOR}/{REPO}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR}/{REPO}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
