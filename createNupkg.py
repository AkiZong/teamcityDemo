#!/usr/bin/env python

import argparse
import os
import subprocess
import sys
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove


def replaceVersion (nuspec_path, new_version):
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(nuspec_path) as old_file:
            for line in old_file:
                new_file.write(line.replace("<version>1.0.0</version>", "<version>"+new_version+"</version>"))
    remove(nuspec_path)
    move(abs_path, nuspec_path)

def nugetPack (nuspec_path):
	# cmd = 'C:/Users/bzong/Desktop/installPkg/nuget.exe pack ' + nuspec_path
	cmd = 'C:/TeamCity/buildAgent/tools/NuGet.CommandLine.4.7.1/tools/NuGet.exe pack ' + nuspec_path
	os.system(cmd)

def copyNupkg (nuspkg_id, new_version):
	cmd = 'mkdir package'
	os.system(cmd)

	nuspkg = nuspkg_id + "." + new_version + '.nupkg'
	cmd = 'xcopy /Y ' + nuspkg + ' package'
	os.system(cmd)

	# xcopy /Y .\%newPkgName% .\package

if __name__ == "__main__":
	for arg in sys.argv[1:]:
		print arg

	# argv[1] - nuspec_path
	# argv[2] - new_version
	# argv[3] - nuspkg_id
	replaceVersion(sys.argv[1], sys.argv[2])
	nugetPack(sys.argv[1])
	copyNupkg(sys.argv[3], sys.argv[2])


