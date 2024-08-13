import tkinter
window=tkinter.Tk()
window.minsize(width=300,height=200)
window.title("Mile to Km Converter")

entry_=tkinter.IntVar()
entry=tkinter.Entry(width=10,textvariable=entry_)
entry.grid(row=1,column=1,padx=10,pady=10)
label_M=tkinter.Label(text="Miles").grid(row=1,column=2)

label_ql=tkinter.Label(text="is equal to ").grid(row=2,column=0,padx=10)
label_f=tkinter.Label(text=f"0")
label_f.grid(row=2,column=1)
label_km=tkinter.Label(text="Km").grid(row=2,column=2)
def run():
    x=entry_.get()
    km=round(x*1.609344,2)
    label_f.config(text=km)
cal_button=tkinter.Button(text="Calculate",command=run).grid(row=3,column=1,pady=10)


window.mainloop()