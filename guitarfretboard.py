import argparse
from itertools import cycle,dropwhile,islice,product
from prettytable import PrettyTable
from termcolor import colored
from sys import exit


notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
cycled_notes = cycle(notes)

def generateScale(rootNote,scaleIntervals):
	notesIterator = dropwhile(lambda x: x!=rootNote,cycled_notes)
	noteList = list(islice(notesIterator,None,13))
	scale = [rootNote]
	noteCounter = 0
	for i in scaleIntervals:
		noteCounter = noteCounter + i
		scale.append(noteList[noteCounter])
	del scale[len(scale) - 1]
	return scale

def main():
	scaleSteps = {'maj':[2,2,1,2,2,2,1],'natMin':[2,1,2,2,1,2,2],'pentMin':[3,2,2,3,2],'blues':[3,2,1,1,3,2],'pentMaj':[2,2,3,2,3],'harMin':[2,1,2,2,1,3,1],'melMin':[2,1,2,2,2,2,1]}
	parser = argparse.ArgumentParser(description='Prints fretboard for tunning given')
	parser.add_argument('-t','--tuning',nargs=6, choices = notes+ [x.lower() for x in notes],help=argparse.SUPPRESS)
	parser.add_argument('-n','--frets', type=int,choices=list(range(1,25)),help=argparse.SUPPRESS)
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f','--find',type=str,choices=notes+ [x.lower() for x in notes],help=argparse.SUPPRESS)
	group.add_argument('-s','--scale',nargs=2,action='append',help=argparse.SUPPRESS)
	args = parser.parse_args()
	tuning = args.tuning
	numberOfFrets = args.frets
	elementToShow = args.find
	scale = args.scale
	if tuning is None:
		tuning = ['E','A','D','G','B','E']
	tuning = [x.upper() for x in tuning]
	if numberOfFrets is None:
		numberOfFrets = 12	

	if scale is not None:
			if scale[0] in [list(x) for x in (product(notes,(list(scaleSteps.keys()))))]:
				scaleRoot = scale[0][0]
				scaleType = scaleSteps[scale[0][1]]
				scaleNotes = generateScale(scaleRoot,scaleType)
				print("Scale Notes are: " + ' '.join(scaleNotes))
				if scale[0][1] == "pentMaj":
					relativeScale = generateScale(scaleRoot,scaleSteps['maj'])
					chords = getChords(relativeScale)
				elif scale[0][1] == "pentMin":
					relativeScale = generateScale(scaleRoot,scaleSteps['natMin'])
					chords = getChords(relativeScale)
				else:
					chords = getChords(scaleNotes)
				chordChart = PrettyTable(["Chord Type", "Root", "Third", "Fifth"])
				print("Chords in scale are:")
				for v in chords:
					chordChart.add_row([colored(v[0][0] + " " + v[1], "green"),
						 colored(v[0][0], 'blue', attrs=['bold']),
						 colored(v[0][1], 'blue', attrs=['bold']),
						 colored(v[0][2], 'blue', attrs=['bold'])
					])
				print(chordChart)
			else:
				raise ValueError("Incorrect scale input, see help!")
				exit()
	
	fretboard = PrettyTable()
	fretboard.field_names = [colored(x, 'dark_grey') for x in range(0, numberOfFrets+1)]
	
	for current_note in reversed(tuning):
		notesIterator = dropwhile(lambda x:x!=current_note,cycled_notes)
		noteList = (list(islice(notesIterator,1,numberOfFrets+1)))
		if elementToShow is not None:
			noteList = colored(current_note, 'red', attrs=['bold']) + [colored(x, 'green',  attrs=['bold']) if x==elementToShow else colored('-', 'dark_grey') for x in noteList]
		elif scale is not None:
			noteList = [colored(current_note, 'red', attrs=['bold'])] + [(colored(x, 'blue', attrs=['bold']) if x is scaleRoot else colored(x,'green', attrs=['bold'])) if x in scaleNotes else colored('-', 'dark_grey') for x in noteList]
		fretboard.add_row(noteList)
	print("\nFretboard--->")
	print(fretboard)

def getChords(scale_notes):
	len_scale = len(scale_notes)
	steps = 2
	chord_triads = []
	for i in range(len_scale):
		rootNote = scale_notes[i]
		thirdNote = scale_notes[(i+steps)%len_scale]
		fifthNote = scale_notes[(i+steps+steps)%len_scale]
		chordType = getChordType(rootNote,thirdNote,fifthNote)
		chord_triads.append([(rootNote,thirdNote,fifthNote),chordType])
	return chord_triads

def getChordType(rootNote,thirdNote,fifthNote):
	intervals = (getInterval(rootNote,thirdNote),getInterval(thirdNote,fifthNote))
	if (intervals == (4,3)):
		return "Major"
	elif (intervals == (3,4)):
		return "Minor"
	elif (intervals == (3,3)):
		return "Diminished"
	elif (intervals == (4,4)):
		return "Augmented"
	else:
		return "Undefined"

def getInterval(note1,note2):
	index_note1 = notes.index(note1)
	for i in range(12): # 12 notes always
		if notes[(index_note1 + i) % 12] == note2:
			return i

if __name__ == "__main__":
	main()