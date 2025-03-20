def vowel_counts(string):
    string = string.lower()
    vowel ="aeiou"
    count = 0
    
    for char in string :
        if char in vowel:
            count +=1
            print(vowel)
    return count

text = input("Enter a sting : ")
vowel_count = vowel_counts(text)
print(f"Number of vowels: {vowel_count}")