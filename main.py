import qrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

#Screen Setup
root = tk.Tk()
root.geometry("370x420")
root.title("EasyQR")
root.configure(background="gray")
root.resizable(width=False, height=False)


def qrcode_maker(data):
    code_image = qrcode.make(data)
    code_image.save("QRCode.png")
    qr_image=Image.open("QRCode.png")
    qr_image=qr_image.resize((370, 370))
    qr_image=ImageTk.PhotoImage(qr_image)
    image_dis.configure(image=qr_image)
    image_dis.image=qr_image

def save_qrcode():
    code_image = Image.open("QRCode.png")
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    code_image.save(f"{file_path}")
    
    
#QR Display
qr_image = ImageTk.PhotoImage(Image.open("DefaultQRCode.png"))
image_dis = Label(root, image=qr_image).grid(row=1, column=1)
#image_dis.pack()

#Text Entry
entry = Text(root, height=1, width=100, yscrollcommand=True).grid(row=1, column=1)
#entry.pack()

#Enter Button
e_button = Button(root, text="Create", command=lambda: qrcode_maker(entry.get(1.0, "end-1c"))).grid(row=1, column=1)
#e_button.pack()

#Save Button
s_button = Button(root, text="Save", command=save_qrcode).grid(row=1, column=1)
#s_button.pack()




root.mainloop()




