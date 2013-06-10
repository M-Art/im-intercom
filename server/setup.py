from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

config = {
    'name': 'intercom-server',
    'version': '0.0.1',
    'description': 'Intercom Raspberry Pi server',    
    'long_description': readme,
    'license': license,
    'author': '',
    'author_email': '',
    'url': 'https://github.com/M-Art/im-intercom/',
    'download_url': '',
    'install_requires': requirements,
    'packages': find_packages(),
    'scripts': [],
    'entry_points': {
        'setuptools.installation': [
            'eggsecutable = server:main',
        ]
    }
}

setup(**config)
