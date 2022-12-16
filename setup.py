from setuptools import setup, find_packages

setup(
    packages=find_packages("starname"),
    package_data={
        "starname": ["database/*"],
    },
    entry_points={
        "console_scripts": "starname = starname:console_main",
    },
)
