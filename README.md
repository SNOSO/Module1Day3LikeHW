README
Module 1 Day 3 Homework
The aim of this project is to determine a subnetwork of nodes and edges based on 
a preexisting network and a set of disease specific (Fanconi anemia) genes.


Project Description
This python script iterates the disease specific query genes over a given network to find matches from both objects.
If a match is found, the script adds the row to a newly created list in Cytoscape-friendly format (i.e. gene1 gene2 edgeattribute).
The script will export the gene query list to a new file a specified path for visualization in Cytoscape.

Some of the challenges you faced and features you hope to implement in the future.


How to Install and Run the Project
Python3 must be installed with the following dependencies:
- pandas
- numpy

Navigate to the directory containing `Mod1Day3LikeHW.py`.
Run `python3 Mod1Day3LikeHW.py` in terminal and wait for your results.

Using a code text editor of your choice, you can change the 'input_file' and 'string' variables to the path of your specific files and save changes.
Your results will be in the designated output folder in the script.

Software is tested and runs in less than 10 minutes on a standard laptop for the complete dataset.

Further project description and motivation can be found here: https://docs.google.com/document/d/1I39nYymqYyjDHmHoOmxpRw9psYLTbxNzEr9WV4KXstk/edit?usp=sharing
