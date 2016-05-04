a = "|__|__|__|__|__|__|__|__| 5"

b = a.split("|")

b[4] = "WP"

print b




def fix_design(b) :
	for i in range(0, len(b) - 1) :
		aux = "|"
		b[i] = aux + b[i] + aux
	return b
b.pop(0)
b = fix_design(b)
print b

"""
a = ""
print a.join(b)

"""