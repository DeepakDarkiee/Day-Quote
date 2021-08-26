from setuptools import setup, find_packages

setup(
    name='dayquote',
    version='0.1',
    description='Get Day Quote',
    url='https://github.com/DeepakDarkiee/Day-Quote.git',
    author='Deepak Patidar',
    author_email='info.deepakpatidar@gmail.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:display_quote']
    )
)