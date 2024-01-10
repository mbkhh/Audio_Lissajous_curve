import pygame
import sys
import numpy as np
import threading
import sounddevice as sd

cycle_duration = .001
duration = 60
sampling_freq = 44100  

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.arg1 = None
        self._stop_event = threading.Event()
    def stop(self):
        self._stop_event.set()
        raise SystemExit
    def run(self):
        t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)
        signalY = np.zeros_like(t)
        signalX = np.zeros_like(t)
        if(self.arg1 == "circle"):
            signalX =  np.cos(2 * np.pi * 50000 * t);
            signalY =  np.sin(2 * np.pi * 50000 * t);
        elif(self.arg1 == "heart"):
            signalX = 16*(np.sin(2 * np.pi * 1000 * t)**3)
            signal1 = 13*np.cos(2 * np.pi * 1000 * t)
            signal2 = -5*np.cos(2 * np.pi * 2000 * t)
            signal3 = -2*np.cos(2 * np.pi * 3000 * t)
            signal4 = -1*np.cos(2 * np.pi * 4000 * t)
            signalY = signal1 + signal2 + signal3 + signal4
            signalY /= np.max(np.abs(signalY))
            signalX /= np.max(np.abs(signalX))
        elif(self.arg1=="ellips"):
            signalX = np.cos(2 * np.pi * 20000 * t);
            signalY = .4*np.sin(2 * np.pi * 20000 * t);
        elif(self.arg1=="diamond"):
            num_samples = int(duration * sampling_freq)
            for i in range(num_samples):
                time_in_cycle = t[i] % cycle_duration
                if time_in_cycle < cycle_duration / 4:
                    signalY[i] = 1
                elif time_in_cycle < 2*cycle_duration / 4:
                    signalY[i] = 0
                elif time_in_cycle < 3*cycle_duration / 4:
                    signalY[i] = -1
                else :
                    signalY[i] = 0
            for i in range(num_samples):
                time_in_cycle = t[i] % cycle_duration
                if time_in_cycle < cycle_duration / 4:
                    signalX[i] = 0
                elif time_in_cycle < 2*cycle_duration / 4:
                    signalX[i] = -1
                elif time_in_cycle < 3*cycle_duration / 4:
                    signalX[i] = 0
                else :
                    signalX[i] = 1
        elif(self.arg1=="square"):
            signalY = np.sign(np.sin(2 * np.pi * 500 * t))
            signalX = np.sign(np.sin(2 * np.pi * 500 * t + np.pi/2))
            #num_samples = int(duration * sampling_freq)
            #for i in range(num_samples):
            #    time_in_cycle = t[i] % cycle_duration
            #    if time_in_cycle < cycle_duration / 4:
            #        signalY[i] = 1
            #    elif time_in_cycle < 2*cycle_duration / 4:
            #        signalY[i] = 0
            #    elif time_in_cycle < 3*cycle_duration / 4:
            #        signalY[i] = -1
            #    else :
            #        signalY[i] = 0
            #for i in range(num_samples):
            #    time_in_cycle = t[i] % cycle_duration
            #    if time_in_cycle < cycle_duration / 4:
            #        signalX[i] = 0
            #    elif time_in_cycle < 2*cycle_duration / 4:
            #        signalX[i] = -1
            #    elif time_in_cycle < 3*cycle_duration / 4:
            #        signalX[i] = 0
            #    else :
            #        signalX[i] = 1
        elif(self.arg1=="animatedCircle"):
            signalX = np.exp(-t)* np.cos(2 * np.pi * 20000 * t);
            signalY = np.exp(-t)* np.sin(2 * np.pi * 20000 * t);
        elif(self.arg1=="stop"):
            signalY = np.zeros_like(t)
            signalX = np.zeros_like(t)
        else:
            print("invalid COMMAND!")
    
        stereo_signal = np.column_stack(( signalY , signalX))
        sd.play(stereo_signal, samplerate=sampling_freq, blocking=True) 
# Initialize Pygame
pygame.init()

# Set the window size
window_width = 380
window_height = 300

# Set the button size
button_width = 150
button_height = 50

# Set the colors
bg_color = (255, 255, 255)
button_color = (150, 150, 150)
button_hover_color = (200, 200, 200)
text_color = (0, 0, 0)

# Set the border radius
border_radius = 8

# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Final project")

# Create the buttons
button1 = pygame.Rect(20, 20, button_width, button_height)
button2 = pygame.Rect(200, 20, button_width, button_height)
button3 = pygame.Rect(20, 90, button_width, button_height)
button4 = pygame.Rect(200, 90, button_width, button_height)
button5 = pygame.Rect(20, 160, button_width, button_height)
button6 = pygame.Rect(20, 230, 340, button_height)
button7 = pygame.Rect(200, 160, button_width, button_height)



my_thread = MyThread()
# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "circle"
                    new_thread.start()
                    #generateSignal("circle")
                    #play_thread = threading.Thread(target=generateSignal, args=("circle"))
                elif button2.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "heart"
                    new_thread.start()
                elif button3.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "square"
                    new_thread.start()
                elif button4.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "ellips"
                    new_thread.start()
                elif button5.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "animatedCircle"
                    new_thread.start()
                elif button6.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "stop"
                    new_thread.start()
                elif button7.collidepoint(mouse_pos):
                    new_thread = MyThread()
                    new_thread.arg1 = "diamond"
                    new_thread.start()

    # Clear the window
    window.fill(bg_color)

    # Draw the buttons
    pygame.draw.rect(window, button_color, button1, border_radius=border_radius)
    pygame.draw.rect(window, button_color, button2, border_radius=border_radius)
    pygame.draw.rect(window, button_color, button3, border_radius=border_radius)
    pygame.draw.rect(window, button_color, button4, border_radius=border_radius)
    pygame.draw.rect(window, button_color, button5, border_radius=border_radius)
    pygame.draw.rect(window, button_color, button6, border_radius=border_radius)
    pygame.draw.rect(window, button_color, button7, border_radius=border_radius)


    mouse_pos = pygame.mouse.get_pos()
    if button1.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button1, border_radius=border_radius)
    if button2.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button2, border_radius=border_radius)
    if button3.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button3, border_radius=border_radius)
    if button4.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button4, border_radius=border_radius)
    if button5.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button5, border_radius=border_radius)
    if button6.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button6, border_radius=border_radius)
    if button7.collidepoint(mouse_pos):
        pygame.draw.rect(window, button_hover_color, button7, border_radius=border_radius)

    # Add text to the buttons
    font = pygame.font.Font(None, 24)
    text1 = font.render("Circle", True, text_color)
    text2 = font.render("Heart", True, text_color)
    text3 = font.render("Square", True, text_color)
    text4 = font.render("Ellipse", True, text_color)
    text5 = font.render("Animated Circle", True, text_color)
    text6 = font.render("Stop", True, text_color)
    text7 = font.render("Diamond", True, text_color)
    window.blit(text1, (button1.x + 50, button1.y + 15))
    window.blit(text2, (button2.x + 50, button2.y + 15))
    window.blit(text3, (button3.x + 50, button3.y + 15))
    window.blit(text4, (button4.x + 50, button4.y + 15))
    window.blit(text5, (button5.x + 10, button5.y + 15))
    window.blit(text6, (button6.x + 150, button6.y + 15))
    window.blit(text7, (button7.x + 40, button7.y + 15))

    # Update the display
    pygame.display.update()
