from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

test_requirements = [

]

setup(
    name='capitals',
    version='v1.0',
    description='Capitals on your terminal',
    long_description=readme + '\n\n' + history,
    author='Luis Louro',
    author_email='lapisdecor@gmail.com',
    url='https://github.com/lapisdecor/capitals',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    include_package_data=True,
    licence='MIT licence',
    zip_safe=False,
    keywords='capitals',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.12',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    scripts=['bin/capitals']
)