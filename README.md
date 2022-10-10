# Plagiarism Detector
A plagiarism checker uses advanced database software to scan for matches between your text and existing texts. They are used by universities to scan student assignments. There are also commercial plagiarism checkers you can use to check your own work before submitting.

## DiffLib

This module provides classes and functions for comparing sequences. It can be used for example, for comparing files, and can produce information about file differences in various formats, including HTML and context and unified diffs.

## SequenceMatcher

SequenceMatcher is a class available in python module named “difflib”. It can be used for comparing pairs of input sequences. The objective of this article is to explain the SequenceMatcher algorithm through an illustrative example. Due to the limited docs available, I thought to share the concept through a step by step example which can help the reader in understanding the entire procedure in a lucid manner.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install difflib.

```bash
pip install difflib
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
