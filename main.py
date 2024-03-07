import pyautogui
import time
import datetime

NO_OF_CAMERAS = 4
DELAY = 0.0
TIME_X_POSITION = 514
TIME_Y_POSITION = 676
pyautogui.FAILSAFE = False

def cut_at_camera(no):
    # Split clips of all track 
    pyautogui.hotkey('ctrl', 'shift', 'k')

    # Turn on Video Tracks 
    for i in range(NO_OF_CAMERAS, no, -1):
        pyautogui.hotkey('ctrl', 'alt', str(i))
        time.sleep(DELAY)

    # Selecting Video Tracks 
    time.sleep(DELAY)
    pyautogui.press('d')
    time.sleep(DELAY)
    # Deleting Video Tracks 
    pyautogui.press('backspace')
    time.sleep(DELAY)

    # Turning Off Video Tracks 
    for i in range(NO_OF_CAMERAS, no, -1):
        pyautogui.hotkey('ctrl', 'alt', str(i))

def main():
    time.sleep(2)

    with open('TIMESTAMPS.txt', 'r') as file:
        camera_mapping = {'5': '1', '8': '3', '7': '2', '6': '4'}
        for key, value in camera_mapping.items():
             camera_timings_file = camera_timings_file.replace("\n" + key, "\n" + value)
        
        # Removing Duplicates from camera logs
        timings = [["-1", "-1"]]
        for i in range(0, len(camera_timings_file) - 1, 2):
            if timings[-1][1] != camera_timings_file[i + 1]:
                timings.append([camera_timings_file[i][-11:], camera_timings_file[i + 1]])
        timings.pop(0)

        for i in range(len(timings) - 1, -1, -1):
            # Moving Timecode to duration
            pyautogui.moveTo(TIME_X_POSITION, TIME_Y_POSITION)
            time.sleep(DELAY)
            pyautogui.click()
            time.sleep(DELAY)
            pyautogui.typewrite(timings[i][0])
            time.sleep(DELAY)
            pyautogui.press('enter')
            time.sleep(DELAY)
            pyautogui.press('esc')
            time.sleep(DELAY)

            # Skiping top angle
            if(NO_OF_CAMERAS == int(timings[i][1])):
                time.sleep(DELAY)
                pyautogui.hotkey('ctrl', 'shift', 'k')
                time.sleep(DELAY)
                continue

            cut_at_camera(int(timings[i][1]))
            
        print(*timings, sep="\n")
        print(len(timings))

if __name__ == "__main__":
    main()