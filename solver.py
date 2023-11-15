import subprocess
process = subprocess.Popen(
	['python3', 'sudoku_generator.py', 'base.txt', 'easy'],
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE)
out, err = process.communicate()
#print (out)



def parse_puzzle(out):
	out = str(out).split('\\r\\n')[12:]
	out[-1] = out[-1].replace('\\n', '').replace("\'",'')
	sudoku = []
	for row in out:
		sudoku.append(row.split('|'))
	return sudoku

def show(puzzle):
	for row in puzzle:
		print (row)
	print ('==============================================')

def report_missing_numbers(set):
	all_sudoku_numbers = {str(i) for i in range(1,10)}
	cleaned_set = {x for x in set if x != '_'}
	return all_sudoku_numbers.difference(cleaned_set)

def check_cols(puzzle):
	"""
		Get each column in the puzzle as a list.
		Return the missing numbers for each of those lists.
	"""
	# Get each column in the puzzle
	col = [i for i in range(9)]
	for column in col:
		next_col = []
		for row in puzzle:
			next_col.append(row[column])
		missing = report_missing_numbers(next_col)
		print (next_col, missing)
		#break

def solve_puzzle(puzzle):
	show(puzzle)

	# Check all columns for missing cells.
	check_cols(puzzle)

solve_puzzle(parse_puzzle(out))

#print ([str(i) for i in range(1,10)])