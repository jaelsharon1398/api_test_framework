from setuptools import setup, find_packages

setup(
    name="api_test_framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "requests>=2.28.0",
        "pyyaml>=6.0",
        "faker>=18.0",
        "allure-pytest>=2.13.0",
        "pytest-html>=3.2.0",
    ],
    python_requires=">=3.7",
)