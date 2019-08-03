row = []
out = "with canvas(device) as draw:\n"

print("Put X sign to flash single led and 0 to leave it off.")
for i in range(0,8):
	row.append(str(input("Row%s: " %(i+1))))

for i in range(0, 8):
	for j in range(0, 8):
		if (str(row[i])[j]) == "x":
			out += ("\tdraw.point((%d, %d), fill=\"red\")\n"%(7-i, j))

out += "time.sleep(timeofwait)"

print(out)
