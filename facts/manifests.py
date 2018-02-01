#!/usr/bin/python

'''
return a list of manifests that are applied on this machine

by @nathanperkins (GitHub)
https://github.com/nathanperkins/
'''

import os

manifests_dir = '/Library/Managed Installs/manifests'

def fact():
    """ return a list of manifests that are applied on this machine """
    manifests = [x for x in os.walk(manifests_dir)]

    return { 'manifests': manifests }

if __name__ == '__main__':
    # run with /usr/bin/python
    print fact()
