import tkinter as tk
from tkinter import ttk, messagebox
import random
from utils import *

# Function to read words from multiple files
def read_words_from_files(file_list):
    global words
    words = []
    for file_name in file_list:
        with open(file_name, 'r') as file:
            words.extend([line.strip() for line in file])
    return words

# Function to display a set of 7 random words
def display_words():
    global popup, timer_label, words, time_limit

    if len(words) < 7:
        messagebox.showinfo("End", "Not enough words left to display.")
        if not words:
            root.destroy()
        return

    selected_words = random.sample(words, 7)
    for word in selected_words:
        words.remove(word)

    # Close the previous message box if it exists
    root.update_idletasks()

    # If popup window already exists, destroy its children
    if popup:
        for widget in popup.winfo_children():
            widget.destroy()
    else:
        # Create a custom popup window
        popup = tk.Toplevel()
    
    popup.title(f"bootleg {time_limit} seconds")
    popup.configure(bg='#282c34')
    popup.protocol("WM_DELETE_WINDOW", quit_game)  # Bind the close button to quit_game

    # Adjust label font size based on window size
    label_font = ("Helvetica", 20, "bold")

    words_text = "\n".join(selected_words)
    label = tk.Label(popup, text=words_text, font=label_font, bg='#282c34', fg='#61dafb', padx=20, pady=20)
    label.pack(expand=True)

    # Add a timer label
    timer_label = tk.Label(popup, text="Time remaining: 39 seconds", font=("Helvetica", 16), bg='#282c34', fg='#ff6f61', padx=20, pady=10)
    timer_label.pack(expand=True)

    # Start the countdown timer
    countdown(timer_label, time_limit)

def countdown(timer_label, remaining):
    if remaining <= 0:
        timer_label.config(text=f"Time remaining: {remaining} seconds")
        time_up_popup()
    else:
        timer_label.config(text=f"Time remaining: {remaining} seconds")
        root.after(1000, countdown, timer_label, remaining - 1)

def time_up_popup():
    global popup, timer_label

    popup.title("Time's up!")
    # Add the "Time's up!" label at the bottom
    label = tk.Label(popup, text="Time's up!", font=("Helvetica", 20, "bold"), bg='#282c34', fg='#ff6f61', padx=20, pady=20)
    label.pack(side=tk.BOTTOM, expand=True)

    # Create an "End Game" button to exit the application
    end_button = ttk.Button(popup, text="End Game", command=quit_game)
    end_button.pack(side=tk.BOTTOM, pady=10, expand=True)

    # Create a "Next" button to display the next set of words
    next_button = ttk.Button(popup, text="Next", command=display_words)
    next_button.pack(side=tk.BOTTOM, pady=10, expand=True)

def quit_game():
    global root
    root.destroy()

def start_screen():
    global popup, time_limit

    # Create a start screen popup window
    popup = tk.Toplevel()
    popup.title("Start Screen")
    popup.configure(bg='#282c34')
    popup.protocol("WM_DELETE_WINDOW", quit_game)  # Bind the close button to quit_game

    # Add a welcome label
    welcome_label = tk.Label(popup, text=f"Welcome to Bootleg {time_limit} Seconds", font=("Helvetica", 20, "bold"), bg='#282c34', fg='#61dafb', padx=20, pady=20)
    welcome_label.pack(expand=True)

    # Add a start button
    start_button = ttk.Button(popup, text="Start Game", command=display_words)
    start_button.pack(pady=10, expand=True)


# Function to generate file names from chapter numbers
def generate_file_list(chapters, chapter_folder):
    return [f'{chapter_folder}/chapter{chapter}.txt' for chapter in chapters]

def start_game(chapters, chapter_folder, time):
    global words, popup, root, time_limit
    time_limit = time
    # Generate the list of files containing words
    file_list = generate_file_list(chapters, chapter_folder)
    # Read words from the files
    words = read_words_from_files(file_list)
    # Create the main application window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    # Apply a theme to the Ttk widgets
    style = ttk.Style()
    style.theme_use('clam')
    # Initialize popup as None
    popup = None
    # Show the start screen
    start_screen()
    # Run the application
    root.mainloop()