#!/usr/bin/env python
import os
import sys
import pathlib
import argparse
import jupyter

my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    '--input', help='File to convert', required=True,
)
# mp_parser.add_argument(
#     '-i', '--input_files',

my_parser.add_argument(
    '-o', '--output', help='Output file', required=False,
)

# Verify if the file exists
files_arg = my_parser.parse_args().file
file = pathlib.Path(files_arg)
if not file.exists():
    print(f'File {files_arg} does not exist')
    sys.exit(1)

def main():
    print(f'File Found: {files_arg}')
    print('Full path:', file.resolve())
    os.system(f'jupyter nbconvert --to markdown {files_arg} --output {my_parser.parse_args().output}')
    print(f'Converted to markdown: {my_parser.parse_args().output}')
    print('Done')
    print('Conversion done')
    sys.exit(0)



if __name__ == '__main__':
    main()
    sys.exit(0)



# my_parser.add_argument('--input', '-e', action='store', type=int, required=True, default="0")
# my_parser.add_argument('--id', '-i', action='store', type=int)

# args = my_parser.parse_args()

# print(args.input)
