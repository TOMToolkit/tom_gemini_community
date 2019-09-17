import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tom-gemini-community',
    version='0.1.0',
    author="Bryan Miller",
    author_email="millerwbryan@gmail.com",
    description="Gemini Observatory Community TOM Broker Modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TOMToolkit/tom_gemini_community",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords=['tomtoolkit', 'astronomy', 'astrophysics', 'cosmology', 'science', 'fits', 'observatory', 'gemini'],
    install_requires=[
        'tomtoolkit',
        'gsselect'
    ]
)