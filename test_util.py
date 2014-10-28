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

