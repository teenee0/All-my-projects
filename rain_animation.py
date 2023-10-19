import tkinter as tk
import random

def create_raindrop():
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    length = random.randint(10, 30)
    raindrop = canvas.create_line(x, y, x, y + length, fill="blue")
    speed = length / 7
    raindrops.append((raindrop, speed,length))

def animate_rain():
    if len(raindrops) < num_raindrops.get():
        for i in range(num_raindrops.get() - len(raindrops)):
            create_raindrop()

    for raindrop, speed, lena in raindrops:
        speed = lena / abs(11 - speed_rain.get())
        canvas.move(raindrop, 0, speed)
        x1, y1, x2, y2 = canvas.coords(raindrop)
        if y2 > canvas_height:
            canvas.coords(raindrop, x1, -20, x2, -20+lena)

    # Удаляем лишние капли дождя
    while len(raindrops) > num_raindrops.get():
        raindrop, _, non = raindrops.pop()
        canvas.delete(raindrop)


    root.after(10, animate_rain)

root = tk.Tk()
root.title("Анимация дождя")

canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()


num_raindrops = tk.Scale(root, from_=0, to=1000, orient="horizontal",label = "кол-во капель")
num_raindrops.pack()
speed_rain = tk.Scale(root, from_=1, to=10, orient="horizontal",label = "скорость")
speed_rain.pack()

raindrops = []

animate_rain()

root.mainloop()