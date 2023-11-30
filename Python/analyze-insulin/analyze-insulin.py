# Analyze insulin
with open('preproinsulin-seq.txt', 'r') as file:
    lines = file.readlines()

# Remove specified characters and spaces
characters_to_remove = ['ORIGIN', '1', '61', '//', ' ', '\n', '\r']

modified_lines = []
for line in lines:
    modified_line = line
    for char in characters_to_remove:
        modified_line = modified_line.replace(char, '')
    modified_lines.append(modified_line)

# Write the modified content back to the file
with open('preproinsulin-seq.txt', 'w') as file:
    file.writelines(modified_lines)
