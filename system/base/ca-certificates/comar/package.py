#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/update-ca-certificates --fresh")

def postRemove():
    pass
