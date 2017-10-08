import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("--path", help="enter the path of the folder to be arranged", type=str)
args = parser.parse_args()
if args.path is None:
    args.path = '.'
if '~' in args.path:
    args.path = args.path.replace('~',os.getenv('HOME'))
os.chdir(args.path)
