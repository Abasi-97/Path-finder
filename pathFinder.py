import os
import re

rootPath = 'D:'

search = 'question'
escaped = re.escape(search)
pattern = re.compile(escaped.replace(r"\ ", r"\s*"), re.IGNORECASE)
def recursiveDirFinder(root,target):
    dirs = os.listdir(root)
    for dir in dirs:
        try:
            path = os.path.join(root,f"{dir}\\")
            if target.search(dir):
                print(path)
            else:
                if os.path.isdir(path):
                    recursiveDirFinder(path,target)
                else:
                    continue
        except UnicodeEncodeError:
            #print(f"Error processing {dir}")
            continue
        except PermissionError:
            #print(f"{dir} cannot be accessed")
            continue
        except OSError:
            continue

recursiveDirFinder(rootPath,pattern)