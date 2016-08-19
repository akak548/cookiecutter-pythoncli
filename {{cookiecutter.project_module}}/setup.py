import os
from setuptools import setup


with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

requires = [
]

test_requirements = [
]

packages = [
    {{cookiecutter.project_module}}
]

keywords = 'development setuptools'

setup(
    name={{cookiecutter.project_module}},
    version={{cookiecutter.version}},
    description={{cookiecutter.description}},
    long_description=readme + '\n\n' + history,
    author={{cookiecutter.author_name}},
    author_email={{cookiecutter.email}},
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'requests': 'requests'},
    include_package_data=True,
    install_requires=requires,
    license={{cookiecutter.license}},
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
    keywords=keywords,
    scripts=['bin/{{cookiecutter.project_name}}'],
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)


