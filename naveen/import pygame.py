import pygame as py
import cv2

# Initialize Pygame
py.init()

class x:
     c=0
     count=0
     buttonColor = "black"
     textColor = "white"
     rectButton = py.Rect(545, 500, 200, 60)  # x, y, width, height

     quitbuttonColor = "black"
     quittextcolor = "white"
     quitButton = py.Rect(20, 20, 120, 50)
 
     backbuttonColor = "black"
     backtextcolor = "white"
     backButton = py.Rect(20, 20, 120, 50)

     yesbuttonColor = "black"
     yestextColor = "white"
     yesButton = py.Rect(500, 370, 120, 70)

     nobuttonColor = "black"
     notextColor = "white"
     noButton = py.Rect(690, 370, 120,70)

# Set up the display
screen=py.display.set_mode((1300,700))
py.display.set_caption("astrology")

# images
bgimg = py.image.load("image1.jpg")
bgimg = py.transform.scale(bgimg, (1300,700))

# videos
video1 = cv2.VideoCapture("video2.mp4")
video2 = cv2.VideoCapture("video1.mp4")

# fonts
titleFont = py.font.Font("gxdo3.otf", 40)
atartFont = py.font.Font('Avenir.ttf', 40)
Font = py.font.Font('Avenir.ttf', 30)
dialogboxFont = py.font.Font('Avenir.ttf', 45)

# music
loadingSound = py.mixer.Sound("Loading-audio.mp3")
startbuttonSound = py.mixer.Sound("startbutton-sound.mp3")
backbuttonSound = py.mixer.Sound("backbutton-sound.mp3")
quitbuttonSound = py.mixer.Sound("backbutton-sound.mp3")
buttonSound = py.mixer.Sound("button-sound.mp3")

def LoadingVideo():
     if x.count<1:
        frames=0
        while frames < 270:
            val1,frame1 = video1.read()
            if not val1:
                video1.set(cv2.CAP_PROP_POS_FRAMES,0)
                val1, frame1 = video1.read()
                
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            frame1 = cv2.resize(frame1, (1300, 700))
            frame1 = py.surfarray.make_surface(frame1.swapaxes(0, 1))
            screen.blit(frame1, (0, 0))
            py.display.update()
            frames+=1
            x.count+=1
     else:
          BackgroundVideo()


def BackgroundVideo():
    val,frame = video2.read()
    if not val:
         video2.set(cv2.CAP_PROP_POS_FRAMES,0)
         val, frame = video2.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (1300, 700))
    frame = py.surfarray.make_surface(frame.swapaxes(0, 1))
    screen.blit(frame, (0, 0))

def titleDisplay():
    if x.c < 1:
        titleImg =titleFont.render("CELESTIAL COMPASS", True, 'turquoise')
        subtitleImg =titleFont.render("Navigate Your Life with Astrology ", True, 'turquoise')
        title_width, title_height = titleImg.get_size()
        
        screen.blit(titleImg, (460, 300))
        screen.blit(subtitleImg, (360, 350))
        py.time.wait(15)

def startButton():
     py.draw.rect(screen, x.buttonColor, x.rectButton, border_radius=25)
     startText = atartFont.render("START", True, x.textColor)
     screen.blit(startText, (584,504))
     
def quitButton():
     py.draw.rect(screen, x.quitbuttonColor, x.quitButton, border_radius=25)
     quitText = Font.render("QUIT", True, x.quittextcolor)
     screen.blit(quitText, (40,25))
     
def backButton():
     py.draw.rect(screen, x.backbuttonColor, x.backButton, border_radius=25)
     backText = Font.render("BACK", True, x.backtextcolor)
     screen.blit(backText, (37,25))

def dialogBox():
     confirmBox = py.Rect(443, 250, 425, 230)
     py.draw.rect(screen, "skyblue", confirmBox, border_radius=35)
     confirm_font = dialogboxFont.render("Want to Leave?", True, "black")
     screen.blit(confirm_font, (485,280))
     py.draw.rect(screen, x.yesbuttonColor, x.yesButton, border_radius=25)
     yesbuttonFont = Font.render("YES", True, x.yestextColor)
     screen.blit(yesbuttonFont,(530,385))
     py.draw.rect(screen, x.nobuttonColor, x.noButton, border_radius=25)
     nobuttonFont = Font.render("NO", True, x.notextColor)
     screen.blit(nobuttonFont, (725,385))

# pages
PAGE1 = 0
PAGE2 = 1
PAGE3 = 2
page = PAGE1


while True:
    for event in py.event.get():
        if event.type==py.QUIT:
                py.quit()
        if event.type == py.MOUSEBUTTONDOWN:
             if page == PAGE1:
                if x.rectButton.collidepoint(event.pos):
                      startbuttonSound.play()
                      x.buttonColor = "white"
                      x.textColor = "blue"
                elif x.quitButton.collidepoint(event.pos):
                     quitbuttonSound.play()
                     x.quitbuttonColor = "black"
                     x.quittextcolor = "red"
             elif page == PAGE2:        
                if x.backButton.collidepoint(event.pos):
                     backbuttonSound.play()
                     x.backbuttonColor = "black"
                     x.backtextcolor = "red"
             elif page == PAGE3:
                  if x.yesButton.collidepoint(event.pos):
                     backbuttonSound.play()
                     x.yesbuttonColor = "white"
                     x.yestextColor = "chartreuse"
                  elif x.noButton.collidepoint(event.pos):
                     x.nobuttonColor = "white"
                     x.notextColor = "red"
                     buttonSound.play()
                
        if event.type == py.MOUSEBUTTONUP:
             if page == PAGE1:
                if x.rectButton.collidepoint(event.pos):
                      x.buttonColor = "black"
                      x.textColor = "white" 
                      page = PAGE2
                elif x.quitButton.collidepoint(event.pos):
                     x.quitbuttonColor = "black"
                     x.quittextcolor = "white"
                     page = PAGE3
             elif page == PAGE2:
                if x.backButton.collidepoint(event.pos):
                     x.backbuttonColor = "black"
                     x.backtextcolor = "white"
                     page = PAGE1
             elif page == PAGE3:
                  if x.yesButton.collidepoint(event.pos):
                     x.yesbuttonColor = "black"
                     x.yestextColor = "white"
                     py.time.wait(350)
                     py.quit()
                  elif x.noButton.collidepoint(event.pos):
                     x.nobuttonColor = "black"
                     x.notextColor = "white"
                     page = PAGE1

    if page == PAGE1:
        loadingSound.play()
        LoadingVideo()
        loadingSound.stop()
        LoadingVideo()
        titleDisplay()
        startButton()
        quitButton()
    
    elif page == PAGE2:
         screen.blit(bgimg,(0,0))
         backButton()

    elif page == PAGE3:
         BackgroundVideo()
         titleDisplay()
         startButton()
         quitButton()
         dialogBox()

    # update the screen everytime
    py.display.update()

# quit pygame
video1.release()
video2.release()
py.quit()
