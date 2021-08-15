import tkinter as tk
from tkinter import filedialog, Text
import os     #interact with OS

root = tk.Tk()  # The whole structure
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt","r") as f:
        tmpapp=f.read()
        tmpapp = tmpapp.split(",")
        apps = [x for x in tmpapp if x.strip()]
        

def addapp(): #<- Function required for running the app.

    for widget in frame.winfo_children():
        widget.destroy()
        
    filename = filedialog.askopenfilename(initialdir="/", title = "Select File", filetypes = (("executables","*.exe"),("allfiles","*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "grey")
        label.pack()

def runapp():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height = 700, width = 700, bg = "black") #Canvas to add colours and
canvas.pack()#structure to the dialog box. Where to attach canvas? -> To root

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

#buttons
openFile = tk.Button(root,text = "Open File", padx = 10, pady=5, fg="white", bg = "black", command = addapp)

openFile.pack()  #<- This one is to attach to the root file

runFile = tk.Button(root,text = "Run!", padx = 10, pady=5, fg="white", bg = "black", command= runapp)

runFile.pack()  #<- This one is to attach to the root file




 
root.mainloop()   #To run

for app in apps:
    label = tk.Label(frame,text =app)
    label.pack()


with open("saved.txt","w") as f:
    for app in apps:
        f.write(app + ',')
    
