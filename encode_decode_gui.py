from tkinter import *
import base64

root=Tk()   #builds basic components
root.title("Encode and Decode")
# photo = PhotoImage(file = "py.png")
# root.iconphoto(False, photo)

#width x height
root.geometry("600x350")
root.resizable(0,0)

#variables
message=StringVar()
key=StringVar()
m=StringVar()
res=StringVar()

#message
Label(text=" Enter the Message : ",font="arial 13",bg="light yellow",borderwidth=2,relief="groove").place(x=100,y=64)  #creates 
Entry(root,textvariable=message,font = 'arial 13', fg='black', bg = 'light blue',borderwidth=2,relief="groove").place(x=280, y = 66)

#key
Label(text=" Enter the Key\t: ",font="arial 13",bg="light yellow",borderwidth=2,relief="groove").place(x=100,y=100) 
Entry(root,textvariable=key,font = 'arial 13', fg='black', bg = 'light blue',borderwidth=2,relief="groove").place(x=280, y = 100)

#mode   
Label(text="Select Mode (1/2)\t: ",font="arial 13",bg="light yellow",borderwidth=2,relief="groove").place(x=100,y=136) 
Entry(root,textvariable=m,font = 'arial 13', fg='black', bg = 'light blue',borderwidth=2,relief="groove").place(x=280, y = 134)

def encode():
    enc=[]
    mess = message.get()
    keys=key.get() 
    for i in range(len(mess)):       
        ki = keys[i % len(keys)] 
        enc.append(chr((ord(mess[i]) + ord(ki)) % 256)) 
    e=base64.b64encode("".join(enc).encode()).decode()
    print(e)
    return e

def decode():
    dec=[]
    mess = message.get()
    keys=key.get()
    mess = base64.b64decode(mess).decode()
    print(mess)
    for i in range(len(mess)):
        ki = keys[i % len(keys)]                              
        dec.append(chr((256 + ord(mess[i])- ord(ki)) % 256))    
    d="".join(dec)
    return d

def method():
    mode=m.get()
    if(mode=='1'):
        res.set(encode())
    elif(mode=='2'):
        res.set(decode())
    else:
        res.set("Select Valid Mode")
       

#result
Label(text="Output\t:",font="arial 13",bg="light yellow",borderwidth=3,relief="groove").place(x=174,y=250)
Button(root, font = 'arial 10', text = 'RESULT'  ,bg ='lime green' ,command = method,relief="groove").place(x=340, y = 190)
Entry(root, textvariable = res,font = 'arial 13',fg='black', bg = 'ghost white',borderwidth=3,relief="groove").place(x=277, y = 250)


root.mainloop()  