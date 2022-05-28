
import tkinter as tk  

window = tk.Tk()

window.title('My Window')

window.geometry('500x300') 

var = tk.StringVar()        
l = tk.Label(window, textvariable=var, bg='green', fg='white',  font=('Arial', 12), width=30, height=2)
l.pack()

on_hit = False

ls = ["茄子", "西红柿", "土豆"]
var.set(ls[0])

def hit_me():
    var.set(ls[1])


b = tk.Button(window, text='hit me', font=('Arial', 12),
              width=10, height=1, command=hit_me)
b.pack()

window.mainloop()
