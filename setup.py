from setuptools import setup, find_packages

setup(
    name='ytmp4',
    version='0.1',
    packages=['app.py'],
     install_requires=[
        'pytube==15.0.0',
    ],
    entry_points={
        'console_scripts': [
            'ezvideo=app.py:',
        ],
    },
)