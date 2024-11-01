import tkinter as tk
from tkinter import messagebox

class WordCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter")
        self.root.geometry("400x300")

        # Label and Text area for input text
        tk.Label(root, text="Enter text:", font=("Arial", 14)).pack(pady=10)
        self.text_entry = tk.Text(root, font=("Arial", 12), height=6, width=40)
        self.text_entry.pack(pady=5)

        # Count button
        count_button = tk.Button(root, text="Count Words", font=("Arial", 14), command=self.count_words)
        count_button.pack(pady=20)

        # Label to display result
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def count_words(self):
        # Get text and count words
        text = self.text_entry.get("1.0", tk.END).strip()
        word_count = len(text.split())

        # Display result
        self.result_label.config(text=f"Word Count: {word_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounter(root)
    root.mainloop()
