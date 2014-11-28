import os
import time
import operator
import shutil

def latestDir(path):
    alist={}
    now = time.time()
    directory=os.path.join(path,"")
    os.chdir(directory)
    for file in os.listdir("."):
        if os.path.isdir(file):
            timestamp = os.path.getmtime( file )
            # get timestamp and directory name and store to dictionary
            alist[os.path.join(os.getcwd(),file)]=timestamp
    # sort the timestamp
    for i in sorted(alist.iteritems(), key=operator.itemgetter(1)):
        latest="%s" % ( i[0])
    print "newest directory is ", latest
    return latest

def del_and_copy(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def copydir(from_path, to_path):
    for root, dirs, files in os.walk(from_path):
        print root, dirs, files
        x = os.listdir(dirs)
        for files in x:
            print files
#        for file in os.listdir(dirs):
#            print file

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        shutil.copyfile(src, dest)
