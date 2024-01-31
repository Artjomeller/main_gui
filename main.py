from tkinter import *
from tkinter import ttk, messagebox

"""
Paiguta aknale uus label(olemasolevale framele) uus label. 
Label näitab hiire x ja y koordinate kujul x, y ehk 281, 123
label.config(text='Mida Näidata') Muudab labeli teksti
"""
def welcome(event):
    name = txt_name.get().strip().title()
    if name:
        text = f"Tere {name}"
        messagebox.showinfo(title="Tervitus", message=text)
    else:
        messagebox.showerror(title="Viga", message="Nime pole sisestatud!")
   # print(name)   # Testimiseks

def mouse_motion(event):
    x, y = event.x, event.y
    # print('x={}, y={}'.format(x, y))
    # lbl_cordinates.config(text=f'x:{x}, y:{y}')
    lbl_mouse.config(text=f'x:{x}, y:{y}')



window = Tk()
window.title("Simple GUI")
window.geometry("400x350")   # 300 korda 250 pikslit laius,kõrgus

# Frame loomine
frame = Frame(window, bg='orange')  # Värv
frame.pack(expand=True, fill='both')

# Label frame-ile
lbl_name = Label(frame, text='Sisesta nimi')   # Teksti sisu
# lbl_name.place(x=5, y=5)    # Koha määramine
# lbl_name.grid(row=0, column=0)
lbl_name.pack(side='left', anchor='n', padx=2, pady=5)
# lbl_cordinates = Label(frame)
# lbl_cordinates.pack(side='left', anchor='n', padx=2, pady= 5)

# Sisestus kasti tegemine
txt_name = Entry(frame)
# txt_name.place(x=80, y=5)
# txt_name.grid(row=0, column=1)
txt_name.pack(side='left', anchor='n', padx=2, pady=5)
txt_name.focus()  # Teeb sisetus kasti aktiivseks

# Sisestus nupp
btn_submit = Button(frame, text='Kliki mind', command=lambda: welcome(""))
# btn_submit.place(x=90, y=40)
# btn_submit.grid(row=1, column=1, sticky='ew')
btn_submit.pack(side='left', anchor='n', padx=2, pady=5)

# Hiire koordinaadid labelil
lbl_mouse = Label(frame, text='Koordinaadid', bg='orange', fg='yellow')
lbl_mouse.pack(side='left', anchor='n', padx=2, pady=5)

# Kuula ENTER klahvi vajutust
window.bind("<Return>", welcome)
window.bind("<Motion>", mouse_motion)  # Kuulab/vaatab kus on hiir

window.mainloop()