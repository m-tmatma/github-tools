#!/usr/bin/python
#
# MIT License
#
# Copyright (c) [2017] [Masaru Tsuchiyama]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
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
#

"""
enum releases at github.com and returns them as a list
"""
def enum_release(owner, repos):
    import urllib2
    import re
    
    # https://api.github.com/repos/<owner>/<repos>/releases
    URL = '/'.join(["https://api.github.com/repos", owner, repos, "releases"])

    result = urllib2.urlopen(URL)

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
