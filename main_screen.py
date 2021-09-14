from tkinter import *
from PIL import Image
from PIL import ImageTk
from pygame import mixer
import os

root = Tk()

mixer.init()
songstatus = StringVar()
songstatus.set("choosing")
global song_label, curr_label


def vol_control(vol):
    vols = int(vol) / 100
    mixer.music.set_volume(vols)


def volume():
    global scale, volume_label
    scale = Scale(root, from_=0, to_=100, orient=HORIZONTAL, fg="white", bg="black", width=30, length=222,
                  command=vol_control)
    scale.place(x=590, y=500)
    volume_label = Label(root, text='  Volume:  ', fg='white', bg='black', font='Consolas 18 bold')
    volume_label.place(x=430, y=520)


def pause_song():
    songstatus.set("Paused")
    # curr_label.setText(Paused)
    # curr_label.config(root, text="Currently Paused")
    mixer.music.pause()


def stop_song():
    song_label.destroy()
    songstatus.set("Stopped")
    mixer.music.stop()


def resume_song():
    songstatus.set("Resuming")
    mixer.music.unpause()


def display_buttons():
    global pause_btn, stop_btn, Resume_btn
    pause_btn = Button(root, text="  PAUSE  ", command=pause_song)
    pause_btn.config(text="  PAUSE  ", font="Consolas 16 bold", bg="black", fg="white")
    pause_btn.place(x=630, y=220)

    stop_btn = Button(root, text="  STOP  ", command=stop_song)
    stop_btn.config(text="  STOP   ", font="Consolas 16 bold", bg="black", fg="white")
    stop_btn.place(x=630, y=280)

    Resume_btn = Button(root, text="  RESUME  ", command=resume_song)
    Resume_btn.config(text="  RESUME  ", font="Consolas 16 bold", bg="black", fg="white")
    Resume_btn.place(x=630, y=340)

    global back_button
    back_button = Button(root, text='<--Back', font="Consolas 16 bold", fg="white", bg="black")
    back_button.place(x=20, y=50)


def beats():
    pass
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, resume_gen, stop_gen
    genre_label.destroy()
    pause_gen.destroy()
    stop_gen.destroy()
    resume_gen.destroy()
    beats_button.destroy()
    dance_button.destroy()
    hip_button.destroy()
    classical_button.destroy()
    pop_button.destroy()
    anime_button.destroy()
    volume()
    beats_label = Label(root, text='   Study & Chill   ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    beats_label.place(x=340, y=40)

    playlist1 = Listbox(root, selectmode=SINGLE, fg="white", bg='black', font='Consolas 16 bold', width=40)
    playlist1.place(x=80, y=150)

    def play_song():
        song = playlist1.get(ACTIVE)
        print(song)
        mixer.music.load(song)
        songstatus.set("Playing")
        global song_label
        song_label = Label(root, text=song, fg='white', bg='black', font="Consolas 16 bold")
        song_label.place(x=10, y=520)
        mixer.music.play()

    os.chdir(r'C:\PycharmProjects\Python Projects\music-player\songs\study beats')
    songs = os.listdir()
    for s in songs:
        playlist1.insert(END, s)

    global curr_label
    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)
    play_btn = Button(root, text="play", command=play_song)
    play_btn.config(text="  PLAY   ", font="Consolas 16 bold", bg="black", fg="white")
    play_btn.place(x=630, y=150)
    display_buttons()

    def go_back():
        playlist1.destroy()
        beats_label.destroy()
        play_btn.destroy()
        pause_btn.destroy()
        Resume_btn.destroy()
        stop_btn.destroy()
        back_button.destroy()
        volume_label.destroy()
        scale.destroy()
        # curr_label.destroy()
        global song_label
        # song_label.destroy()
        genre()

    back_button.config(command=go_back)


