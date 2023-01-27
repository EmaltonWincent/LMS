from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database



def __init__(self, window):
    self.window = window
    self.flag = 0

    self.frame = Frame(self.window, bg='Orange', width=400, height=300)  # creating frame

db = Database("Library.db")
book = Tk()
book.title("Library Management System")
book.geometry("1920x1080+0+0")
book.config(bg="#2c3e50")
book.state("zoomed")

name = StringVar()
isbn = StringVar()
author = StringVar()
publication = StringVar()
status = StringVar()


        # Entries Frame
entries_frame = Frame(book, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Library Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblIsbn = Label(entries_frame, text="ISBN", font=("Calibri", 16), bg="#535c68", fg="white")
lblIsbn.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtIsbn = Entry(entries_frame, textvariable=isbn, font=("Calibri", 16), width=30)
txtIsbn.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblAuthor = Label(entries_frame, text="Author", font=("Calibri", 16), bg="#535c68", fg="white")
lblAuthor.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtAuthor = Entry(entries_frame, textvariable=author, font=("Calibri", 16), width=30)
txtAuthor.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblPublication = Label(entries_frame, text="Publication", font=("Calibri", 16), bg="#535c68", fg="white")
lblPublication.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtPublication = Entry(entries_frame, textvariable=publication, font=("Calibri", 16), width=30)
txtPublication.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblStatus = Label(entries_frame, text="Status", font=("Calibri", 16), bg="#535c68", fg="white")
lblStatus.grid(row=3, column=0, padx=10, pady=10, sticky="w")
compoStatus = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=status, state="readonly")
compoStatus['values'] = ("Available", "Not_available")
compoStatus.grid(row=3, column=1, padx=10, sticky="w")



def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
        #print(row)
    name.set(row[1])
    isbn.set(row[2])
    author.set(row[3])
    publication.set(row[4])
    status.set(row[5])


def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_book():
    if txtName.get() == "" or txtIsbn.get() == "" or txtAuthor.get() == "" or txtPublication.get() == "" or compoStatus.get() == "" :
        return
    db.insert(txtName.get(),txtIsbn.get(), txtAuthor.get() , txtPublication.get() ,compoStatus.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_book():
    if txtName.get() == "" or txtIsbn.get() == "" or txtAuthor.get() == "" or txtPublication.get() == "" or compoStatus.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtIsbn.get(), txtAuthor.get(), txtPublication.get(), compoStatus.get())

    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_book():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    isbn.set("")
    author.set("")
    publication.set("")
    status.set("")



btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_book, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_book, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_book, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(book, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1600, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 14),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="ISBN")
tv.column("3", width=5)
tv.heading("4", text="Author")
tv.column("4", width=10)
tv.heading("5", text="Publication")
tv.column("5", width=12)
tv.heading("6", text="Status")
tv.column("6", width=10)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
book.mainloop()