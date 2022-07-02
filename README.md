# SATautograder
Grades the reading, writing section of a SAT collegboard form given a picture

<img width="1393" alt="Screen Shot 2022-06-23 at 8 41 08 PM" src="https://user-images.githubusercontent.com/85262856/175457602-e1fd2db5-dc5a-4389-b3c0-fa579a2e84f2.png">


# Usage
Take a picture of your test form preferably using your phone camera. Alternatively you could take a picture with your webcam; Of course, it is possible, since I originally intended to use only webcam pictures, although **results would be inconsistent**, so it is best to be used with high resolution phone cameras. The problem with webcam is that the resolution will be so garbage and its very hard to keep your paper still while you press capture on your webcam app that the program will have a hard time distinguishing between bubbles and question numbers, motion blur, etc. . 

In the settings file, type the year/date of the test (KA PT#3 or May 2018 U.S.) you are checking, the section of the test (reading/writing), and other options. When you run scanner.py, the program auto grades your test and gives you a score as well as all the questions you missed.

Currently this program only works with the old version of the SAT scantron. In recent years, a different scantron is used, but no functionality has been added for that because one is enough. Make sure the scantron you are using **MATCHES** what the sample picture uses.

# Errors

The most common error would be the program over/undercounting the bubbles, it mostly never happens with phone camera, but can be pretty common on webcam photos.

However, if the program is bugging out, you probably didn't do one of these things: Held the sheet in front of the webcam so that the bubbles are clearly visible, held the sheet straight and not curved (although a slight curve would still work properly). A 720p webcam works fine also.

As long as your bubbles are filled in neatly and within the lines correctly, everything should work fine. The program tolerates messy bubbles AS LONG AS there are no bubbles connecting to each other horizontally through pencil marks.

This would **NOT** work, because the program would see choices A & B as **one** bubble instead of **two**

<img width="1101" alt="Screen Shot 2022-07-02 at 11 24 00 AM" src="https://user-images.githubusercontent.com/85262856/177012241-32cf7767-4bd6-43c3-be39-a873f9c997d2.png">

# Libs

No machine learning used, just python OpenCV, a computer image library in C++/python/Java which isn't really machine learning tbh

# Credits

pyimagesearch's OMR blog was a insanely helpful post that aided me and I used some code snippets in mine. I also noticed almost every python amateur bubble scanner on google/github uses this blog as some type of source...
