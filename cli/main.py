
from ArchivesSpaceScraper.archivist import ArchiveCloner
from ArchivesSpaceScraper.credentials import get_from_file as get_credentials_from_file

from progress.bar import Bar #IncrementalBar as Bar
import argparse

def get_arr(resource, key):
    if key not in resource.keys(): return []
    return [x["ref"] for x in resource[key]]#["ref"]

def combine_all_arrs(resources, key="subjects"):
    ret = []
    for resource in resources:
        arr = get_arr(resource, key)
        ret = list(set(ret + arr))
    return sorted(ret)

def copy_resources(client, arr, label="items"):

    bar = Bar("📜  Downloading %d %s now..." % (len(arr), label),
        max=len(arr),
        suffix='%(percent)d%%')

    # resources=[]
    # for resource_id in resource_ids:
    #     resources.append(repo.copy_resource("/repositories/%s/resources/%s" % (args.repo_id, str(resource_id)), redownload=args.force))



    ret = []
    for resource_ref in arr:
        ret.append(client.copy_resource(resource_ref))
        bar.next()
    print()

    return ret

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-id",
        type=int,
        required=True,
        help="numeric repo ID")
    parser.add_argument("--output-dir",
        type=str,
        help="local to store downloaded objects",
        default="./out"
    )
    parser.add_argument("-p", "--profile",
        help="which profile to use from credentials file",
        default="default"
    )
    parser.add_argument("-c", "--credentials-file",
        help="path to credentials file",
        default="~/.archives-space-scraper/credentials"
    )

    parser.add_argument("-f", "--force",
        help="force redownloading of existing files",
        action="store_true"
    )

    return parser.parse_args()

def main():

    args = get_args()

    # Load credentials
    try:
        print ("Reading password for '%s' from '%s'..." % (args.profile, args.credentials_file))
        credentials = get_credentials_from_file(
                fpath=args.credentials_file,
                profile=args.profile
                )
    except Exception as e:
        print ("Error: %s" % e)
        exit(-1)

    # Log in to API
    try:
        print ("Logging in as %s at %s..." % (credentials["username"], credentials["baseurl"]))
        repo = ArchiveCloner(args.repo_id,
            root=args.output_dir,
            credentials=credentials
        )
    except Exception as e:
        print ("Error: %s" % e)
        exit(-1)


    # Download the index of resource ids
    url="/repositories/%d/resources?all_ids=true" % args.repo_id
    resource_ids = repo.copy_resource(url, redownload=args.force)

    # Download each resource
    print ("Downloaded index of %d resources..." % len(resource_ids))
    # num_items = len(resource_ids)
    resources = copy_resources(
        repo,
        ["/repositories/%s/resources/%s" % (args.repo_id, str(resource_id)) for resource_id in resource_ids],
        label="resources")


    # Get all of the linked subjects and agents

    combine_all_subject_ids = lambda resources: combine_all_arrs(resources, key="subjects")
    combine_all_agent_ids = lambda resources: combine_all_arrs(resources, key="linked_agents")

    all_subject_ids = combine_all_subject_ids(resources)
    all_agent_ids = combine_all_agent_ids(resources)

    copy_resources(repo,
        all_subject_ids,
        label="subjects referenced by resources"
    )

    copy_resources(repo,
        all_agent_ids,
        label="agents referenced by resources"
    )

    print ("done!")

if __name__ == "__main__":
    main()
