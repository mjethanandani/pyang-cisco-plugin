import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyang-cisco-plugin',
    version='0.1',
    description=('A pyang plugin to validate Cisco native models'),
    long_description=read('README.md'),
    packages=['plugins'],
    author='Mahesh Jethanandani',
    author_email='mjethanandani@gmail.com',
    license='New-style BSD',
    url='https://github.com/mjethanandani/pyang-cisco-plugin',
    download_url='https://github.com/mjethanandani/pyang-cisco-plugin/archive/0.1.tar.gz',
    install_requires=['pyang'],
    include_package_data=True,
    keywords=['yang', 'validation'],
    classifiers=[],
    entry_points={'pyang.plugin': 'cisco_pyang_plugin=plugins.cisco:pyang_plugin_init'}
)
