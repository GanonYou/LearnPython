import webbrowser,sys,pyperclip

if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
else:
    address = pyperclip.paste() #粘贴至address

webbrowser.open('http://www.google.com/maps/place/' + address)
