import zipfile

filename="C:\\Users\\13290\\Desktop\\5.zip"

dictFile="pwd.txt"

password=open(dictFile,'r')

for p in password:

    zf=zipfile.ZipFile(filename)

    p=p.strip('\n')

    try:
        zf.extractall("C:\\Users\\13290\\Desktop\\",pwd=p)

        print ("crash. Password is %s" %p)

        exit(0)
    except:
        pass
