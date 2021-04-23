from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='randdate',
      version='0.1.0',
      description='Generate a list of random dates or resp. datetime objects',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/randdate',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['randdate'],
      # install_requires=[],
      python_requires='>=3.6',
      zip_safe=False)