def dance():
    pass
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, stop_gen, resume_gen
    genre_label.destroy()
    pause_gen.destroy()
    stop_gen.destroy()
    resume_gen.destroy()
    beats_button.destroy()
    dance_button.destroy()
    hip_button.destroy()
    classical_button.destroy()
    pop_button.destroy()
    anime_button.destroy()
    volume()
    beats_label = Label(root, text=' Electronic/Dance  ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    beats_label.place(x=340, y=40)

    playlist1 = Listbox(root, selectmode=SINGLE, fg="white", bg='black', font='Consolas 16 bold', width=40)
    playlist1.place(x=80, y=150)

    def play_song():
        song = playlist1.get(ACTIVE)
        print(song)
        mixer.music.load(song)
        songstatus.set("Playing")
        global song_label
        song_label = Label(root, text=song, fg='white', bg='black', font="Consolas 16 bold")
        song_label.place(x=10, y=520)
        mixer.music.play()

    os.chdir(r'C:\PycharmProjects\Python Projects\music-player\songs\electronic music')
    songs = os.listdir()
    for s in songs:
        playlist1.insert(END, s)

    global curr_label
    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)
    play_btn = Button(root, text="play", command=play_song)
    play_btn.config(text="  PLAY  ", font="Consolas 16 bold", bg="black", fg="white")
    play_btn.place(x=630, y=150)
    display_buttons()

    def go_back():
        playlist1.destroy()
        beats_label.destroy()
        play_btn.destroy()
        pause_btn.destroy()
        Resume_btn.destroy()
        stop_btn.destroy()
        back_button.destroy()
        curr_label.destroy()
        volume_label.destroy()
        scale.destroy()
        # song_label.destroy()
        genre()

    back_button.config(command=go_back)


def hip():
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, resume_gen, stop_gen
    genre_label.destroy()
    beats_button.destroy()
    pause_gen.destroy()
    resume_gen.destroy()
    stop_gen.destroy()
    dance_button.destroy()
    hip_button.destroy()
    classical_button.destroy()
    pop_button.destroy()
    anime_button.destroy()
    volume()
    beats_label = Label(root, text=' Hip-Hop  ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    beats_label.place(x=340, y=40)

    playlist1 = Listbox(root, selectmode=SINGLE, fg="white", bg='black', font='Consolas 16 bold', width=40)
    playlist1.place(x=80, y=150)

    def play_song():
        song = playlist1.get(ACTIVE)
        print(song)
        mixer.music.load(song)
        songstatus.set("Playing")
        global song_label
        song_label = Label(root, text=song, fg='white', bg='black', font="Consolas 16 bold")
        song_label.place(x=10, y=520)
        mixer.music.play()

    os.chdir(r'C:\PycharmProjects\Python Projects\music-player\songs\indian classical music')
    songs = os.listdir()
    for s in songs:
        playlist1.insert(END, s)

    global curr_label
    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)
    play_btn = Button(root, text="play", command=play_song)
    play_btn.config(text="  PLAY  ", font="Consolas 16 bold", bg="black", fg="white")
    play_btn.place(x=630, y=150)
    display_buttons()

    def go_back():
        playlist1.destroy()
        beats_label.destroy()
        play_btn.destroy()
        pause_btn.destroy()
        Resume_btn.destroy()
        stop_btn.destroy()
        back_button.destroy()
        curr_label.destroy()
        volume_label.destroy()
        scale.destroy()
        # song_label.destroy()
        genre()

    back_button.config(command=go_back)


