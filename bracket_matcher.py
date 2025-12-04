def BracketMatcher(strParam):
  count = 0
  for char in strParam:
    if char == '(':
      count += 1
    elif char == ')':
      count -= 1
            
    if count < 0:
      return 0
    
  return 1 if count == 0 else 0

# keep this function call here 
print(BracketMatcher(input()))