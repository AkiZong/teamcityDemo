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
    
    # clean output directory
    if os.path.exists('Test'):
        shutil.rmtree('Test')
        
    f = open("test22.txt", "w+")
    f.write("This is test of branch 2.2.")
    f.close()
    
    


if __name__== "__main__":
    main()
