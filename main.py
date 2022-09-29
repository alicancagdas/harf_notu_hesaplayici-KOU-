# harf notu uygulaması
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import *

root = Tk()


photo = PhotoImage(file=r"image1.png")
photo1 = PhotoImage(file=r"zyro-image (2).png")



Button(root, text='Click Me !', image=photo).place(x=788,y=20)
Button(root, text='Click Me !', image=photo1).place(x=650,y=150)




root.title("HARF NOTU HESAPLAYICI")
root.geometry("1200x500")
root.config(bg="grey")





def butonBas():
    finalyuzde = int(ent1.get())
    vizenotu = float(ent2.get())
    finalnotu = float(ent3.get())
    sinifort = float(ent4.get())
    ssapma = float(ent5.get())


    ortalama = ((finalnotu * finalyuzde) + (vizenotu * (100 - finalyuzde))) / 100

    Tpuani = 0
    if sinifort < 42.5:
        Tpuani = (((ortalama - sinifort) / ssapma) * 10) + 50

    elif 80 <= sinifort:
        Tpuani = ortalama
    elif 42.5 <= sinifort < 80:
        Tpuani = (((ortalama - sinifort) / ssapma) * 10) + 50
    if finalnotu < 40:
        e7.config(text="BASARISIZ")

        Tpuani = 1.0

    if 80 <= sinifort < 100:
        if Tpuani < 30:
            e7.config(text="FF,BASARISIZ")

        if 30 <= Tpuani < 40:
            e7.config(text="FD,BASARISIZ")

        if 40 <= Tpuani < 50:
            e7.config(text="DD,BASARISIZ")

        if 50 <= Tpuani < 60:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 60 <= Tpuani < 70:
            e7.config(text="CC,BASARILI")

        if 70 <= Tpuani < 75:
            e7.config(text="CB,BASARILI")

        if 75 <= Tpuani < 85:
            e7.config(text="BB,BASARILI")

        if 85 <= Tpuani < 90:
            e7.config(text="BA,BASARILI")

        if 90 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 70 <= sinifort < 80:
        if Tpuani < 24:
            e7.config(text="FF,BASARISIZ")

        if 24 <= Tpuani < 29:
            e7.config(text="FD,BASARISIZ")

        if 29 <= Tpuani < 34:
            e7.config(text="DD,BASARISIZ")

        if 34 <= Tpuani < 39:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 39 <= Tpuani < 44:
            e7.config(text="CC,BASARILI")

        if 44 <= Tpuani < 49:
            e7.config(text="CB,BASARILI")

        if 49 <= Tpuani < 54:
            e7.config(text="BB,BASARILI")

        if 54 <= Tpuani < 59:
            e7.config(text="BA,BASARILI")

        if 59 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 62.5 < sinifort < 70:
        if Tpuani < 26:
            e7.config(text="FF,BASARISIZ")

        if 26 <= Tpuani < 31:
            e7.config(text="FD,BASARISIZ")

        if 31 <= Tpuani < 36:
            e7.config(text="DD,BASARISIZ")

        if 36 <= Tpuani < 41:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 41 <= Tpuani < 46:
            e7.config(text="CC,BASARILI")

        if 46 <= Tpuani < 51:
            e7.config(text="CB,BASARILI")

        if 51 <= Tpuani < 56:
            e7.config(text="BB,BASARILI")

        if 56 <= Tpuani < 61:
            e7.config(text="BA,BASARILI")

        if 61 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 57.5 < sinifort < 62.5:
        if Tpuani < 28:
            e7.config(text="FF,BASARISIZ")

        if 28 <= Tpuani < 33:
            e7.config(text="FD,BASARISIZ")

        if 33 <= Tpuani < 38:
            e7.config(text="DD,BASARISIZ")

        if 38 <= Tpuani < 43:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 43 <= Tpuani < 48:
            e7.config(text="CC,BASARILI")

        if 48 <= Tpuani < 53:
            e7.config(text="CB,BASARILI")

        if 53 <= Tpuani < 58:
            e7.config(text="BB,BASARILI")

        if 28 <= Tpuani < 63:
            e7.config(text="BA,BASARILI")

        if 63 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 52.5 < sinifort < 57.5:
        if Tpuani < 30:
            e7.config(text="FF,BASARISIZ")

        if 30 <= Tpuani < 35:
            e7.config(text="FD,BASARISIZ")

        if 35 <= Tpuani < 40:
            e7.config(text="DD,BASARISIZ")

        if 40 <= Tpuani < 45:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 45 <= Tpuani < 50:
            e7.config(text="CC,BASARILI")

        if 50 <= Tpuani < 55:
            e7.config(text="CB,BASARILI")

        if 55 <= Tpuani < 60:
            e7.config(text="BB,BASARILI")

        if 60 <= Tpuani < 65:
            e7.config(text="BA,BASARILI")

        if 65 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 47.5 < sinifort < 52.5:
        if Tpuani < 32:
            e7.config(text="FF,BASARISIZ")

        if 32 <= Tpuani < 37:
            e7.config(text="FD,BASARISIZ")

        if 37 <= Tpuani < 42:
            e7.config(text="DD,BASARISIZ")

        if 42 <= Tpuani < 47:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 47 <= Tpuani < 52:
            e7.config(text="CC,BASARILI")

        if 52 <= Tpuani < 57:
            e7.config(text="CB,BASARILI")

        if 57 <= Tpuani < 62:
            e7.config(text="BB,BASARILI")

        if 62 <= Tpuani < 67:
            e7.config(text="BA,BASARILI")

        if 67 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 42.5 < sinifort < 47.5:
        if Tpuani < 34:
            e7.config(text="FF,BASARISIZ")

        if 34 <= Tpuani < 39:
            e7.config(text="FD,BASARISIZ")

        if 39 <= Tpuani < 44:
            e7.config(text="DD,BASARISIZ")

        if 44 <= Tpuani < 49:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 49 <= Tpuani < 54:
            e7.config(text="CC,BASARILI")

        if 54 <= Tpuani < 59:
            e7.config(text="CB,BASARILI")

        if 59 <= Tpuani < 64:
            e7.config(text="BB,BASARILI")

        if 64 <= Tpuani < 69:
            e7.config(text="BA,BASARILI")

        if 69 <= Tpuani:
            e7.config(text="AA,BASARILI")

    if 0 <= sinifort < 47.5:
        if Tpuani < 36:
            e7.config(text="FF,BASARISIZ")

        if 36 <= Tpuani < 41:
            e7.config(text="FD,BASARISIZ")

        if 41 <= Tpuani < 46:
            e7.config(text="DD,BASARISIZ")

        if 46 <= Tpuani < 51:
            e7.config(text="DC,DC ntou kosullu gecme notudur")

        if 51 <= Tpuani < 56:
            e7.config(text="CC,BASARILI")

        if 56 <= Tpuani < 61:
            e7.config(text="CB,BASARILI")

        if 61 <= Tpuani < 66:
            e7.config(text="BB,BASARILI")

        if 66 <= Tpuani < 71:
            e7.config(text="BA,BASARILI")

        if 71 <= Tpuani:
            e7.config(text="AA,BASARILI")
    round(Tpuani, 6)
    str(Tpuani)
    e8.config(text=Tpuani)


