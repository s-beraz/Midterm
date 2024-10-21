#Midterm Exam
#Problem2.py
#Name: Skye Beraz
#Date: 10/20/2024

def findVowel(string):
    string = string.upper()
    vowelList = "AEIOU"
    freq = [0,0,0,0,0]
    for ch in string:
        position = (vowelList.find(ch))
        if position != -1:
            freq[position] += 1
    output = ""	
    for i in range(5):
        print(vowelList[i], ":", freq[i])
        line = vowelList[i] + "," + str(freq[i]) + "\n"
        output = output + line
		
def main():
    string = input("Enter a sentence: ")
    findVowel(string)
