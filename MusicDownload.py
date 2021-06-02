from pytube import YouTube
import moviepy.editor as mp
import re
import os
import threading

class Downloader:
    def __init__(self, link, path):
        self.link = link
        self.path = path
        self.yt = YouTube(self.link)

    def mp3_(self):
        print("O seu audio esta sendo baixado.")
        self.yt = self.yt.streams.filter(only_audio=True).first().download(self.path)
        for file in os.listdir(self.path):
            if re.search(".mp4", file):
                mp4_path = os.path.join(self.path, file)
                mp3_path = os.path.join(self.path, os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        print("Download de audio completo!")

    def mp4_(self):
        print("O seu video esta sendo baixado.")
        self.yt = self.yt.streams.filter(only_video=True).first().download(self.path)
        print("Download de video completo!")
    


# link = input("Insira o link do video que vc quer baixar")
# path = input("Digite o diretorio mque deseja salvar")

_qnt = int(input("Quantos arquivos sera baixados ?"))



for i in range(_qnt):
    link = input("Insira o link do video que vc quer baixar")
    extension = input("Insira a extenção desejada (exit se estiver satisfeito com q quantidade)")
    path = input("Digite o diretorio mque deseja salvar")

    d = Downloader(link, path)

    if extension == 'mp3':
        d.mp3_()
    elif extension == 'mp4':
        d.mp4_()
    elif extension == 'exit':
        i = _qnt
    else:
        print("Digite uma extenção valida, mp3 ou mp4")
        if i == 0:
            i = 0
        else:
            i = i-1
