"""Before Running the program run the following commands in command prompt in administrator mode first :-
1. pip install opencv-python
2. pip install mediapipe
3. pip install pyautogui
4. pip install msvc-runtime
5. After finally running the program start a youtube video and click on it then do hand gestures  
 """





import cv2 
import mediapipe as mp
import pyautogui

def count_fingers(list):
    cnt = 0

    thresh = (list.landmark[0].y*100 - list.landmark[9].y*100)/2
    if (list.landmark[5].y*100 - list.landmark[8].y*100) > thresh:
        cnt+=1
    if (list.landmark[9].y*100 - list.landmark[12].y*100) > thresh:
        cnt+=1
    if (list.landmark[13].y*100 - list.landmark[16].y*100) > thresh:
        cnt+=1
    if (list.landmark[17].y*100 - list.landmark[20].y*100) > thresh:
        cnt+=1
    if (list.landmark[5].x*100 - list.landmark[4].x*100) >5:
        cnt+=1
    
    
    return cnt

cap = cv2.VideoCapture(0)




drawing = mp.solutions.drawing_utils 
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands = 1)

prev = -1

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    res = hand_obj.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:


        hand_keypoints = res.multi_hand_landmarks[0]
        cnt = (count_fingers(hand_keypoints))
        if not(prev==cnt):
            if cnt==1:
                pyautogui.press("right")
            elif cnt==2:
                pyautogui.press("left")
            elif cnt==3:
                pyautogui.press("up")
            elif cnt==4:
                pyautogui.press("down")
            elif cnt==5:
                pyautogui.press("space")

        prev = cnt  

        drawing.draw_landmarks(frame, hand_keypoints, hands.HAND_CONNECTIONS) 

    cv2.imshow("window", frame)
    
    
    
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break