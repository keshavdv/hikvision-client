from setuptools import setup, find_packages
from os.path import join, dirname
import re
import hikvisionapi

version = hikvisionapi.__version__

setup(name='hikvisionapi',
      version=version,
      description='The client for HIKVISION cameras, DVR',
      url='https://github.com/MissiaL/hikvision-client',
      author='Petr Alekseev',
      author_email='petrmissial@gmail.com',
      packages=find_packages(),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      download_url='https://github.com/MissiaL/hikvision-client/tarball/{}'.format(version),
      keywords=['api', 'hikvision', 'hikvision-client'],
      install_requires=['xmltodict', 'requests']
      )
