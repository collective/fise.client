from setuptools import setup, find_packages
import sys, os

version = '1.1'
shortdesc = 'Apache Stanbol FISE: RESTful Python Client.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
tests_require = ['interlude']

setup(name='fise.client',
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
      keywords='',
      author='Jens Klein',
      author_email='jens@bluedynamics.com',
      url=u'',
      license='Python Software Foundation License',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'setuptools',
            'restkit',
            'rdflib',
            'surf.sparql_protocol',
            'surf.rdflib',

      ],
      tests_require=tests_require,
      test_suite="fise.client.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
)
