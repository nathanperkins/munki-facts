#!/usr/bin/python

'''
modify list of relevant groups in the search_groups list
and this fact will return any of the groups
that the top user belongs to.

designed for utilizing munki-conditions to control
package deployment with active directory groups

upload config/groups.json to your munki server:
https://servername/munkirepo/config/groups.json

by @nathanperkins (GitHub)
https://github.com/nathanperkins/
'''

import subprocess
import json

from Foundation import CFPreferencesCopyAppValue

from facts.helpers.users import get_users


def get_repo_url():
    """ returns the munki repo url set in the ManagedInstalls prefs """
    return CFPreferencesCopyAppValue('SoftwareRepoURL', 'ManagedInstalls')

def get_json_groups():
    """ returns an array of the groups found in the munki repo at config/groups.json """
    json_url = get_repo_url() + "/config/groups.json"

    cmd = ['curl', json_url]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()

    try:
        search_groups = json.loads(out).get("search_groups")
    except ValueError:
        search_groups = ""

    return search_groups

def fact():
    """ returns an array of the groups that the likeliest_user belongs to """
    likeliest_user = get_users(sorted_by='connect_time')[0]
    cmd = ['id', likeliest_user]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()

    search_groups = get_json_groups()
    if not search_groups:
        return {'group_memberships': "JSON file not found."}

    found_groups = []

    for group in search_groups:
        if group in out:
            found_groups.append(group)

    return {
        'group_memberships': found_groups,
    }

if __name__ == '__main__':
    # run with /usr/bin/python
    print fact()
    # print get_json_groups()
