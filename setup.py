from setuptools import setup

setup(
    name="anomaly_detection",
    packages=["anomaly_detection"],
    version="0.0.2",
    install_requires=["scipy", "statsmodels"],
    description="A python implementation of https://github.com/twitter/AnomalyDetection",
)
