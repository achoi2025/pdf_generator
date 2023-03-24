import tkinter as tk
from PIL import Image
from utils import load_main_image, pillow_to_tk_image
from event import start_event, load_event, save_event
#from utils import...

def main():
    window = tk.Tk() 
    monitor_width  = window.winfo_screenwidth()
    monitor_height = window.winfo_screenheight()
    # window size 
    window_height = monitor_height - 100
    window_width  = int(window_height*0.7) 
    # image(logo) size 
    image_height = window_height - 100
    image_width  = window_width
    image_size   = (300, 300) 
    # geometry 
    window.geometry('{}x{}+0+0'.format(800, 600))
    # title
    window.title('Generator') 
    window.resizable(False, False)
    #main image load
    main_image = load_main_image()
    main_image = main_image.resize(image_size)
    main_tk_image = pillow_to_tk_image(main_image)
    #label
    label = tk.Label(window, image=main_tk_image)
    label.pack()

    json_dict = {}

    #button_frame
    button_frame = tk.Frame(window)
    button_frame.pack(side='bottom', fill='both', expand=True)
    # [0] start
    start_button = tk.Button(
        button_frame, text='start', overrelief='solid',
        width=5, command = lambda: start_event(window, label, json_dict, image_size)
    )
    start_button.pack(side='left', expand=True, fill='x')
    # [1] load
    load_button = tk.Button(
        button_frame, text='load', overrelief='solid',
        width=5, command= lambda: load_event(window, label, json_dict, image_size)
    )
    load_button.pack(side='left', expand=True, fill='x')
    # [2] save
    save_button = tk.Button(
        button_frame, text='save', overrelief='solid',
        width=5, command= lambda: save_event(window, label, json_dict, image_size)
    )
    save_button.pack(side='left', expand=True, fill='x')
    window.mainloop()

if __name__ == '__main__':
    main()