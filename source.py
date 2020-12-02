from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image

root = Tk()
root.title("BookMyTicket")
root.geometry('600x400')

# Tab Styling
style = ttk.Style(root)
style.configure("lefttab.TNotebook", tabposition='wn', background='#003399')
style.configure("tab1s.TFrame", background='#cc0000')
style.configure("tab2s.TFrame", background='#3399ff')

# Tab layout
tab_control = ttk.Notebook(root, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control, style='tab1s.TFrame')
tab2 = ttk.Frame(tab_control, style='tab2s.TFrame')
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

# Add tabs to Notebook
tab_control.add(tab1, text=f'{"Home":^30s}')
tab_control.add(tab2, text=f'{"Bookings":^30s}')
tab_control.add(tab3, text=f'{"Seating":^30s}')
tab_control.add(tab4, text=f'{"About":^30s}')
tab_control.pack(expand=1, fill="both")

# HOME
Label1 = Label(tab1, text='Welcome to GJA Theater',
               bg='#ffcc00', font=("Verdana", 24, "bold"))
Label1.grid(row=1, column=2, columnspan=3, pady=70, padx=10)
Label2 = Label(tab1, text='Book your ticket and enjoy the movie', bg='#ffcc00', font=("Verdana", 16, "italic")).grid(
    row=2, column=2, columnspan=3, padx=5)


# Booking Section

# Booking Success
def bookingsuccess():
    # Booking.destroy()
    # showtime.destroy()
    # root.destroy()
    tk.messagebox.showinfo(
        title="Success", message="Your Ticket has been booked successfully \n\n Thank you")

# Final Menu
def menu2():
    Booking = Tk()
    Booking.title("Booking")
    Booking.configure(bg='#2fbdc6')
    Booking.geometry('480x400')

    typeL = Label(Booking, text="Class", bg='#2fbdc6')
    typeL.grid(row=0, column=0, padx=10)

    tickettype = ttk.Combobox(Booking, state='readonly', width=50)
    tickettype['values'] = ("Silver(Rs. 100)", "Gold(Rs. 150)", "Platinum(Rs. 200)")

    tickettype.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

    ticketcountL = Label(Booking, text='No of tickets', bg='#2fbdc6')
    ticketcountL.grid(row=1, column=0, padx=10)

    ticketcount = Entry(Booking, width=50)
    ticketcount.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

    calculate = Button(Booking, text="Calculate", command=lambda: getAmount())
    calculate.grid(row=2, column=2)

    ticketprices = [100, 150, 200]

    totalL = Label(Booking, text='Total =', bg='#2fbdc6')
    totalL.grid(row=3, column=1, padx=10)

    amountdisplay = Entry(Booking, width=10)
    amountdisplay.grid(row=3, column=2, padx=10, pady=10)

    def getAmount():
        numtickets = ticketcount.get()
        selectedtype = tickettype.get()
        j = 0
        for t in tickettype['values']:
            if t == selectedtype:
                break
            else:
                j += 1

        selectedPrice = ticketprices[j]

        amount = selectedPrice * int(numtickets)
        print(amount)
        amountdisplay.insert(END, str(amount))

    nameL = Label(Booking, text='Name', bg='#2fbdc6')
    nameL.grid(row=4, column=0, padx=10)

    namecustomer = Entry(Booking, width=50)
    namecustomer.grid(row=4, column=1, columnspan=4, padx=10, pady=10)

    phoneL = Label(Booking, text='Phone No', bg='#2fbdc6')
    phoneL.grid(row=5, column=0, padx=10)

    phonecustomer = Entry(Booking, width=50)
    phonecustomer.grid(row=5, column=1, columnspan=4, padx=10, pady=10)

    PayemntmodeL = Label(Booking, text='Mode of Payment', bg='#2fbdc6')
    PayemntmodeL.grid(row=6, column=0, padx=10)

    cash = tk.Checkbutton(Booking, text='Cash').grid(row=6, column=1)
    card = tk.Checkbutton(Booking, text='Card').grid(row=6, column=2)

    paynow = Button(Booking, text="Pay Now", width=20,
                    bg='#76c6ba', command=bookingsuccess)

    paynow.grid(row=7, column=1, columnspan=2, pady=20, padx=10)

    displayamount = Text(tab2, height=6, width=40)
    displayamount.grid(row=2, column=1, columnspan=3, pady=30)

    cancel = Button(Booking, text="Cancel", bg='#e31a01',
                    fg='#fff', width=10, command=Booking.destroy)
    cancel.grid(row=7, column=3, pady=20, padx=10)

    Booking.mainloop()


