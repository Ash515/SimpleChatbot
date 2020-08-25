from tkinter import *
root=Tk()

def send():
    send="you:"+a.get()
    text.insert('end',"\n"+send)
    if(a.get()=='hi'):
        text.insert('end','\n'+"Ash Bot : hello")
    elif(a.get()=='hello'):
        text.insert('end', '\n' + "Ash Bot : hi")
    elif(a.get()=='How are you?'):
        text.insert('end', '\n' + "Ash Bot : I am fine. How are you?")
    elif(a.get()=="I am fine"):
        text.insert('end', '\n' + "Ash Bot : Nice to hear that budy")
    else:
        text.insert('end', '\n' + "Ash Bot : I did't get it.")




root.title("Ashwin's Chatbot.....")
text=Text(root,bg="yellow")
text.grid(row=0, column=0, columnspan=2)
a= Entry(root, width=80)

Send=Button(root, bg='orange', text="Send", width=20,command=send)
Send.grid(row=1,column=1)
a.grid(row=1, column=0)
root.mainloop()


