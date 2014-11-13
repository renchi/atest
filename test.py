import test_util
import os
import sys
import shutil

INSTALL_Sw = ""
INSTALL_LatestSW = ""

def main():
    SCRIPTPath = os.getcwd()

    srcPath = INSTALL_Sw
    if INSTALL_Sw == "Bugfix_1" and INSTALL_LatestSW == "Yes":
        currentPath = os.getcwd() + "/workdir/swversion"
        srcPath = test_util.latestDir( currentPath )

    print ('srcPath ' + srcPath)

    os.chdir(SCRIPTPath)
    dstPath = os.getcwd() + "/workdir/destfolder"
    print( 'destPath =' + dstPath)

    test_util.del_and_copy(srcPath, dstPath)


if __name__ == '__main__':
    INSTALL_Sw =  sys.argv[1]
    INSTALL_LatestSW = sys.argv[2]
    print "INSTALLSW = " + INSTALL_Sw
    print "INSTALL_LatestSW = " + INSTALL_LatestSW
    main()