#
#To upload the latest version, change "version=0.X.X+1" and type:
#	python setup.py sdist upload
#
#
#

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pytplot',
      version='0.2.4',
      description='A python version of IDL tplot libraries',
      url='http://github.com/MAVENSDC/Pytplot',
      author='MAVEN SDC',
      author_email='mavensdc@lasp.colorado.edu',
      license='MIT',
      keywords='tplot maven lasp idl',
      packages=['pytplot'],
      install_requires=['bokeh>=0.12.5', 
                        'pandas', 
                        'numpy', 
                        'matplotlib'],
      include_package_data=True,
      zip_safe=False)