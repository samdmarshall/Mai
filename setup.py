from setuptools import setup

setup(
    name='xcbuild',
    version='0.1',
    description='External Xcode scheme build tool',
    url='https://github.com/samdmarshall/xcbuild',
    author='Sam Marshall',
    author_email='me@samdmarshall.com',
    license='BSD 3-Clause',
    packages=['xcbuild', 'xcbuild/xcode', 'xcbuild/xcode/PBX', 'xcbuild/xcode/XCSchemeActions'],
    entry_points = {
        'console_scripts': ['xcbuild = xcbuild:main'],
    },
    zip_safe=False
)