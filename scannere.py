import cv2,os, glob
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
from answerkey import *
from settings import *

sections = {1: "Reading", 2: "Writing", 3: "Math-No-Calc", 4: "Math-Calc"}
answers = allTests[test + sections[section]]
folder_dir = os.getcwd()
files_list = glob.glob(folder_dir + "/*")
img_list = []
for file in files_list:
    if (file.lower().endswith(".jpg") | file.lower().endswith(".png") | file.lower().endswith(".jpeg")):
        img_list.append(file)
#imgpath = max(img_list, key=os.path.getctime) #most recently modified image, assuming this is the onen you used
imgpath = "/Users/joshuayang/Documents/DevelopmentCoding/MCQscanner/PT7a.JPG"
def runAllTests():
    for file in files_list:
        if (file.lower().endswith(".jpg") | file.lower().endswith(".png") | file.lower().endswith(".jpeg")):
            filepath = os.path.join(folder_dir, file)
            checkAns(filepath)
def findRectContour(img, cntrs):
    areas = []
    ma = 0
    cntr = None
    for c in cntrs:
        area = cv2.contourArea(c)
        areas.append(area)
        (x, y, w, h) = cv2.boundingRect(c)
        cntrImg = cv2.drawContours(img.copy(), c, -1, (255, 0, 0), 1)
        cv2.rectangle(cntrImg, (x, y), (x+w, y+h), (0, 0, 255), 2)
        if (area >= ma):
            ma = area
            cntr = c
    return cntr
