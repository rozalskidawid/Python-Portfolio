import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"Your BMI is {bmi:.2f}.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()