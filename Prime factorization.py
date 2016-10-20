n= int(input('Enter the number you would like to know the factors for...'))
#n = int(input())
a=0
for z in range (0, n):
   a=a+1
   if n % a == 0:
      c= int(n / a)
      print(a, 'times', c, 'equals', n)
      continue
   else:
      continue
        
        # trying for prime factorization
      x= a
      y= c
      while a % 2 == 0:
         a= a/2
         continue
      if a != x:
         print(a)
      else:
         print('no prime factors')
      while c %2 == 0:
         c= c/2
         continue
      if y != c:
         print(c)
      else:
         print('no prime factors')