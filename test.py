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
    f = open("test.txt", "w+")
    f.write("This is test.")
    f.close()


if __name__== "__main__":
    main()
