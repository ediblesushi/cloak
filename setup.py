
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cloak',
    version='1.0',
    author='Chris Doucette',
    author_email='chrisdoucette15@gmail.com',
    description="",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/ediblesushi/mystify',
    packages=setuptools.find_packages(),
    install_requires=[
    'click'
    ],
    entry_points={
    'console_scripts': [
      'cloak = cloak:main'
    ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
