import os
import re
import argparse


def convert_file_from_pokeit_to_h2n(filename, output=False, outputdir=None):
    """Convert file form pokeit format to Hand 2 Note format"""

    if not os.path.isfile(filename):
        raise FileNotFoundError(
            "Could not find the file \"{}\"".format(filename))

    with open(filename, 'r') as f:
        pokeit_lines = f.readlines()

    regex = re.compile(r'[p][p]\d+')

    for i, _ in enumerate(pokeit_lines):
        pokeit_lines[i] = pokeit_lines[i].replace("PokerMaster", "PokerStars")
        # pokeit_lines[i] = pokeit_lines[i].replace("$", "¥")
        # pokeit_lines[i] = pokeit_lines[i].replace("USD", "CNY")
        usernames = regex.findall(pokeit_lines[i])
        if len(usernames) > 0:
            for username in usernames:
                pokeit_lines[i] = pokeit_lines[i].replace(
                    username, username[2:])

    if outputdir is not None:
        filename = filename.split("\\")[-1]
        output_file = os.path.join(outputdir, '{}-converted.txt'.format(filename[:-4]))
        with open(output_file, 'w+') as f:
            f.write("".join(pokeit_lines))
        if output:
            print("Converted {}".format(filename))


if __name__ == '__main__':
    current_dir = os.path.abspath(os.getcwd())
    parser = argparse.ArgumentParser(
        prog='Format Converter for Pokeit to H2N', description="CLI to convert pokeit to H2N")
    parser.add_argument('-f', '--file', type=str,
                        default=None, nargs='*', help='Specify files')
    parser.add_argument('-d', '--dir', type=str, default=".",
                        nargs=1, help='Specify a directory')
    parser.add_argument('-o', '--outputdir', type=str, default=None,
                        nargs=1, help='Specify an output directory')
    args = parser.parse_args()
    if args.outputdir:
        os.makedirs(args.outputdir[0], exist_ok=True)
        if os.path.isabs(args.outputdir[0]):
            outputdir = args.outputdir[0]
        else:
            outputdir = os.path.join(current_dir, args.outputdir[0])
    else:
        outputdir = current_dir
    if args.dir == '.' and not args.file:
        if args.dir == '.':
            dirname = current_dir
            files = os.listdir(current_dir)
        else:
            if os.path.isdir(args.dir[0]):
                dirname = args.dir[0]
                files = os.listdir(dirname)
            else:
                raise FileNotFoundError(
                    "Could not find directory: \"{}\"".format(dirname))
        for i, file in enumerate(files):
            print("\r", "Processing file {:>3} of {:>3}".format(
                i+1, len(files)), end='')
            if file.endswith('.txt') and 'converted' not in file:
                convert_file_from_pokeit_to_h2n(
                    os.path.join(dirname, file), outputdir=outputdir)

    elif args.file:
        files = args.file
        for i, filename in enumerate(args.file):
            print("\r", "Processing file {:>3} of {:>3}".format(
                i+1, len(files)), end='')
            if not os.path.isabs(filename):
                filepath = os.path.join(current_dir, filename)
            else:
                filepath = filename

            if os.path.isfile(filepath):
                convert_file_from_pokeit_to_h2n(filepath, outputdir=outputdir)
            else:
                raise FileNotFoundError(
                    "Specified file \"{}\" not found in current directory \"{}\"".format(filename, current_dir))
