import tkinter as tk

def check_palindrome():
    input_string = input_entry.get()
    cleaned_string = input_string.lower().replace(" ", "")

    if cleaned_string == cleaned_string[::-1]:
        result_label.config(text=f"'{input_string}' is a palindrome.")
    else:
        result_label.config(text=f"'{input_string}' is not a palindrome.")

root = tk.Tk()
root.title("Palindrome Checker")

input_label = tk.Label(root, text="Enter a word or phrase:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

check_button = tk.Button(root, text="Check Palindrome", command=check_palindrome)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()