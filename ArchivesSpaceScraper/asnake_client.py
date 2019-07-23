from asnake.client import ASnakeClient
import os
# from .credentials import get_from_file as get_credentials

# uname = os.environ['ARCHIVESSPACE_USERNAME']
# pword = os.environ['ARCHIVESSPACE_PASSWORD']


# def get_client(profile="default"):
#     # TODO - enable get_client to accept an alternate credentials file path
#     #      - for now it just defaults to ~/.archives-scraper/credentials
#     c = get_credentials(profile=profile)

#     print (profile, c)
#     client = ASnakeClient(
#         baseurl=c["baseurl"],
#         username=c["username"],
#         password=c["password"]
#     )

#     client.authorize()

#     return client


def get_client(credentials):
    c = credentials

    client = ASnakeClient(
        baseurl=c["baseurl"],
        username=c["username"],
        password=c["password"]
    )

    client.authorize()

    return client