from pynput import mouse

def on_click(x, y,button,pressed):
    if pressed:
        print(str(button)+" pressed("+str(x)+", "+str(y)+")")
    else:
        print(str(button)+" released at ("+str(x)+", "+str(y)+")")

with mouse.Listener(
    on_click=on_click) as listener:

    listener.join()


listener = mouse.Listener(
    #on_press=on_press,
    #on_release=on_release
    on_click=on_click)
listener.start()