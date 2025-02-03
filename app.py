import tkinter as tk
from tkinter import messagebox
from func import *

class HealthLifestyle:
    def __init__(self, root):
        self.root = root
        self.root.title("Sleep Disorder Calculator")
        self.root.geometry("500x600")  # Set a larger square window
        self.root.configure(bg="#f0f0f0")
        
        self.setup()

    def setup(self):
        self.title = tk.Label(self.root, text="Sleep Disorder Calculator", font=("Arial", 22, "bold"), bg="#f0f0f0")
        self.title.pack(pady=20)
        
        self.inputs = []
        self.labels = []
        fields = [
            "Input your age:",
            "Input your sleep duration (1-10):",
            "Input your quality of sleep (1-10):",
            "Input your physical activity level (1-100):",
            "Input your stress level (1-10):",
            "Input your sleeping heart rate:"
        ]

        for text in fields:
            label = tk.Label(self.root, text=text, font=("Arial", 12), bg="#f0f0f0")
            label.pack(pady=5)
            entry = tk.Entry(self.root, font=("Arial", 12))
            entry.pack(pady=5, ipadx=5, ipady=3)
            self.labels.append(label)
            self.inputs.append(entry)

        self.start_button = tk.Button(self.root, text="Submit", font=("Arial", 14, "bold"), bg="#007BFF", fg="white", command=self.start)
        self.start_button.pack(pady=20, ipadx=10, ipady=5)

    def start(self):
        try:
            values = []
            for i in range(6):
                value = self.inputs[i].get().strip()
                values.append(float(value))

            disorder_type = calculateHealth(values[0], values[1], values[2], values[3], values[4], values[5])

            result_texts = [
                "🟢 Low probability of having a sleep disorder.",
                "🔴 High probability of having Sleep Apnea.",
                "🔴 High probability of having Insomnia."
            ]

            self.title.pack_forget()
            for input in self.inputs:
                input.pack_forget()
            
            for label in self.labels:
                label.pack_forget()
            self.start_button.pack_forget()

            result_label = tk.Label(self.root, text="The results are in:", font=("Arial", 20, "bold"), bg="#f0f0f0")
            result_label.pack(pady=20)

            outcome_label = tk.Label(self.root, text=result_texts[disorder_type], font=("Arial", 18), bg="#f0f0f0")
            outcome_label.pack(pady=20)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthLifestyle(root)
    root.mainloop()
