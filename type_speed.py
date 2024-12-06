import tkinter as tk
import time 
import random
SENTENCES = [
"The sun set behind the mountains, casting a warm glow over the valley below.",
"Reading books can transport you to different worlds filled with adventure and imagination.",
"Healthy eating and regular exercise contribute significantly to overall physical and mental well-being.",
"Traveling opens your mind to new cultures, perspectives, and experiences beyond your hometown.",
"Writing in a journal can help clarify thoughts and express feelings in a constructive way."
]
class TypingSpeedTestApp:
    def __init__(self,root):
        self.root = root
        self.root.title("typing speed test")
        self.root.minsize(height = 200,width = 400)

        self.start_time = 0
        self.sentence = random.choice(SENTENCES)

        self.instruction_label = tk.Label(root,text = "TYPE THE BELOW SENTENCE AS FAST AS YOU CAN",font = ("Arial",20,"bold"))
        self.instruction_label.pack(padx=10)

        self.sent_label = tk.Label(root,text = self.sentence,font = ("Helvetica",14),wraplength=400)
        self.sent_label.pack(pady=10)

        self.entry = tk.Text(root,font=("arial",14,"normal"))
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>",self.start_typing)
        self.entry.bind("<Return>",self.end_typing)

        self.result_label = tk.Label(root,text="")
        self.result_label.pack(pady = 10)

        self.retry_btn = tk.Button(root,text ="try again",command = self.retry)
        self.retry_btn.pack(pady= 10)

    def start_typing(self,event):
        if self.start_time == 0:
            self.start_time = time.time()


    def end_typing(self,event):
        end_time = time.time()
        typed_text = self.entry.get()

        time_taken = end_time - self.start_time

        word_length = len(typed_text.split())
        
        wps = word_length/time_taken

        accuracy = sum(1 for a,b in zip(self.sentence,typed_text) if a == b)/len(self.sentence) 
        accuracy = accuracy*100

        self.result_label.config(text = f"accuracy {accuracy:.2f} || speed {wps:.2f}")

    def retry(self):
        self.sentence = random.choice(SENTENCES)
        self.sent_label.config(text=self.sentence)
        self.result_label.config(text="")
        self.entry.delete(0,tk.END)
        self.start_time = 0
    
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()