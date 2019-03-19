from setuptools import setup, find_packages

setup(
    name='mypacktk',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/K1TS/mypackage.git',
    author='TREVOR SENYANE',
    author_email='makhiler@gmail.com'
)
