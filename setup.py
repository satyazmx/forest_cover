import setuptools

__version__ = "0.0.0"
AUTHOR_USER_NAME = "ineuron.ai"

setuptools.setup(
     version=__version__,
     name="forest_cover",
     author=AUTHOR_USER_NAME,
     package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)