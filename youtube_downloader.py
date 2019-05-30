import youtube_dl
from tkinter import *
from tkinter.filedialog import askdirectory
import os

win = Tk()

win.title("Youtube Downloader")
win.geometry("640x300")

rep = ""
aff_rep = StringVar()
URL_text = StringVar()
URL = ""
loading = StringVar()

def choose_dir():
    global rep
    global aff_rep
    rep = askdirectory(initialdir="/",title='Choisissez un repertoire')
    aff_rep.set('Répertoire choisi : ' + rep)

def get_url():
    global URL
    URL = URL_text.get()

def hook(d):
    if d["status"] == 'finished':
        loading.set("Terminé")
    #print(d['status'])

def download():
    global URL
    global rep
    global to_dl
    loading.set("Téléchargement...")
    os.chdir(rep)

    if URL != "" and rep != "":
        if to_dl.get() == 2:
            ydl_opts = {'progress_hooks' : [hook],}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([URL])
        elif to_dl.get() == 1:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'progress_hooks' : [hook],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([URL])
        else:
            print("Error")

to_dl = IntVar()
to_dl.set(0)

frame_video = LabelFrame(win, text='URL de la vidéo : ')
frame_video.pack()

URL_text.set("Entrez l'URL ici")
URL_box = Entry(frame_video, textvariable=URL_text, width= 50)
URL_box.pack()
button_validate=Button(frame_video, text='Valider', command=get_url)
button_validate.pack()

frame_download = LabelFrame(win, text="Téléchargement de : ")
frame_download.pack()

button_son = Radiobutton(frame_download, text="Son", variable=to_dl, value=1)
button_video = Radiobutton(frame_download, text="Video", variable=to_dl, value=2)
button_son.pack()
button_video.pack()

frame_rep = Label(win, text='Répertoire de stockage du téléchargement : ')
frame_rep.pack()

btnchoixrep = Button(win, text='Choisir', command = choose_dir)
btnchoixrep.pack()

frame_choice = Label(win, textvariable=aff_rep)
frame_choice.pack(padx=5, pady=5)

button_download = Button(win, text = "Télécharger", command= download)
button_download.pack()

btnquitter = Button(win, text='Quitter', command = win.destroy)
btnquitter.pack()

frame_loading = Label(win, textvariable=loading)
frame_loading.pack()

win.mainloop()
