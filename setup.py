# setup.py

from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    author="Trevor Malone",
    author_email="malonetrevor12@gmail.com",
    description="A package to detect emotions in text using IBM Watson NLP API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tmalone1250",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
