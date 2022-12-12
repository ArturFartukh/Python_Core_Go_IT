from setuptools import setup, find_packages
from os.path import join, dirname
from clean_folder import __version__


setup(name='clean_folder',
      version=__version__,
      packages=find_packages(),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      url='https://github.com/ArturFartukh/go_it-python_core_hw07/tree/main/clean_folder',
      author='Artur Fartukh',
      author_email='ar4ik.8933@gmail.com',
      entry_points={'console_scripts':
                          ['clean-folder = clean_folder.clean:main']
                    }
)