#Input string
text = input("Input your text: ")
suffix = input("Input your suffix: ")
# condition to remove end string
if text.endswith(suffix):
    text = text[:-len(suffix)]
#Output
print(text)
