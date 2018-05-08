from setuptools import setup

setup(
    name='ieee-signin',
    version='1.0.0',
    packages=['ieee-signin'],
    include_package_data=True,
    install_requires=[
        "pycodestyle==2.4.0",
        "pydocstyle==2.1.1",
        "pylint==1.8.4"
    ],
    entry_points={
        'console_scripts': [
            'ieee-signin = ieee-signin.__main__:main'
        ]
    },
)