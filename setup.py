from setuptools import find_packages
from setuptools import setup

setup(
    name='test-hook',
    packages=find_packages('.')
    entry_points={
        'console_scripts': [
            'dummy_check = dummy_check:main',
        ],
    },
)