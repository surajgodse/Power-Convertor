from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Power Convertor App")
root.geometry("800x600+50+50")
f = ("Cambria", 30, "bold")
root.configure(bg="lavender blush")


def convert_hp():
	
	value_hpw = ent_value.get()
	if value_hpw == "":
		showerror("issue", "values cannot be empty")
		return

	if value_hpw.isalpha():
		showerror("issue", "values cannot be text")
		return

	if value_hpw.isspace():
		showerror("issue", "values cannot contain spaces")
		return
	try:
		values = float(value_hpw)

		if values < 0:
			showerror("issue", "values cannot be negative")
			return
		if values < 1 or values > 1000:
			showerror("issue", "values must be between 1 and 1000")
			return


		if s.get() == 1:
			result = values * 745.7
			round_result = round(result, 4)
			msg = "horsepower to watts value = " + str(round_result)
			lab_result.configure(text=msg)
			showinfo("Sucess", "success")
			ent_value.delete(0, END)
			ent_value.focus()
			


		else:
			result = values / 745.7
			round_result = round(result, 4)
			msg = "Watts to horsepower value = " + str(round_result)
			lab_result.configure(text=msg)
			showinfo("success", "success")
			ent_value.delete(0, END)
			ent_value.focus()
		
	except Exception:
		showerror("invalid input", "values must be a numeric")
		return
	
	

	
	
		
	
def clear():
	ent_value.delete(0, END)
	ent_value.focus()



lab_title = Label(root, text="Power Convertor", font=f, bg="lavender blush")
lab_title.pack(pady=10)

lab_value = Label(root, text="Enter Value", font=("Arial", 15), bg="lavender blush")
ent_value = Entry(root, font=f, width=15)
lab_value.pack(pady=10)
ent_value.pack(pady=5)

s = IntVar()
s.set(1)
rb_hw = Radiobutton(root, text="Horsepower to Watts", font=("Arial", 15), variable = s, value=1, bg="lavender blush")
rb_wh = Radiobutton(root, text="Watts to Horsepower", font=("Arial", 15), variable= s, value=2, bg="lavender blush")
rb_hw.pack(pady=20)
rb_wh.pack(pady=5)

btn_convert = Button(root, text="convert", font=f, width=8, bg="dodger blue", command=convert_hp)
btn_convert.pack(pady=10)

btn_clear = Button(root, text="Clear", font=f, width=8, bg="red2", command=clear)
btn_clear.pack(pady=10)
lab_result = Label(root, font=f, bg="lavender blush")
lab_result.pack(pady=10)

root.mainloop()