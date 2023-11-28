from tkinter import *
import ssl
import smtplib
from tkinter import messagebox


def send_gmail():

    if True:
        try:

            gmail = gmail_entry.get()
            password = password_entry.get()

            client = client_entry.get()
            
            message = message_entry.get()

            context = ssl.create_default_context()
            port = int(port_entry.get())
            host = host_entry.get()

            email_server = smtplib.SMTP_SSL(host=host_entry.get(),port=port,context=context)
            email_server.login(gmail,password)
            email_server.sendmail(gmail,client,message)

            messagebox.showinfo("Info","Email sent successfully.")

        except ValueError:
            messagebox.showwarning("Warning","Oops!  That was no valid number.  Try again...")


window = Tk()
window.title("Send Gmail")
window.geometry("800x400")

from_frame = Frame(window,bg="Aqua")
from_frame.place(relwidth=0.5,relheight=0.5)

to_frame = Frame(window,bg="Yellow")
to_frame.place(rely=0.5,relwidth=0.5,relheight=0.5)

info_frame = Frame(window,bg="Brown")
info_frame.place(relx=0.5,relwidth=0.5,relheight=1)

from_label = Label(from_frame,text="FROM",width=60,height=1,bg="Aqua",font="Times 20 italic")
from_label.place(x=-120)

gmail_label = Label(from_frame,text="Gmail:",bg="Aqua",font="Helvetica 10 bold")
gmail_label.place(x=50,y=72)

gmail_entry = Entry(from_frame,width=30,bd=5)
gmail_entry.place(x=150,y=70)

password_label = Label(from_frame,text="Password:",bg="Aqua",font="Helvetica 10 bold")
password_label.place(x=50,y=102)

password_entry = Entry(from_frame,width=30,bd=5)
password_entry.place(x=150,y=100)

to_label = Label(to_frame,text="TO",width=60,height=2,bg="Yellow",font="Times 20 italic")
to_label.place(x=-120)

client_label = Label(to_frame,text="Client:",bg="Yellow",font="Helvetica 10 bold")
client_label.place(x=50,y=72)

client_entry = Entry(to_frame,width=30,bd=5)
client_entry.place(x=150,y=70)

to_label = Label(info_frame,text="INFO",width=60,height=2,bg="Brown",font="Times 20 italic")
to_label.place(x=-120,y=80)

message_label = Label(info_frame,text="Message:",bg="Brown",font="Helvetica 10 bold")
message_label.place(x=50,y=162)

message_entry = Entry(info_frame,width=30,bd=5)
message_entry.place(x=150,y=160)

port_label = Label(info_frame,text="Port:",bg="Brown",font="Helvetica 10 bold")
port_label.place(x=50,y=192)

port_entry = Entry(info_frame,width=30,bd=5)
port_entry.place(x=150,y=190)

host_label = Label(info_frame,text="Host:",bg="Brown",font="Helvetica 10 bold")
host_label.place(x=50,y=222)

host_entry = Entry(info_frame,width=30,bd=5)
host_entry.place(x=150,y=220)

send_button = Button(info_frame,text="Send",command=send_gmail,font="Helvetica 10 bold",bg="Gray")
send_button.place(x=225,y=260)

mainloop()
