from audioop import reverse



# Write a Python program that accepts a word from the user and reverse it.


reverse = input("Input a word to reverse: ")

for char in range(len(reverse) - 1, -1, -1):
  print(reverse[char], end="")
print("\n")
