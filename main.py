import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="enter the path of the folder to be arranged", type=str, default = os.getcwd())
parser.add_argument("-v","--verbose", action ="count",help="outputs more details")
args = parser.parse_args()
args.path = args.path.replace('~',os.getenv('HOME'))
path = args.path
os.chdir(path)
cdir = os.listdir()
fileindir = [obj.lower for obj in cdir if not os.path.isdir(os.path.join(path, obj))]
dirtype={
"images":['.tif','.tiff','.gif','.jpeg','.jpg','.jif','.jfif','.jp2','.jpx','.j2k','.j2c','.fpx','.pcd','.png'],
"videos":[".mp4",".avi",".mkv",".webm",".flv",'.ogv','.gifv','.mov','.wmv','.m4p','.mpg','.mpeg','.3gp']
}
for obj in list(dirtype.keys()):
    if obj not in cdir:
        os.mkdir(obj)
