"""
keyme and fetch_creds -- Tools for interacting with GOOGLE SAML SSO and AWS
SAML with STS.
"""

from setuptools import find_packages, setup

dependencies = [
    'click',
    'boto3',
    'beautifulsoup4',
    'requests',
    'py',
    'six'
]

setup(name='keyme',
      version='0.8.1',
      description='Google SAML STS login library',
      long_description=(
          'This tool allows you to login into AWS using Google SAML Apps as '
          'part of Google For Work'
      ),
      url='http://github.com/wheniwork/keyme',
      author='Richard Genthner',
      author_email='richard.genthner@wheniwork.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=dependencies,
      tests_require=['pytest', 'mock'],
      license='MIT',
      entry_points = '''
        [console_scripts]
            fetch_creds=keyme.cli.fetch_creds:cli
        ''',
      platforms='any',
      zip_safe=False,
      classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
