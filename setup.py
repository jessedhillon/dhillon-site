import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, 'README.rst')).read()

requires = []

setup(
    name='Dhillon-site',
    version='0.1',
    description="Site customization for Jesse Dhillon",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Jesse Dhillon',
    author_email='jesse@deva0.net',
    url='https://github.com/jessedhillon',
    keywords='util paste',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='dhillon_site',
    install_requires = requires,
    entry_points = """\
    [pyramid.scaffold]
    dhillon=dhillon_site.scaffolds:DhillonTemplate
    """,
)
