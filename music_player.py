import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x350')
        self.root.resizable(False,False)
        self.root.config(background='grey')
        self.root.title("Music Player")
        
        # Initialize pygame
        pygame.init()
        
        self.playlist = []
        self.current_track = 0

        # Create and configure the playlist listbox
        self.playlist_box = tk.Listbox(root)
        self.playlist_box.pack(fill="both", expand=True)

        # Create buttons for control
        play_button = tk.Button(root, text="Play", width=30,command=self.play_music)
        pause_button = tk.Button(root, text="Pause", width=30,command=self.pause_music)
        stop_button = tk.Button(root, text="Stop", width=30,command=self.stop_music)
        add_button = tk.Button(root, text="Add to Playlist", width=30,command=self.add_to_playlist)
        
        play_button.pack()
        pause_button.pack()
        stop_button.pack()
        add_button.pack()

        # Add events for double-click on playlist item
        self.playlist_box.bind("<Double-1>", self.play_selected)

    def add_to_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            if self.playlist:
                pygame.mixer.music.load(self.playlist[self.current_track])
                pygame.mixer.music.play()
                self.update_title()
    
    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    
    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def play_selected(self, event):
        selected_index = self.playlist_box.curselection()
        if selected_index:
            self.current_track = selected_index[0]
            self.play_music()

    def update_title(self):
        if self.playlist:
            track_title = os.path.basename(self.playlist[self.current_track])
            self.root.title("Music Player - " + track_title)

def main():
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
