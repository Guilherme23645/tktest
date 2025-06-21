import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()

window.title('Simple GUI')

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def load_image(path, width=None, height=None):
	img = Image.open(path)
	if width and height:
		img = img.resize((width,height))
	return ImageTk.PhotoImage(img)

def your_name():
	response.config(text=f"Name: {txt.get('1.0','end-1c')}")
	txt.delete('1.0', tk.END)

label = tk.Label(window,text="Tell us who you are")
label.pack(pady=(10,10))

tk_image = load_image('user.png',200,200)
lblImage = tk.Label(window, image=tk_image)
lblImage.pack()

caption = tk.Label(window, text='(Please upload your photo)')
caption.pack(pady=(0,10))

txt = tk.Text(window, height=1, width=15)
txt.pack(pady=(0,10))

btn = tk.Button(window, text='Submit', command=your_name)
btn.pack(pady=(0,10))

response = tk.Label(window, text='')
response.pack()

window.mainloop()
