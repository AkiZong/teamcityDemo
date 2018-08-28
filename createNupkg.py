#!/usr/bin/env python

import argparse
import os
import subprocess
import sys
import shutil
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import re


def replaceVersion (nuspec_path, new_version, branch):
	lowBranch = float(branch)-0.1
	highBranch = float(branch)+0.1
	fh, abs_path = mkstemp()
	with fdopen(fh, 'w') as new_file:
		with open(nuspec_path) as old_file:
			for line in old_file:
				line = re.sub(r'version=""', 'version="(' + str(lowBranch) + ',' + str(highBranch) + ')"', line)
				line = re.sub(r'<version>.*</version>', '<version>' + new_version + '</version>', line)
				new_file.write(line)
	remove(nuspec_path)
	move(abs_path, nuspec_path)


def nugetPack (nuspec_path):
	cmd = 'C:/TeamCity/buildAgent/tools/NuGet.CommandLine.4.7.1/tools/NuGet.exe pack ' + nuspec_path
	os.system(cmd)
	

def copyNupkg (nupkg_id, new_version):
	if os.path.exists('package'):
		shutil.rmtree('package')

	cmd = 'mkdir package'
	os.system(cmd)

	nupkg = nupkg_id + '.' + new_version + '.nupkg'
	cmd = 'xcopy /Y ' + nupkg + ' package'
	os.system(cmd)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Generate NuGet package in TeamCity.")
	parser.add_argument("--nuspec", help="path of .nuspec file")
	parser.add_argument("--new_version", help="new version of nupkg")
	parser.add_argument("--nupkg_id", help="Nupkg ID")
	parser.add_argument("--branch", help="branch ID in repository")

	args = parser.parse_args()

	replaceVersion(args.nuspec, args.new_version, args.branch)
	nugetPack(args.nuspec)
	copyNupkg(args.nupkg_id, args.new_version)
