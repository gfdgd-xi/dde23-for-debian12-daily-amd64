#!/usr/bin/env python3
import os
import json
def ReadTXT(path):
    with open(path, "r")as file:
        things = file.read()
    return things
allList = []
for k in ["build-dde-base.json", "build-dtk.json", "build-other.json", "build.json"]:
    for i in json.loads(ReadTXT(k)):
        allList.append(i)

while True:
    url = input("url>")
    if url in allList:
        print("True")
        continue
    print("False")