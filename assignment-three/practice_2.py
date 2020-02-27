## coding: utf-8

#!/usr/bin/python -tt
# Credit guipsamora on Github
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Data exploration with Pandas
# Getting and Knowing your Data
# Fill in the code for the functions below, as discussed in class. 
# This time you are going to add your code directly in main() 
# Tests will be embedded in your code, printing 'OK' when each part is correct.
# Please do not edit anything that is within these two lines
# #### BEGIN DO NOT EDIT and
# #### END DO NOT EDIT lines

# NOTE: In order for tests to run you need to assign to variable called out the answer of the question
# looks like this: out = your answer code


# Provided simple test() function used in main() to # what each function returns vs. what it's supposed to return.
def test(got, expected, points = 1):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

	grade = 0
	if prefix == ' OK ':
		grade = points

	return grade


def main():
	score = 0
	out = 0

	# ### Step 1. Import the necessary libraries (pandas named pd and numpy named np)

	# +++your code here+++
	import pandas as pd
	import numpy as np

	# ### Step 2. Import the dataset from this [address](
	# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
	URL = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

	# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

	users = pd.read_table(URL, sep='|', index_col='user_id')

	# ### Step 4. See the first 25 entries
	# +++your code here+++
	print(users.head(25))

	# ### Step 5. See the last 10 entries
	# +++your code here+++
	print(users.tail(10))

	# ### Step 6. What is the number of observations in the dataset?
	# +++your code here+++
	# out = len(users.count(axis=1))

	# #### BEGIN DO NOT EDIT
	score += test(out, 943, 2)
	# #### END DO NOT EDIT

	# ### Step 7. What is the number of columns in the dataset?
	# +++your code here+++
	out = len(users.columns)

	# #### BEGIN DO NOT EDIT
	score += test(out, 4, 2)
	# #### END DO NOT EDIT

	# ### Step 8. Print the name of all the columns.
	# +++your code here+++
	out = users.columns

	# #### BEGIN DO NOT EDIT
	score += test(str(out), "Index(['age', 'gender', 'occupation', 'zip_code'], dtype='object')", 2)
	# #### END DO NOT EDIT

	# ### Step 9. How is the dataset indexed?
	# "the index" (aka "the labels")
	# +++your code here+++

	# #### BEGIN DO NOT EDIT
	score += test(str(out), "Int64Index([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,\n            ...\n          "
							"  934, 935, 936, 937, 938, 939, 940, 941, 942, 943],\n           dtype='int64', "
							"name='user_id', length=943)", 2)
	# #### END DO NOT EDIT

	# ### Step 10. What is the data type of each column?
	# +++your code here+++

	# ### Step 11. Print only the occupation column
	# +++your code here+++

	# ### Step 12. How many different occupations there are in this dataset?
	# +++your code here+++

	# #### BEGIN DO NOT EDIT
	score += test(out, 21, 3)
	# #### END DO NOT EDIT

	# ### Step 13. How often does the most frequent occupation appear?
	# +++your code here+++

	# #### BEGIN DO NOT EDIT
	score += test(out, 196, 3)
	# #### END DO NOT EDIT

	# ### Step 14. Summarize the DataFrame.
	users.describe()  # Notice is only the numeric column

	# ### Step 15. Summarize all the columns
	# +++your code here+++

	# ### Step 16. Summarize only the occupation column
	# +++your code here+++

	# ### Step 17. What is the mean age of users?
	# +++your code here+++

	# #### BEGIN DO NOT EDIT
	score += test(out, 34, 3)
	# #### END DO NOT EDIT

	# ### Step 18. What is the age with least occurrence?
	# +++your code here+++

	# #### BEGIN DO NOT EDIT
	score += test(out, 1, 3)
	# #### END DO NOT EDIT

	print('Your current score is: {}'.format(score))

	f_temp = open("temp_grade", "w+")
	f_temp.write(str(score))


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()

