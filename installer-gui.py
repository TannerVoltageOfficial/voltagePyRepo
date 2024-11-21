import os
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext
import sys

class VoltageRepoGUI:
    def __init__(self, master):
        self.master = master
        master.title("voltage!pyRepo Installer")
        master.geometry("500x400")

        self.label = tk.Label(master, text="voltage!pyRepo Installer")
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15)
        self.text_area.pack(pady=10)

        self.download_button = tk.Button(master, text="Download", command=self.download)
        self.download_button.pack(pady=5)

        self.run_button = tk.Button(master, text="Run App", command=self.run_app, state=tk.DISABLED)
        self.run_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

        self.VOLTAGEREPODLURL = "https://gitlab.com/voltagestudios/pyrepo/-/raw/main/runner.py?ref_type=heads"
        self.voltage_repo_dir = os.path.join(os.path.expanduser("~"), ".voltagepyrepo")
        self.app_file_path = os.path.join(self.voltage_repo_dir, "app.py")
        self.dev_file_path = os.path.join(self.voltage_repo_dir, ".isdevbranch")

    def log(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)

    def download(self):
        self.log("Creating voltage!pyRepo directory...")
        os.makedirs(self.voltage_repo_dir, exist_ok=True)
        self.log("voltage!pyRepo directory ready!")

        self.log("Downloading...")
        if os.path.exists(self.app_file_path):
            os.remove(self.app_file_path)

        try:
            response = requests.get(self.VOLTAGEREPODLURL, stream=True)
            response.raise_for_status()

            with open(self.app_file_path, 'wb') as app_file:
                for chunk in response.iter_content(chunk_size=8192):
                    app_file.write(chunk)

            self.log(f"Downloaded voltage!pyrepo at {self.app_file_path}")
            if os.path.exists(self.dev_file_path):
                os.remove(self.dev_file_path)
            self.run_button.config(state=tk.NORMAL)
        except requests.RequestException as e:
            self.log("Failed to download the file. Please check your firewall and internet connection.")
            messagebox.showerror("Download Error", "Failed to download the file. Please check your firewall and internet connection.")

    def run_app(self):
        self.log("Running the app...")
        try:
            with open(self.app_file_path, 'r') as file:
                exec(file.read())
        except Exception as e:
            self.log(f"Error running the app: {str(e)}")
            messagebox.showerror("Run Error", f"Error running the app: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoltageRepoGUI(root)
    root.mainloop()