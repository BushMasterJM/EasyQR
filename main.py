import qrcode
# import tkinter as tk_
import ttkbootstrap as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

#Screen Setup
root = tk.Window()
# root.geometry("420x560")
root.title("EasyQR")
root.configure(background="gray")
root.resizable(width=False, height=False)

def qrcode_maker(data):
    code_image = qrcode.make(data)
    code_image.save("QRCode.png")
    qr_image=Image.open("QRCode.png")
    qr_image=qr_image.resize((409, 409))
    qr_image=ImageTk.PhotoImage(Image.open("QRCode.png").resize((409, 409)))
    image_dis.configure(image=qr_image)
    image_dis.image=qr_image

def save_qrcode(*burn):
    code_image = Image.open("QRCode.png")
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    code_image.save(f"{file_path}")
    
    
#QR Display
qr_image = ImageTk.PhotoImage(Image.open("DefaultQRCode.png"))
image_dis = Label(root, image=qr_image).grid(row=0, column=0)
#image_dis.pack()

#Text Entry
# entry = Text(root, height=5, width=1, yscrollcommand=True)
entry = Entry(root)
def enter(event):
    qrcode_maker(list(entry.get()))
    s_button.focus()
entry.bind("<Return>", enter)
#entry.pack()
entry.get()
#Enter Button
e_button = Button(root, text="Create", command=lambda: qrcode_maker(entry.get()))

#Save Button
s_button = Button(root, text="Save", command=save_qrcode)
s_button.bind("<Return>", save_qrcode)

#Display stuff
image_dis.grid(column=0, row=0, columnspan=2, sticky="nesw", padx=5, pady=5)
entry.grid(column=0, row=1, columnspan=2, sticky="ew", padx=5)
e_button.grid(column=0, row=3, sticky="ew", padx=5, pady=5)
s_button.grid(column=1, row=3, sticky="ew", padx=5, pady=5)

entry.focus()


# def keypress(event):
#     print([event.char])
# root.bind("<Key>", keypress)

root.mainloop()


