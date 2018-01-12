#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import git
import os

if len(sys.argv) == 1:
    print("Podaj nazwę gałęzi, exit")
    exit()

issueNumber = sys.argv[1]

g = git.Git(os.getcwd())

branches = set([])

for branch in g.branch().split('\n'):
    branches.add(branch.strip())

for branch in g.branch('-r').split('\n'):
    branches.add(branch.replace('origin/', '').strip())

matchesBranches = []
for branch in branches:
    if issueNumber.lower() in branch.lower():
        matchesBranches.append(branch)

if len(matchesBranches) == 0:
    print("Nie znaleziono nic, exit")
    exit()

if len(matchesBranches) == 1:
    g.checkout(matchesBranches[0])

if len(matchesBranches) > 1:
    for branch in matchesBranches:
        index = matchesBranches.index(branch)
        print(str(index) + ':' + branch)
    inputIndex = input("Znaleziono więcej niż jedną gałąź, Podaj index: ")
    g.checkout(matchesBranches[int(inputIndex)])