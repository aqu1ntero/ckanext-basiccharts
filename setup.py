from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-basiccharts',
	version=version,
	description="Basic charts for CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Vitor Baptista',
	author_email='vitor.baptista@okfn.org',
	url='https://github.com/okfn/ckanext-basiccharts',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.basiccharts'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    [ckan.plugins]
	basiccharts=ckanext.basiccharts.plugin:BasicCharts
	""",
)