def checkAns(imgpath):
    img = cv2.imread(imgpath)
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) #converting image to grayscale format
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("blur", blur)

    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 13)

    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)

    cntrs, hiearchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #simple because we only need a rectangle
    cntrsImg = cv2.drawContours(img.copy(), cntrs, -1, (255, 0, 0), 1)
    cv2.imshow("Contours", cntrsImg)
    cv2.waitKey(0)

    cntr = findRectContour(img, cntrs)

    peri = cv2.arcLength(cntr, True)
    approx = cv2.approxPolyDP(cntr, 0.02 * peri, True) #approximate rectangular contour
    cntrImg = cv2.drawContours(img.copy(), cntr, -1, (255, 0, 0), 3)
    shape = cv2.drawContours(img.copy(), approx, -1, (255, 0, 0), 5)
    cv2.imshow("Rectangular Region", cntrImg)
    cv2.imshow("Shape", shape)
    cv2.waitKey(0)

    cntrImg = cv2.drawContours(img.copy(), cntr, -1, (255, 0, 0), 3)

    #an easy method from imutils lib that converts image to birds-eye view
    corners = approx.reshape(4, 2)
    paper = four_point_transform(img, corners)
    papergray = cv2.cvtColor(paper.copy(), cv2.COLOR_BGR2GRAY)

    cv2.imshow("Top-View Paper", paper)
    cv2.imshow("Gray Top-View Paper", papergray)
    cv2.waitKey(0)

    #binary image conversion
    thresh2 = cv2.adaptiveThreshold(papergray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 61, 10)
    thresh3 = cv2.threshold(papergray, 150, 255, cv2.THRESH_BINARY_INV)[1]
    thresh4 = cv2.adaptiveThreshold(papergray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 13)
    thresh = cv2.threshold(papergray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #thresh = cv2.ximgproc.niBlackThreshold(papergray, 255, cv2.THRESH_BINARY_INV, 41, -0.1, binarizationMethod=cv2.ximgproc.BINARIZATION_NICK)

    cv2.imshow("Binary", thresh)
    cv2.imshow("Adpative",thresh2)
    cv2.imshow("Manual Binary", thresh3)
    cv2.imshow("Adaptive2 Binary", thresh4)
    cv2.waitKey(0)

    #open cv find contours aims to find white objects, not black
    cntrs, hiearchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #sometimes external works better
    #cntrs, hiearchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    papercntrs = cv2.drawContours(paper.copy(), cntrs, -1, (0, 255, 0), 1)

    cv2.imshow("All-contours", papercntrs)
    cv2.waitKey(0)

    bounds = paper.shape
    pw = bounds[1]
    ph = bounds[0]

    bubbles = []
    widths = []
    heights = []
    bubble_areas = []
    rect_areas = []

    filtered_rect = paper.copy()
    filtered_cntrs = []
    maxw = 0
    maxh = 0

    if (section == 1): #the bubble size cannot exceed these safety bounds
        maxw = pw/20
        maxh = ph/13
    elif (section == 2):
        maxw = pw/20
        maxh = ph/9
    for c in cntrs:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = h / float (w) #either vertical rectangle or quasi square
        if w <=maxw and h<=maxh and w >= 2 and h>= 2 and ar >= 0.6 : #no straight lines with no shape allowed or big blobs no wide rectangles (which are normally 2-digit question numbers )
            widths.append(w)
            heights.append(h)
            cv2.rectangle(filtered_rect, (x, y), (x+w, y+h), (0, 0, 255), 2)
            filtered_cntrs.append(c)
            bubble_areas.append(cv2.contourArea(c)) 
            rect_areas.append(w*h)
    
    cv2.imshow("filtered", filtered_rect)
    widths.sort(reverse=True)
    heights.sort(reverse=True)
    bubble_areas.sort(reverse=True)
    rect_areas.sort(reverse=True)

    totalq = 0
    if (section == 1):
        totalq = 52
    elif (section == 2):
        totalq = 44

    widthbound = widths[totalq*4-1] #from testing normally 15-25 pixels
    heightbound = heights[totalq*4-1] #from testing normally 15-25 pixels + there are exactly 208 bubbles on the reading portion
    bubbleareabound = bubble_areas[totalq*4-1]
    rectareabound = rect_areas[totalq*4-1]

    print(widthbound)
    print(heightbound)
    print(rectareabound)
    print(bubbleareabound)
    print(heights)
    print(len(heights))

    bubbles_cntr = paper.copy()
    bubbles_rect = paper.copy()

    for c in filtered_cntrs:
        (x, y, w, h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if  area >= bubbleareabound : #filter out circles by size // w>= widthbound and h >= heightbound and w <=pw/20 and h<=ph/13 and ar >= 0.7 and  #w>= widthbound and h >= heightbound and 
            bubbles.append(c)
            cv2.rectangle(bubbles_cntr, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("bubbles",bubbles_cntr)

    for c in filtered_cntrs:
        (x, y, w, h) = cv2.boundingRect(c)
        betterarea = w*h #imo more reliable than contourArea()
        if  w>= widthbound and h >= heightbound and betterarea >= rectareabound : #filter out circles by size // w>= widthbound and h >= heightbound and w <=pw/20 and h<=ph/13 and ar >= 0.7 and 
            #bubbles.append(c)
            cv2.rectangle(bubbles_rect, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("bubblesrect",bubbles_rect)
    cv2.waitKey(0)

    bubbles = contours.sort_contours(bubbles, method="left-to-right")[0]

    qpercol = 0
    if (section == 1):
        qpercol = 13
    elif (section == 2):
        qpercol = 9
    correct = 0
    wrong = ""
    qnum = 0
    sum = 0.0
    print(len(bubbles))
    for (row, r) in enumerate(np.arange(0, len(bubbles), qpercol*4)): #iterative every column or every 13 questions
        #sorting the first 13 questions (4 choices each)
        col = contours.sort_contours(bubbles[r:r + qpercol*4], "top-to-bottom")[0]
        for (q, i) in enumerate(np.arange(0, len(col), 4)): #then find the first four bubbles ( for one qustion)
            cnts = contours.sort_contours(col[i:i + 4],"left-to-right")[0] #left to right sort
            qnum += 1
            bubbled = None
            values = []
            for (j, c) in enumerate(cnts):
                (x, y, w, h) = cv2.boundingRect(c)
                mask = np.zeros(thresh.shape, dtype="uint8")  #mask a question turning black and white
                cv2.drawContours(mask, [c], -1, 255, -1)
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)
                total = cv2.countNonZero(mask) #count largest amount of white pixels
                sum += total
                ratio = total/float(w*h)
                values.append(ratio)
                if bubbled is None or ratio > bubbled[0]:
                    bubbled = (ratio, j)

            print(qnum) 
            ans = ord(answers[qnum-1])-ord('A')

            nobubble = False
            values.sort()
            avg = sum / (float(4*qnum))
            # check to see if the bubbled answer is correct
            color = (0, 0, 255)
            if ans == bubbled[1]:
                color = (0, 255, 0)
                correct += 1
            else:
                wrong += (str(qnum) + " ")
            print(values)
            if (ShowAnswer == True): # draw the outline of the correct answer on the test
                cv2.drawContours(paper, [cnts[ans]], -1, color, 2)
            else: #alternatively simply mark whether the user's answer is right or wrong
                cv2.drawContours(paper, [cnts[bubbled[1]]], -1, color, 2)

    fontScale = 0.8
    cv2.putText(paper, f"{correct}/{totalq} | Wrong answers: {wrong}", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 0, 255), 2)
    cv2.imshow("Final Corrected Paper",paper)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#runAllTests()
checkAns(imgpath)