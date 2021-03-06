# SATautograder
Grades the reading, writing section of a SAT collegboard form given a picture; does not work for math, and don't plan on making it do so

**_This is in Beta and prone to errors, although it works most% of time rn for me, provided the conditions below are satisfied_**

<img width="700" alt="Screen Shot 2022-07-02 at 11 52 16 AM" src="https://user-images.githubusercontent.com/85262856/177013001-60dfa261-b583-40eb-9ef3-af229169e720.png">

# Python Libraries/Preresiquites
[OpenCV](https://pypi.org/project/opencv-python/), a computer vision library; [imutils](https://github.com/PyImageSearch/imutils), a libary simplifying opencv actions into easy-to-use functions; and [numpy](https://numpy.org/) is used. **Install each respective python library.**

# Usage


Currently this program only works with the [old version](https://github.com/joshuayanggithub/SATautograder/files/9072963/PrepScholar-sat-practice-answer-sheet.pdf)
 of the SAT scantron. In recent years, [a different scantron was used for official SAT testing](https://github.com/joshuayanggithub/SATautograder/files/9072966/AnswerSheet.pdf)
, but that does not work yet. Make sure the scantron you are using **MATCHES** what the sample picture uses.

Take a picture of your test form preferably using your phone camera. The problem with webcam photos or any other poor quality camera is that the resolution will be very bad and the **results would be inconsistent** as a result, because the program will have a hard time pinpointing bubbles, so it is best to be used with high resolution phone cameras.

Jpg, png, jpeg format only, and sample working photos located in tests folder.

Take the picture zoomed in enough so the paper is focused clearly on the rectangular bubble region with the nearest black outline completely visible. Make sure the paper outline isn't fully visible:

<img width="400" alt="Correct" src="https://user-images.githubusercontent.com/85262856/177921523-46dbc7a5-34d2-41bd-8a93-e9a44623b05a.JPG">
If you take the picture too-zoomed-out of the black outline bubble region like below it won't work; make sure you can't see the full paper outline like you can below:

<img width="400" alt="Wrong" src="https://user-images.githubusercontent.com/85262856/177921532-6cb93200-f736-4e67-9f6c-b3ca1a04c9eb.jpg">
Drag the photo into the folder of this file, make sure it isn't some random folder like Desktop but a exclusive one. 

In the settings.py file, type the year/date of the test you are checking, the section of the test (reading/writing), and other options. When you run scanner.py, the program auto grades your test and gives you a score as well as all the questions you missed.

The 'answers.txt' file has all the reading/writing test answers for all CB practice tests #1-10 as well as a lot of QAS assesment answers i.e. May 2019 or May 2017. If you want to add any extras that I missed, use the **same** format I use in the file.

Once you run the scanner.py file a python window will open. Click on the window and **keep pressing the spacebar key** until the final grade photo is reached (there will be multiple python windows opened in the process to show the steps taken to pinpointing the bubble responses).


# Errors

The most common error would be the program over/undercounting the bubbles, it mostly never happens with phone camera, but can be pretty common on webcam photos.

However, if the program is bugging out, **you probably did one of these things:** You took the photo wrong because rectangular bubble region isn't clearly visible, the bubbles were filled in poorly, or the photo is terrible resolution/terrible lighting.

As long as your bubbles are filled in neatly and within the lines correctly, everything should work fine. The program tolerates messy bubbles AS LONG AS there are no bubbles connecting to each other horizontally through pencil marks.

# Good v.s. Bad quality photos

<img width="700" alt="Screen Shot 2022-07-02 at 11 34 12 AM" src="https://user-images.githubusercontent.com/85262856/177012494-1472d1bd-4843-43f6-b0df-ed43fe94a41b.png">
<img width="700" alt="Screen Shot 2022-06-23 at 8 41 08 PM" src="https://user-images.githubusercontent.com/85262856/175457602-e1fd2db5-dc5a-4389-b3c0-fa579a2e84f2.png">
From these two photos you can clearly tell the difference between Webcam and phone resolutions, as well as how the bubble outlines are much thinner on the phone picture despite, the size of the outlines in the pixel being a fixed value; in other words, the bubble outline on the webcam photo appears much thicker because the resolution is worse. **_9 times out of ten_** the program will **ERROR** out with webcam/poor quality photos.

# Miscounting Bubbles

This would **NOT** work, because the program would see choices A & B as **one** bubble instead of **two**

<img width="700" alt="Screen Shot 2022-07-02 at 11 24 00 AM" src="https://user-images.githubusercontent.com/85262856/177012241-32cf7767-4bd6-43c3-be39-a873f9c997d2.png">


# Shoutout Adrian Rosebrock

pyimagesearch's OMR blog was a insanely helpful post that aided me and I used some code snippets in mine. I also noticed almost every python amateur bubble scanner on google/github uses this blog's code in some type of variation...
