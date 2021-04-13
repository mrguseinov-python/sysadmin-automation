"""
Check for running processes and show information about them.
"""

import subprocess
import sys

program_name = input("Enter the name of the program to check: ")

processes = subprocess.getoutput(f"ps -aux | grep {program_name}").splitlines()
processes = [process for process in processes if f"grep {program_name}" not in process]

if not processes:
    print("No processes were found.")
    sys.exit()

for process in processes:
    data = process.split()
    print()
    print(f"Owner:             {data[0]}")
    print(f"Process ID:        {data[1]}")
    print(f"CPU Usage, %:      {data[2]}")
    print(f"Memory usage, %:   {data[3]}")
    print(f"Memory usage, KiB: {data[4]}")
    print(f"Starting time:     {data[8]}")
    print(f"Command:           {data[10]}")
