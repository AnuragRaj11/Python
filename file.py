# wrt="genius"
# f=open("file.txt","a")
# data=f.write(wrt)
# print(data)
# f.close

with open("file.txt","r") as f:
    print(f.read())