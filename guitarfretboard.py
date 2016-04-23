import argparse
from itertools import cycle,dropwhile,islice,product
from prettytable import PrettyTable
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
	parser.add_argument('-t','--tuning',nargs=6, choices = notes+ map(lambda x:x.lower(),notes),help=argparse.SUPPRESS)
	parser.add_argument('-n','--frets', type=int,choices=range(1,25),help=argparse.SUPPRESS)
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-f','--find',type=str,choices=notes+ map(lambda x:x.lower(),notes),help=argparse.SUPPRESS)
	group.add_argument('-s','--scale',nargs=2,action='append',help=argparse.SUPPRESS)
	args = parser.parse_args()
	tuning = args.tuning
	numberOfFrets = args.frets
	elementToShow = args.find
	scale = args.scale
	if tuning is None:
		tuning = ['E','A','D','G','B','E']
	tuning = map(lambda x:x.upper(),tuning)
	if numberOfFrets is None:
		numberOfFrets = 12	

	if scale is not None:
			if scale[0] in map(lambda x:list(x),(product(notes,(scaleSteps.keys())))):
				scaleRoot = scale[0][0]
				scaleType = scaleSteps[scale[0][1]]
				scaleNotes = generateScale(scaleRoot,scaleType)
				print "Scale Notes are: " + '-'.join(scaleNotes)
			else:
				raise ValueError("Incorrect scale input, see help!")
				exit()

	fretboard = PrettyTable()
	fretboard.add_column("0",range(1,numberOfFrets+1))
	for i in range(len(tuning)):
		current_note = tuning[i]
		notesIterator = dropwhile(lambda x:x!=current_note,cycled_notes)
		noteList = (list(islice(notesIterator,1,numberOfFrets+1)))
		if elementToShow is not None:
			noteList = map(lambda x: x if x==elementToShow else 'x',noteList)
		elif scale is not None:
			noteList = map(lambda x: x if x in scaleNotes else 'x',noteList)
		fretboard.add_column(current_note,noteList)

	print fretboard
if __name__ == "__main__":
	main()