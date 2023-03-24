from tkinter import filedialog
import tkinter as tk
from PIL import Image
from utils import pillow_to_tk_image
import json 

def start_event(root, label, json_dict, image_size):
    # implement
    img = Image.new(mode='RGB', size=image_size)
    imgtk = pillow_to_tk_image(img)

    label.config(image=imgtk)
    label.image = imgtk
def load_event(root, label, json_dict, image_size):
    root.file = filedialog.askopenfile(
        initialdir='path',
        title='choose personal json file',
        filetypes=(('json files', '*json'), ('all files', '*.*'))
    )
    #make json files
    json_dict['image'] = True
    print(json_dict)
    print(root.file.name)
def save_event(root, label, json_dict, image_size):
    with open('user_defined_layout.json', 'w') as f:
        json.dump(json_dict, f, indent='\t')
    popup_window = tk.Toplevel()
    popup_window.title("Result")
    popup_window.geometry("200x200")
    label = tk.Label(popup_window, text ="successfully saved!")
    label.pack()