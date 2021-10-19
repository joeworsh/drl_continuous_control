# Copyright Joe Worsham 2021

from setuptools import setup, find_packages

setup(name='ddpg',
      version='0.1.0',
      description='DRL Agents for Udacity Continuous Control Project',
      license='MIT',
      author='Joe Worsham',
      url='https://github.com/joeworsh/drl_continuous_control',
      packages=find_packages(),
      install_requires=[
            "tensorflow==1.7.1",
            "Pillow>=4.2.1",
            "matplotlib",
            "numpy>=1.11.0",
            "jupyter",
            "pytest>=3.2.2",
            "docopt",
            "pyyaml",
            "protobuf==3.5.2",
            "grpcio==1.11.0",
            "torch",
            "pandas",
            "scipy",
            "ipykernel"
      ]
)
