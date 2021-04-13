"""
Search for files and show their permissions.
"""

import os
import stat
import subprocess
import sys

file_pattern = input("Enter the file pattern to search for: ")
files = subprocess.getoutput(f"find {file_pattern} -type f").splitlines()

if not files or ("No such file or directory" in files[0]):
    print("No files were found.")
    sys.exit()

for file in files:
    mode = stat.S_IMODE(os.lstat(file).st_mode)

    print(f"\nFile '{file}':")
    for level in ["USR", "GRP", "OTH"]:
        permitions = [
            permition
            for permition in ["R", "W", "X"]
            if mode & getattr(stat, f"S_I{permition}{level}")
        ]
        print(f"{level} permitions: {permitions}")
