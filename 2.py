import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import threading
import requests
import os

# 画像と音声のURLを指定してください
image_url = 'https://github.com/Piliman22/1---/blob/main/sad.jpg?raw=true'
sound_url = 'https://github.com/Piliman22/1---/blob/main/sound.mp3?raw=true'

# ファイルをダウンロードする関数
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# 画像と音声をダウンロード
image_path = 'sad.jpg'
sound_path = 'sound.mp3'

download_file(image_url, image_path)
download_file(sound_url, sound_path)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)  # ループ再生

def show_image():
    window = tk.Toplevel()  # 新しいウィンドウを作成
    window.title("野獣先輩")  # タイトルを設定
    window.iconbitmap('sad.jpg')  # アイコンを設定
    
    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)
    
    label = tk.Label(window, image=img_tk)
    label.img_tk = img_tk  # 画像をガベージコレクションから守るために参照を保持
    label.pack()
    
    # ランダムな位置にウィンドウを配置
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    window_width = img.width  # 画像の幅を取得
    window_height = img.height  # 画像の高さを取得
    
    random_x = random.randint(0, screen_width - window_width)
    random_y = random.randint(0, screen_height - window_height)
    
    window.geometry(f'{window_width}x{window_height}+{random_x}+{random_y}')
    
    window.after(175, show_image) 

# 音声再生を別スレッドで実行
sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

root = tk.Tk()
root.withdraw()  # メインウィンドウを隠す
show_image()
root.mainloop()
