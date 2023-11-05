import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import os
from qr_generator import generate_qr

class QRCodeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Generator")
        self.geometry("400x600")

        tk.Label(self, text="Enter URL:").pack(pady=10)
        self.url_entry = tk.Entry(self, width=40)
        self.url_entry.pack(pady=10)

        self.generate_button = tk.Button(self, text="Generate QR Code", command=self.generate)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Save QR Code", command=self.save, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.pack(pady=10)
        self.img = None

    def generate(self):
        url = self.url_entry.get()
        try:
            # Create a QR code image
            self.img = generate_qr(url)
            # Ensure the image is in RGB mode
            self.update_qr_code(self.img)
            self.save_button.config(state=tk.NORMAL)
        except ValueError as e:
            tk.messagebox.showerror("Error", str(e))

    def save(self):
        default_dir = os.path.expanduser('~\\Downloads')
        file_path = filedialog.asksaveasfilename(initialdir=default_dir, title="Save QR Code",
                                                 filetypes=(("PNG files", "*.png"), ("All files", "*.*")),
                                                 defaultextension=".png")
        if file_path:
            self.img.save(file_path)

    def update_qr_code(self, img):
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.config(width=self.tk_img.width(), height=self.tk_img.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()
