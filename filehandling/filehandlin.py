#pathlib.path.exists()
from pathlib import Path
file=Path("F:/Tutedude-py/filehandling/filehandlin.py")

#os.path.exists()

# import os 
# file="F:/Tutedude-py/filehandling/filehandlin.py"

if file.exists():
     print("file exist")

else:
     print("file not ")
     #jo na thay to ahii create no code lkahi nakhvi 





#with ststement

# with open("file3.txt",'r') as fd:
#     content=fd.read()
# print(content)



#mode r.x.w.a.t.b => rt is default mode

# file_handler = open("practice.txt",'rt')
# print(file_handler.read())
# file_handler.close()
# print(file_handler)

# x mode -> crete

# fh=open("file3.txt",'xt')
# fh.write('hello world')
# fh.close()
# fh.write('hello world')

# w mode - open file for write owerwrite file

# fh=open("file3.txt",'wt')
# fh.write('hello world my name is gaurav\n')
# fh.write('hello worldmy dream is big job ')
# fh.write('hello worldmy  ')

# fh.close()


#read operation
#read()
# fd = open("file3.txt", 'rt')
# content1 = fd.read()
# content1 = fd.readline() # read 1 line 
# content1= fd.readlines() # in list print and all is read with \n
# print(content1)       # actual content
# print(type(content1)) # type of returned data

# for line in content1:
    # print(line)
    # print(line.rstrip('\n'))


#'a' mode append 

# fd = open("file3.txt", 'a')
# fd.write("\n i am gaurav mandli ")
# fd.write("\n write now i am pursuing mca ")
# fd.write("\n my skill are java python c++ php ")
