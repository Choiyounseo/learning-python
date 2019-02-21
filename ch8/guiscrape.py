from tkinter import *
from tkinter import ttk, filedialog, messagebox
import base64
import json
import os
from bs4 import BeautifulSoup
import requests

# alert
def _sb(msg):
    _status_msg.set(msg)
def _alert(msg):
    messagebox.showinfo(message=msg)

# fetch web-page
config = {}
def fetch_url():
    url = _url.get()
    config['images'] = []
    _images.set(()) # initialized as an empty tuple
    try:
        page = requests.get(url)
    except requests.RequestException as rex:
        _sb(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = fetch_images(soup, url)
        if images:
            _images.set(tuple(img['name'] for img in images))
            _sb('Images found: {}'.format(len(images)))
        else:
            _sb('No images found')
        config['images'] = images

def fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = ('{base_url}/{src}'.format(base_url=base_url, src=src))
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url=img_url))
    return images

# save the images
def save():
    if not config.get('images'):
        _alert('No images to save')
        return
    
    if _save_method.get() == 'img':
        # ask user to choose a directory, where to save the images
        dirname = filedialog.askdirectory(mustexist=True)
        _save_images(dirname)
    else:
        # pass an initial filename, user can change it if they don't like it
        filename = filedialog.asksaveasfilename(
            initialfile ='images.json',
            filetypes=[('JSON, '.json )])
        _save_json(filename)

def _save_images(dirname):
    if dirname and config.get('images'):
        for img in config['images']:
            img_data = requests.get(img['url']).content
            filename = os.path.join(dirname, img['name'])
            with open(filename, 'wb') as f:
                f.write(img_data)
        _alert('Done')

def _save_json(filename):
    if filename and config.get('images'):
        data = {}
        for img in config['images']:
            img_data = requests.get(img['url']).content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data

        with open('images.json', 'w') as ijson:
            ijson.write(json.dumps(data))
        _alert('Done')


if __name__ == "__main__":
    _root = Tk()
    _root.title('Scrap app')

    # _root : parent, with padding=padding
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    # place _mainframe on the first row=0, first column=0
    _mainframe.grid(row=0, column=0, sticky=(E,W,N,S))

    # _mainframe : parent object
    _url_frame = ttk.LabelFrame(_mainframe, text='URL', padding='5 5 5 5')
    # sticky : should expand to the left and to the right
    _url_frame.grid(row=0, column=0, sticky=(E, W))
    _url_frame.columnconfigure(0, weight=1)
    _url_frame.rowconfigure(0, weight=1)

    _url = StringVar()
    _url.set('http://localhost:8000')

    # _url_frame : parent
    _url_entry = ttk.Entry(_url_frame, width=40, textvariable=_url)
    _url_entry.grid(row=0, column=0, sticky=(E, W, S, N), padx=5)
    # command=fetch_url : when click the button, we call the 'fetch_url' function => 'callback'
    _fetch_btn = ttk.Button(_url_frame, text='Fetch info', command=fetch_url)
    _fetch_btn.grid(row=0, column=1, sticky=W, padx=5)

    _img_frame = ttk.LabelFrame(_mainframe, text='Content', padding='9 0 0 0')
    _img_frame.grid(row=1, column=0, sticky=(N, S, E, W))

    _images = StringVar()

    _img_listbox = Listbox(_img_frame, listvariable=_images, height=6, width=25)
    _img_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)
    # command=_img_listbox.yview : contract between Listbox and Scrollbar
    _scrollbar = ttk.Scrollbar(_img_frame, orient=VERTICAL, command=_img_listbox.yview)
    _scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
    # contract with Listbox and Scrollbar
    _img_listbox.configure(yscrollcommand=_scrollbar.set)


    _radio_frame = ttk.Frame(_img_frame)
    _radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))
    _choice_lbl = ttk.Label(_radio_frame, text="Choose how to save images")
    _choice_lbl.grid(row=0, column=0, padx=5, pady=5)
    
    _save_method = StringVar()
    _save_method.set('img')
    
    _img_only_radio = ttk.Radiobutton(_radio_frame, text='As Images', variable=_save_method, value='img')
    _img_only_radio.grid(row=1, column=0, padx=5, pady=2, sticky=W)
    _img_only_radio.configure(state='normal')

    _json_radio = ttk.Radiobutton(_radio_frame, text='As JSON', variable=_save_method, value='json')
    _json_radio.grid(row=2, column=0, padx=5, pady=2, sticky=W)

    _scrape_btn = ttk.Button(_mainframe, text='Scrape!', command=save)
    _scrape_btn.grid(row=2, column=0, sticky=E, pady=5)

    _status_frame = ttk.Frame(_root, relief='sunken', padding='2 2 2 2')
    _status_frame.grid(row=1, column=0, sticky=(E, W, S))
    _status_msg = StringVar()
    _status_msg.set('Type a URL to start scraping...')
    _status = ttk.Label(_status_frame, textvariable=_status_msg, anchor=W)
    _status.grid(row=0, column=0, sticky=(E, W))

    # run the application by calling 'mainloop' method on 'Tk' instance
    _root.mainloop()