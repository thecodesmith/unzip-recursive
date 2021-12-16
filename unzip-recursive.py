#!/usr/bin/env python2

# Adapted from this GitHub Gist: https://gist.github.com/pmuellr/706664
# Requires Python 2.x

import os
import sys
import subprocess

#-----------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    helpMessage = """Usage:
    unzip-recursive [files|directories]

Examples:
    unzip-recursive .
    unzip-recursive *.jar *.tar.gz"""

    # Print help and exit 1 if no args provided
    if not args:
        print helpMessage
        sys.exit(1)

    # Print help and exit 0 if help requested
    for arg in sys.argv[1:]:
        if arg in ["help", "--help", "-h"]:
            print helpMessage
            sys.exit()

    # Iterate through files/dirs provided and extract
    for fileName in args:
        if isArchive(fileName):
            unzip(fileName)
        elif os.path.isdir(fileName):
            walkFiles(fileName)
        elif os.path.isfile(fileName):
            continue
        else:
            print "Specified file '%s' does not exist" % fileName

#-----------------------------------------------------------------------------
def unzip(fileName):
    oDir = getExpandedDirName(fileName)

    os.makedirs(oDir)

    print "Processing: %s into: %s" % (fileName, oDir)

    ext = fileName[-4:]

    if ext in [".zip", ".jar"]:
        command = "unzip %s -d %s" % (fileName, oDir)
    else:
        command = "tar xzf %s -C %s" % (fileName, oDir)

    process = subprocess.Popen(command, shell=True)
    status  = os.waitpid(process.pid, 0)[1]

    walkFiles(oDir)

#-----------------------------------------------------------------------------
def walkFiles(dirName):
    print "walking the files of %s" % dirName

    dirs = os.walk(dirName)

    for (dirPath, dirNames, fileNames) in dirs:
        for fileName in fileNames:
            if isArchive(fileName):
                unzip(os.path.join(dirPath, fileName))

#-----------------------------------------------------------------------------
def getExpandedDirName(fileName):
    fileDir  = os.path.dirname(fileName)
    baseName = "%s.contents" % os.path.basename(fileName)

    return os.path.join(fileDir, baseName)

#-----------------------------------------------------------------------------
def isArchive(fileName):
    for ext in [".zip", ".jar", ".tar.gz", ".tgz"]:
        if fileName.endswith(ext):
            return True

    return False

#-----------------------------------------------------------------------------
main()
