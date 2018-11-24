from psychopy import visual, core, gui, event
import random
import datetime
import os
import sys
size = [50,30]
bgColor = "Black"
numberColor = "White"
posLeft = -50
posRight = 50
clock = core.Clock()

dt = datetime.datetime.now()

date = dt.strftime("%x");
time = dt.strftime("%X");




class Number:
    
    def __init__(self, id, value, size,pos):
      self.id = id
      self.value = value
      self.size = size
      self.pos = pos
      self.sti = visual.TextStim(
                win=win,
                text=value,
                color=numberColor,
                pos=(pos,0),
                height = size
            )

def dialogInitial():

    
    dlg = gui.Dlg()
    dlg.addText("Please fill this form:")
    dlg.addField("Name:")
    dlg.addField("Age:")
    dlg.addField('Gender:', choices=["Male", "Female"])
    dlg.show()
    file = "exp-"+dlg.data[0]+".csv"
    file = file.lower()

    if os.path.exists(file):
        sys.exit("File already exists")
def showInstructor():
    intromsg2 = visual.TextStim(
        win=win,
        wrapWidth=800,
        text="""
        We will now start with the real experiment.\n
        Please press again the correct button as fast as possible:\n\n
        A for left Number \n
        L for right Number \n\n
        Press any key to start.""",
        color="White"
    )   
    intromsg2.draw()

def dataInitial():
    list_data_left = []
    list_data_right = []
    for i in range (1,9):
        for s in size:
            list_data_left.append(Number(i,i,s,posLeft))
            list_data_right.append(Number(i,i,s,posRight))
    n1 = random.choice(list_data_left)
    n2 = random.choice(list_data_right)
            
    train = [
        [random.choice(list_data_left),random.choice(list_data_right)] ,
        [random.choice(list_data_left),random.choice(list_data_right)] ,
        [random.choice(list_data_left),random.choice(list_data_right)] ,
        [random.choice(list_data_left),random.choice(list_data_right)] 
        
    ]

    return  train
def show(data):
    for pair in data: 
    
        n1 = pair[0]
        n2 = pair[1]
        
        clock.reset()
        
        while clock.getTime() < .5:
            fixation.draw()
            win.flip()
          
        keys = []

        event.clearEvents()
        
        clock.reset()

        while clock.getTime() < 1.75:
            n1.sti.draw()
            n2.sti.draw()
            win.flip()
        
        keys = event.getKeys(
            keyList=["a","l"],
            timeStamped = clock
        )
        
        if keys:      
            if (keys[0][0]=="a" and n1.size == size[1]) or (keys[0][0]=="l" and n2.size ==  size[1]):
                pressed = -999
                reaction = -999
                currenttime = clock.getTime()
                while clock.getTime() < currenttime + 4:
                    errormsg.draw()
                    win.flip()
            else: 
                pressed = keys[0][0]
                reaction = keys[0][1]
        else: 
            pressed = -999
            reaction = -999
            currenttime = clock.getTime()
            while clock.getTime() < currenttime + 4:
                errormsg.draw()
                win.flip()
    print("hello")

# Create window
dialogInitial()
win = visual.Window(
        size=[1024, 768],
        units="pix",
        fullscr=False,
        color=[0, 0, 0]
)
errormsg = visual.TextStim(
    win=win,
    text="No correct button was pressed",
    color="White"
)
fixation = visual.Rect(
    win=win, 
    size=10,
    lineColor="White",
    fillColor="White")

showInstructor()
win.flip()
wait = event.waitKeys()
train = dataInitial()
show(train)
win.flip()
wait = event.waitKeys()

        