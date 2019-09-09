from distutils.core import setup

setup (
    name='csvsplit',
    version='0.0.1',
    author='Jonathan Montgomery',
    lisence='MIT',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'csvsplit=csvsplit:cli_entry'
        ]
    },
    scripts=['src/csvsplit.py']
)
