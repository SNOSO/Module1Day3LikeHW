input_file = 'Input.gmt.txt'
string = 'STRING1.txt'

FA_genes = [] # create empty list for keyword list
all_genes = [] # create empty list for string
filtered_list = [] # create empty list for filtered list

with open(input_file, 'r') as f: # open file
    for line in f: # for each line in file
        line = line.split('\t') # split line by tab
        FA_genes.append(line[2:])

with open(string, 'r') as f: # open file
    for line in f: # for each line in file
        line = line.split('\t') # split line by tab
        all_genes.append(line) # append first column to list

# find string in FA_genes from all_genes and append to filtered_list
for row in all_genes: # for each row in all_genes
    if row[0] in FA_genes: # if first column in row is in FA_genes
        if row[1] in FA_genes: # if second column in row is in FA_genes
            filtered_list.append(row) # append row to filtered_list

# write filtered_list to file
with open('string_filtered.txt', 'w') as f:
    for row in filtered_list:
        f.write('\t'.join(row))


