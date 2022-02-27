#!/usr/bin/env python
from argparse import ArgumentError
from argparse import ArgumentParser
import glob
from pathlib import Path


def main():
    parser = ArgumentParser("Post process HebPipe output")
    parser.add_argument("-f", "--folder", metavar="FOLDER", help="Input folder", required=True)
    parser.add_argument("-o", "--output", help='Output folder. If not provided, FOLDER is used')

    args = parser.parse_args()

    if not Path(args.folder).is_dir():
        raise ArgumentError(None, message="--folder must be a valid folder")
    output = args.output or args.folder
    if not Path(output).is_dir():
        raise ArgumentError(None, message="--output must be a valid folder")

    files = glob.glob(str(Path(args.folder) / '*'))

    for fname in files:
        with open(fname) as f:
            lines = [clean_line(line) for line in f.readlines()]
        outname = str(Path(output) / (Path(fname).name + '.out'))
        with open(outname, 'w') as f:
            f.write(' '.join(lines).strip())


def clean_line(line):
    line = line.strip().replace("|", " ")
    if line in ("<s>", "</s>"):
        return '\n'
    else:
        return line


if __name__ == '__main__':
    try:
        main()
    except ArgumentError as e:
        print(e)
        exit(1)
