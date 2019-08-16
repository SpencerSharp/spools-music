"""HELLO CLI
Usage:
    hello.py
    hello.py <name>
    hello.py -h|--help
    hello.py -v|--version
Options:
    <name>  Optional name argument.
    -h --help  Show this screen.
    -v --version  Show version.
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DEMO 1.0')
    if arguments['play']:
        play(arguments)
    else:
        init()