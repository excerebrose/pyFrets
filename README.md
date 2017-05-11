# pythonGuitarFretboard
A simply python tool to visualise a guitar keyboard in alternate tunings, includes predefined scales
For usage:


Run the program with 
```
python guitarfretboard.py.
```
Basic parameters are:
```
-t --tuning  : Alternate tuning from 6th to 1st. Usage:Notes seperated by spaces (Can be lowercase/upper case, however no flats allowed) Default tuning is E A D G B E
-n --frets  : Integer that cuts the number of frets to display min = 1, max = 24. Default is 12 frets
```
Furthermore,
You have an option between displaying a scale or finding a particular note
```
-f --find: Find a note in the guitar fretboard and display everywhere it occurs. Works with alternate tunings too
-s --scale: Display scale notes on the guitar fretboard. Works with alternate tunings too. Available scales are 'maj','natMin','harmMin','melMin','pentMin','pentMaj','blues'

```
sample for finding G major scale in Alternate tuning of E A C# A A E with 20 frets:
```
python guitarfretboard.py -t E A C# A A E -n 20 -s G maj
```

## MIT License

Copyright (c) 2017 Harjyot Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
