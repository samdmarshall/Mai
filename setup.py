from setuptools import setup

setup(
    name='mai',
    version='0.1',
    description='External Xcode scheme build tool',
    url='https://github.com/samdmarshall/Mai',
    author='Sam Marshall',
    author_email='me@samdmarshall.com',
    license='BSD 3-Clause',
    package_data = {'mai/xcode/xcparse': ['defaults.xcconfig']},
    packages=[
        'mai',
        'mai/xcode/xcparse', 
        'mai/xcode/xcparse/Helpers', 
        'mai/xcode/xcparse/Xcode', 
        'mai/xcode/xcparse/Xcode/PBX', 
        'mai/xcode/xcparse/Xcode/XCSchemeActions', 
        'mai/xcode/xcparse/Xcode/BuildSystem', 
        'mai/xcode/xcparse/Xcode/BuildSystem/XCSpec', 
        'mai/xcode/xcparse/Xcode/BuildSystem/LangSpec',
        'mai/xcode/xcparse/Xcode/BuildSystem/Environment'
    ],
    entry_points = {
        'console_scripts': ['mai = mai:main'],
    },
    zip_safe=False
)