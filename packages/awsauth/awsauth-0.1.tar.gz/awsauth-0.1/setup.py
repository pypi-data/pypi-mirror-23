from setuptools import setup

setup(name='awsauth',
      version='0.1',
      description='AWS STS/MFA auth helper script',
      url='https://github.com/ConnectedHomes/dp-awsauth',
      author='Piotr Wreczycki',
      author_email='piotr.wreczycki@hivehome.com',
      license='MIT',
      scripts=['bin/awsauth.py'],
      install_requires=[
          'boto3',
          'botocore'
      ],
      packages=['awsauth'],
      zip_safe=False)