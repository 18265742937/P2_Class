import tkinter as tk  



window = tk.Tk()


window.title('My Window')


window.geometry('500x300')  

a = "茄子"
b = "西红柿"
def hit_me():
    l = tk.Label(window, text=b, bg='green', font=('Arial', 33), width=500, height=300)
    l.pack() 
    
l = tk.Label(window, text=a, bg='green', font=('Arial', 33), width=500, height=300)
l.pack()

b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()




 


window.mainloop()
