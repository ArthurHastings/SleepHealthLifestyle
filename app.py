import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from func import *
class HealthLifestyle:

    def __init__(self, root):
        self.root = root
        self.age = 0
        self.sleep_duration = 0
        self.quality_of_sleep = 0
        self.physical_activity = 0
        self.stress_level = 0
        self.heart_rate = 0

        self.setup()

    def setup(self):
        self.frame = tk.Frame(self.root, width=300, height=200)
        self.frame.pack()
        
        self.title = tk.Label(self.root, text="Sleep Disorder Calculator", font=("Helvetica", 20))
        self.title.pack(pady=50)

        self.input1 = tk.Label(self.root, text = "Input your age:")
        self.input1.pack(pady=20)

        self.age = tk.Entry(self.root)
        self.age.pack()

        self.input2 = tk.Label(self.root, text = "Input your sleep duration (1-10):")
        self.input2.pack(pady=20)

        self.sleep_duration = tk.Entry(self.root)
        self.sleep_duration.pack()

        self.input3 = tk.Label(self.root, text = "Input your quality of sleep (1-10):")
        self.input3.pack(pady=20)

        self.quality_of_sleep = tk.Entry(self.root)
        self.quality_of_sleep.pack()

        self.input4 = tk.Label(self.root, text = "Input your physical activity level (1-100):")
        self.input4.pack(pady=20)

        self.physical_activity = tk.Entry(self.root)
        self.physical_activity.pack()

        self.input5 = tk.Label(self.root, text = "Input your stress level (1-10):")
        self.input5.pack(pady=20)

        self.stress_level = tk.Entry(self.root)
        self.stress_level.pack()

        self.input6 = tk.Label(self.root, text = "Input your sleeping heart rate:")
        self.input6.pack(pady=20)

        self.heart_rate = tk.Entry(self.root)
        self.heart_rate.pack()

        self.start_button = tk.Button(self.root, text="Submit!", command=self.start)
        self.start_button.pack()
    
    def start(self):
        age_val = int(self.age.get().strip())  # Remove accidental spaces
        sleep_val = float(self.sleep_duration.get().strip())
        quality_val = int(self.quality_of_sleep.get().strip())
        physical_score_val = int(self.physical_activity.get().strip())
        stress_lvl_val = int(self.stress_level.get().strip())
        heart_rate_val = int(self.heart_rate.get().strip())


        self.title.pack_forget()
        self.age.pack_forget()
        self.input1.pack_forget()
        self.sleep_duration.pack_forget()
        self.input2.pack_forget()
        self.quality_of_sleep.pack_forget()
        self.input3.pack_forget()
        self.physical_activity.pack_forget()
        self.input4.pack_forget()
        self.stress_level.pack_forget()
        self.input5.pack_forget()
        self.heart_rate.pack_forget()
        self.input6.pack_forget()
        self.start_button.pack_forget()

        self.disorder_type = calculateHealth(age_val, sleep_val, quality_val, physical_score_val, stress_lvl_val, heart_rate_val)

        self.msg = tk.Label(self.root, text="The results are in:", font=("Helvetica", 20))
        self.msg.pack(pady=50)

        if self.disorder_type == 0:
            self.result1 = tk.Label(self.root, text="🟢 Low probability of having a sleep disorder.", font=("Helvetica", 20))
            self.result1.pack(pady=50)
        elif self.disorder_type == 1:
            self.result1 = tk.Label(self.root, text="🔴 High probability of having Sleep Apnea.", font=("Helvetica", 20))
            self.result1.pack(pady=50)
        elif self.disorder_type == 2:
            self.result1 = tk.Label(self.root, text="🔴 High probability of having Insomnia.", font=("Helvetica", 20))
            self.result1.pack(pady=50)


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthLifestyle(root)
    root.mainloop()