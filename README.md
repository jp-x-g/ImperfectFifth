![Software logo](logo-imperfectfifth.png)
# Imperfect Fifth, v1.0
This is a cute little program that takes an audio file (.WAV only) and uses it as a basis for generating a full set of 88 notes.<br />
It's not very sophisticated, and the lower/higher ends might sound very weird, but it is good enough to be usable.<br />
At the very least, it is good for memeing around.

This requires that the ```sox``` package be installed.

I use Linux; I don't know what happens if you run this program on a closed-sores OS. It probably won't work very well.

Usage: ```generate.py [-h] [-i FILE.WAV] [-b A4] [-o s] [-p "prefix"]```

Optional arguments:
#### -h, --help 
Show this help message, print version information and exit.
#### -i ```FILE.WAV```, --input ```FILE.WAV```
Input file; default is "input.wav".
#### -b ```A4```, --basenote ```A4```
Note to parse input file as (A4, C#6, Db1, etc).<br />
If you make this low, the generated files will be higher; if you make this high, the generated files will be lower.<br />
The highest you can co is is B8 (7902Hz) and the lowest is A0 (27.5Hz). The default is A4 (440Hz). Sorry, 432 guys.
#### -o ```s```, --output ```s```
Output naming scheme. Options are as follows:
* ```n``` (name of note: "A4.wav"),
* ```k``` (key number: "49.wav"),
* ```s``` (note but sortable: "49-A4.wav"),
* ```m``` (MIDI note: "69.wav").
The default mode is ```s```.
#### -p ```"blah-"```, --prefix ```"blah-"```
Optional: output prefix, to put before file names when they're being saved. This is going to belch out 88 files when you run it, so it is wise to use a prefix. Use quotation marks around it.