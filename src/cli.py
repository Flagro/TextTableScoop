import argparse
import argcomplete


def get_args():
    parser = argparse.ArgumentParser(description='Convert project files to text')
    parser.add_argument('path', help='Path to the file or directory')
    parser.add_argument('-t', '--temp', help='Path to a custom temp folder', default=None)
    parser.add_argument('-p', '--project', help='Path to a project folder the file belongs to', default=None)
    parser.add_argument('--ignore', help='Comma-separated list of patterns to ignore', default='')
    argcomplete.autocomplete(parser)
    return parser.parse_args()
