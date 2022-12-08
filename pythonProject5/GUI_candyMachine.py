from tkinter import *
from tkinter import messagebox


# Contains the Tk package
Candy_Machine_GUI = Tk()
# List of the product cost.
Candy_Machine__Main = [10,20,15,30]
# Main Title of the Candy Machine
Label(Candy_Machine_GUI, text="Justin's Candy Machine", font=("Helvetica", 18, "bold"), fg="yellow", bg="#114B5F").pack(padx=10,pady=10)
Label(Candy_Machine_GUI, text="Need some sugar? Justin's Candy Machine is at your service. ", font=("Helvetica", 12, "bold"), fg="white", bg="#114B5F").pack(padx=10,pady=1)

# The format of the window
def Candy_Machine_Format():
    Candy_Machine_GUI.geometry('600x330')
    Candy_Machine_GUI.config(bg="#114B5F")
    Candy_Machine_GUI.resizable(0, 0)
    Candy_Machine_GUI.title("Candy Machine: Main window")

Candy_Machine_Format()

#A window that will show a thankyou message.
def thankyoumessage():
    thankyoumessage_GUI = Tk()
    thankyoumessage_GUI.title("Input")
    thankyoumessage_GUI.geometry('600x330')
    thankyoumessage_GUI.config(bg="#114B5F")
    thankyoumessage_GUI.resizable(0, 0)
    Label(thankyoumessage_GUI , text="Thank you! snack well.", font=("Helvetica", 12, "bold"), fg="white",
          bg="#114B5F").pack(padx=10, pady=1)
    Button(thankyoumessage_GUI , text="Okay", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20,
           command= exit).place(x=80, y=80)
def candy_window():
    global candyPay
    candy_GUI = Tk()
    candy_GUI.title("Input")
    candy_GUI.geometry('600x330')
    candy_GUI.config(bg="#114B5F")
    candy_GUI.resizable(0, 0)
    Label(candy_GUI, text="To buy candy, please insert 10 cents. ",font=("Helvetica", 12, "bold"), fg="white", bg="#114B5F").pack(padx=10, pady=1)
    candyPay= Entry(candy_GUI, bg="#C6DABF", width=80 )
    candyPay.place(x= 50, y=50)
    Button(candy_GUI, text="Okay", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = candyPaymentChecker).place(x=80, y=80)
    Button(candy_GUI, text="Cancel", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = candy_GUI.destroy).place(x=300, y=80)


def chips_window():
    global chipsPay
    chips_GUI = Tk()
    chips_GUI.title("Input")
    chips_GUI.geometry('600x330')
    chips_GUI.config(bg="#114B5F")
    chips_GUI.resizable(0, 0)
    Label(chips_GUI, text="To buy chips, please insert 20 cents. ",font=("Helvetica", 12, "bold"), fg="white", bg="#114B5F").pack(padx=10, pady=1)
    chipsPay = Entry(chips_GUI, bg="#C6DABF", width=80)
    chipsPay.place(x= 50, y=50)
    Button(chips_GUI, text="Okay", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = chipsPaymentChecker).place(x=80, y=80)
    Button(chips_GUI, text="Cancel", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = chips_GUI.destroy).place(x=300, y=80)


def gum_window():
    global gumPay
    gum_GUI = Tk()
    gum_GUI.title("Input")
    gum_GUI.geometry('600x330')
    gum_GUI.config(bg="#114B5F")
    gum_GUI.resizable(0, 0)
    Label(gum_GUI, text="To buy gum, please insert 15 cents. ",font=("Helvetica", 12, "bold"), fg="white", bg="#114B5F").pack(padx=10, pady=1)
    gumPay = Entry(gum_GUI, bg="#C6DABF", width=80 )
    gumPay.place(x= 50, y=50)
    Button(gum_GUI, text="Okay", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = gumPaymentChecker).place(x=80, y=80)
    Button(gum_GUI, text="Cancel", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = gum_GUI.destroy).place(x=300, y=80)

