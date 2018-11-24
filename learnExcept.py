def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    print(symbol * width)

temp = (('*',4,4),('#',20,5),('#',3,2),('ZZ',4,6))
for s,w,h in temp:
    try:
        boxPrint(s,w,h)
    except Exception as err:
        print("An exception occured: " + str(err))