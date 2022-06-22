from random import randint
from time import time
from tkinter import *

def func():
    print("testing function")

def game():
    class Ball():
        def __init__(self,x,y,size,vx,vy,colour):
            #x pos
            self.x=x
            #y pos
            self.y=y
            #size
            self.size=size
            #x distance moved per frame
            self.vx=vx
            #y distance moved per frame
            self.vy=vy
            self.colour=colour

        def getx(self):
            return self.x
        
        def gety(self):
            return self.y
        
        def move(self):
            self.x+=self.vx
            self.y+=self.vy
            if self.y+self.size>=300:
                self.y=300-self.size
                self.vy=self.vy*-1
            if self.y<=0:
                self.y=0
                self.vy=self.vy*-1
            if self.x+self.size>=400:
                self.x=400-self.size
                self.vx=self.vx*-1
            if self.x<=0:
                self.x=0
                self.vx=self.vx*-1
            canvas.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.colour)
        
        def collision(self):
            for item in balls:
                if item.getx==self.x+5 and item.gety==self.y+5:
                    self.vx=self.vx*-1
                    self.vy=self.vy*-1
    
    
    def makeball(x,y,size,vx,vy,colour):
        ball=Ball(x,y,size,vx,vy,colour)
        balls.append(ball)

    def addball():
        vx=0
        while vx==0:
            vx=randint(-10,10)
            vx=vx/50
        vy=0
        while vy==0:
            vy=randint(-10,10)
            vy=vy/50
        makeball(randint(0,400),randint(0,300),10,vx,vy,"red")
    
    def ball_click(event):
        global x,y,t_end
        x=event.x
        y=event.y
        if x>balls[0].x and x<balls[0].x+20:
            if y>balls[0].y and y<balls[0].y+20:
                t_end = time() + 5
                addball()
        
    
    makeball(50,50,20,0.05,0.05,"blue")
    
    game=Toplevel()
    game.geometry("400x400")

    canvas=Canvas(game,width=400,height=300,bg="black")
    canvas.pack()
    playing=True
    while playing==True:
        global t_end
        t_end = time() + 5
        while time() < t_end:
            canvas.delete(ALL)
            for item in balls:
                    item.move()
                    item.collision()
            canvas.update()
            canvas.bind("<Button 1>", ball_click)
            if time()>=t_end:
                playing=False


if __name__=="__main__":
    #Sets the balls storage
    balls=[]

    """Creates the layout of the Main Menu"""
    #Sets the main menu window
    master = Tk()
    master.configure( bg=("#a8a8a8"))
    master.resizable(False,False)
    master.title("Main Menu")
    master.geometry("400x500")
    
    #Creates an "image" of a pixel
    pixel = PhotoImage(width=1, height=1)
        
    #Creates 3 Frames to help keep everything centered in the window
    left_frame=Frame(master, bg=("#a8a8a8"), width=75)
    left_frame.grid(column=0)
    right_frame=Frame(master, bg=("#a8a8a8"), width=75)
    right_frame.grid(column=2)
    central_frame=Frame(master, bg=("#a8a8a8"), width=250)
    central_frame.grid(column=1)

    #Creates the game title
    game_title=Label(central_frame, bg=("#a8a8a8"), text="Balls", font=("TkDefaultFont", 48))
    game_title.grid(row=0, column=1, pady=25)

    #Creates space inbetween the title and the buttons
    white_space=Label(central_frame, bg=("#a8a8a8"), image=pixel, height=100)
    white_space.grid(row=1,column=1)

    #Creates the buttons that give access to the rules and master modes
    game_btn=Button(central_frame, text="Play Game", image=pixel, font=("TkDefaultFont", 24), width=250, compound="c", command=game)
    game_btn.grid(row=2, column=1, pady=10)
    rules_btn=Button(central_frame, text="Rules", image=pixel, font=("TkDefaultFont", 24), width=250, compound="c", command=func)
    rules_btn.grid(row=3, column=1, pady=10)
    
    master.mainloop()
