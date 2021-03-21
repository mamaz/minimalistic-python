from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lic = f.read()

setup(
    name='minimalistic-python',
    version='1.0.0',
    description='Simple Python package example',
    long_description=readme,
    author='Mamaz',
    author_email='hisma.mulya@gmail.com',
    url='https://github.com/mamaz/minmalistic-python',
    license=lic,
    packages=find_packages(exclude=('tests', 'docs'))
)
