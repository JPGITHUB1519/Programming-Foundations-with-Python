import os
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def rename_files() :
        # 1- get files names froma folder
   
        #we have to put an r in the file string
        
        filelist = os.listdir("C:\Documents and Settings\Secret Message")
        save_path = os.getcwd()
        
        #2 - for each file rename_files
        os.chdir("C:\Documents and Settings\Secret Message")
        for file_name in filelist :
                """
                print file_name
		print "Old name - " + file_name
		print "New name - " + file_name.translate(None, "0123456789")"""

		os.rename(file_name, file_name.translate(None, "0123456789"))
	
        os.chdir(save_path)

rename_files()
