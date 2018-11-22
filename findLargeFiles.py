import os

for root,dirs,files in os.walk('/Users/YWY'):
    for dirName in dirs:
        if os.path.getsize(os.path.join(root,dirName)) > 1024 * 1024 * 100:
            print(dirName + " is larger than 100MB...")
    for fileName in files:
        #一定要判断一下是否存在该文件，否则会有错误
        #原因是某些实际上已经不存在的文件仍然有记录
        if os.path.exists(os.path.join(root,fileName)):
            if os.path.getsize(os.path.join(root,fileName)) > 1024 * 1024 * 100:
                print(fileName + " is larger than 100MB...")
