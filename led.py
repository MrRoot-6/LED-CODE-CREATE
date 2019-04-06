row1 = str(input("Row1: "))
row2 = str(input("Row2: "))
row3 = str(input("Row3: "))
row4 = str(input("Row4: "))
row5 = str(input("Row5: "))
row6 = str(input("Row6: "))
row7 = str(input("Row7: "))
row8 = str(input("Row8: "))

print("\n", row1, "\n", row2, "\n", row3, "\n", row4, "\n", row5, "\n", row6, "\n", row7, "\n", row8)

row1_code = ""
row2_code = ""
row3_code = ""
row4_code = ""
row5_code = ""
row6_code = ""
row7_code = ""
row8_code = ""

for i in range(0,8):
	if row1[i] == "x":
		row1_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row2[i] == "x":
		row2_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row3[i] == "x":
		row3_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row4[i] == "x":
		row4_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row5[i] == "x":
		row5_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row6[i] == "x":
		row6_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row7[i] == "x":
		row7_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)
for i in range(0,8):
	if row8[i] == "x":
		row8_code += ("\tdraw.line((7,%d), fill=\"red\")\n"%i)

holecode = ""
holecode += "with canvas(device) as draw:\n"
holecode += row1_code
holecode += row2_code
holecode += row3_code
holecode += row4_code
holecode += row5_code
holecode += row6_code
holecode += row7_code
holecode += row8_code
holecode += "time.sleep(timeofwait)"
print(holecode)
