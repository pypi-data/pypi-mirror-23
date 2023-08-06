from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='modus',
    author='cookkkie',
    url='https://github.com/cookkkie/modus',
    version='0.0.4',
    packages=find_packages(),
    license='MIT',
    description='',
    include_package_data=True,
    install_requires=requirements
)
