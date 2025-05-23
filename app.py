from pyexpat import model
import tkinter as tk
from tkinter import messagebox
from func import *

class HealthLifestyle:
    def __init__(self, root):
        self.root = root
        self.root.title("Sleep Disorder Calculator")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f0f0")
        
        self.intro()

    def intro(self):
        self.title_1 = tk.Label(self.root, text="Sleep Disorder Calculator", font=("Arial", 22, "bold"), bg="#f0f0f0")
        self.title_1.pack(pady=20)

        self.choose_model = tk.Label(
            self.root,
            text="Choose what model you want to use: \n1. Linear regession model\n2. Logistic regression model",
            font=("Arial", 12),
            bg="#f0f0f0")
        self.choose_model.pack(pady=20)

        self.model_select = tk.Entry(self.root, font=("Arial", 12))
        self.model_select.pack(pady=5, ipadx=5, ipady=3)

        self.select_model_button = tk.Button(self.root, text="Confirm", font=("Arial", 14, "bold"), bg="#007BFF", fg="white", command=self.setup)
        self.select_model_button.pack(pady=20, ipadx=10, ipady=5)

    def setup(self):

        self.title_1.pack_forget()
        self.choose_model.pack_forget()
        self.model_select.pack_forget()
        self.select_model_button.pack_forget()

        self.title_2 = tk.Label(self.root, text="Sleep Disorder Calculator", font=("Arial", 22, "bold"), bg="#f0f0f0")
        self.title_2.pack(pady=20)
        
        model = int(self.model_select.get().strip())

        self.inputs = []
        self.labels = []
        fields = [[
            "Input your age:",
            "Input your sleep duration (1-10):",
            "Input your quality of sleep (1-10):",
            "Input your physical activity level (1-100):",
            "Input your stress level (1-10):",
            "Input your sleeping heart rate:"
            ],
            [
            "Input your age:",
            "Input your sleep duration (1-10):",
            "Input your quality of sleep (1-10):",
            "Input your physical activity level (1-100):",
            "Input your stress level (1-10):",
            "Input your sleeping heart rate:",
            "Input your daily steps (0-10000):"
            ]
        ]
        
        for text in fields[model-1]:
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
            print("ZAZAAAAAAAAAAAAAAAA")
            print(model, values)
            disorder_type = loadModel(model, values)

            result_texts = [
                "🟢 Low probability of having a sleep disorder.",
                "🔴 High probability of having Sleep Apnea.",
                "🔴 High probability of having Insomnia."
            ]

            self.title_2.pack_forget()
            for input in self.inputs:
                input.pack_forget()
            
            for label in self.labels:
                label.pack_forget()
            self.start_button.pack_forget()

            result_label = tk.Label(self.root, text="The results are in:", font=("Arial", 20, "bold"), bg="#f0f0f0")
            result_label.pack(pady=20)

            outcome_label = tk.Label(self.root, text=result_texts[disorder_type], font=("Arial", 18), bg="#f0f0f0")
            outcome_label.pack(pady=20)

            image_paths = ["images/healthy.png", "images/sleep-apnea.png", "images/insomnia.png"]
            self.result_image = tk.PhotoImage(file=image_paths[disorder_type])
            self.image_label = tk.Label(self.root, image=self.result_image, bg="#f0f0f0")
            self.image_label.pack(pady=20)
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthLifestyle(root)
    root.mainloop()
