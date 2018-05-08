from setuptools import setup

setup(
    name='ieee-signin',
    version='1.0.0',
    packages=['ieee_signin'],
    include_package_data=True,
    install_requires=[
        "gspread==3.0.0",
        "google-api-python-client==1.6.7",
        "oauth2client==4.1.2",
        "pycodestyle==2.4.0",
        "pydocstyle==2.1.1",
        "pylint==1.8.4",
        "PyOpenSSL==17.5.0"
    ],
    entry_points={
        'console_scripts': [
            'ieee-signin=ieee_signin.__main__:main'
        ]
    },
)