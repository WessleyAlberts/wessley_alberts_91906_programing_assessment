from random import randint
from time import time
from tkinter import *
from easygui import msgbox

def rules():
    """Opens an EasyGui message box with the rules"""
    msgbox("""Objective:
To click on the ball as many times as possible.

Rules:
You have 5 seconds to click the Big Blue Ball before you lose.
If you click the ball, the 5 seconds reset and a Smaller Red Ball appears.
           """,
           "Rules")


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
            #colour of ball
            self.colour=colour

        def get_x(self):
            """Gets the x pos of the ball"""
            return self.x
        
        def get_y(self):
            """Gets the y pos of the ball"""
            return self.y
        
        def get_size(self):
            """Gets the size of the ball"""
            return self.size
        
        def move(self):
            """Moves the ball """
            #Moves the ball
            self.x+=self.vx
            self.y+=self.vy
            #Finalizes the movement of the ball
            canvas.create_oval(self.x,self.y,self.x+self.size,self.y+self.size,fill=self.colour)
        
        def collision(self):
            """Checks if the ball is coliding with another ball or the wall"""
            #Checks if the ball is coliding with another ball
            for item in balls:
                x=item.get_x()
                y=item.get_y()
                size=item.get_size()
                
                if self.x<x<self.x+self.size or x<self.x<x+size:
                    if self.y<y<self.y+self.size or y<self.y<y+size:
                        self.vx=self.vx*-1
                        self.vy=self.vy*-1
                        
            #Checks if the ball is coliding with the wall 
            if self.y+self.size>=screen_height-canvas_height*2:
                self.y=screen_height-canvas_height*2-self.size
                self.vy=self.vy*-1
                
            if self.y<=0:
                self.y=0
                self.vy=self.vy*-1
                
            if self.x+self.size>=screen_width-canvas_width*2:
                self.x=screen_width-canvas_width*2-self.size
                self.vx=self.vx*-1
                
            if self.x<=0:
                self.x=0
                self.vx=self.vx*-1
    
    
    def makeball(x,y,size,vx,vy,colour):
        """Creates and stores a ball"""
        ball=Ball(x,y,size,vx,vy,colour)
        balls.append(ball)

    def addball():
        """Creates the properties of a new ball"""
        makeball(randint(0,screen_width-round(screen_width/50)),randint(0,screen_height-round(screen_height/50)),50,randint(-10,10)/50,randint(-10,10)/50,"red")
    
    def ball_click(event):
        """Confirms if the ball was clicked"""
        global x,y,t_end
        x=event.x
        y=event.y
        if x>balls[0].x and x<balls[0].x+balls[0].size:
            if y>balls[0].y and y<balls[0].y+balls[0].size:
                t_end = time() + 5
                addball()
        
    
    #Sets the balls storage
    balls=[]
    
    #Sets the screen dimensions
    global screen_width, screen_height, canvas_width, canvas_height
    game=Toplevel()
    screen_width = game.winfo_screenwidth()
    screen_height = game.winfo_screenheight()
    canvas_width = int(round(screen_width/100))
    canvas_height = int(round(screen_height/100))
    
    game.title("Game")
    game.geometry(str(screen_width-canvas_width*2)+"x"+str(screen_height-canvas_height*2)+"+0+0")
    Frame(game,height=(screen_height/100)).pack()
    canvas=Canvas(game,width=screen_width-(canvas_width),height=screen_height-(canvas_height),bg="black")
    canvas.pack()
    
    #Creates the target ball
    makeball(randint(0,screen_width-canvas_width*2),randint(0,screen_height-canvas_height*2),100,0.2,0.2,"blue")
    
    playing=True
    while playing==True:
        global t_end
        t_end = time() + 5
        while time() < t_end:
            canvas.delete(ALL)
            for item in balls:
                    item.collision()
                    item.move()
            canvas.update()
            canvas.bind("<Button 1>", ball_click)
            if time()>=t_end:
                playing=False


if __name__=="__main__":
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
    rules_btn=Button(central_frame, text="Rules", image=pixel, font=("TkDefaultFont", 24), width=250, compound="c", command=rules)
    rules_btn.grid(row=3, column=1, pady=10)
    
    master.mainloop()
