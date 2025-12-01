import csv

# --- Step 1: Write Data to CSV ---
# newline='' prevents blank lines between rows on Windows
with open("dat.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["Name", "Age", "Place"])
    w.writerow(["Aju", 22, "Kochi"])
    w.writerow(["Remya", 25, "TVM"])

# --- Step 2: Read Specific Columns ---
with open("dat.csv", "r") as f:
    reader = csv.reader(f)
    
    # Loop through each row in the CSV
    for row in reader:
        # row[0] is Name, row[2] is Place
        print(row[0], row[2])