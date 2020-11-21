import os
mydir = r"E:\Mylearning\Learnings\pyQuestion\delete"
filelist = [ f for f in os.listdir(mydir)]
for f in filelist:
    os.remove(os.path.join(mydir, f))
    os.remove(mydir)
