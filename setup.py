from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='self-rag',
    version='1.0.0',
    author='suoloordi',
    author_email='suoloordi@github.com',
    description='self rag',
    long_description='self rag',
    long_description_content_type='text/markdown',
    url='https://github.com/suoloordi/self-rag',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'factscore': ['factscore==0.1.5']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)