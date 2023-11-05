from setuptools import setup

setup(
    name='watchlog-connect-py',
    version='0.0.1',
    description='This is a package for connect to watchlog and send custom metrics',
    author='mohammadnajm',
    author_email='mohammadnajm75@email.com',
    packages=['watchlog.py'],
    install_requires=['websockets'],  # List your package dependencies
)