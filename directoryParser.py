import os
rootPath = 'C:\\'
def recursiveDirWalker(root):
    print(root)
    dirs = os.listdir(root)
    for dir in dirs:
        try:
            path = os.path.join(root,f"{dir}\\")
            if os.path.isdir(path):
                recursiveDirWalker(path)
            else:
                print(path)
        except UnicodeEncodeError:
            print(f"Error processing {dir}")
        except PermissionError:
            print(f"{dir} cannot be accessed")

recursiveDirWalker(rootPath)