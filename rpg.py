from tkinter import *
import random, string
import pyperclip

#Creating a  window
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title(" RANDOM PASSWORD GENERATOR")

bg_photo = PhotoImage(file= "bgg8.png")

# Show image using label
label1 = Label(root, image=bg_photo)
label1.place(x=0, y=0)

# heading
heading = Label(root, text='PYTHON PASSWORD GENERATOR ',fg = "blue",bg = "white", font='Times 12 bold').pack()
Label(root, text= 'Made By: \nGladwin George, Osheen Rawat, Ayan sharma', font='arial 10 bold', fg = "black",bg = "white").pack(side=BOTTOM)


#password length
pass_label = Label(root, text='Select your Password Length \n(min----to----max)' , font='arial 9 bold', fg = "black", bg = "white").pack(pady = 30)
pass_len = IntVar()
length = Scale(root, from_=6, to_=20, variable=pass_len, width=20 ,orient = HORIZONTAL,fg = "white",bg = "orange" ).pack()

#define function
pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


#button
Button(root, text="GENERATE PASSWORD", command=Generator, bg = "red", fg = "white").pack(pady=10)

Entry(root, textvariable=pass_str).pack()


#function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=Copy_password, bg = "green", fg = "white").pack(pady=5)

# loop to run program
root.mainloop()