def cookies_window():
    global cookiesPay
    cookies_GUI = Tk()
    cookies_GUI.title("Input")
    cookies_GUI.geometry('600x330')
    cookies_GUI.config(bg="#114B5F")
    cookies_GUI.resizable(0, 0)
    Label(cookies_GUI, text="To buy cookies, please insert 30 cents. ",font=("Helvetica", 12, "bold"), fg="white", bg="#114B5F").pack(padx=10, pady=1)
    cookiesPay = Entry(cookies_GUI, bg="#C6DABF",width=80 )
    cookiesPay.place(x= 50, y=50)
    Button(cookies_GUI, text="Okay", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = cookiesPaymentChecker).place(x=80, y=80)
    Button(cookies_GUI, text="Cancel", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=20, command = cookies_GUI.destroy).place(x=300, y=80)
# This is what makes the buttons visible and responsinble in calling their respective functions


def candyPaymentChecker():
    userInput1 = candyPay.get()
    if userInput1  == str(Candy_Machine__Main[0]):
            # It will select the index of the element that match what the user is finding
        thankyoumessage()
    elif userInput1  > str(Candy_Machine__Main[0]):
        messagebox.showerror("Error", "We have received overpayment.\n Received coins are returned")
    elif userInput1  < str(Candy_Machine__Main[0]):
        messagebox.showerror("Error", "Insufficient coins")

def chipsPaymentChecker():
    userInput2 = chipsPay.get()
    if userInput2  == str(Candy_Machine__Main[1]):
            # It will select the index of the element that match what the user is finding
        thankyoumessage()
    elif userInput2 > str(Candy_Machine__Main[1]):
        messagebox.showerror("Error", "We have received overpayment.\n Received coins are returned")
    elif userInput2 < str(Candy_Machine__Main[1]):
        messagebox.showerror("Error", "Insufficient coins")


def gumPaymentChecker():
    userInput3 = gumPay.get()
    if userInput3  == str(Candy_Machine__Main[2]):
             # It will select the index of the element that match what the user is finding
         thankyoumessage()
    elif userInput3 > str(Candy_Machine__Main[2]):
        messagebox.showerror("Error", "We have received overpayment.\n Received coins are returned")
    elif userInput3 < str(Candy_Machine__Main[2]):
        messagebox.showerror("Error", "Insufficient coins")

def cookiesPaymentChecker():
    userInput4 = cookiesPay.get()
    if userInput4  == str(Candy_Machine__Main[3]):
             # It will select the index of the element that match what the user is finding
         thankyoumessage()
    elif userInput4 > str(Candy_Machine__Main[3]):
        messagebox.showerror("Error", "We have received overpayment.\n Received coins are returned")
    elif userInput4 < str(Candy_Machine__Main[3]):
        messagebox.showerror("Error", "Insufficient coins")

def Exit():
    isExit = messagebox.askyesno("Goodbye message", "Do you want to continue")
    if isExit == True:
        Candy_Machine_GUI.destroy()
    else:
        False


def Candy_MachineButtons():
    Button(Candy_Machine_GUI, text="Candy", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=50, command =candy_window).place(x=45, y=80)
    Button(Candy_Machine_GUI, text="Chips", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=50, command = chips_window).place(x=45, y=125)
    Button(Candy_Machine_GUI, text="Gum", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=50, command = gum_window).place(x=45, y=170)
    Button(Candy_Machine_GUI, text="Cookies", font='Calibri 14 bold', bg='turquoise4', foreground="white", width=50,command = cookies_window).place(x=45, y=215)
    Button(Candy_Machine_GUI, text="Exit", font='Calibri 14 bold', bg='turquoise4', foreground="red", width=50, command = Exit).place(x=45, y=260)

Candy_MachineButtons()


Candy_Machine_GUI.mainloop()