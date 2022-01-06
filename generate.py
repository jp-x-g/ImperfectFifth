# JPxG, 2022 January 5

import os
import traceback
import argparse

outputdir = "output/"

parser = argparse.ArgumentParser(description="Imperfect Fifth, v0.1.", epilog="This generates a set of pitch-shifted sample files, based on an input file.")
parser.add_argument("-i", "--input",      metavar="FILE.WAV",       help="Input file.", default="default.wav")
parser.add_argument("-b", "--basenote",      metavar="A4",       help="Note to parse input file as (A4, C#6, Db1, etc). If you make this low, the generated files will be higher; if you make this high, the generated files will be lower. Highest is B8 (7902Hz) and lowest is A0 (27.5Hz). Default is A4 (440Hz).", default="A4")
parser.add_argument("-o", "--output", metavar="s", help="Output naming scheme. Options are \"n\" (name of note: \"A4\"), \"k\" (key number: \"49.wav\"), \"s\" (note but sortable: \"49-A4\"), and \"m\" (MIDI note: \"69\"). Default is \"s\".", default="s")
parser.add_argument("-p,", "--prefix", metavar="\"impfif\"", help="Output prefix, to put before file names when they're being saved. Use quotation marks around it.")

args = parser.parse_args()

base = args.basenote
inp = args.input
out = args.output
pre = args.prefix

base = base.upper()
# Shift to uppercase, it shouldn't matter if the user types "DB4" or "Db4"

replaces = [
["C#", "Db"],
["D#", "Eb"],
["F#", "Gb"],
["G#", "Ab"],
["A#", "Bb"],
["DB", "Db"],
["EB", "Eb"],
["GB", "Gb"],
["AB", "Ab"],
["BB", "Bb"]
]

# Replace sharp notes with flat notes, uniform capitalization

for a in replaces:
	base = base.replace(a[0], a[1])

print("Running with input file \"" + inp + "\", base note \"" + base + "\", output format \"" + out + "\", and output prefix \"" + pre + "\". Wowzies!" )

# Okay, now we have the settings set. Time to do some stuff.

notes = [
"A0","Bb0","B0",
"C1","Db1","D1","Eb1","E1","F1","Gb1","G1","Ab1","A1","Bb1","B1",
"C2","Db2","D2","Eb2","E2","F2","Gb2","G2","Ab2","A2","Bb2","B2",
"C3","Db3","D3","Eb3","E3","F3","Gb3","G3","Ab3","A3","Bb3","B3",
"C4","Db4","D4","Eb4","E4","F4","Gb4","G4","Ab4","A4","Bb4","B4",
"C5","Db5","D5","Eb5","E5","F5","Gb5","G5","Ab5","A5","Bb5","B5",
"C6","Db6","D6","Eb6","E6","F6","Gb6","G6","Ab6","A6","Bb6","B6",
"C7","Db7","D7","Eb7","E7","F7","Gb7","G7","Ab7","A7","Bb7","B7",
"C8"]

print(len(notes))

start = 48
# Note that the note numbers are off by one, since Python arrays are 0-indexed.
# Therefore, note 1 will be notes[0], etc.
# So A4 is key 49, yet A4 is notes[48].

notesSortable = []

for c, v in enumerate(notes):
	if v == base:
		start = c
		# Find index of base note.
	s = v[-1] + v[0:-1]
	# "D7" -> "7D"
	if len(s) == 2:
		s += "n"
	# "7D" -> "7Dn" (for "natural")
	notesSortable.append(s)
	# Append to array.

#print(notesSortable)

for a in range(88):
	# Compose output filename.
	if out == "n":
		string = pre + notes[a]
	if out == "k":
		string = pre + str(a + 1).zfill(2)
	if out == "m":
		string = pre + str(a + 21).zfill(2)
	if out == "s":
		string = pre + str(a + 1).zfill(2) + "-" + notes[a]
	string += ".wav"
	#print(string)
	cents = int((a - start) * 100)
	execString = "sox " + inp + " " + outputdir + string + " pitch " + str(cents)

	os.system(execString)
	print(execString)

print("Wow! We're finished!")

#os.system("sox -i " + inp + " -o ")