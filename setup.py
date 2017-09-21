from setuptools import setup, find_packages

setup(
    name='aws-nagios-checks',
    version='0.1',
    description='AWS Nagios Checks',
    url='https://github.com/johnnybus/aws-nagios-checks',
    author='Joao Carreira',
    author_email='jddcarreira@gmail.com',
    license='MIT',
    packages=find_packages(where='.'),
    install_requires=[
        'boto3',
        'docopt'
    ],
    scripts=['aws_nagios_checks/aws-nagios-checks'],
    zip_safe=False
)
