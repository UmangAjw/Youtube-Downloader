from pytube import YouTube
from tkinter import *
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk, ImageSequence
from threading import *
from tkinter.messagebox import askyesno
import urllib.request

video_size = 0
audio_size = 0
# Video downloading Thread


def downloadVideoThread():
    thread = Thread(target=videoDownloader)
    thread.start()


# Video Download Progress


def downloadVideoProgress(chunk, file_handle, remaining):
    global download_status
    file_downloaded = video_size - remaining
    percentage = (file_downloaded/video_size) * 100
    download_status.config(text='{:00.0f} % downloaded'.format(percentage))

# Video Downloader


def videoDownloader():
    global video_size, download_status
    video_btn.config(state=DISABLED)
    download_status.place(x=230, y=245)
    try:
        try_url = url.get()
        path = askdirectory()
        yt = YouTube(try_url, on_progress_callback=downloadVideoProgress)
        video = yt.streams.filter(
            progressive=True, subtype='mp4').order_by("resolution").last()
        video_size = video.filesize
        video.download(path)
        download_status.place(x=155, y=245)
        download_status.config(text='Video Downloaded Successfully...')
        result = askyesno('Youtube Video Downloader',
                          'Do you want to download another Video?')
        if (result == 1):
            url.delete(0, END)
            video_btn.config(state=NORMAL)
            download_status.config(tect=' ')
        else:
            root.destroy()
    except Exception as e:
        if(str(e) == "'cipher'"):
            download_status.place(x=100, y=245)
            download_status.config(
                text='Failed! Most Likely, Copyrighted Content!!!')
        else:
            download_status.config(
                text='Failed!!!')
        result = askyesno('Youtube Video Downloader',
                          'Try Downloading Again?')
        if (result == 1):
            url.delete(0, END)
            video_btn.config(state=NORMAL)
            download_status.config(tect=' ')
        else:
            root.destroy()

# Audio downloading Thread


def downloadAudioThread():
    thread = Thread(target=audioDownloader)
    thread.start()


# Audio Download Progress


def downloadAudioProgress(chunk, file_handle, remaining):
    global download_status
    file_downloaded = audio_size - remaining
    percentage = (file_downloaded/audio_size) * 100
    download_status.config(text='{:00.0f} % downloaded'.format(percentage))

# Audio Downloader


def audioDownloader():
    global audio_size, download_status
    audio_btn.config(state=DISABLED)
    download_status.place(x=230, y=245)

    try:
        try_url = url.get()
        path = askdirectory()
        yt = YouTube(try_url, on_progress_callback=downloadAudioProgress)
        audio = yt.streams.filter(
            only_audio=True).first()
        audio_size = audio.filesize
        audio.download(path)
        download_status.place(x=155, y=245)
        download_status.config(text='Audio Downloaded Successfully...')
        result = askyesno('Youtube Downloader',
                          'Do you want to download anything else from YouTube?')
        if (result == 1):
            url.delete(0, END)
            audio_btn.config(state=NORMAL)
            download_status.config(text=' ')
        else:
            root.destroy()
    except Exception as e:
        if(str(e) == "'cipher'"):
            download_status.place(x=100, y=245)
            download_status.config(
                text='Failed! Most Likely, Copyrighted Content!!!')
        else:
            download_status.config(
                text='Failed!!!')
        result = askyesno('Youtube Downloader',
                          'Try Downloading Again?')
        if (result == 1):
            url.delete(0, END)
            audio_btn.config(state=NORMAL)
            download_status.config(text=' ')
        else:
            root.destroy()

# Thumbnail Downloader


