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
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'tomtoolkit',
        'gsselect'
    ]
)