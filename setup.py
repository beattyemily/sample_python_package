from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for learning how to write a package',
    long_description=readme,
    author='Emily Beatty',
    author_email='emilyebeatty@hotmail.co.uk',
    url='https://github.com/beattyemily/sample_python_package',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)