from setuptools import setup

setup(name='cuatro_en_linea',
      version='0.1',
      description='Basic implementation of the connect four game',
      url='https://github.com/apojomovsky/cuatro_en_linea',
      license='Apache',
      install_requires=[
          'mock==2.0.0',
          'tabulate',
          'numpy==1.12.0',
          'scipy==0.18.1',
      ],
zip_safe=False)
