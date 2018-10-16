def printPicnic(dict,lWidth,rWidth):
    print('PICNIC ITEMS'.center(lWidth + rWidth,'-'))
    for k,v in dict.items():
        print(k.ljust(lWidth,'.') + str(v).rjust(rWidth))

picnic = {'sandwiches':4,'apples':12,'cups':4,'cookies':8000}
printPicnic(picnic,12,5)
printPicnic(picnic,20,6)