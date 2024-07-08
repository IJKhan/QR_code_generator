import qrcode
from tkinter import *
from tkinter import messagebox
import time

def reset() :
    webEntry.delete (0, END)
    webEntry.config (bg="white")
    status.config(image="",text="",width=20, height=20)

def QR_gen() :
    fileName = (time.strftime("%Y%m%d-%H%M%S")+".png")
    website = webEntry.get()
    img = qrcode.make(website) 
    img.save(fileName) 
    root.photo = PhotoImage(file=fileName)
    status.config(image=root.photo, text="QR Code Generated Successfully!", fg="green",width=300, height=300)
    messagebox.showinfo("Saved","QR code saved as " + fileName + " successfully")

root = Tk() 
root.title("QR Code Generator")
root.geometry("520x550")
root.resizable (0,0)

appName = Label(root,text="QR CODE GENERATOR", font=("Arial",25,"underline","bold"))
appName.pack()

website = Label(root, text="Enter Website:",font=("Arial",10)) 
website.pack()
webEntry = Entry(root,fg="blue",bd=3,width=40)
webEntry.pack()

getQRCode = Button(root, text="get QR Code",bg="green",fg="white", command=QR_gen)
getQRCode.pack()

resetApp= Button (root, text="Reset",bg="red",fg="white", width=15, bd=3, command=reset)
resetApp.pack()
status = Label(root)
status.pack()

root.mainloop()