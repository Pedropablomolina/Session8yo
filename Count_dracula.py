# plan:
# 1. open the book (fp = open())
# 2. define a count variable
# 3. read line by line
# 4. if "Dracula" in the line.... increase the counter
# 5. profit! print counter

fp = open("dracula.txt")
count = 0
for line in fp:
    # if "dracula" in line.lower():
    #     count = count + 1
    line = line.lower()
    count = count + line.count("dracula")
print(f"The word Dracula shows up {count} times!")
