import cv2
import numpy as np
print("package imported")
#image import(chapter 1 and 2)
#img=cv2.imread("resources/img.png")
#kernal=np.ones((5,5),np.uint8)
#imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Output",imgGray)
#imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
#imgCanny=cv2.Canny(img,100,100)
#imgDialation=cv2.dilate(imgCanny,kernal,iterations=1)
#imgEroded=cv2.erode(imgDialation,kernal,iterations=1)
#cv2.imshow("Bur Image",imgBlur)
#cv2.imshow("Canny Image",imgCanny)
#cv2.imshow("Dilated image",imgDialation)
#cv2.imshow("Eroded image",imgEroded)
#cv2.waitKey(0)
#video and web cam import
#cap=cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
#cap.set(10,100)
#while True:
    #success, img=cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #breakq
#chapter 3 (open cv convensions )
#img=cv2.imread("resources/img_1.png")
#print(img.shape)
#imgResize=cv2.resize(img,(300,200))
#print(imgResize.shape)
#imgCropped=img[0:200,200:500]
#cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
#cv2.imshow("Image Cropped",imgCropped)
#cv2.waitKey(0)

#shapes and texts ch 4
#img=np.zeros((512,512,3),np.uint8)
#print(img)
#img[200:300,100:300]=255,0,0
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#cv2.circle(img,(400,50),30,(255,255,0),5)
#cv2.putText(img,"RonitRT",(300,200),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),2)
#cv2.imshow("Image",img)
#cv2.waitKey(0)
#chapter 5
#img=cv2.imread("resources/img_2.png")
#width,height=250,350
#pts1=np.float32([[133,448],[159,548],[309,520],[285,413]])
#pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
#matrix=cv2.getPerspectiveTransform(pts1,pts2)
#imgOutput=cv2.warpPerspective(img,matrix,(width,height))
#cv2.imshow("Cards",img)
#cv2.imshow("output",imgOutput)
#cv2.waitKey(0)
##chapter 6 joining images

# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         ver = hor
#     return ver
#
#
#
#
#
# img=cv2.imread("resources/img.png")
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgStack=stackImages(0.5,([img,imgGray,img],[img,img,img]))
#
# #imghor=np.hstack((img,img))
# #imgver=np.vstack((img,img))
# #cv2.imshow("horizontali",imghor)
# #cv2.imshow("veritcal",imgver)
# cv2.imshow("vImage stack",imgStack)
# cv2.waitKey(0)
#colour detection chapter 7
def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
path="resources/img_1.png."
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue MIN","TrackBars",69,179,empty)
cv2.createTrackbar("Hue MAX","TrackBars",114,179,empty)
cv2.createTrackbar("Saturation MIN","TrackBars",41,255,empty)
cv2.createTrackbar("Saturaion max","TrackBars",255,255,empty)
cv2.createTrackbar("Val MIN","TrackBars",116,255,empty)
cv2.createTrackbar("Val MAX","TrackBars",248,255,empty)
while True:
    img=cv2.imread(path)

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue MIN","TrackBars")
    h_max=cv2.getTrackbarPos("Hue MAX","TrackBars")
    s_min=cv2.getTrackbarPos("Saturation MIN","TrackBars")
    s_max=cv2.getTrackbarPos("Saturaion max","TrackBars")
    v_min=cv2.getTrackbarPos("Val MIN","TrackBars")
    v_max=cv2.getTrackbarPos("Val MAX","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)

    imgResult=cv2.bitwise_and(img,img,mask=mask)

    # cv2.imshow("original",img)
    # cv2.imshow("new image",imgHSV)
    # cv2.imshow("mask", mask)
    # cv2.imshow("Result", imgResult)


    imgstacked=stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgstacked)
    cv2.waitKey(1)


