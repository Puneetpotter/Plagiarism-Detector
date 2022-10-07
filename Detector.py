pip install difflib

#import the required library 
from difflib import SequenceMatcher
	#opening two text files 
	with open('file_one.txt') as file_1, open('file_two.txt') as file_2:
		#read the files in another variables 
		file1_data = file_1.read() 
		file2_data = file_2.read() 
		#since we have taken two files for detecting plagiarism, we mention to them here 
		similarity_ratio = SequenceMatcher(None, filel_data, file2_data).ratio() 
		#print the plagiarsim ratio 
		print( similarity_ratio)
