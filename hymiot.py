feeling = int(input("How do you feel? (1-10) "))


if feeling <= 7 and feeling >= 4:
	print("A suitable smiley would be :-|")
elif feeling <= 4 and feeling > 1:
	print("A suitable smiley would be :-(")

elif feeling == 1:
	print("A suitable smiley would be :'(")
elif feeling >= 8 and  feeling < 10:
	print("A suitable smiley would be :-)")
elif feeling == 10:
	print("A suitable smiley would be :-D")
elif feeling > 10 or feeling <= 0:
	print("Bad input!")