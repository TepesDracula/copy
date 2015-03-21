"""writing a script to copy the content of a folder having multiple folders with multiple files to a single folder"""
#Importing modules

import os
import shutil

#Getting destinatopn Folder
def get_dest():
   get = True
   while get == True:
      dst_name = raw_input("Enter the destination folder : ")
      if os.path.exists(dst_name):
         print "FOLDER ALREADY EXISTS ."
      else :
         return dst_name
         get = False


#Getting source folder
def get_src():
   get = True 
   while get == True:
      src_name = raw_input("Enter the name of the folder where files are : ")
      if os.path.exists(src_name):
         return src_name
         get = False
      else:
         print "Folder Doesn't exist. Try again .."

def copy_file(y):
   files = os.listdir(src+"/"+y)
   for i in files:
      shutil.copy(src+"/"+y+"/"+i,dest)
      print "File : " +src+"/"+ y +"/"+ i
      os.rename(dest+'/'+i,dest+"/"+y+" "+i)
   


print "Welcome to File Copy ..!"
print "We will copy all the files from multiple folders to a single folder."
src = get_src()
dest = get_dest()
os.mkdir(dest)
dirs = os.listdir(src)
for dir in dirs:
   copy_file(dir)
print "DONE ..!"
   




