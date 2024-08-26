import pandas

content=pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict={row.letter:row.code for (index,row) in content.iterrows()}
word=input("Enter a word: ").upper()
list1=[new_dict[n] for n in word if n in new_dict]
print(list1)
