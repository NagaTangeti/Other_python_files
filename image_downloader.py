#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:00:54 2023

@author: nagatangeti
"""

import requests
import os

def image_downloader(url, folder):
    # Send a GET request to the URL
    response = requests.get(url)

    # Get the file name from the URL
    filename = os.path.join(folder, url.split('/')[-1])

    # Write the image to a file
    with open(filename, 'wb') as f:
        f.write(response.content)

# Example usage
image_downloader('https://www.example.com/image.jpg', 'images')


def image_downloader(url, folder):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        # Get the file name from the URL
        filename = os.path.join(folder, url.split('/')[-1])

        # Create the folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Write the image to a file
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded and saved as {filename}")
    else:
        print(f"Failed to download image from {url}")

# Example usage
image_downloader('https://www.example.com/image.jpg', 'images')
