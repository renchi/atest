import autotest
import os
import shutil

currentPath = "C:\jenkins\copyfolders\swversion"
srcPath = autotest.latestDir( currentPath )
print ('srcPath ' + srcPath)

dstPath = "C:\jenkins\copyfolders\destFolder"
print( 'destPath =' + dstPath)

autotest.del_and_copy(srcPath, dstPath)
