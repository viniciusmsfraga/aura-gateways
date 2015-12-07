from setuptools import setup

setup(name='AuraGateways',
      version='0.1',
      author='Vinícius Matos da Silveira Fraga',
      author_email='vinicius.vmsf@gmail.com',
      packages=['gatewayExample'],
      install_requires=[
          'paho-mqtt',
      ],
      entry_points = {
        'console_scripts': ['auraGateway=gateways.gateway_example:main'],
      }
      )