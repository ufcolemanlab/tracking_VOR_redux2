# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:22:06 2015

@author: jtrinity
"""

import cv2
import numpy as np
import scipy.io as sio
from glob import glob
import tkFileDialog
import Tkinter as tk

#global stimFrameList

#add TK here
def load_data(filename_vid, filename_mat):
#    dirname = '/#DATA/fam1/'
#    filename_vid = 'vid_mouse1_1_Day3_45s2.h264'
#    filename_mat = 'vid_mouse1_1_Day3_45s2.h264.mat'
    
    data_matfile = sio.loadmat(filename_mat)
    stimFrameArray = np.concatenate(data_matfile['stimFrames'])
    stimFrameList = stimFrameArray.tolist()
    
    return data_matfile, stimFrameList


def get_frame(number):
    for i in range(number):
        (ret, img) = cap.read()
        if ret == False:
            print "invalid frame"
            print(str(number))
    return img

def show_onset(number,filename_vid):
    frameMinus2 = get_frame(number-2)
    frameMinus1 = get_frame(1)
    frame0 = get_frame(1)
    framePlus1 = get_frame(1)
    framePlus2 = get_frame(1)

    print([frameMinus2, frameMinus1, frame0, framePlus1, framePlus2])    
    
    images = np.hstack([frameMinus2, frameMinus1, frame0, framePlus1, framePlus2])
    cv2.imshow("frame: " + str(number), images)
    cv2.imwrite(filename_vid.replace(".h264", "") + '_frame'+str(number)+'.png', images)
    #if cv2.waitKey(-1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    cap.release()
    number=[]

def main():
    global cap
    
    #GUI stuff
    root = tk.Tk()
    root.withdraw()
    dirname = tkFileDialog.askdirectory()
    
    #Setup file lists
    vidName = str(dirname) +"/vid*.h264"
    matName = str(dirname) +"/vid*.h264.mat"

    filename_vidlist = glob(vidName)
    filename_matlist = glob(matName)
    
    # bug check1
    print dirname
    print filename_vidlist
    print filename_matlist
    
    saveimages = False
    

    for i in range(len(filename_matlist)):
        filename_vid = filename_vidlist[i]
        filename_mat = filename_matlist[i]
        
        data_matfile, stimFrameList = load_data(filename_vid, filename_mat)
    
        if len(stimFrameList) == 10:
            saveimages = True
        elif len(stimFrameList) != 10:
            stimFrameList = [7487, 10070, 10823, 13405, 14158, 16741, 17493, 20076, 20829, 23411]
            print "Unexpected # of stim frames. Using: " + str(stimFrameList)
            saveimages = True
        
        if saveimages:
            for i in range(len(stimFrameList)):
                print filename_vid
                cap = cv2.VideoCapture(filename_vid)
                show_onset(stimFrameList[i],filename_vid)
                print(str(stimFrameList[i]))

# __main__
if __name__ == "__main__":
    main()

# CODE TESTING BELOW THIS LINE   
#dirname = '/#DATA/fam1/'
#filename_vid = 'vid_mouse1_2_Day3_45s1.h264'
#filename_mat = 'vid_mouse1_2_Day3_45s1.h264.mat'
#
#saveimages = False
#    
#data_matfile3, stimFrameList3 = load_data(dirname, filename_vid, filename_mat)
#
#if len(stimFrameList3) == 10:
#    saveimages = True
#
#if saveimages:
#    for i in range(len(stimFrameList)):
#        cap = cv2.VideoCapture(dirname + filename_vid)
#        show_onset(stimFrameList[i])
#        print(str(stimFrameList[i]))