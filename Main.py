import Window

win = Window.Window(600,600,"My Game")
win.createPlayer((0,255,0),[40,40,100,60],True)

run = True
while run:
    win.run()