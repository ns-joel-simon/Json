import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
import json

class ExcelToJsonConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel to JSON Converter")

        # Create widgets
        self.label = tk.Label(root, text="Select an Excel file:", font="Arial")
        self.label.pack(pady=100)

        self.file_path_entry = tk.Entry(root, width=100)
        self.file_path_entry.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.convert_button = tk.Button(root, text="Convert to JSON", command=self.convert_to_json)
        self.convert_button.pack(pady=10)

        self.success_label = tk.Label(root, text="", fg="green")
        self.success_label.pack(pady=10)

        self.navigate_button = tk.Button(root, text="Open Result Folder", command=self.open_result_folder)
        self.navigate_button.pack(pady=10)

        self.result_folder = "result"
        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx;.xls")])
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def convert_to_json(self):
        file_path = self.file_path_entry.get()
        if not file_path:
            messagebox.showerror("Error", "Please select an Excel file.")
            return

        try:
            df = pd.read_excel(file_path)
            json_data = df.to_json(orient="records")
            result_file_path = os.path.join(self.result_folder, "result.json")
            with open(result_file_path, "w") as json_file:
                json.dump(json.loads(json_data), json_file, indent=4)
            self.success_label.config(text="Conversion successful! Result saved in result/result.json")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def open_result_folder(self):
        os.startfile(self.result_folder)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelToJsonConverter(root)
    root.mainloop()
