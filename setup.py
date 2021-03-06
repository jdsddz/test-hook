from setuptools import find_packages
from setuptools import setup

setup(
    name='test-hook',
    packages=find_packages(),
    install_requires=['pipfile'],
    entry_points={
        'console_scripts': [
            'dummy_check = pre_commit_hooks.dummy_check:main',
        ],
    },
)