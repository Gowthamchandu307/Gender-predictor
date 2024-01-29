import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gender-predictor", 
    version="1.0.0",
    author="Gowtham chandu",
    author_email="gowthamchandu307@gmail.com",
    description="A python package used to predict gender of a firstname of a person by the help of LSTM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gowthamchandu307",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.7',
)
