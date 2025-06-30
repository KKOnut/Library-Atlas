from tkinter import *
from db_main import *

def get_main_input():
    main_data = (e_isbn.get(), e_title.get(), e_author.get(), e_genre.get(), e_page_count.get(), e_publish_date.get(), e_publisher.get())
    ins_main_data(main_data)

def new_window():
    top_level = Toplevel()
    canvas = Canvas(window, height= 300, width= 300)
    canvas.pack()

#init 
window = Tk()
window.geometry('300x350')
window.title("Library Atlas")


#title
Label(window, text="LibAtlas", font=("Arial", 16, "bold")).place(x=10, y= 30)

#items
Label(window, text="ISBN - 13", font=("Arial", 12)).place(x=10, y= 70)
Label(window, text="Title", font=("Arial", 12)).place(x=10, y= 100)
Label(window, text="Author", font=("Arial", 12)).place(x=10, y= 130)
Label(window, text="Genre", font=("Arial", 12)).place(x=10, y=160)
Label(window, text="Page Count", font=("Arial", 12)).place(x=10, y= 190)
Label(window, text="Publication Date", font=("Arial", 12)).place(x=10, y= 220)
Label(window, text="Publisher", font=("Arial", 12)).place(x=10, y= 250)

#entry
e_isbn = Entry(window)
e_isbn.place(x=140, y=73)

e_title = Entry(window)
e_title.place(x=140, y=103)

e_author = Entry(window)
e_author.place(x=140, y=133)

e_genre = Entry(window)
e_genre.place(x=140, y=163)

e_page_count = Entry(window)
e_page_count.place(x=140, y=193)

e_publish_date = Entry(window)
e_publish_date.place(x=140, y=223)

e_publisher = Entry(window)
e_publisher.place(x=140, y=253)

#button
btn_insert = Button(window, text="INSERT", command=get_main_input)
btn_insert.place(x=10, y= 300)

btn_change = Button(window, text="CHANGE WINDOW", command= new_window)
btn_change.place(x=100, y= 300)



window.mainloop()