def thumbnailDownloader():
    global download_status
    thumbnail_btn.config(state=DISABLED)
    download_status.place(x=230, y=245)

    try:
        try_url = url.get()
        path = askdirectory()
        yt = YouTube(try_url)
        thumb_url = str(yt.thumbnail_url)
        url_title = str(yt.title)
        if(len(url_title) > 10):
            url_title = url_title[:9]
        url_title += ' Thumbnail.jpg'
        url_title = url_title.replace(' ', '_')
        path += '\\' + url_title
        urllib.request.urlretrieve(thumb_url, path)
        download_status.place(x=145, y=245)
        download_status.config(text='Thumbnail Downloaded Successfully...')
        result = askyesno('Youtube Downloader',
                          'Do you want to download anything else from YouTube?')
        if (result == 1):
            url.delete(0, END)
            thumbnail_btn.config(state=NORMAL)
            download_status.config(text=' ')
        else:
            root.destroy()
    except Exception as e:
        if(str(e) == "'cipher'"):
            download_status.place(x=100, y=245)
            download_status.config(
                text='Failed! Most Likely, Copyrighted Content!!!')
        else:
            download_status.config(
                text='Failed!!!')
        result = askyesno('Youtube Downloader',
                          'Try Downloading Again?')
        if (result == 1):
            url.delete(0, END)
            audio_btn.config(state=NORMAL)
            download_status.config(tect=' ')
        else:
            root.destroy()

# Tool tip


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 37
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#fff", relief=SOLID, borderwidth=1,
                      font=("Lato Light", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


if __name__ == "__main__":
    root = Tk()
    root.call('wm', 'iconphoto', root._w, PhotoImage(
        file=r'C:\Users\umang\Desktop\Projects\YouTube Video Downloader\img\YTD_logo.png'))
    root.wm_geometry("600x400")
    root.title('YouTube Downloader')
    root['bg'] = 'white'
    root.resizable(0, 0)

    img = Image.open(
        r'C:\Users\umang\Desktop\Projects\YouTube Video Downloader\img\YTD_banner_fit.png')  # Image Logo
    img = img.resize((640, 80), Image.ANTIALIAS)  # Image resize
    img = ImageTk.PhotoImage(img)
    head = Label(root, image=img)
    head.config(anchor=CENTER)
    head.pack()

    enter_url = Label(root, text='Enter URL: ', bg="#fff")
    enter_url.config(font=('Lato', 13))
    enter_url.place(x=50, y=135)
    url = Entry(root, width=38, border=1,
                relief=SUNKEN, font=('Lato Light', 12))
    # url.insert(0, 'Enter YouTube URL')
    url.place(x=150, y=135)

    style = ttk.Style()
    style.configure('C.TButton', font=('Lato Light', 12), borderwidth=0)
    style.map("C.TButton",
              foreground=[('pressed', 'red'), ('active', '#ED1E2E')],
              background=[('pressed', '!disabled', '#ED1E2E'),
                          ('active', '#ED1E2E')]
              )

    video_btn = ttk.Button(root, text="Video Download",
                           style="C.TButton", command=downloadVideoThread)
    video_btn.place(x=53, y=180)
    CreateToolTip(video_btn, 'Best Quality Video')

    audio_btn = ttk.Button(root, text="Audio Download",
                           style="C.TButton", command=downloadAudioThread)
    audio_btn.place(x=192, y=180)
    CreateToolTip(audio_btn, 'Best Quality Audio')

    thumbnail_btn = ttk.Button(root, text="Thumbnail Download",
                               style="C.TButton", command=thumbnailDownloader)
    thumbnail_btn.place(x=338, y=180)
    CreateToolTip(thumbnail_btn, 'Best Quality Thumbnail')

    footer = Label(root, text="Made with         by Umang Ajwalia", bg="#fff")
    footer.config(font=('Lato Light', 12))
    footer.place(x=185, y=370)

    footer_heart_img = Image.open(
        r'C:\Users\umang\Desktop\Projects\YouTube Video Downloader\img\heart.png')
    footer_heart_img = footer_heart_img.resize((16, 16), Image.ANTIALIAS)
    footer_heart_img = ImageTk.PhotoImage(footer_heart_img)
    footer_heart_label = Label(root, image=footer_heart_img, bg="#fff")
    footer_heart_label.place(x=265, y=374)

    download_status = Label(root, text='Please wait...',
                            font=('Lato Light', 15), bg='white')
    root.mainloop()
