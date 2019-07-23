import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ArchivesSpaceScraper",
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="Scrape a repository from ArchivesSpace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jake-kara/archives-space-scraper",
    #packages=["ArchivesSpaceScraper"],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts":[
            "archives-space-scraper=cli.main:main"
        ]
    },
    install_requires=[
        "ArchivesSnake",
        "progress",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)