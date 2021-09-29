'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  a=5
  if a<2:
    return False
  elif a==2:
    return True
  else:
    ok=True
    for i in range(3,a/2+1,2):
      if a%i==0:
        ok=False
      if ok==1:
        return True
      else:
        return False

    


  
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p1=0
  for val in lst:
    p1*=val

  print (p1)
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  return True
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  return True
  
  
def main():
  return True

if __name__ == '__main__':
  main()
