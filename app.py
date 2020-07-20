import tkinter as tk

window = tk.Tk()


frame_1 = tk.Frame(master=window, width=200, height=500, bg="grey")
frame_1.pack(side=tk.LEFT, fill=tk.Y)

frame_2 = tk.Frame(master=window, width=800, height=500)
frame_2.pack(side=tk.RIGHT, fill=tk.BOTH)

label = tk.Label(master=frame_2, text="URL")
entry = tk.Entry(master=frame_2, width="90")
label.place(relx=0.1,rely=0.1)
entry.place(relx=0.2,rely=0.1)

button_enter = tk.Button(master=frame_2, text="Enter")
button_enter.place(relx=0.9,rely=0.1)

button_download = tk.Button(master=frame_2,text="Download")
button_download.place(relx=0.9, rely=0.9)







window.mainloop()