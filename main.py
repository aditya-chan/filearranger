import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="enter the path of the folder to be arranged", type=str, default = os.getcwd())
parser.add_argument("-v","--verbose", action ="count",help="outputs more details")
args = parser.parse_args()
args.path = args.path.replace('~',os.getenv('HOME'))
path = args.path
os.chdir(path)
cdir = os.listdir()
fileindir = [obj for obj in cdir if not os.path.isdir(os.path.join(path, obj))]
if __file__ in fileindir: fileindir.remove(__file__)
dirtype={
"images":['.tif','.tiff','.gif','.jpeg','.jpg','.jif','.jfif','.jp2','.jpx','.j2k','.j2c','.fpx','.pcd','.png'],
"videos":[".mp4",".avi",".mkv",".webm",".flv",'.ogv','.gifv','.mov','.wmv','.m4p','.mpg','.mpeg','.3gp'],
"code":[".py",".c",".go"],
"zips":[".zip",".tar",".rar",".7zip",".gz"],
"docs":[".docx",".doc",".pdf",".xls",".ods"],
"torrents":['.torrent'],
"music":[".mp3",".wmv"],
"subtitles":[".srt"],
"others":[]
}
for obj in list(dirtype.keys()):
    if obj not in cdir:
        os.mkdir(obj)
for obj in fileindir:
    for key in dirtype:
        for i in dirtype[key]:
            if i in obj.lower()[(-1*len(i)):]:
                os.rename(os.path.join(path, obj),os.path.join(path,key,obj))
                fileindir.remove(obj)
for obj in fileindir:
    os.rename(os.path.join(path, obj),os.path.join(path,"others",obj))
