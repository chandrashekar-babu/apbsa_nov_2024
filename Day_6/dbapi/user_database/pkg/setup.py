import setuptools

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="userdb", # Replace with your own username
    version="0.0.1",
    author="Chandrashekar Babu",
    author_email="training@chandrashekar.info",
    description="A simple database abstraction library",
#    long_description=long_description,
#    long_description_content_type="text/markdown",
    url="https://github.com/chandrashekar_babu/userdb",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)