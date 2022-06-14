# Strings

text = "X-DSPAM-Confidence:    0.8475"


def myinput():
  text = "X-DSPAM-Confidence:    0.8475"
  return text
def compute(text): 
  pos=text.find(":")
  peice=text[pos+1:] #string slicing or even strip fuction can also be used
  convert=float(peice)
  return convert
def output(convert): 
  print(convert)
def main():
  text=myinput()
  c=compute(text)
  output(c)
main()  