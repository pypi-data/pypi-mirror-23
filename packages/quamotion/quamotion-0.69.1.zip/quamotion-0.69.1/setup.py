from setuptools import setup

setup(name='quamotion',
      version='0.69.1',
      description='Python client for the Quamotion WebDriver',
      url='http://github.com/quamotion/python',
      author='Quamotion',
      author_email='info@quamotion.mobi',
      license='Apache',
      packages=['quamotion'],
      install_requires=[
          'selenium',
          'requests'
      ],
      zip_safe=False)