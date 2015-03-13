from setuptools import setup

setup(
    name='mai',
    version='0.1',
    description='External Xcode scheme build tool',
    url='https://github.com/samdmarshall/Mai',
    author='Sam Marshall',
    author_email='me@samdmarshall.com',
    license='BSD 3-Clause',
    packages=[
        'mai',
        'xcparse'
    ],
    install_requires=[
        'xcparse',
    ],
    entry_points = {
        'console_scripts': ['mai = mai:main'],
    },
    zip_safe=False
)