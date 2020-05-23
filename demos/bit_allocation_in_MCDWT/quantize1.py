#!/usr/bin/env python

import os
import argparse
try:
    import cv2
except:
    os.system("pip3 install opencv-python --user")
try:
    import numpy as np
except:
    os.system("pip3 install numpy -user")

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass

parser = argparse.ArgumentParser(description = "Quantize an image\n\n"
                                 "Example:\n\n"
                                 "  python -O quantize.py -i ../sequences/stockholm/000.png -o /tmp/000.png -q 64\n",
                                 formatter_class=CustomFormatter)

parser.add_argument("-i", "--input", help="Input image", default="../sequences/stockholm/000.png")
parser.add_argument("-o", "--output", help="Output image", default="/tmp/000.png")
parser.add_argument("-q", "--q_step", type=int, help="Quantization step", default=32)
parser.add_argument("-s", "--select", type=int, help="Select the Quantizer", default=1)

args = parser.parse_args()

image = cv2.imread(args.input, -1)

#if __debug__:
#    print("Quantizing with step {}".format(args.q_step))
if args.select==1:
    #deadzone
	print ("this is deadzone")
	tmp = image.astype(np.float32)
	tmp -= 32768
	image = (tmp/args.q_step).astype(np.int16)*args.q_step
#
#    if __debug__:
#    print("Max value at output: {}".format(np.amax(image)))
#    print("Min value at output: {}".format(np.amin(image)))

	tmp = image.astype(np.float32)
	tmp += 32768
	image = tmp.astype(np.uint16)
	
elif args.select==2:
    #midtread 
	print ("this is midtread")
	tmp = image.astype(np.float32)
    #y = np.round(x)
	tmp -= 32768
	image = np.round(tmp/args.q_step)*args.q_step
	tmp = image.astype(np.float32)
	tmp += 32768
	image = tmp.astype(np.uint16)
	
elif args.select==3 :
    #midrise
	print ("this is midrise")
	tmp = image.astype(np.float32)
	tmp -= 32768
	image = (np.floor(tmp/args.q_step)+1/args.q_step
)*args.q_step
	tmp = image.astype(np.float32)
	tmp += 32768
	image = tmp.astype(np.uint16)



#if __debug__:
#    print("Max value at output: {}".format(np.amax(image)))
#    print("Min value at output: {}".format(np.amin(image)))

cv2.imwrite(args.output, image)

