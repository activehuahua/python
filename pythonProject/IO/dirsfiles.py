import os

root=r"E:\pythonProject"
def gci(path):
    parents=os.listdir(path)
    for parent in parents:
        child=os.path.join(path,parent)
        if os.path.isdir(child):
            print(child)
            gci(child)
        else:
            print('\t',child)

gci(root)
