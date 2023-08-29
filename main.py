import tkinter as tk
from tkinter import filedialog


class TikTokApp(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # Create the main window.
        self.main_window = tk.Frame(self)
        self.main_window.pack()

        # Create the video player.
        self.video_player = tk.Label(self.main_window)
        self.video_player.pack()

        # Create the buttons.
        self.record_button = tk.Button(self.main_window, text="Record")
        self.record_button.pack()
        self.play_button = tk.Button(self.main_window, text="Play")
        self.play_button.pack()
        self.pause_button = tk.Button(self.main_window, text="Pause")
        self.pause_button.pack()
        self.stop_button = tk.Button(self.main_window, text="Stop")
        self.stop_button.pack()

        # Create the file chooser button.
        self.file_chooser_button = tk.Button(self.main_window, text="Add Media")
        self.file_chooser_button.pack()

        # Bind the button events.
        self.record_button.bind("<Button-1>", self.on_record_button_clicked)
        self.play_button.bind("<Button-1>", self.on_play_button_clicked)
        self.pause_button.bind("<Button-1>", self.on_pause_button_clicked)
        self.stop_button.bind("<Button-1>", self.on_stop_button_clicked)
        self.file_chooser_button.bind("<Button-1>", self.on_file_chooser_button_clicked)

    def on_record_button_clicked(self):
        print("Recording...")

    def on_play_button_clicked(self):
        print("Playing...")

    def on_pause_button_clicked(self):
        print("Pausing...")

    def on_stop_button_clicked(self):
        print("Stopping...")

    def on_file_chooser_button_clicked(self):
        # Get the selected file.
        file_path = filedialog.askopenfilename(
            title="Select a media file",
            filetypes=[("Image files", "*.jpg *.jpeg *.png"), ("Video files", "*.mp4 *.mov")])

        # If a file is selected, add it to the video player.
        if file_path:
            print(f"Adding media '{file_path}'...")


if __name__ == "__main__":
    root = tk.Tk()
    app = TikTokApp(root)
    app.mainloop()
