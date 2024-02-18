Name: Suhas Badrinath Kowligi

UTA ID: 1002157070 (Email: sxk7070@mavs.uta.edu)

Programming Language: Python (versions 3.6 and above)

Code Structure:

The search strategy implementation follows object-oriented approach where the class - "StateSpaceSearch" encapsulates the 2 important methods - "UCS()" -> for uninformed search and "A_star()". Based on the arguments passed from the command line, especially the last argument which specifies the heuristic file path, the appropriate strategy is chosen for finding the optimal route between source and destination. In the "__main__" block, we initialize an object with input file, source, destination along with the search strategy in the "__init__" constructor. After initialising, we call an encapsulated method - "find_route()". This method will invoke the appropriate search method based on the selected strategy. The two strategies are defined using Enums (built-in). There are other helper functions to construct graph from the input file, construct heuristic data structure from the heuristic file and a function to print the route from source to destination in desired format as well.

Instructions:

• The main script to run is "find_route.py". 

• Before running it, make sure the Python's version is ***AT LEAST 3.6*** since f-strings are used to print the desired output. To confirm the version: "python --version". If both Python2 and Python3 exists in the system, use "python3" directly instead of just "python" command while running the script.

• Use the following format while running: "python find_route.py <input_file> (required) <source> (required) <destination> (required) <heuristic_file> (optional)". If number of arguments is insufficient except for the last one (heuristic file), then it will throw an error.