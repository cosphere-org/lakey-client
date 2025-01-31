import json
import os
from setuptools import setup


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


#
# REQUIREMENTS
#
def parse_requirements(requirements):

    return [
        r.strip()
        for r in requirements
        if (
            not r.strip().startswith('#') and
            not r.strip().startswith('-e') and
            r.strip())
    ]


with open(os.path.join(BASE_DIR, 'requirements.txt')) as f:
    requirements = parse_requirements(f.readlines())


#
# CONFIG
#
with open(os.path.join(BASE_DIR, '.lily', 'config.json')) as f:
    config = json.loads(f.read())


# -- SETUP
setup(
    name=config['name'],
    packages=['lakey_client'],
    description=(
        'Lakey Client for interacting with lakey from jupyter notebook'),
    url=config['repository'],
    version=config['version'],
    author='CoSphere Team',
    install_requires=requirements,
    data_files=[(
        'lakey_client',
        [
            'requirements.txt',
            '.lily/config.json',
        ],
    )],
    include_package_data=True,
    keywords=['lakey', 'client'],
    classifiers=[])
