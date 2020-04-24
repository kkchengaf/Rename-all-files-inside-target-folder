import os
import sys

def rename(src_dir, des, n_remove=0, prepend=True):
	dict = {}
	repeat = []
	if des in ['null', 'NULL']:
		des = ''
	if prepend in ['false','FALSE', 'False', 'F', 'f']:
		prepend = False

	try:
		os.listdir(src_dir)
	except:
		print('Cannot find target folder at ' + src_dir + '. Please ensure target folder exists.')
		return
	
	try:
		n_remove = int(n_remove)
	except:
		print(n_remove + ' is not an integer. Please ensure the argument is an integer')
		return

	for filename in os.listdir(src_dir):
		if len(filename) < abs(n_remove):
			print('Cannot remove ' + str(n_remove) + ' character(s) from ' + filename)
		else:
			s_start = max(0, n_remove)
			s_end = n_remove if n_remove < 0 else  len(filename)
			newfilename = des + filename[s_start:s_end] if prepend else (filename[s_start:s_end] + des)
			dict[filename] = newfilename 
			if newfilename in repeat:
				print('Filename conflicts: ' + filename + ' -> ' + newfilename)
				print('Please ensure no repeated filename after renaming')
				return
			else:
				repeat.append(newfilename)


	print('Current directory: ' + src_dir + '\n')
	for filename in os.listdir(src_dir):
		f0 = src_dir+'\\'+filename
		f1 = src_dir+'\\'+dict[filename]
		try:
			os.rename(f0, f1)
		except:
			print('Filename conflicts: ' + filename + ' --> ' + dict[filename])
			print('Please ensure no repeated filename after renaming')
			return
		print(filename + ' --> ' + dict[filename])



def main():
	if(len(sys.argv)==3):
		rename(sys.argv[1], sys.argv[2])
	elif(len(sys.argv)==4):
		rename(sys.argv[1], sys.argv[2], sys.argv[3])
	elif(len(sys.argv)==5):
		rename(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	else:
		print('This program is to rename all filenames in the target file (can change file type)')
		print('usage: python rename.py [absolute directory of target folder] [string to be prepended] [# of char to be removed (+ve at front) (-ve at back)] [prepend mode (default=True)]\n')
		print('Prepand \'abc\' at the front of all files names in target_folder\n')
		print('		python rename.py C:\\Users\\xxx\\target_folder abc\n')
		print('appand \'abc\' at the back of all files names in target_folder (DANGEROUS, CAN CORRUPT YOUR FILE)\n')
		print('		python rename.py C:\\Users\\xxx\\target_folder abc 0 f\n')
		print('remove first char in all files name in target_folder\n')
		print('		python rename.py C:\\Users\\xxx\\target_folder null 1\n')
		print('remove last char in all files name in target_folder (DANGEROUS, CAN CORRUPT YOUR FILE)\n')
		print('		python rename.py C:\\Users\\xxx\\target_folder null -1\n')
		print('change last 3 char to txt in all files name in target_folder (DANGEROUS, CAN CORRUPT YOUR FILE)\n')
		print('		python rename.py C:\\Users\\xxx\\target_folder txt -3 f\n')
		print('Please use at your own risk: File can be corrupted if not manipulated correctly')
if __name__ == '__main__': 
	main()
