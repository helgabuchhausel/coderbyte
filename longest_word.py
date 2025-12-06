import re 

def LongestWord(sen):
  clean_sen = re.sub(r'[^a-zA-Z0-9]', ' ', sen)
  words = clean_sen.split()
  sen = max(words, key=len)
  return sen

# keep this function call here 
print(LongestWord(input()))