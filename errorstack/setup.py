from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Uncover solutions for python errors '
LONG_DESCRIPTION = 'Automate the process of finding solutions and exterminating bugs in your projects using the ErrorStack package'


setup(
       
        name="ErrorStack", 
        version=VERSION,
        author="Moses Kariuki",
        author_email="musaspacecadet@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'fix error','find bugs' ,'error','solution'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)