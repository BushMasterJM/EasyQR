import qrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

#Screen Setup
root = tk.Tk()
root.geometry("500x500")
root.title("EasyQR")
root.configure(background="gray")
root.resizable(width=False, height=False)


def qrcode_maker(data):
    code_image = qrcode.make(data)
    code_image.save("QRCode.png")
    qr_image=ImageTk.PhotoImage(Image.open("QRCode.png"))
    image_dis.configure(image=qr_image)
    image_dis.image=qr_image

def save_qrcode():
    code_image = Image.open("QRCode.png")
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    code_image.save(f"{file_path}")
    
    
#QR Display
qr_image = ImageTk.PhotoImage(Image.open("DefaultQRCode.png"))
image_dis = Label(root, image=qr_image)
image_dis.pack()

#Text Entry
entry = Text(root, height=2, width=36, yscrollcommand=True)
entry.pack()

#Enter Button
e_button = Button(root, text="Create", command=lambda: qrcode_maker(entry.get(1.0, "end-1c")))
e_button.pack()

#Save Button
s_button = Button(root, text="Save", command=save_qrcode)
s_button.pack()




root.mainloop()