def pop():
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, resume_gen, stop_gen
    genre_label.destroy()
    beats_button.destroy()
    pause_gen.destroy()
    stop_gen.destroy()
    resume_gen.destroy()
    dance_button.destroy()
    hip_button.destroy()
    classical_button.destroy()
    pop_button.destroy()
    anime_button.destroy()
    volume()
    beats_label = Label(root, text=' Pop Culture  ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    beats_label.place(x=340, y=40)

    playlist1 = Listbox(root, selectmode=SINGLE, fg="white", bg='black', font='Consolas 16 bold', width=40)
    playlist1.place(x=80, y=150)

    def play_song():
        song = playlist1.get(ACTIVE)
        print(song)
        mixer.music.load(song)
        songstatus.set("Playing")
        global song_label
        song_label = Label(root, text=song, fg='white', bg='black', font="Consolas 16 bold")
        song_label.place(x=10, y=520)
        mixer.music.play()

    os.chdir(r'C:\PycharmProjects\Python Projects\music-player\songs\pop music')
    songs = os.listdir()
    for s in songs:
        playlist1.insert(END, s)

    global curr_label
    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)
    play_btn = Button(root, text="play", command=play_song)
    play_btn.config(text="  PLAY  ", font="Consolas 16 bold", bg="black", fg="white")
    # play_btn.grid(row=1, column=0)
    play_btn.place(x=630, y=150)
    display_buttons()

    def go_back():
        playlist1.destroy()
        beats_label.destroy()
        play_btn.destroy()
        pause_btn.destroy()
        Resume_btn.destroy()
        stop_btn.destroy()
        back_button.destroy()
        scale.destroy()
        volume_label.destroy()
        curr_label.destroy()
        # song_label.destroy()
        genre()

    back_button.config(command=go_back)


def classical():
    pass
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, stop_gen, resume_gen
    genre_label.destroy()
    pause_gen.destroy()
    stop_gen.destroy()
    resume_gen.destroy()
    beats_button.destroy()
    dance_button.destroy()
    hip_button.destroy()
    classical_button.destroy()
    pop_button.destroy()
    anime_button.destroy()
    volume()
    beats_label = Label(root, text=' Indian-Classical  ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    beats_label.place(x=340, y=40)

    playlist1 = Listbox(root, selectmode=SINGLE, fg="white", bg='black', font='Consolas 16 bold', width=40)
    playlist1.place(x=80, y=150)

    def play_song():
        song = playlist1.get(ACTIVE)
        print(song)
        mixer.music.load(song)
        songstatus.set("Playing")
        global song_label
        song_label = Label(root, text=song, fg='white', bg='black', font="Consolas 16 bold")
        song_label.place(x=10, y=520)
        mixer.music.play()

    os.chdir(r'C:\PycharmProjects\Python Projects\music-player\songs\indian classical')
    songs = os.listdir()
    for s in songs:
        playlist1.insert(END, s)

    global curr_label
    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)
    play_btn = Button(root, text="play", command=play_song)
    play_btn.config(text="  PLAY  ", font="Consolas 16 bold", bg="black", fg="white")
    # play_btn.grid(row=1, column=0)
    play_btn.place(x=630, y=150)
    display_buttons()

    def go_back():
        playlist1.destroy()
        beats_label.destroy()
        play_btn.destroy()
        pause_btn.destroy()
        Resume_btn.destroy()
        stop_btn.destroy()
        back_button.destroy()
        volume_label.destroy()
        scale.destroy()
        curr_label.destroy()
        # song_label.destroy()
        genre()

    back_button.config(command=go_back)


def anime():
    pass
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, stop_gen, resume_gen
    genre_label.destroy()
    pause_gen.destroy()
    stop_gen.destroy()
    resume_gen.destroy()
    beats_button.destroy()
    dance_button.destroy()
    hip_button.destroy()
    classical_button.destroy()
    pop_button.destroy()
    anime_button.destroy()
    volume()
    beats_label = Label(root, text=' Anime  ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    beats_label.place(x=340, y=40)

    playlist1 = Listbox(root, selectmode=SINGLE, fg="white", bg='black', font='Consolas 16 bold', width=40)
    playlist1.place(x=80, y=150)

    def play_song():
        song = playlist1.get(ACTIVE)
        print(song)
        mixer.music.load(song)
        songstatus.set("Playing")
        global song_label
        song_label = Label(root, text=song, fg='white', bg='black', font="Consolas 16 bold")
        song_label.place(x=10, y=520)
        mixer.music.play()

    os.chdir(r'C:\PycharmProjects\Python Projects\music-player\songs\anime-songs')
    songs = os.listdir()
    for s in songs:
        playlist1.insert(END, s)

    global curr_label
    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)
    play_btn = Button(root, text="play", command=play_song)
    play_btn.config(text="  PLAY  ", font="Consolas 16 bold", bg="black", fg="white")
    play_btn.place(x=630, y=150)
    display_buttons()

    def go_back():
        playlist1.destroy()
        beats_label.destroy()
        play_btn.destroy()
        pause_btn.destroy()
        Resume_btn.destroy()
        stop_btn.destroy()
        back_button.destroy()
        genre()
        scale.destroy()
        curr_label.destroy()
        # song_label.destroy()
        volume_label.destroy()

    back_button.config(command=go_back)


