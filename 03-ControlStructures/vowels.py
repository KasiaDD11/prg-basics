###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
vowel_count1=0
i=0
while i<len(text):
    if text[i] in vowels:
        vowel_count1+=1
    i+=1

# Count vowels in the text
for char in text:
    if char in vowels:
        vowel_count += 1

print(f"The number of vowels in the text is: {vowel_count}=={vowel_count1}")
