
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
window=tk.Tk()
window.title('Scaper Tool')
window.geometry('1000x400')
window.resizable('False','False')
header_frame= tk.Frame(master=window,borderwidth=0,pady=0)
center_frame= tk.Frame(window,borderwidth=0,pady=0)
center_frame.grid(row=1,column=0)
#center=tk.Label(center_frame,bg='yellow',height=8,width=149)

s = IntVar()
a = IntVar()
f = IntVar()
center_1=tk.Frame(center_frame,borderwidth=0,pady=0)
center_2=tk.Frame(center_frame,borderwidth=0,pady=0)
center_3=tk.Frame(center_frame,borderwidth=0,pady=0)

icon=tk.PhotoImage(file = "final1.png")
smaller_image = icon.subsample(2, 2)
centi1=tk.Label(center_1,image=smaller_image,height='120',width='1038')
centi2=tk.Label(center_2,bg="#05ACD3",height='6',width='148')
centi3=tk.Label(center_3,bg="#BBBF95",height='7',width='148')

center_2_1=tk.Frame(center_2,borderwidth=0).grid(row=0,column=0)
center_2_2=tk.Frame(center_2,borderwidth=0).grid(row=0,column=1)
center_2_2=tk.Frame(center_2,borderwidth=0).grid(row=0,column=2)


radiobuts_1=tk.Frame(center_2_1,borderwidth=0).grid(row=0,column=0)
radiobuts_2=tk.Frame(center_2_1,borderwidth=0).grid(row=1,column=0)
radiobuts_3=tk.Frame(center_2_1,borderwidth=0).grid(row=2,column=0)

r1 = Radiobutton(window,text='CSV',value=1 ,variable=a,bg='#05ACD3',fg='white',selectcolor='#05ACD3')
r1.config(font=('helvetica',10,'bold'))
r2 = Radiobutton(window,text='JSON',value=2,variable=a,bg='#05ACD3',fg='white',selectcolor='#05ACD3')
r2.config(font=('helvetica',10,'bold'))
r3 = Radiobutton(window,text='XML',value=3,variable=a,bg='#05ACD3' ,fg='white',selectcolor='#05ACD3')
r3.config(font=('helvetica',10,'bold'))
r1.grid(column=0,row=0)
r2.grid(column=1,row=0)
r3.grid(column=2,row=0)

rr1 = Radiobutton(window,text='CSV',value=1 ,variable=f,bg='#05ACD3',fg='white',selectcolor='#05ACD3')
rr1.config(font=('helvetica',10,'bold'))
rr2 = Radiobutton(window,text='JSON',value=2,variable=f,bg='#05ACD3',fg='white',selectcolor='#05ACD3')
rr2.config(font=('helvetica',10,'bold'))
rr3 = Radiobutton(window,text='XML',value=3,variable=f,bg='#05ACD3' ,fg='white',selectcolor='#05ACD3')
rr3.config(font=('helvetica',10,'bold'))

rrr1 = Radiobutton(window,text='CSV',value=1 ,variable=s,bg='#05ACD3',fg='white',selectcolor='#05ACD3')
rrr1.config(font=('helvetica',10,'bold'))
rrr2 = Radiobutton(window,text='JSON',value=2,variable=s,bg='#05ACD3',fg='white',selectcolor='#05ACD3')
rrr2.config(font=('helvetica',10,'bold'))
rrr3 = Radiobutton(window,text='XML',value=3,variable=s,bg='#05ACD3' ,fg='white',selectcolor='#05ACD3')
rrr3.config(font=('helvetica',10,'bold'))

r1.place(relx=1, x=-750, y=210, anchor='ne')
r2.place(relx=1, x=-742, y=240, anchor='ne')
r3.place(relx=1, x=-750, y=270, anchor='ne')

rr1.place(relx=1, x=-480, y=210, anchor='ne')
rr2.place(relx=1, x=-473, y=240, anchor='ne')
rr3.place(relx=1, x=-480, y=270, anchor='ne')

rrr1.place(relx=1, x=-200, y=210, anchor='ne')
rrr2.place(relx=1, x=-192, y=240, anchor='ne')
rrr3.place(relx=1, x=-200, y=270, anchor='ne')

