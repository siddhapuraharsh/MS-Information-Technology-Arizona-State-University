## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 10/14/2023

import tkinter as tk

# Define the segments for each vowel 'a', 'e', 'i', 'o', 'u'
vowel_segments = {
    'a': [1, 1, 1, 1, 1, 1, 0],
    'e': [1, 1, 0, 1, 1, 0, 1],
    'i': [0, 0, 1, 0, 0, 1, 0],
    'o': [1, 1, 1, 0, 1, 1, 1],
    'u': [0, 1, 1, 0, 1, 1, 1]
}

def draw_segment(canvas, x, y, width, height, is_on, color):
    if is_on:
        canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline=color, width=2)
    else:
        canvas.create_rectangle(x, y, x + width, y + height, fill="white", outline="gray")

def draw_vowel(canvas, x, y, width, height, vowel, outline_width=1):
    segments = vowel_segments[vowel]
    segment_width = width * 1
    segment_height = height * 2
    padding = 2
    glow_color = "red"

    draw_segment(canvas, x + padding, y, segment_width - 2*padding, padding, segments[0], glow_color, ) # Segment 'a'
    draw_segment(canvas, x, y + 2*padding + segment_height - padding, padding,segment_height - 2*padding, segments[1], glow_color) # Segment 'e'
    draw_segment(canvas, x + segment_width + padding, y + padding, padding,segment_height - 2*padding, segments[2], glow_color) # Segment 'b'
    draw_segment(canvas, x + padding, y + padding + segment_height - padding,segment_height - padding, padding,segments[3], glow_color) # Segment 'g'
    draw_segment(canvas, x, y + padding, padding, segment_height - 2*padding, segments[4],glow_color) # Segment 'f'
    draw_segment(canvas, x + segment_width + padding, y + 2*padding +segment_height, padding, segment_height - 2*padding,segments[5], glow_color) # Segment 'c'
    draw_segment(canvas, x + padding, y + 2*padding + 2*segment_height - padding,segment_width - 2*padding, padding, segments[6], glow_color) # Segment 'd'

def display_vowel(canvas, x, y, width, height, vowel, outline_width=1):
    canvas.delete("all")
    draw_vowel(canvas, x, y, width, height, vowel, outline_width)

# Test the display sequence using a simple for loop
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Vowel Display")
    canvas_width, canvas_height = 100, 200
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()
    delay_time = 1000  # Delay between each vowel in milliseconds (1 second)

    vowels = ['a', 'e', 'i', 'o', 'u']
    outline_width = 2
    for vowel in vowels:
        display_vowel(canvas, 10, 10, canvas_width - 20, (canvas_height - 30) // 4, vowel, outline_width)
        root.update()  # Update the GUI to show the new vowel
        root.after(delay_time)  # Delay before displaying the next vowel

    root.mainloop()