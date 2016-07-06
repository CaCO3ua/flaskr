from setuptools import setup

setup(
    name='Flaksr',
    version='1.0',
    packages=['flaskr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)