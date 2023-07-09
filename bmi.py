# import tkinter as tk


# def calculate_bmi():
#     weight = float(weight_entry.get())
#     height = float(height_entry.get())
#     bmi = weight/(height**2)
#     bmi_value.set("BMI : {:.2f}".format(bmi))

#     if bmi<18.5:
#         window.config(bg = "blue")
#         bmi_sign.set("Underweight")
#     elif(bmi>=18.5 and bmi<25):
#         window.config(bg = "green")
#         bmi_sign.set("Healthy")
#     elif(bmi>=25 and bmi<30):
#         window.config(bg = "yellow")
#         bmi_sign.set("Overweight")
#     else:
#         window.config(bg = "red")
#         bmi_sign.set("Obese")

# window = tk.Tk()
# window.minsize(300,200)
# window.title("BMI Calculator")

# weight_label = tk.Label(window, text="Weight (kg):")
# weight_label.pack()
# weight_entry = tk.Entry(window)
# weight_entry.pack()

# height_label = tk.Label(window, text="Height (m):")
# height_label.pack()
# height_entry = tk.Entry(window)
# height_entry.pack()

# bmi_value = tk.StringVar()
# bmi_label = tk.Label(window,textvariable = bmi_value )
# bmi_label.pack()

# calc_button = tk.Button(window,text ="Calculate BMI",command = calculate_bmi )
# calc_button.pack(pady = 20)

# bmi_sign = tk.StringVar()
# bmi_label = tk.Label(window,textvariable = bmi_sign )
# bmi_label.pack()

# window.mainloop()   

