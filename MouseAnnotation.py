import cv2

rect_start=[]
rect_end=[]

# import os
# print(os.getcwd())
def imgCrop(target,start,end):
    x1, y1 = min(start[0], end[0]), min(start[1], end[1])
    x2, y2 = max(start[0], end[0]), max(start[1], end[1])

    cropImg = target[y1:y2, x1:x2]
    #cv2.imshow("Cropped Image", cropImg)
    #cv2.waitKey(0)
    cv2.imwrite("CropImage.png", cropImg)

def drawRect(event, x, y, flags, userdata):
    global rect_end, rect_start

    if event==cv2.EVENT_LBUTTONDOWN:
        rect_start = (x, y)
        cv2.rectangle(working_img, rect_start, rect_start , (255, 0, 255), 2, lineType=cv2.LINE_AA);
    elif event == cv2.EVENT_LBUTTONUP:
        rect_end = (x, y)
        cv2.rectangle(working_img, rect_start, rect_end , (255, 0, 255), 2, lineType=cv2.LINE_AA);
        cv2.imshow("Window", working_img)
        cv2.waitKey(3)
        imgCrop(working_img,rect_start,rect_end)



img = cv2.imread("sample.jpg")
working_img = img.copy()
cv2.namedWindow("Window")

cv2.setMouseCallback("Window", drawRect)
k = 0
# loop until escape character is pressed
while k!=27 :

    cv2.imshow("Window", working_img)
    cv2.putText(working_img,'''Choose top left conrer, and drag,?''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX,
              0.7,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF


cv2.destroyAllWindows()



