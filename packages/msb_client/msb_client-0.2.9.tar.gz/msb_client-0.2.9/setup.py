# coding=utf-8
from distutils.core import setup
setup(
  name='msb_client',
  packages=['msb_client'],
  version='0.2.9',
  description='MSB client implementation for python 3',
  author='Andy Grabow',
  author_email='andy@freilandkiwis.de',
  url='https://bitbucket.org/kakulukia/msb-client-py',
  download_url='https://bitbucket.org/kakulukia/msb-client-py/get/0.2.9.tar.gz',
  keywords=['VFK', 'MSB', 'Client'],
  classifiers=[],
  install_requires=[
        "ws4py==0.3.5", 'python-dateutil==2.5.3', 'autobahn', 'twisted',
    ],
)
