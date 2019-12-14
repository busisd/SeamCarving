# SeamCarving
A python implementation of the Seam Carving image manipulation algorithm.

Given an image, finds paths of unimportant pixels from the top to the bottom of the image, and removes them. 
In each iteration, the chosen path minimizes the sum of the grayscale gradient value over that path.

Proper usage:
```
python3 seamcarving.py filename number_of_seams
```

For example, if we start with the following image: 

![Castle](https://raw.githubusercontent.com/busisd/SeamCarving/master/castle.jpg)

We can carve out 100 seams:
```
python3 seamcarving.py castle.jpg 100
```

![Castle_100](https://raw.githubusercontent.com/busisd/SeamCarving/master/castle_seams100.jpg)

Or 200 seams:
```
python3 seamcarving.py castle.jpg 200
```
![Castle_200](https://raw.githubusercontent.com/busisd/SeamCarving/master/castle_seams200.jpg)
