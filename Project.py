from tkinter import *
import pyscreenrec

root=Tk()
root.geometry("450x570")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(True,True)

def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec=pyscreenrec.ScreenRecorder()

# This Sets Icon of Program (Present at left corner)

Photo_icon=PhotoImage(file="record.png")
root.iconphoto(False,Photo_icon)

image1=PhotoImage(file="blue.png")
Label(root,image=image1,bg="#fff").place(x=-20,y=35)

image2=PhotoImage(file="yelllow.png")
Label(root,image=image2,bg="#fff").place(x=325,y=200)

lbl=Label(root,text="Screen Record",bg="#fff",font="arial 20 bold")
lbl.pack(pady=20)

image3=PhotoImage(file="recording.png")
Label(root,image=image3,bd=0).pack(pady=30)

Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=14,font="arial 15")
entry.place(x=125,y=350)
Filename.set("Untitled")

Start=Button(root,text="Start",font="arial 20",bd=0,command=start_rec)
Start.place(x=160,y=260)

image4=PhotoImage(file="pause.png")
pause=Button(root,image=image4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=50,y=450)

image5=PhotoImage(file="resume.png")
resume=Button(root,image=image5,bd=0,bg="#fff",command=resume_rec)
resume.place(x=150,y=450)

image6=PhotoImage(file="stop.png")
stop=Button(root,image=image6,bd=0,bg="#fff",command=stop_rec)
stop.place(x=250,y=450)



root.mainloop()