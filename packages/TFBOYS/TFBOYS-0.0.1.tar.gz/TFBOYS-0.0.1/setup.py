import os

from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='TFBOYS',
    version='0.0.1',
    install_requires=[
        'TensorFlow'
    ],
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='TensorFlow BOYS',
    long_description=README,
    url='https://github.com/nypisces/TFBOYS',
    author='NY',
    author_email='nypisces@live.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
