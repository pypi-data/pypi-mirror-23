from setuptools import setup
import sys
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ""


requires = [
    'ConfigArgParse',
    'coloredlogs>=5.2',
    'async_timeout>=1.1',
    'pyzmq>=16.0',
    'aiodocker',
    'aiozmq>=0.7',
    'aiohttp>=2.0.6',
    'aioredis>=0.2.8',
    'aiobotocore>=0.3.0',
    'msgpack-python',
    'namedlist',
    'requests',
    'requests_unixsocket',
    'simplejson',
    'uvloop>=0.8',
]
build_requires = [
    'pypandoc',
    'wheel',
    'twine',
]
test_requires = [
    'pytest>=3.1',
    'pytest-asyncio',
    'pytest-mock',
    'asynctest',
    'flake8',
    'pep8-naming',
]
dev_requires = build_requires + test_requires + [
    'pytest-sugar',
]
ci_requires = []
monitor_requires = [
    'datadog>=0.16.0',
    'raven>=6.1',
]

sys.path.insert(0, '.')
import sorna.agent


setup(
    name='sorna-agent',
    version=sorna.agent.__version__,
    description='Sorna agent',
    long_description=long_description,
    url='https://github.com/lablup/sorna-agent',
    author='Lablup Inc.',
    author_email='joongi@lablup.com',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],

    packages=['sorna.agent'],
    namespace_packages=['sorna'],

    python_requires='>=3.6',
    install_requires=requires,
    extras_require={
        'build': build_requires,
        'test': test_requires,
        'dev': dev_requires,
        'ci': ci_requires,
        'monitor': monitor_requires,
    },
)
