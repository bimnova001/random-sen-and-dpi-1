from tkinter import *
import random

dpilist = ["400", "800", "1200", "1600", "2000", "2400", "2800"]

def proxd():
    senlist = random.randint(1, 999)
    A = random.choice(dpilist)
    outputdpi.config(text=A, font=("Arial", 12))
    outputsen.config(text="0." + str(senlist), font=("Arial", 12), fg="blue")
    # เพิ่มผลลัพธ์ลงใน Listbox
    results_list.insert(END, f"DPI: {A}, Senlist: 0.{senlist}")

def clean_list():
    # ลบรายการทั้งหมดใน Listbox
    results_list.delete(0, END)

window = Tk()
window.title("APP")
window.geometry("500x500")

text1 = Label(window, text="random sen and dpi")
text1.pack()

b1 = Button(window, text="random now", command=proxd)
b1.pack()

outputsen = Label(window)
outputsen.pack()

outputdpi = Label(window)
outputdpi.pack()

# สร้าง Listbox เพื่อแสดงผลลัพธ์
results_list = Listbox(window)
results_list.pack()

# เพิ่มปุ่ม clean list
clean_button = Button(window, text="Clean List", command=clean_list)
clean_button.pack()

window.mainloop()
