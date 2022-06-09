import tkinter as tk
from tkinter  import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os 

root = tk.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.state('zoomed')
root.title('dotpdf-v-1')
root.configure(bg='white')

def browseFiles():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
    title='Select pdf file',
    filetype=(('PDF File','.pdf'),
              ('PDF File','.PDF'),
              ('ALL file','.txt')))
    v1=pdf.ShowPdf()
    v2=v1.pdf_view(root,pdf_location=open(filename,'r'),width=150,height=100)
    v2.pack(pady=(0,0))

def do_zoom():
    if(str1=='plus'):
        font1[1]=font1[1]+2
    else:
        font1[1]=font1[1]-2
    t1.config(font=font1)

# create a button here 
tk.Button(root,text='open', command=browseFiles, width=40,
font='arial 20',bd=4).pack()

b1=tk.Button(root,text='+',command=lambda:do_zoom(str1)('plus'))

b2=tk.Button(root,text='-',command=lambda:do_zoom(str1)('minus'))



root.mainloop()
