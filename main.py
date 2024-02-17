import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog  # Allows ut to open files from our system


def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a file to compress")  # Use askopenfilename instead of askopenfile
    return filename

def compression(i, o):
    compress(i, o)

def decompression(i, o):
    decompress(i, o)


window = tk.Tk()
window.title("Comppress/Decompress")

compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), 'compressedoutput1.txt'))
decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(open_file(), 'Decompressedoutput1.txt'))

compress_button.grid(row=2, column=1)
decompress_button.grid(row=7, column=1)
window.mainloop()
