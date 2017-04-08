import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dar-command',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='DAR Command: Command line interface',
    long_description=README,
    url='https://github.com/000darfw000/dar-command',
    author='Ariel Calzada',
    author_email='ariel.calzada@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: The GNU General Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    scripts=[
        'bin/dar-command.py'
    ],
    install_requires=[
        'django',
    ],
)