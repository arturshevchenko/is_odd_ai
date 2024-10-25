from setuptools import setup, find_packages

setup(
    name="is_odd",
    version="0.1.0",
    description="A simple library to determine if number is odd or odd with power of AI",
    author="Artur Shevchenko",
    author_email="artur.shev8@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "python-dotenv==1.0.1",
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "urllib3==2.2.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
