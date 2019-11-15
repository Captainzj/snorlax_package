import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='snorlaxse',
    version="0.0.3",
    author="snorlaxse",
    author_email="841145636@qq.com",
    description="upload some self useful code",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Captainzj/snorlax_package.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)