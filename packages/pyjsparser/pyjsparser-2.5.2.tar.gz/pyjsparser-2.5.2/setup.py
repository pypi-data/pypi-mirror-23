from distutils.core import setup

# python3 setup.py sdist upload -r pypi
setup(
    name='pyjsparser',
    version='2.5.2',
    packages=['pyjsparser'],
    url='https://github.com/PiotrDabkowski/pyjsparser',
    install_requires = [],
    license='MIT',
    author='Piotr Dabkowski',
    author_email='piodrus@gmail.com',
    description='Fast javascript parser (based on esprima.js)'
)
