"""
Perform tar archive operations based on menu choices.
"""

import os
import sys
import tarfile
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: 'example-2.py <path-to-archive>'.")
    sys.exit()

file_name = sys.argv[1]
if not os.path.exists(file_name):
    print(f"Error: The file '{file_name}' was not found.")
    sys.exit()

if not tarfile.is_tarfile(file_name):
    print(f"Error: The file '{file_name}' is not a tar archive.")
    sys.exit()

print()
print("=============================================")
print("| (1) List files in the archive.            |")
print("| (2) Extract files from the archive.       |")
print("| (3) Show info about files in the archive. |")
print("| (4) Exit.                                 |")
print("=============================================")

command = input("\nEnter the command (a number): ")
if command not in "1 2 3 4".split():
    print("Wrong command. Try again.")
    sys.exit()

if command == "4":
    sys.exit()

with tarfile.open(file_name, "r") as archive:
    if command == "1":
        [print(name) for name in archive.getnames()]

    elif command == "2":
        directory = file_name.split(".tar")[0]
        archive.extractall(directory)
        print(f"Extracted to '{directory}'.")

    elif command == "3":
        pattern = "|{:^18}|{:^7}|{:^8}|{:^21}|{:^10}|{:^11}|"

        header = pattern.format("Name", "Perms", "Size", "Modified", "User", "Group")
        dashes = "-" * len(header)

        print(dashes)
        print(header)
        print(dashes)

        for file in archive:
            print(
                pattern.format(
                    file.name,
                    format(file.mode, "o"),
                    f"{file.size / 1024:.1f}K",
                    str(datetime.fromtimestamp(file.mtime)),
                    file.uname,
                    file.gname,
                )
            )

        print(dashes)
