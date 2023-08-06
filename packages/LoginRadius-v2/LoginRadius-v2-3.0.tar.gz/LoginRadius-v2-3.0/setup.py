from distutils.core import setup
setup(
    name = 'LoginRadius-v2',
    version= '3.0',
    packages=["LoginRadius","LoginRadius.sdk"],
    description = 'Social Login and User Registration for Python.',
	long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author='LoginRadius',
    author_email='developers@loginradius.com',
    url='http://loginradius.com/',
    classifiers=['Programming Language :: Python', 'Programming Language :: Python :: 2.7','Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.6','Operating System :: OS Independent', 'License :: OSI Approved :: MIT License',
                 'Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers',
                 'Topic :: Internet', 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
