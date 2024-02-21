from tkinter import *
import tkinter as tk
# creating window
window = Tk()
#creating window size
window.geometry("350x350")
window.title("Simple Calculator App")
window.configure(bg="#FFE5B4")
#adding entry field
Entry_field = Entry(window, width=20,font=('Arial',20),justify='right',bg="white",fg='black',bd=1)
Entry_field.pack()
def button_clicked(btn_text):
    input_text = Entry_field.get()
    if btn_text == '=':
            try:
                result = eval(input_text)
                Entry_field.delete(0, tk.END)
                Entry_field.insert(tk.END, str(result))
            except Exception as e:
                Entry_field.delete(0, tk.END)
                Entry_field.insert(tk.END, 'Error')
    elif btn_text=="AC":
        Entry_field.delete(0,tk.END)
    elif btn_text=="<--":
        Entry_field.delete(0, tk.END)
        input_text = input_text[:len(input_text)-1]
        Entry_field.insert(tk.END, input_text)
    else:
        Entry_field.insert(tk.END,btn_text)
frame = Frame(window)
btns_list = [['AC','%','/','<--'],
             ['7','8','9','*'],
             ['4','5','6','+'],
             ['1','2','3','-'],
             ['0','00','.','=']]
row=0;col=0
for i in range(len(btns_list)):
    for j in range(len(btns_list[0])):
        btn_text = btns_list[i][j]
        btn = Button(frame, text=btn_text, width=8,height=3, font=('Helvetica',9,'bold'),cursor='hand2',relief = FLAT,\
            border=1,  command=lambda text=btn_text: button_clicked(text),bg='#007bff',fg="white")
        btn.grid(row=i, column=j, padx=3, pady=3)
frame.pack()


window.mainloop()