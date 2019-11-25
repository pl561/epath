from setuptools import setup


classif = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Scientific research, multiple filenames :: Path handling',

    # Pick your license as you wish (should match "license" above)
     'License :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
],


setup(
    name="epath",
    version="1.0.0",
    author="pl561",
    author_email="plefevre561@gmail.com",
    url="https://github.com/pl561/epath",
    description="This module contains tools for manipulating Linux paths.",
    license="MIT License",
    classifiers=classif,
    install_requires=["pathlib", "opencv-python"]
)


