from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
style = ttk.Style()
style.configure('Alarm.TFrame',background = 'black')
style.configure('A.TButton',background = 'white',foreground = 'black')
style.configure('TLabel',background = 'orange')
root.configure(background = 'red')

#-------------------------FIRST FRAME------------------------
frame1 = ttk.Frame(root,width = 50)
frame1.pack()
frame1.config(relief= 'ridge',padding = (30,10),height = 50,width = 60)
style.configure('TFrame',background = 'blue')

                   #LOGO DISPLAY
labellogo= ttk.Label(frame1,text = 'Logo')
logo = PhotoImage(file = "C:\\CF.gif")
slogo = logo.subsample(3,3)
labellogo.config(image = slogo)
labellogo.grid(row=0,column = 0,columnspan = 2,sticky = 'nw')
style.configure('TLabel')
                     #HEADER DISPlay
header = ttk.Label(frame1,text = 'YOUR SUGGESTIONS HERE')
header.grid(row=0,column = 2,sticky = 'n',padx = 5)
header.config(foreground = 'red',background = 'black',font = ('Courier',10,'italic'))

                    #After Header
message = ttk.Label(frame1,text = 'Yogendra Swaroop Srivastava\nComfest\'15 \nJaipuria Computer Club')
message.grid(row = 0,column = 2,columnspan = 2,sticky = 'w',padx = 5)
message.config(foreground = 'Black',background = 'red',font = ('Arial',10,'italic'))

#----------------------SECOND FRAME-------------------------

frame2 =  ttk.Frame(root)
frame2.pack()
frame2.config(relief = 'sunken')
frame2.config(style='Alarm.TFrame')
              #name,email label

labelname =  ttk.Label(frame2,text = 'Name:')
labelname.grid(row = 0, column =0,sticky = 'sw',padx = 5)
labelemail =  ttk.Label(frame2,text  ='Email:')
labelemail.grid(row = 0,column = 4,padx = 5,sticky = 'sw')

            #name,email entry

nameentry = ttk.Entry(frame2,width = 25)
nameentry.grid(row = 2,column = 0,padx = 5,sticky = 'nsew')

emailentry = ttk.Entry(frame2,width = 25)
emailentry.grid(row = 2,column = 4,padx = 5,sticky = 'nsew',type = password)


        #CommentsField
commentlabel = ttk.Label(frame2,text = 'Comments:')
commentlabel.grid(row = 4,column = 0,padx = 5,sticky = 'nsew',ipadx = 5)
text = Text(frame2,width = 30,height = 10)
text.grid(row = 6,column = 0,padx = 5,sticky = 'nsew',ipadx = 5)

    #PhotoComfest
cf = PhotoImage(file = "C:\\CF.gif").subsample(2,2)

labelcf = ttk.Label(frame2,text = 'Comfest')
labelcf.grid(row = 6,column = 4,padx = 5,sticky = 'e')
labelcf.config(image = cf)


#------------Adding Buttons and functions--------
#---Submit Button-------
def submitcall():
    f = open("E:\\file.txt",'a')
    f.writelines('\nName-:')
    f.writelines(nameentry.get())
    f.writelines('\nEMail Address-:')
    f.writelines(emailentry.get())
    f.writelines('\nComments:-')
    f.writelines(text.get('1.0','end'))
    f.close()
    messagebox.showinfo(title = 'Information',message = 'Submitted, Thankyou!')
    print ('Job Done!')

    

submit = ttk.Button(frame2,text = 'Submit',width=10)
submit.grid(row = 10,column = 3,padx = 5,pady = 5,sticky = 'e')
submit.config(command = submitcall)
submit.config(style = 'Alarm.TButton')

#-----Clear Button------

def clearcall():
    nameentry.delete(0,'end')
    emailentry.delete(0,'end')
    text.delete('1.0','end')
    messagebox.showinfo(title = 'Information',message = 'Cleared!')
    print ('Cleared!')

clear = ttk.Button(frame2,text = 'Clear',width = 10)
clear.grid(row = 10,column = 4 ,padx =5,sticky = 'w',pady = 5)
clear.config(command= clearcall)

