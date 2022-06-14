# Lists

filename = "dataset/romeo.txt"
def myinput():
  fname = input("Enter file name: ")
  return fname
def compute(fname):
  f=open(fname)
  li=list()  
  for line in f:
    l=line.split()
    for w in l:
      if w not in li:
        li.append(w)
  return li
def output(li):
  li.sort()
  print(li)  
def main():
  fname=myinput()
  li=compute(fname)
  output(li)
main()    



def myinput():
  
  fname = input("dataset/mbox-short.txt")
  return fname

  
def compute(fname):
  count=0  
  f=open(fname) 
  word=list()
  for line in f:
    if line.startswith("From "): 
      w=line.split() 
      word.append(w[1])  
      count=count+1  
  return word,count 
  
  
def output(word,count):
  for i in word:  
    print(i)
  print("There were",count, "lines in the file with From as the first word")

  
def main():
  fname=input()
  word,count=compute(fname)
  output(word,count)
main()    