import test_util
import os
import sys
import shutil

INSTALL_Sw = ""
INSTALL_LatestSW = ""

def main():
    dstPath = os.getcwd() + "/workdir/destfolder"
    if INSTALL_Sw == "Bugfix_1":
        currentPath = os.getcwd() + "/workdir/swversion"
        srcPath = test_util.latestDir( currentPath )
        test_util.del_and_copy(srcPath, dstPath)
    else:
        srcPath = INSTALL_Sw
        os.path.dirname(srcPath)
        test_util.del_and_copy(srcPath, dstPath)

if __name__ == '__main__':
    INSTALL_Sw =  sys.argv[1] 
    print( "INSTALLSW = " + INSTALL_Sw )

    main()
