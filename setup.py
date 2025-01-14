from setuptools import setup

setup(
    name='re_upload',
    version='1.0.0',
    description='A script for uploading files to the RealEarth server',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://realearth.ssec.wisc.edu',
    author='Your Name',
    author_email='your.email@example.com',
    scripts=['re_upload.sh'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)