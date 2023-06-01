#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:33:08 2023

@author: nagatangeti
"""


import cv2

# Load the image
#img = cv2.imread('image.jpg')

# Check if the image is empty or uninitialized
#if img is None:
#    print('Error: Failed to load image!')
#else:
    # Convert the image to grayscale
#    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

import face_recognition




def mad_face_recognition():
    print("Welcome to the Mad Scientist's Face Recognition Program!")

    # Load the image and convert it to RGB format
    image = cv2.imread("image.jpg")
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the faces in the image
    face_locations = face_recognition.face_locations(rgb_image)

    # Print the number of faces detected
    print(f"Found {len(face_locations)} face(s) in the image!")

    # Draw a rectangle around each face
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the image with the faces detected
    cv2.imshow("Mad Scientist's Face Recognition Program", image)
    cv2.waitKey(0)

mad_face_recognition()