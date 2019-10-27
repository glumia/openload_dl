import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="openload_dl",
    version="2.0.1",
    author="Giuseppe Lumia",
    author_email="glumia@protonmail.com",
    description="openload_dl is a python library and CLI tool which makes easy to download files from openload.co",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glumia/openload_dl",
    packages=["openload_dl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["openload-dl = openload_dl.script:openload_cli"]},
    install_requires=["requests", "selenium", "click", "tqdm"],
)
