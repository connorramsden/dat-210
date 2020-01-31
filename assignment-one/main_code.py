# coding: utf-8

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
	if(prefix == ' OK '):
		grade = points

	return grade


def main():
	score = 0
	# This time we are going to pull data directly from the internet.
	# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
	#
	# ### Step 1. Import the necessary libraries (pandas named pd and numpy named np)

	# +++your code here+++
	import pandas as pd
	import numpy as np

	# ### Step 2-3. Import the dataset from this
	# [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv).
	# ### Assign it to a variable called chipo.
	# +++your code here+++
	chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep='\t')

	# ### Step 4. See the first 10 entries
	# +++your code here+++
	print(chipo.head(10))

	# ### Step 5. What is the number of observations in the dataset?
	# NOTE: In order for tests to run you need to assign to variable called out the answer of the question
	# looks like this: out = your answer code
	# #### BEGIN DO NOT EDIT
	out = 0
	# #### END DO NOT EDIT

	# +++your code here+++
	out = chipo.shape[0]

	# #### BEGIN DO NOT EDIT
	score += test(out, 4622)
	# #### END DO NOT EDIT

	# ### Step 6. What is the number of columns in the dataset?
	# +++your code here+++
	num_columns = chipo.shape[1]
	out = num_columns

	# #### BEGIN DO NOT EDIT
	score += test(out, 5, 2)
	# #### END DO NOT EDIT

	# ### Step 7. Get the name of all the columns.
	# +++your code here+++
	out = chipo.columns

	# #### BEGIN DO NOT EDIT
	score += test(str(out), "Index(['order_id', 'quantity', 'item_name', 'choice_description',\n       'item_price'],\n      dtype='object')")
	# #### END DO NOT EDIT

	# ### Step 8. How is the dataset indexed?
	# +++your code here+++
	out = chipo.index

	# #### BEGIN DO NOT EDIT
	score += test(str(out), 'RangeIndex(start=0, stop=4622, step=1)', 2)
	# #### END DO NOT EDIT

	# ### Step 9. How many times was the most ordered item ordered?
	# +++your code here+++
	orders = chipo.groupby('item_name')
	most_ordered = orders.sum().sort_values(['quantity'], ascending=False)
	out = most_ordered['quantity'].iloc[0]

	# #### BEGIN DO NOT EDIT
	score += test(out, 761, 2)
	# #### END DO NOT EDIT

	# ### Step 10. How many items were ordered?
	# +++your code here+++
	total_items = most_ordered.quantity.sum()
	out = total_items

	# #### BEGIN DO NOT EDIT
	score += test(out, 4972, 2)
	# #### END DO NOT EDIT

	# ### Step 11. How many times was the most ordered item in the choice_description column ordered?
	# +++your code here+++
	choice = chipo.groupby(['choice_description']).sum()
	most_choice = choice.sort_values(['quantity'], ascending=False)
	out = most_choice.head(1)['quantity'].sum()

	# #### BEGIN DO NOT EDIT
	# Diet Coke 159
	score += test(out, 159, 2)
	# #### END DO NOT EDIT

	# ### Step 13. Turn the item price into a float
	# This one is done for you, use the exact code here
	dollarizer = lambda x: float(x[1:])
	chipo.item_price = chipo.item_price.apply(dollarizer)
	# +++copy/uncomment above code here +++

	# ### Step 14. How much was the revenue for the period in the dataset?
	# +++your code here+++
	revenue = chipo.item_price.sum()
	out = np.round(revenue, 2)  # same as Jupyter notebook on Canvas, not sure why the expected outcome is different

	# #### BEGIN DO NOT EDIT
	score += test(out, 39237.020000000055, 2)
	# #### END DO NOT EDIT

	# ### Step 15. How many orders were made in the period?
	# +++your code here+++
	orders = chipo['order_id'].iloc[-1]  # pandas-approved way of retrieving last item in a Series
	out = orders

	# #### BEGIN DO NOT EDIT
	score += test(out, 1834, 2)
	# #### END DO NOT EDIT

	# ### Step 16. What is the average amount per order?
	# +++your code here+++
	avg = chipo['item_price'].mean()
	out = avg

	# #### BEGIN DO NOT EDIT
	score += test(out, 18.811428571428689, 2)
	# #### END DO NOT EDIT

	# ### Step 17. How many different items are sold?
	# +++your code here+++
	unique = chipo['item_name'].drop_duplicates().shape[0]
	out = unique

	# #### BEGIN DO NOT EDIT
	score += test(out, 50, 2)
	# #### END DO NOT EDIT

	print('Your current score is: {}'.format(score))

	f_temp = open("temp_grade", "w+")
	f_temp.write(str(score))


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
