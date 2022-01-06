# JPxG, 2022 January 5

import os
import traceback
import argparse


parser = argparse.ArgumentParser(description="Imperfect Fifth, v0.1.", epilog="This generates a set of pitch-shifted sample files, based on an input file.")
parser.add_argument("-i", "--input",      metavar="FILE.WAV",       help="Input file.", default="default.wav")
parser.add_argument("-b", "--basenote",      metavar="A4",       help="Note to parse input file as (A4, C#6, Db1, etc). If you make this low, the generated files will be higher; if you make this high, the generated files will be lower. Highest is B8 (7902Hz) and lowest is A0 (27.5Hz). Default is A4 (440Hz).", default="A4")
parser.add_argument("-o", "--output", metavar="s", help="Output naming scheme. Options are \"n\" (name of note: \"A4\"), \"k\" (key number: \"49.wav\"), and \"s\" (note but sortable: \"4A0\", \"4Ab\"). Default is \"s\".", default="s")
parser.add_argument("-p,", "--prefix", metavar="impfif", help="Output prefix, to put before file names when they're being saved.")

args = parser.parse_args()

base = args.basenote
inp = args.input

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

print(base)