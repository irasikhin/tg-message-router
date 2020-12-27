from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='tg-message-router',
    description='Telegram Message Router',
    author='Ivan Rasikhin',
    author_email='',
    url='https://github.com/irasikhin/tg-message-router',
    packages=find_packages(include=['python_application']),
    package_dir={'python-application': 'python_application'},
    entry_points={
        'console_scripts': [
            'python-application=python_application.__main__:main',
        ],
    },
    python_requires='>=3.6.0',
    version='0.0.0',
    long_description=readme,
    include_package_data=True,
    install_requires=[
        'telethon',
    ],
    license='MIT',
)
