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

def main():
    f = open("branch21.txt", "w+")
    f.write("This is component from branch 2.1.")
    f.close()
    
    # clean output directory
    if os.path.exists('Test'):
        shutil.rmtree('Test')


if __name__== "__main__":
    main()
