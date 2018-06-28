from setuptools import setup

setup(name='nettools',
      version='1.0',
      description='The networking toolkit for Python. Only for UNIX (Linux + macOS) systems!',
      url='http://github.com/hkamran80/nettools',
      author='H. Kamran',
      author_email='hkamran@unisontech.org',
      license='GPLv3+',
      packages=['nettools'],,
      install_requires=[
          'ipwhois', 'dnspython3',
      ],
      zip_safe=False)
