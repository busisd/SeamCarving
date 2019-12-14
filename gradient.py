# Adapted from: https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html

import cv2

def get_gradient(filename):
	src = cv2.imread(filename, cv2.IMREAD_COLOR)
	# src = cv2.GaussianBlur(src, (3, 3), 0)
	src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	dst = cv2.Laplacian(src_gray, cv2.CV_16S, ksize=3)
	abs_dst = cv2.convertScaleAbs(dst)
	return abs_dst
