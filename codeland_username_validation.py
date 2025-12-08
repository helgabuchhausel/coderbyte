import re 
def CodelandUsernameValidation(strParam):
  # code goes here
  pattern = r"^[a-zA-Z][a-zA-Z0-9_]{2,23}[a-zA-Z0-9]$"
  if re.fullmatch(pattern, strParam):
    return "true"
  else:
    return "false"


# keep this function call here 
print(CodelandUsernameValidation(input()))