def temizle():
    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete(0, tk.END)
    ent5.delete(0, tk.END)
    e7.config(text="HARF NOTU")
    e8.config(text="TPUANI")


e1 = tk.Label(text="Final yüzdesi", font="Arial 12 bold")
e1.place(x=15, y=10)
ent1 = tk.Entry(width=30)
ent1.place(x=200, y=10)

e2 = tk.Label(text="Vize notu", font="Arial 12 bold")
e2.place(x=15, y=60)
ent2 = tk.Entry(width=30)
ent2.place(x=200, y=60)

e3 = tk.Label(text="Final notu", font="Arial 12 bold")
e3.place(x=15, y=110)
ent3 = tk.Entry(width=30)
ent3.place(x=200, y=110)

e4 = tk.Label(text="Sınıf ortalamasi", font="Arial 12 bold")
e4.place(x=15, y=160)
ent4 = tk.Entry(width=30)
ent4.place(x=200, y=160)

e5 = tk.Label(text="Standart Sapma", font="Arial 12 bold")
e5.place(x=15, y=210)
ent5 = tk.Entry(width=30)
ent5.place(x=200, y=210)

b1 = tk.Button(text="Hesapla", bg="red", fg="white", font="Arial 16 bold",  command=butonBas)
b1.place(x=30, y=350)
b2 = tk.Button(text="Temizle", bg="red", fg="white", font="Arial 16 bold", command=temizle)
b2.place(x=330, y=350)

e7 = tk.Label(text="Harf Notunuz: ----", font="Arial 12 bold", fg="blue")
e7.place(x=30, y=300)

e8 = tk.Label(text="Tpuaniniz: ----", font="Arial 12 bold", fg="blue")
e8.place(x=330, y=300)

root.mainloop()