def genre():
    start_label.destroy()
    start_button.destroy()
    global genre_label, beats_button, dance_button, hip_button, classical_button, pop_button, anime_button, pause_gen, stop_gen, resume_gen
    genre_label = Label(root, text='   Music Genres   ', padx=10, pady=10, font="Consolas 17 bold",
                        borderwidth=2, relief=SUNKEN, bg="black", fg="white")
    genre_label.place(x=340, y=40)

    # Study Beats
    beats_button = Button(root, text="Study beats", font="Consolas 16 bold", bg="black", fg="white", command=beats)
    beats_button.place(x=140, y=140)

    # Electronic/Dance
    dance_button = Button(root, text=" Dance/Electronic ", font="Consolas 16 bold", bg="black", fg="white",
                          command=dance)
    dance_button.place(x=340, y=140)

    # Hip-Hop
    hip_button = Button(root, text=" Hip-Hop ", font="Consolas 16 bold", bg="black", fg="white", command=hip)
    hip_button.place(x=600, y=140)

    # Indian classical
    classical_button = Button(root, text=" Indian-Classical ", font="Consolas 16 bold", bg="black", fg="white",
                              command=classical)
    classical_button.place(x=600, y=140)

    # Pop culture
    pop_button = Button(root, text="  Pop culture  ", font="Consolas 16 bold", bg="black", fg="white",
                        command=pop)
    pop_button.place(x=280, y=230)

    # Anime music
    anime_button = Button(root, text="  Anime  ", font="Consolas 16 bold", bg="black", fg="white",
                          command=anime)
    anime_button.place(x=540, y=230)

    curr_label = Label(root, text="Currently Playing:", font="consolas 16 bold", fg="white", bg="black")
    curr_label.place(x=10, y=460)

    pause_gen = Button(root, text=" PAUSE ", command=pause_song, font="Consolas 16 bold", bg="black", fg="white")
    # pause_gen.config(text="  PAUSE  ", font="Consolas 16 bold", bg="black", fg="white")
    pause_gen.place(x=460, y=500)

    stop_gen = Button(root, text=" STOP ", command=stop_song, font="Consolas 16 bold", bg="black", fg="white")
    # stop_gen.config(text="  STOP   ", font="Consolas 16 bold", bg="black", fg="white")
    stop_gen.place(x=590, y=500)

    resume_gen = Button(root, text=" RESUME/PLAY ", command=resume_song, font="Consolas 16 bold", bg="black",
                        fg="white")
    # resume_gen.config(text="  RESUME/PLAY  ", font="Consolas 16 bold", bg="black", fg="white")
    resume_gen.place(x=700, y=500)


root.title('music player system')
root.geometry("900x600")
root.resizable(False, False)
bg = Image.open("images/new_concert.jpg")
bg = ImageTk.PhotoImage(bg)
my_label = Label(image=bg)
my_label.place(x=900, y=600)
bg_image = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
start_label = Label(root, text='Music, the universal language of mankind.', padx=10, pady=10, font="Consolas 17 bold",
                    borderwidth=2, relief=SUNKEN, bg="black", fg="white")
start_label.place(x=200, y=120)
start_button = Button(root, text="Dive in-->", font="Consolas 16 bold", bg="black", fg="white", command=genre)
start_button.place(x=390, y=240)
root.mainloop()
