
# Read a file
from pydoc import text


f = open("doc.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#Read a single Line
f = open("doc.txt", "r")
line1 = f.readline()
print(line1)
f.close()

# Write function to overwrite Line 
f = open("test.txt", "w")
f.write("Hi i am a Full Stack Developer")
f.close()

# Append function to add content in Line 
f = open("test.txt", "a")
f.write("\n After that node js") #\n for next line
f.close()

with open("sample.text", "w") as f:
    f.write("This is a Sample file")
    f.close()