'''
from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import os
window = Tk()
window.title('spider')
window.geometry('800x500')
window.configure(bg='lightblue')
lbl = Label(window, text='Welcome to our spider',font=('Snap ITC',30))
lbl.grid(column=4,row=1)
s = IntVar()
r1 = Radiobutton(window,text='CSV',value=1 ,variable=s)
r2 = Radiobutton(window,text='JSON',value=2,variable=s)
r3 = Radiobutton(window,text='XML',value=3,variable=s)
r1.grid(column=1,row=2)
r2.grid(column=1,row=3)
r3.grid(column=1,row=4)
lbl2 = Label(window, text='It is flipcart scrapper . which scrap mobile details!1',font=('Snap ITC',10))
lbl2.grid(column=1,row=5) '''
def clickedflipkart():
    p = messagebox.askyesno('Alert', 'really want to scrape!!')
    global prog
    if p==True:
        messagebox.showwarning('Task Running', 'crawler is running wait for message')
        if f.get()==1:
            os.system('scrapy crawl flipcart -o flipkart.csv')
        elif f.get()==2:
            os.system('scrapy crawl flipcart -o flipkart.json')
        else :
            os.system('scrapy crawl flipcart -o flipkart.xml')

        messagebox.showinfo('Task Finished', 'page successfully scrapped!!')
    else :
        messagebox.showinfo('operation Cancelled!!', 'Try again')

def clickedshop():
    p = messagebox.askyesno('Alert', 'really want to scrape!!')
    global prog
    if p==True:
        messagebox.showwarning('Task Running', 'crawler is running wait for message')
        if s.get()==1:
            os.system('scrapy crawl shopclues -o shopclues.csv')
        elif s.get()==2:
            os.system('scrapy crawl shopclues -o shopclues.json')
        else :
            os.system('scrapy crawl shopclues -o shopclues.xml')

        messagebox.showinfo('Task Finished', 'page successfully scrapped!!')
    else :
        messagebox.showinfo('operation Cancelled!!', 'Try again')

def clickedamazon():
    p = messagebox.askyesno('Alert', 'really want to scrape!!')
    global prog
    if p==True:
        messagebox.showwarning('Task Running', 'crawler is running wait for message')
        if a.get()==1:
            os.system('scrapy crawl amazon -o amazon.csv')
        elif a.get()==2:
            os.system('scrapy crawl amazon -o amazon.json')
        else :
            os.system('scrapy crawl amazon -o amazon.xml')

        messagebox.showinfo('Task Finished', 'page successfully scrapped!!')
    else :
        messagebox.showinfo('operation Cancelled!!', 'Try again')


'''
btn = Button(window,text='Start',bg='black',fg='white',command=clicked)
btn.grid(column=1,row=6)

window.mainloop()
'''
center_3_1=tk.Frame(center_3,borderwidth=0).grid(row=0,column=0)
center_3_2=tk.Frame(center_3,borderwidth=0).grid(row=0,column=1)
center_3_2=tk.Frame(center_3,borderwidth=0).grid(row=0,column=2)

centi21=tk.Button(center_3_1, text ="AMAZON", command = clickedamazon,bg='#05ACD3',fg='white')
centi21.place(relx=1, x=-740, y=340, anchor='ne')

centi21=tk.Button(center_3_1, text ="FLIPKART", command = clickedflipkart,bg='#05ACD3',fg='white')
centi21.place(relx=1, x=-480, y=340, anchor='ne')

centi21=tk.Button(center_3_1, text ="SHOPCLUES", command = clickedshop,bg='#05ACD3',fg='white')
centi21.place(relx=1, x=-200, y=340, anchor='ne')

center_1.grid(row=0,column=0)
center_2.grid(row=1,column=0)
center_3.grid(row=2,column=0)


centi1.grid(row=0,column=0)
centi2.grid(row=0,column=0)
centi3.grid(row=0,column=0)


#center.grid(row=0,column=0)
header_frame.grid(row=0,column=0)

header=tk.Label(header_frame,text="SCRAPING WEBSITES TOOL",bg='#012172',fg='white',height='3',width='80',font=('Helvetica 16 bold'))
header.grid(row=0,column=0)
window.mainloop()
