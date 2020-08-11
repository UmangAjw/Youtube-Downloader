# Youtube-Downloader
## Indtroduction & Features
YouTube Downloader is an application through which you will be able to download videos, audio corresponding to a video and thumbnail of a video. You will get the best quality which is available on that respective YouTube video. Also, thumbnail quality will be max resolution which is uploaded by the user. This application uses tkinter GUI.

## Instructions to use
Obviously you need to have python in your systems. Additionally you need to have pytube. Else tkinter and other modules would already included.

### Installing pytube
```pip install pytube3```

### Protips
Bydefault best quality video, audio & thumbnail. If you want to download other resolutions of video & audio you can simply get list all the streams available using
```video = yt.streams.all()```
To get different resolution of thumbnail:
- https://img.youtube.com/vi/<video-id>/default.jpg         (For default resolution)
- https://img.youtube.com/vi/<video-id>/sddefault.jpg       (For standard resolution)
- https://img.youtube.com/vi/<video-id>/mqdefault.jpg       (For medium quality resolution)
- https://img.youtube.com/vi/<video-id>/hqdefault.jpg       (For high quality resolution)
- https://img.youtube.com/vi/<video-id>/maxresdefault.jpg   (For maximum resolution)
  
### Note 
You won't be able to download video/audio/thumbnail of copyrighted videos. (For most of the songs produced by any Label). For thumbnail you can download via video id with the help of above mothod.
