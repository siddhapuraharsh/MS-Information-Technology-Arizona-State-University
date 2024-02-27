## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 10/14/2023

import tkinter as tk

# Define the segments for each digit from 0 to 9
segments = {
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1]
}

def draw_segment(canvas, x, y, width, height, is_on, color):
    if is_on:
        canvas.create_rectangle(x, y, x + width *6, y + height+10, fill=color, outline= color, width=2)
    else:
        canvas.create_rectangle(x, y, x + width *6, y + height+10, fill="white", outline="gray")

def draw_digit(canvas, x, y, width, height, digit, outline_width=1):
    a, b, c, d, e, f, g = segments[digit]
    segment_width = width * 1
    segment_height = height *2
    padding = 2
    glowColor = "red"

    # Draw each segment based on its state (on/off)
    draw_segment(canvas, x + padding, y, segment_width - 2*padding, padding, a, glowColor, )  # Segment 'a'
    draw_segment(canvas, x, y + 2*padding + segment_height - padding, padding, segment_height - 2*padding, e, glowColor)  # Segment 'e'
    draw_segment(canvas, x + segment_width + padding, y + padding, padding, segment_height - 2*padding, b, glowColor)  # Segment 'b'
    draw_segment(canvas, x + padding, y + padding + segment_height - padding, segment_height - padding, padding, g, glowColor) # Segment 'g'
    draw_segment(canvas, x, y + padding, padding, segment_height - 2*padding, f, glowColor)  # Segment 'f'
    draw_segment(canvas, x + segment_width + padding, y + 2*padding + segment_height, padding, segment_height - 2*padding, c, glowColor)  # Segment 'c'
    draw_segment(canvas, x + padding, y + 2*padding + 2*segment_height - padding, segment_width - 2*padding, padding, d, glowColor)  # Segment 'd'
  



def display_digit(canvas, x, y, width, height, digit, outline_width=1):
    canvas.delete("all")
    draw_digit(canvas, x, y, width, height, digit, outline_width)

# Test the display sequence using a simple for loop
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Seven-Segment Display - Display Sequence")

    canvas_width, canvas_height = 100, 200
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    delay_time = 1000  # Delay between each digit in milliseconds (1 second)
    outline_width = 2

    for digit in range(10):  # Display numbers from 0 to 9
        display_digit(canvas, 10, 10, canvas_width - 20, (canvas_height - 30) // 4, digit, outline_width)
        root.update()  # Update the GUI to show the new digit
        root.after(delay_time)  # Delay before displaying the next digit

    root.mainloop()
