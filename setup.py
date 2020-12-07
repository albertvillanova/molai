import setuptools

# INSTALL_REQUIRES = [
#     "rdkit"
# ]


setuptools.setup(
    name="molai",
    version="0.0.1",
    author="Albert Villanova",
    author_email="albert.villanova@aiinnova.com",
    description="Molecule AI",
    url="https://github.com/albertvillanova/molai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    # install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'molai=molai.cli:cli',
        ],
    },
)
