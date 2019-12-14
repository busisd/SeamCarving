# Author: Daniel Busis
# A python implementation of the seam carving algorithm.

from PIL import Image
import gradient
import sys

class Pixel:
	'''
		Used to store info about the color of a pixel in an image,
		and its color in the gradient of that image.
	'''
	def __init__(self, color, grad_color):
		self.color = color
		self.grad_color = grad_color

class DynamHelper:
	'''
		Used during the dynamic programming portion of the seam carving algorithm
		to keep track of the score and parent of each position in the table.
	'''
	def __init__(self, score, parent_pos):
		self.score = int(score)
		self.parent_pos = parent_pos

def carve_seams(pix_arr, seams=5):
	'''
		Performs the Seam Carving algorithm on the passed Pixel array. Carves out
		a number of seams equal to passed variable "seams"
	'''
	for seam in range(seams):
		dynam_array = [[]]
		for col in range(len(pix_arr[0])):
			dynam_array[0].append(DynamHelper(pix_arr[0][col].grad_color, None))

		for row in range(1, len(pix_arr)):
			new_score_row = []
			for col in range(len(pix_arr[row])):
				possible_parents = {}
				if col > 0:
					possible_parents[dynam_array[row-1][col-1]] = [row-1, col-1]
				possible_parents[dynam_array[row-1][col]] = [row-1, col]
				if col < len(pix_arr[row])-1:
					possible_parents[dynam_array[row-1][col+1]] = [row-1, col+1]
				
				best_parent = min(possible_parents.keys(), key = lambda p: p.score)
				new_score = best_parent.score+int(pix_arr[row][col].grad_color)
				new_score_row.append(DynamHelper(new_score, possible_parents[best_parent]))
				
			dynam_array.append(new_score_row)
		
		cur_removal_col = min(enumerate(dynam_array[-1]), key=lambda enum_pair: enum_pair[1].score)[0]
		cur_removal_pos = [len(pix_arr)-1, cur_removal_col]
		while cur_removal_pos is not None:
			pix_arr[cur_removal_pos[0]].pop(cur_removal_pos[1])
			cur_removal_pos = dynam_array[cur_removal_pos[0]][cur_removal_pos[1]].parent_pos
		
		print("Seam", seam, "removed")

def pix_arr_from_file(filename):
	'''
		Given a filename for an image, creates a list of Pixel objects (including 
		their color in the Laplacian gradient of the image)
	'''
	img_grad = gradient.get_gradient(filename)
	img = Image.open(filename)
	
	pix_arr = []
	for row in range(img.size[1]):
		new_row = []
		for col in range(img.size[0]):
			new_row.append(Pixel(img.getpixel((col, row)), img_grad[row][col]))
		pix_arr.append(new_row)

	img.close()

	return pix_arr

def save_img_from_arr(arr, filename = "out.jpg"):
	'''
		Given an array of Pixel objects, creates an image from 
		it and saves that to the given filename.
	'''
	final_im = Image.new("RGB", (len(arr[0]), len(arr)))
	for row in range(len(arr)):
		for col in range(len(arr[0])):
			final_im.putpixel((col, row), arr[row][col].color)
	final_im.save(filename)
	final_im.close()

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Proper use: python3 seamcarving.py filename seams_to_carve")
	pix_arr = pix_arr_from_file(sys.argv[1])
	carve_seams(pix_arr, int(sys.argv[2]))
	
	out_filename_split = sys.argv[1].split(".")
	out_filename_split[-2] = out_filename_split[-2]+"_seams"+sys.argv[2]
	out_filename = ".".join(out_filename_split)
	save_img_from_arr(pix_arr, out_filename)
