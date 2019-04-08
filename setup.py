from setuptools import setup

setup(
    name='pythonMerakiCMX',
    version='1',
    description='A python code to create a Meraki CMX location analytics receiver',
    author='sWallyx',
    keywords=['cisco', 'meraki', 'location', 'count', 'people', 'analytics'],
    classifiers=[],
    install_requires=[
    	'Flask',
    	'flask-jsonpify',
    	'flask-sqlalchemy',
    	'flask-restful',
    	'flask-cors',
	'pprint',
	'pymongo'
    ],
    setup_requires=[],
    tests_require=[],
)
