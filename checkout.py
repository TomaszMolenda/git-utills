#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import git
import os

if len(sys.argv) == 1:
    print("Podaj nazwę gałęzi, exit")
    exit()

issueNumber = sys.argv[1]

isReview = False
if len(sys.argv) == 3:
    isReview = sys.argv[2] == 'r'

g = git.Git(os.getcwd())

branches = set([])

for branch in g.branch('-r').split('\n'):
    branches.add(branch.strip())

if not isReview:
    for branch in g.branch().split('\n'):
        branches.add(branch.strip())

tempMatchesBranches = set([])
for branch in branches:
    if not isReview:
        branch = branch.replace('origin/', '')
    if issueNumber.lower() in branch.lower():
        tempMatchesBranches.add(branch)

matchesBranches = list(tempMatchesBranches)

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