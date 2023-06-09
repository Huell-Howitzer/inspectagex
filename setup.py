from setuptools import setup, find_packages

setup(
    name='inspectagex',
    version='1.0.0',
    description='Python library for file inspection and text manipulation with regular expressions',
    author='Your Name',
    author_email='yourname@example.com',
    url='https://github.com/yourusername/inspectagex',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='file inspection text manipulation regex regular expression',
    python_requires='>=3.6',
    install_requires=[
        # add any dependencies your library requires
    ],
)
