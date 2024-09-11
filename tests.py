import unittest


def Third(n):  
    a_list = [2, 4, -2, -8] 
    largest_sum = a_list[0] 
    for i in range (0, len(a_list)):
      for j in range(i, len(a_list)):
         sum = 0 
         for z in range(i, j+1):
             sum+= a_list[z] 
         if largest_sum < sum : 
             largest_sum = sum  
    return largest_sum 



def Second(n):
    a_list = [2, 4, -2, -8]
    prefix = [0] * (len(a_list)+1)  
    for i in range(0, len(a_list)):
        prefix[i] = a_list[i] + prefix[i-1]
    largest_sum = prefix[-1]
    for j in range(0,len(a_list)):
        for z in range(j, len(a_list)):
            sum = prefix[z] - prefix[j-1]
            if sum > largest_sum:
                largest_sum = sum
    return largest_sum


def First(n):  
    a_list = [2, 4, -2, -8]
    largest_sum = a_list[0]
    sum = 0
    for i in range(0, len(a_list)):
        sum = sum + a_list[i]
        if sum < a_list[i] :
            sum = a_list[i]
        if largest_sum < sum :
            largest_sum = sum
        if sum < 0 : 
            sum = 0 
    return largest_sum


class TestErg(unittest.TestCase):
   def test_ergasiaf(self):
      self.assertEqual(First([2, 4, -2, -8]), 6)

   def test_ergasiafs(self):
      self.assertEqual(Second([2, 4, -2, -8]), 6)


   def test_ergasiat(self):
      self.assertEqual(Third([2, 4, -2, -8]), 6)



if __name__ == "__main__":
    unittest.main()
