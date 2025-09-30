# File Read & Write Challenge

# Open the input file in read mode
with open("input.txt", "r") as infile:
    content = infile.readlines()

# Modify content (example: convert all text to uppercase)
modified_content = [line.upper() for line in content]

# Write modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.writelines(modified_content)

print("File has been read and modified content written to output.txt")
