

"""
link: https://www.codewars.com/kata/5839c48f0cf94640a20001d3
name: Land perimeter
"""


def walk_true(lst, item, n=0):
	i, k = item[0], item[1]
	try:
		# riht
		if lst[i][k + 1] != 'X': n += 1
	except IndexError: n += 1
	if k == 0: n += 1
	else:
		try:
			if lst[i][k - 1] == 'X': n += 0 # left
			else: n += 1
		except IndexError: n += 1
	try:
		# down
		if lst[i + 1][k] != 'X': n += 1

	except IndexError: n += 1
	if i == 0: n += 1
	else:
		#up
		try:
			if lst[i - 1][k] != 'X': n += 1
		except IndexError: n += 1
	return n


def select_x(lst):
	list_x = []
	for i in range(len(lst)):
		for k in range(len(lst[i])):
			if lst[i][k] == "X": list_x.append([i, k])
	return list_x


def land_perimeter(arr, l_per=0):
	lst = select_x(arr)
	for j in lst: l_per += walk_true(arr, j)
	return "Total land perimeter: {}".format(l_per)


# lst =[
# 	"OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO",
# 	"OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]
#
#
# print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]))




print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), 60)
print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), 52)
print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), 40)
print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), 54)
print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), 40)


print(23)
