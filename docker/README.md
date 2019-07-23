# Run in a docker!

### Build the image

From this folder, run:

     docker build --tag ascraper .

### Run the help command 

      docker run\
            -v ~/.archives-space-scraper/credentials:/root/.archives-space-scraper/credentials\
            -v "$PWD/out":/local-data\
            -it\
            --rm ascraper --help
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

Here's an explanation of each argument we passed to docker:
1. That first "-v ~/.archives-space..." line copies our local credentials file from the host into the docker container. If yours is located somewehre else, change the path before the ":"
2. That second "-v" line mounts the local folder ./out so that the application's output files will be saved on the host machine and not just disappear when the container exits
3. "-it" is docker language to make it an interactive session
4. "--rm" is remove the container when it exists
5. ascraper just tells docker which image to run
6. finally, "--help" is the argument to send to the application.

### Download files for repo
Everything is the same as above, except the last line, where we pass a different argument to the application. When we supply a repo-id, the application runs and starts downloading (assuming the credentials file is valid and was stored in the right spot)

        docker run\
              -v ~/.archives-space-scraper/credentials:/root/.archives-space-scraper/credentials\
              -v "$PWD/out":/local-data\
              -it\
              --rm ascraper --repo-id=14
