The First Line: nums = list(map(int, input(...).split())) 

This line transforms a single string of text into a list of integers. 
	
	input(...): Pauses the program to let the user type something (e.g., "10 20 30").
	.split(): Chops that string into a list of smaller strings based on spaces: ["10", "20", "30"].
	 map(int, ...): Goes through that list and converts every string into an actual number (integer)
	 list(...): Collects those numbers and puts them into a formal Python list: [10, 20, 30]

The Second Line: target = int(input(...)) 

This line captures a single specific value. 

	input(...): Asks the user for a value (e.g., "50").
	int(...): Converts that text into a number so you can perform math with it later

 this uses dictionary to "remember" every number it has seen so far and where it found it ({number: index})

	A class in Python is a user-defined template or "blueprint" used to create objects. 
	It allows you to group related data (attributes) and behaviors (methods) into a single, reusable unit

Example Trace:

nums = [2, 7, 11], target = 9

Index 0 (n=2): Needs 7. 7 is not in prevMap. Store {2: 0}.

Index 1 (n=7): Needs 2. 2 is in prevMap!

Result: Returns [0, 1]
