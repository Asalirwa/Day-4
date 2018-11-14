def power(n, p):
   if not ((isinstance(n, int) or isinstance(n, float)) and isinstance(p, int)):
       return 'invalid input'

   if p == 0 or n == 1:
       return 1
   if n == 0:
       return 0

   if p >= 1:
       return n*power(n, p-1)

   p = abs(p)
   return 1/(n*power(n, p-1))


if __name__ == '__main__':
   print(power(-5, -5)) 
def compute_sum(list1):
   if not isinstance(list1, list):
       return 'Invalid argument type. This should be a list'
   mysum=0
   for i in list1:
       if isinstance(i,int):
           mysum+=i

       elif isinstance(i,list):
           mysum+=compute_sum(i)

   return mysum

if __name__ == '__main__':
   print(compute_sum(['a',3,[5,6]]))