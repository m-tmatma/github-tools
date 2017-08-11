#!/usr/bin/python
#
#   This script enumerates releases for github.com
#
#   usage: ./enum-releases.py owner repos
#
#   example
#       $ ./enum-releases.py m-tmatma CopyWithLineNumbers
#       
#       This script accesses the following site, extract the release versions, and show them.
#       https://api.github.com/repos/m-tmatma/CopyWithLineNumbers/releases

"""
enum releases at github.com and returns them as a list
"""
def enum_release(owner, repos):
    import urllib2
    import re
    import json
    
    # https://api.github.com/repos/owner/repos/releases
    URL = '/'.join(["https://api.github.com/repos", owner, repos, "releases"])

    result = urllib2.urlopen(URL)
    length = result.headers['content-length']

    #json_dict = json.load(result)
    #print json_dict

    # "tag_name":"x.xx.x"
    re_release = re.compile(r'"tag_name":"(?P<version>.+?)",')

    content = ""
    for data in result:
        content += data

    releases = []
    iterator = re_release.finditer(content)
    for match in iterator:
        group = match.group('version')
        releases.append(group)

    return releases

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) != 3:
        print "usage:  " + sys.argv[0] + " owner repos"
        print "example: "+ sys.argv[0] + " m-tmatma CopyWithLineNumbers"
        sys.exit(0)

    owner = sys.argv[1]
    repos = sys.argv[2]
    releases = enum_release(owner, repos)

    for release in releases:
        print release
