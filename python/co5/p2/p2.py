# Open 'in.txt' for reading and 'output.txt' for writing at the same time
with open("p2.txt", "r") as f1, open("output.txt", "w") as f2:
    
    # enumerate(f1, start=1) gives us pairs of (line_number, line_content)
    # We start counting at 1 instead of the default 0
    for i, line in enumerate(f1, start=1):
        
        # Check if the line number is odd
        if i % 2 != 0:
            f2.write(line)