from tkinter import *
import time
window = Tk()
window.title("Robot Arena")
canvas = Canvas(window, width=400, height=300,bg='white')
canvas.pack(padx=10,pady=10)
#the velocity, or distance moved per time step
vx=1.0 # x velocity
vy=0.5 # y velocity
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 400.0
y_max = 300.0
id1=canvas.create_rectangle(3,7,3+10,7+10)
#Move robot for 500 timesteps
for t in range (1,50000):
    x1,y1,x2,y2=canvas.coords(id1)
    # if a boundary has been croseed, reverse the direction
    if x2 >= x_max:
        vx = -1.0
    if y1 <= y_min:
        vy = 0.5
    if y2 >= y_max:
        vy = -0.5
    if x1 <= x_min:
        vx = 1.0
    # Move robot a fixed amount
    canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    #pause for 0.1 seconds, then delete the image
    time.sleep(0.01)
window.mainloop()

