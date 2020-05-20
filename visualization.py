from tkinter import *
from constants import shapes, color_map


# The Visualization class will allow us to draw the solution map
class Visualization:

    def __init__(self,
                 canvas_width,
                 canvas_height,
                 line_distance):
        self.matrix = Tk()
        self.width = canvas_width
        self.height = canvas_height
        self.canvas = Canvas(self.matrix,
                             width=canvas_width,
                             height=canvas_height)
        self.box_width = int(canvas_width / line_distance)

        self.shapes = shapes

    def draw_shapes(self, colors):
        self.canvas.pack()
        for i, shape in enumerate(self.shapes):
            polygon = [x * self.box_width for x in shape[0]]
            self.canvas.create_polygon(*polygon, fill=color_map[colors[i]], outline='black')
            self.canvas.create_text((shape[1][0] * self.box_width, shape[1][1] * self.box_width), text=i+1)

    def draw(self):
        self.matrix.mainloop()
