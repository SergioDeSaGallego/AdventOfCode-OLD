def whowin(en,mc):
	if en == "A" and mc == "X":
		return "draw"
	if en == "A" and mc == "Y":
		return "win" 
	if en == "A" and mc == "Z":
		return "lose"
	if en == "B" and mc == "Y":
		return "draw"
	if en == "B" and mc == "X":
		return "lose"
	if en == "B" and mc == "Z":
		return "win"
	if en == "C" and mc == "X":
		return "win"
	if en == "C" and mc == "Y":
		return "lose"
	if en == "C" and mc == "Z":
		return "draw"
