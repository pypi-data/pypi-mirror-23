from setuptools import setup

setup(name='yearonequant',
      version='1.0',
      description='Think as quant, tade as quant',
      url='http://github.com/hyqLeonardo/yearonequant',
      author='Leonardo',
      author_email='hyq335335@163.com',
      license='MIT',
      packages=['yearonequant'],
      install_requires=[
	'numpy',
	'pandas',
	'rqdatac',
	'TA-Lib',
	'plotly',
      ],
      zip_safe=False)
