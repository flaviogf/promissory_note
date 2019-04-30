from setuptools import setup, find_packages

setup(
    name='promissory_note',
    version='0.0.5',
    description='Simple promissory note issuance',
    long_description='Simple promissory note issuance',
    url='https://github.com/flaviogf/promissory_note',
    author='Flavio Fernandes',
    author_email='flavio.fernandes6@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyflunt==1.0.0',
        'pillow==6.0.0',
        'click==7.0',
        'pyfiglet==0.8.post1',
        'sendgrid==6.0.4',
    ],
    entry_points={
        'console_scripts': ['promissory-note-cli=promissory_note.gateways.cli:main'],
    },
    zip_safe=False,
)
