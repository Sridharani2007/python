file = "sample.txt"

# Write to file (overwrite if exists)
with open(file, "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("File handling is important.\n")

# Append to file
with open(file, "a") as f:
    f.write("Practice makes perfect.\n")

# Read file
with open(file, "r") as f:
    text = f.read()

print("File Content:\n", text)

print("Lines:", text.count("\n"))
print("Words:", len(text.split()))
print("Characters:", len(text))
print("Python count:", text.count("Python"))
