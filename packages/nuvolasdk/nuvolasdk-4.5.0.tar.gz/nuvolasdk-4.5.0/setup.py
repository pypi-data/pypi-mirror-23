#!/usr/bin/env python3

from setuptools import setup

LONG_DESC = """\
SDK for building Nuvola Apps scripts.

Documentation: https://github.com/tiliado/nuvolasdk
"""

setup(
	name = "nuvolasdk",
	version = "4.5.0",
	author = "Jiří Janoušek",
	author_email = "janousek.jiri@gmail.com",
	url = "https://github.com/tiliado/nuvolasdk",
	description = "SDK for building Nuvola Apps scripts",
	keywords = 'nuvola sdk development',
	long_description = LONG_DESC,
	license = 'BSD',
	packages = ['nuvolasdk'],
	package_data = {
		'nuvolasdk': [
				'data/*',
				'data/template/*',
				'data/template/src/*',
				'data/examples/*',
				'data/vapi/*',
			]
		},
	exclude_package_data = {
		'nuvolasdk': [
			'data/template',
			'data/template/src',
			'data/examples',
			'data/vapi',
		]
	},
	scripts = ['scripts/nuvolasdk'],
	classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only"
    ]
)
	
