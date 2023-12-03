import argparse
import argcomplete


def get_args():
    parser = argparse.ArgumentParser(description='Convert project files to text')
    parser.add_argument('path', help='Path to the file or directory')
    parser.add_argument('-f', '--file', action='store_true', help='Process a single file')
    parser.add_argument('-t', '--temp', help='Path to a custom temp folder', default=None)
    parser.add_argument('--ignore', help='Comma-separated list of patterns to ignore', default='')
    argcomplete.autocomplete(parser)
    return parser.parse_args()
