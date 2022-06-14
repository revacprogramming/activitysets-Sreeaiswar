# Conditional Execution

#hrs = input("Enter hours? ")
hrs = int((input("Enter Hours:")))
rate = float (input("Enter rate:"))
gross=( hrs * rate) if hrs <= 40 else 40 * rate + 1.5 * rate * (hrs-40)
print(str(gross))


def compute(h,r):
  if h<40:
    m=h*r
  else:
    m=40*r+(h-40)*1.5*r
  return m  
def output(m):
  print(m)
def main():
  hrs = input("Enter hours? ")
  h=float(hrs)
  rate=input("Enter the Rate")
  r=float(rate)
  m=compute(h,r)
  output(m)
main() 



def myinput():
  score = input("Enter Score: ")
  s =  float(score)
  return s  
def compute(s): 
  x = "NULL"
  if s>0.0 and s<1.0:
    if s >= 0.9 and s<=1.0:
	    x = 'A'
    elif s >=0.8:
	    x='B'
    elif s >=0.7:
	    x='C'
    elif s >= 0.6:
	    x='D'
    else:
	    x ='F'
  else:
    x ="Out of Range"
  return x
def output(x):
  print (x)
def main():
  s=myinput()
  x=compute(s)
  output(x)
main()