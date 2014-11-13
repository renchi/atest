import test_util
import os
import shutil

def main():
    currentPath = os.getcwd() + "/workdir/swversion"
    srcPath = test_util.latestDir( currentPath )
    print ('srcPath ' + srcPath)

    dstPath = os.getcwd() + "/workdir/destfolder"
    print( 'destPath =' + dstPath)

    test_util.del_and_copy(srcPath, dstPath)


if __name__ == '__main__':
  main()