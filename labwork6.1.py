#Q.1
'''
Write a Python program to create a text file named sample.txt.
- Write the sentence "Python is a versatile programming language." into the file.
'''
try:
    file=open("sample.txt","x")
    file.close
except FileExistsError:
    print("File already exists.")

with open("sample.txt","w") as file:
    file.write("Python is a versatile programming language.")
        

#Q.2
'''
Write a Python program to open an existing file in read mode and display its content.
- Open the file in write mode, overwrite the content, and write a new sentence
"Learning file handling in Python is fun!".
'''

with open("sample.txt","r") as file:
    content=file.read()
    print(content)

with open("sample.txt","w") as file:
    file.write("Learning file handling in Python is fun!")

#Q.3
'''
Write a Python program to read and print the contents of the file sample.txt line by
line.
'''
with open("sample.txt","r") as file:
    print(file.readlines())



#Q.4
'''
Create a Python program that writes multiple lines of text to a file named notes.txt.
- The content should be:
Line 1: Python is easy to learn.
Line 2: It has numerous libraries.
Line 3: File handling is one of its features.'''

try:
    file=open("notes.txt","x")
    file.close
except FileExistsError:
    print("File already exists.")

with open("notes.txt","w") as file:
    file.writelines("Line 1: Python is easy to learn.\nLine 2: It has numerous libraries.\nLine 3: File handling is one of its features.") 


#Q.5
'''
Write a Python program to append "Line 4: Python supports multiple modes of file
handling." to the file notes.txt.'''

with open("notes.txt","a") as file:
    file.writelines("\nLine 4: Python supports multiple modes of file handling.")

#Q.6
'''
Write a Python program to open a file in binary mode.
- Use rb mode to read the content of a text file and display its content in binary format.'''
with open("notes.txt","rb") as file:
    print(file.read())



#Q.7
'''
Write a Python program that reads a text file and counts the total number of words,
characters, and lines in the file.'''
with open("notes.txt","r") as file:
    content=file.read()
    
lines=len(content.splitlines())
words=len(content.split())
character=len(content)
print(f"\nLINES:{lines},\nWORDS:{words},\nCHARACTER:{character}")
    


#Q.8
'''
Write a Python program to open a text file in read-write mode.
- Read the existing content.
- Append the line "This file was last modified by adding this sentence." to the file.'''

with open("notes.txt","r+") as file:
    content=file.read()
    print(content)
with open("notes.txt","a") as file:
    file.write("\nThis file was last modified by adding this sentence.")



#Q.9
'''
Create a Python program that takes a word as input and searches for it in sample.txt.
- If found, display the line number(s) where the word appears.'''

with open("sample.txt","r") as file:
    lines=file.readlines()

search_word=input("enter word you want to search:").strip()

line_num=1

for line in lines:
    if search_word in line:
        print("found",search_word,"on line",line_num,":",line.strip())
    


#Q.10
'''
Write a Python program to read content from an existing file source.txt and copy it to a
new file backup.txt.'''

import shutil

shutil.copy("sample.txt", "backup.txt")

print("File copied successfully!")

#Q.11
'''
Create a Python program to demonstrate all modes (r, w, a, r+, w+, a+). For each
mode:
- Open a file, Write or read content depending on the mode.
- Close the file properly.'''

print("---Demonstrating Python File Modes---")

# Ensure the file exists before 'r' and 'r+' modes
# Create it initially
with open("python.txt", "w") as f:
    f.write("Initial content for testing file modes.\n")

print("\n1. Read only mode 'r'")
with open("python.txt", "r") as file:
    content = file.read()
    print("Successfully read content:")
    print(content)

print("\n2. Write only mode 'w'")
with open("python.txt", "w") as file:
    file.write("Write mode overwrites old text completely.")
    print("Successfully wrote in 'w' mode (file overwritten).")

print("\n3. Append only mode 'a'")
with open("python.txt", "a") as file:
    file.write("\nAppend mode adds text at the end.")
    print("Successfully appended text in 'a' mode.")

print("\n4. Read and Write mode 'r+'")
with open("python.txt", "r+") as file:
    content = file.read()
    print("Content AFTER previous operations (before writing in r+):")
    print(content)

    file.seek(0)  # Move cursor to start
    file.write("This text is written at the beginning using r+.\n")
    print("Successfully wrote at the beginning in 'r+' mode.")

print("\n5. Write and Read mode 'w+'")
with open("python.txt", "w+") as file:
    file.write("w+ mode overwrites the file and allows reading.")
    file.seek(0)
    print("Reading after writing in 'w+':")
    print(file.read())

print("\n6. Append and Read mode 'a+'")
with open("python.txt", "a+") as file:
    file.write("\nUsing a+ mode: appended this line.")
    file.seek(0)
    print("Reading after writing in 'a+':")
    print(file.read())

mode=("r","w","a","r+","w+","a+")
type_=("read only","write only","append only","read and write","write and read","append and read")

print("-"*9,"|","-"*28,"|")
print(f"{'Mode':<10}|{'Type':<30}|")
print("-"*9,"|","-"*28,"|")

for i in range(len(mode)):
    print(f"{mode[i]:<10}|{type_[i]:<30}|")
print("-"*40)

