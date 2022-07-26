from tkinter import  Tk, Text, Button, messagebox

def encrypt():
    txt = in_w.get()
    txt = txt.lower()
    ans = txt.replace('a','~@@@~').replace('b', '~@@@@@@~').replace('c','~@@@@@@@@@~').replace('d', '~@@@@@@@@@@@@~').replace('e','~@@@@@@@@@@@@@@@~').replace('f','~@@@@@@@@@@@@@@@@@@~').replace('g','~@@@@@@@@@@@@@@@@@@@@~').replace('h','~@@@@@@@@@@@@@@@@@@@@@@@@@~').replace('i','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~').replace('j','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@<>@~').replace('k','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[]@@@@~').replace('l','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||@@@@@@@@@@@@@@@~').replace('m', '~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@#@@@@@@@~').replace('n','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^@~').replace('o','~#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######~').replace('p','~$$$$$$$$$$$$$$$$$$$$$$$~').replace('q','~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~').replace('r','~<><><><><><><><>><<>><>><>><<<><><>>>><>~').replace('s','~@@@@@@@@@@@#$$$$$$$$$$$$$@!@@~').replace('t','~@@@@@@@@@@@@@@@@########$$$$$$$$$$$^^^^^^^^^~').replace('u','~``````````````````````````````````````````~').replace('v','~@$#@$#$@#$@#$@#$@#$@#$@#@$@$#@$@#$@#@$@$#@#@$~').replace('w','~@@@@@@@@#$@!#$@#@$@$#@$@$@#@^**&^~').replace('x','~@@@@@@#@@@@@@@@@#@@@@@@#@@@@@@~').replace('y','~@&^&^&^&^&@&^&&@&@^@^&@^&@^&@^&^@~').replace('z','~&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&~').replace(' ','~<<>##$>>>~').replace(',','~^&^&^&^&&^&^^&*<><><<~').replace('.','~<<<<<<<<<<<>>>>>~').replace('?','~$$$$$$$$$$$$$$$$$$$$$$$############~')

def decrypt():
    txt = in_w.get()
    # txt = txt.lower()
    ans = txt.replace('~@@@~','a').replace('~@@@@@@~','b').replace('~@@@@@@@@@~','c').replace( '~@@@@@@@@@@@@~','d').replace('~@@@@@@@@@@@@@@@~','e').replace('~@@@@@@@@@@@@@@@@@@~','f').replace('~@@@@@@@@@@@@@@@@@@@@~','g').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@~','h').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~','i').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@<>@~','j').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[]@@@@~','k').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||@@@@@@@@@@@@@@@~','l').replace( '~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@#@@@@@@@~','m').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^@~','n').replace('~#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######~','o').replace('~$$$$$$$$$$$$$$$$$$$$$$$~','p').replace('~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~','q').replace('~<><><><><><><><>><<>><>><>><<<><><>>>><>~','r').replace('~@@@@@@@@@@@#$$$$$$$$$$$$$@!@@~','s').replace('~@@@@@@@@@@@@@@@@########$$$$$$$$$$$^^^^^^^^^~','t').replace('~``````````````````````````````````````````~','u').replace('~@$#@$#$@#$@#$@#$@#$@#$@#@$@$#@$@#$@#@$@$#@#@$~','v').replace('~@@@@@@@@#$@!#$@#@$@$#@$@$@#@^**&^~','w').replace('~@@@@@@#@@@@@@@@@#@@@@@@#@@@@@@~','x').replace('~@&^&^&^&^&@&^&&@&@^@^&@^&@^&@^&^@~','y').replace('~&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&~','z').replace('~<<>##$>>>~',' ').replace('~^&^&^&^&&^&^^&*<><><<~',',').replace('~<<<<<<<<<<<>>>>>~','.').replace('~$$$$$$$$$$$$$$$$$$$$$$$############~','?')

def about():
    messagebox.showinfo("About Us","An Open Source encrypter that runs a simple algorithm to encrypt. Use it to encrypt text. Support us at https://github.com/sherry65-code/encrypterNXT")
root = Tk()
root.title("Invento Encryptor NXT")
root.geometry("700x300")
root.resizable(0,0)
root.config(bg='#1b1b1c')
in_w = Text(root, bg='#303745',fg='#ffffff', borderwidth=0, highlightthickness=0, relief='flat', width=57, height=15)
in_w.place(x=20, y=20)
f = ("Segoe UI Light",9)
Button(text="Encrypt", fg='#ffffff', bg='#303745',  borderwidth=0, highlightthickness=0, relief='flat', width=32, height=5, command=encrypt, font=f).place(x=435, y=20)
Button(text="Decrypt", fg='#ffffff', bg='#303745',  borderwidth=0, highlightthickness=0, relief='flat', width=32, height=5, command=decrypt,font=f).place(x=435, y=125)
Button(text="About", fg='#ffffff', bg='#303745',  borderwidth=0, highlightthickness=0, relief='flat', width=32, height=2, command=about,font=f).place(x=435, y=230)
root.mainloop()