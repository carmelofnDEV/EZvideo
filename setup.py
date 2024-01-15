from setuptools import setup, find_packages

setup(
    name='ezvideo',
    version='0.1',
    packages=find_packages(),
     install_requires=[
        'pytube==15.0.0',
    ],
    entry_points={
        'console_scripts': [
            'ezvideo=app.app:main',
        ],
    },
)