from setuptools import setup, find_packages

reqs = [line.rstrip() for line in open('requirements.txt')]
packages = find_packages()

setup(name='plotRawDataDistribution',
    version='0.0.0-alpha',
    description="",
    url='NA',
    author='Erik Borgstroem',
    author_email='eb@spatialtranscriptomics.com',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    setup_requires=reqs,
    install_requires=reqs,
    scripts=['script/plotRawDataDistribution.py']
    )
