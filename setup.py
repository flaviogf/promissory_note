from setuptools import setup

setup(
    name='promissory_note',
    version='0.0.4',
    description='Simple promissory note issuance',
    long_description='Simple promissory note issuance',
    url='https://github.com/flaviogf/promissory_note',
    author='Flavio Fernandes',
    author_email='flavio.fernandes6@gmail.com',
    packages=[
        'promissory_note',
        'promissory_note.gateways',
    ],
    package_date={
        'content': ['*'],
    },
    include_package_data=True,
    install_requires=[
        'pyflunt==1.0.0',
        'pillow==6.0.0',
        'click==7.0',
        'pyfiglet==0.8.post1',
    ],
    entry_points={
        'console_scripts': ['promissory-note=promissory_note.gateways.cli:main'],
    },
)
