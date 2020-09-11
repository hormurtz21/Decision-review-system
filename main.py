
import tkinter 
import cv2 
import PIL.Image, PIL.ImageTk 
from functools import partial
import imutils 

video = cv2.VideoCapture("clip.mp4")
def play(speed):
    print(f" Speed is {speed}")

    # Play the video in reverse mode
    frame1 = video.get(cv2.CAP_PROP_POS_FRAMES)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame =   video.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.create_text(134, 26, fill="red", font="Times 26 bold", text="Decision Pending")
    


def out():
   
    frame = cv2.cvtColor(cv2.imread("out.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.pack()


def not_out():
    frame = cv2.cvtColor(cv2.imread("not_out.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=1023, height=560)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.pack()

# Width and height of our main screen
SET_WIDTH = 1023
SET_HEIGHT = 514

# Tkinter gui starts here
window = tkinter.Tk()
window.maxsize(1023,780)
window.title("DECISION REVIEW SYSTEM")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()


# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Out", width=50, command=out,bg="red",borderwidth=2)
btn.pack()

btn = tkinter.Button(window, text="Not Out", width=50, command=not_out,bg="green")
btn.pack()
window.mainloop()