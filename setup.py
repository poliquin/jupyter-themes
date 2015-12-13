import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='jupyter-themes',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Select and install a Jupyter notebook theme',
    long_description=README,
    author='dunovank, miraculixx',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: jupyter',
        'Intended Audience :: Developers',
        'License :: Commercial',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: CSS',
        # replace these appropriately if you are using Python 3 
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'sh', # shell commands
    ],
    entry_points={
      'console_scripts': [
        'jupyter-theme = themeselect:main',
    ],
}
)
