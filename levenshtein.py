#!/usr/bin/env python3

# Lab 16: Recursion
# Levenshtein Distance

global lev_cache
lev_cache = {}

def main():
	str1 = "armhair"
	str2 = "armchair"
	print(lev(str1, str2))

def lev(str1, str2):
	if str1 == str2 :
		return 0
	if str1 == "" or str2 == "":
		return max([len(str1), len(str2)])

	else:
		if str1[-1] == str2[-1]:
			return lev(str1[:-1], str2[:-1])
		else:
			l1 = lev(str1,str2[:-1])
			l2 = lev(str1[:-1], str2)
			l3 = lev(str1[:-1], str2[:-1])

			levVal = min([l1, l2, l3]) + 1
			return levVal


main()
