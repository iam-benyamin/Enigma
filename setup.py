'''
from cython.Cythonize import cythonize

setup(
      build_ext=cythonize('engima.pyx')
)
'''
# from distutils.core import setup
from setuptools import setup, find_packages

with open('README.md')as file:
    long_description = file.read()

setup(
    name='Enigma',
    version='1.0',
    description='Written based on the Enigma encryption machine algorithm'
    ' belonging to Nazi Germany',
    long_description=long_description,
    author='Benyamin Mahmoudyan, Arthur Scherbius',
    author_email='benyaminmahmoudyan@gmail.com',
    license="MIT",
    packages=find_packages(),
)

