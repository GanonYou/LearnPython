import zipfile,os

def backupToZip(folder):
    #folder = os.path.abspath(folder)

    #保证每次备份的zip文件名称不同，以_1,_2,_3向后递增
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1
    
    backupZip = zipfile.ZipFile(zipFileName,'w')
    print(zipFileName + " has been created!")

    for root,dirs,files in os.walk(folder):
        print("Adding files in " + root)
        backupZip.write(root)
        for file in files:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backupZip.write(os.path.join(root,file))
    
    backupZip.close()
    print("Done!")

backupToZip('test')
