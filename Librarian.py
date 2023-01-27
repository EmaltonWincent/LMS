import tkinter


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from db import Database




db = Database("Library.db")
librarian = Tk()
librarian.title("Library Management System")
librarian.geometry("1920x1080+0+0")
librarian.config(bg="#2c3e50")
librarian.state("zoomed")

firstName = StringVar()
lastName = StringVar()
dob = StringVar()
dateOfJoin = StringVar()
userName = StringVar()
password = StringVar()

def New_Window():
    Window = Tk.Toplevel()
    canvas = Tk.Canvas(Window, height=10, width=20)
    canvas.pack()


# Entries Frame
entries_frame = Frame(librarian, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Library Management System - Admin Pannel", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnManageBook = Button(btn_frame, command=lambda:New_Window(), text="Manage Book", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnIssueBook = Button(btn_frame, command='', text="Issue Book", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnRegisterMember = Button(btn_frame, command='', text="Register Member", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnManageMember = Button(btn_frame, command='', text="Manage Member", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)

btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnChkOverdueBooks = Button(btn_frame, command='', text="Overdue Book", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)


# def getData(event):
#     selected_row = tv.focus()
#     data = tv.item(selected_row)
#     global row
#     row = data["values"]
#     #print(row)
#     name.set(row[1])
#     isbn.set(row[2])
#     author.set(row[3])
#     publication.set(row[4])
#     status.set(row[5])
#
#
# def dispalyAll():
#     tv.delete(*tv.get_children())
#     for row in db.fetch():
#         tv.insert("", END, values=row)
#
#
# def add_book():
#     if txtName.get() == "" or txtIsbn.get() == "" or txtAuthor.get() == "" or txtPublication.get() == "" or compoStatus.get() == "" :
#         return
#     db.insert(txtName.get(),txtIsbn.get(), txtAuthor.get() , txtPublication.get() ,compoStatus.get())
#     messagebox.showinfo("Success", "Record Inserted")
#     clearAll()
#     dispalyAll()
#
#
#
# def update_book():
#     if txtName.get() == "" or txtIsbn.get() == "" or txtAuthor.get() == "" or txtPublication.get() == "" or compoStatus.get() == "":
#         messagebox.showerror("Erorr in Input", "Please Fill All the Details")
#         return
#     db.update(row[0],txtName.get(), txtIsbn.get(), txtAuthor.get(), txtPublication.get(), compoStatus.get())
#
#     messagebox.showinfo("Success", "Record Update")
#     clearAll()
#     dispalyAll()
#
#
# def delete_book():
#     db.remove(row[0])
#     clearAll()
#     dispalyAll()
#
#
# def clearAll():
#     name.set("")
#     isbn.set("")
#     author.set("")
#     publication.set("")
#     status.set("")
#
#
#
# btn_frame = Frame(entries_frame, bg="#535c68")
# btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
# btnAdd = Button(btn_frame, command=add_book, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
#                 bg="#16a085", bd=0).grid(row=0, column=0)
# btnEdit = Button(btn_frame, command=update_book, text="Update Details", width=15, font=("Calibri", 16, "bold"),
#                  fg="white", bg="#2980b9",
#                  bd=0).grid(row=0, column=1, padx=10)
# btnDelete = Button(btn_frame, command=delete_book, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
#                    fg="white", bg="#c0392b",
#                    bd=0).grid(row=0, column=2, padx=10)
# btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
#                   bg="#f39c12",
#                   bd=0).grid(row=0, column=3, padx=10)
#
# # Table Frame
# tree_frame = Frame(root, bg="#ecf0f1")
# tree_frame.place(x=0, y=480, width=1800, height=520)
# style = ttk.Style()
# style.configure("mystyle.Treeview", font=('Calibri', 14),
#                 rowheight=50)  # Modify the font of the body
# style.configure("mystyle.Treeview.Heading", font=('Calibri', 16))  # Modify the font of the headings
# tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6), style="mystyle.Treeview")
# tv.heading("1", text="ID")
# tv.column("1", width=5)
# tv.heading("2", text="Name")
# tv.heading("3", text="ISBN")
# tv.column("3", width=5)
# tv.heading("4", text="Author")
# tv.column("4", width=10)
# tv.heading("5", text="Publication")
# tv.column("5", width=12)
# tv.heading("6", text="Status")
# tv.column("6", width=10)
# tv['show'] = 'headings'
# tv.bind("<ButtonRelease-1>", getData)
# tv.pack(fill=X)
#
# dispalyAll()


librarian.mainloop()