# Timings
def menu1():
    showtime = Tk()
    showtime.title("Show Timings")
    showtime.configure(bg='#5c9e74')
    showtime.geometry('300x250')
    timeL = Label(showtime, text="Select the timings",
                  font=("Times", 16), bg='#5c9e74')
    timeL.grid(row=1, column=1, padx=10, pady=30, columnspan=3)

    timedropdown = ttk.Combobox(showtime, state="readonly", width=10)
    timedropdown['values'] = ("0700", "0930", "1200", "1445", "1805", "2030", "2330")
    timedropdown.grid(row=1, column=4)
    buttoncontinue = Button(showtime, text="Proceed",
                            width=20, bg='#76c6ba', command=menu2)
    buttoncontinue.grid(row=4, column=2, columnspan=2)
    buttoncancel = Button(showtime, text="Cancel", bg='#e31a01',
                          fg='#fff', width=10, command=showtime.destroy)
    buttoncancel.grid(row=4, column=4, pady=10, padx=10)

    showtime.mainloop()


def getMovie():
    # get the selection
    name = moviedropdown.get()

    i = 0
    for m in moviedropdown['values']:
        if name != m:
            i += 1
        else:
            break

    director = directors[i]
    genre = genres[i]
    cast = actors[i]
    rtime = runtimes[i]

    # clear the detail box
    if len(display1.get("1.0", "end-1c")) != 0:
        display1.delete('1.0', END)

    detail1 = "Movie Name: "
    detail2 = "\nDirector: "
    detail3 = "\nGenre: "
    detail4 = "\nCast: "
    detail5 = "\nRunning time(mins): "

    # display in detail box
    display1.insert(END, detail1)
    display1.insert(END, str(name))
    display1.insert(END, detail2)
    display1.insert(END, director)
    display1.insert(END, detail3)
    display1.insert(END, genre)
    display1.insert(END, detail4)
    display1.insert(END, cast)
    display1.insert(END, detail5)
    display1.insert(END, rtime)

    print(name)


movieddL = Label(tab2, text="Movie").grid(row=0, column=0, padx=20)
moviedropdown = ttk.Combobox(tab2, width=50, state="readonly")
moviedropdown['values'] = ("Sholay", "Dilwale Dulhaniya Le Jayenge",
                           "Don", "Dear Zindagi", "Tenet")  # movie names
moviedropdown.grid(row=0, column=1, columnspan=3, padx=20, pady=20)
button1 = Button(tab2, text='Select', bg='#76c6ba', command=lambda: getMovie())
button1.grid(row=1, column=2)

display1 = Text(tab2, height=6, width=40)
display1.grid(row=2, column=1, columnspan=3, pady=30)
directors = ["Ramesh Sippy", "Aditya Chopra",
             "Farhan Akhtar", "Gauri Shinde", "Christopher Nolan"]
genres = ["Action/Drama", "Drama/Romance",
          "Acion/Drama", "Heartfelt/Real", "Drama"]
actors = ["Amitabh Bachchan, Hema Malini, Dharmendra", "Kajol, Shahrukh Khan",
          "Shahrukh Khan, Priyanka Chopra", "Alia Bhatt, Shahrukh Khan", "Robert Pattinson, Dimple Kapadia"]
runtimes = ["180", "150", "140", "130", "120"]
DetailL = Label(tab2, text="Details")
DetailL.grid(row=2, column=0)

# proceed to step 2 Butt
buttonproceed = Button(tab2, text="Proceed to Book",
                       width=25, bg='#76c6ba', command=menu1)
buttonproceed.grid(row=4, column=1, columnspan=2)

# exit button
buttonexit = Button(tab2, text="Exit", bg='#e31a01',
                    fg='#fff', width=10, command=root.destroy)
buttonexit.grid(row=4, column=3)

# About
about_label = Label(
    tab4,
    text="BookMyTicket \n Movie Ticket Booking System \n\n Made by \n Gaurav Kulkarni \n Jui Kulkarni \n Abdul Aseem Shaikh \n(As DSL Mini Project)",
    anchor="center", font=("Times", 20))
about_label.place(x=250, y=160, anchor="center")

root.mainloop()


