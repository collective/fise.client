# Python Software Foundation License

from setuptools import setup, find_packages
import sys, os

version = '1.3.2'
shortdesc = 'Ordered dictionary.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()
tests_require = ['interlude']

setup(name='odict',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Python Software Foundation License',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Software Development',       
      ],
      keywords='odict dict ordered dictionary mapping collection tree',
      author='Robert Niederreiter',
      author_email='rnix@squarewave.at',
      url=u'https://svn.plone.org/svn/archetypes/AGX/odict',
      license='Python Software Foundation License',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=['setuptools'],
      tests_require=tests_require,
      test_suite="odict.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
)