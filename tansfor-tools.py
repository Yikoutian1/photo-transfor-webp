from PIL import Image
import tkinter as tk
from tkinter import filedialog


def convert_to_webp(file_path):
    output_file = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WebP 文件", "*.webp")])
    if output_file:
        image = Image.open(file_path)
        image.save(output_file, 'webp')
        print('图片已转换为WebP格式')


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("图像文件", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        convert_to_webp(file_path)


root = tk.Tk()
root.title("图像转WebP格式转换器")

button = tk.Button(root, text="点击此处选择图像文件\n并转换为WebP", command=select_file)
button.pack()

root.mainloop()
