# ArchivesSpaceScraper

Jake Kara jake.kara@yale.edu jake@jakekara.com

Scraper for ArchivesSpace repositories. Library and CLI tool. The CLI tool
simply makes a local copy of your entire ASpace repo in JSON files, with a
folder structure that matches the API urls. This is useful for data analysis and
restructuring without constantly pinging the API.

This is an offshoot of code I wrote for a specific prnoject. That code will be
available in .ipynb notebooks in the near future, and will make the use case for
this tool more obvious.

## Status

This was thrown together quickly. 

Docs, examples, and tests would help! Example notebooks are forthcoming, but
docs and tests are unlikely.

I've only run it on MacOS. There may be some issues with the setup.py script,
such as missing dependencies, that need to be worked out.

## Step 1: Install the package

First, install the library with:

pip install git+git://github.com/jakekara/archives-space-scraper

## Step 2: Set up credentials file

Next, create a credentials file in:

~/.archives-space-scraper/credentials

Use ./example.credentials in this repo, and fill in your credentials

Authentication using env variables is also supported, but not from the CLI.

## Step 3: Usage

After 1 and 2, you're ready to use the tool...

## CLI tool instructions

        usage: archives-space-scraper [-h] --repo-id REPO_ID [--output-dir OUTPUT_DIR]
                                    [-p PROFILE] [-c CREDENTIALS_FILE] [-f]

        optional arguments:
        -h, --help            show this help message and exit
        --repo-id REPO_ID     numeric repo ID
        --output-dir OUTPUT_DIR
                                local to store downloaded objects
        -p PROFILE, --profile PROFILE
                                which profile to use from credentials file
        -c CREDENTIALS_FILE, --credentials-file CREDENTIALS_FILE
                                path to credentials file
        -f, --force           force redownloading of existing files


## CLI tool example usage:

        $ archives-space-scraper --repo-id=14 --output-dir=./local-data
        🔑  Reading password for 'default' from '~/.archives-space-scraper/credentials'...
        🔐  Logging in as [XXX] at https://archivesspace.library.yale.edu/api...
        📇  Downloaded index of 4521 resources...
        📜  Downloading 4521 resources now... |################################| 100%
        📜  Downloading 5532 subjects referenced by resources now... |################################| 100%
        📜  Downloading 16338 agents referenced by resources now... |################################| 100%
        🌈  done!