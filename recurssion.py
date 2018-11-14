def missing_number_list(list1):

   missing_values_list = list()
   sorted_list = sorted(list1)
   upper = sorted_list[-1]
   lower = sorted_list[0]
   if len(sorted_list) == 0:
       return "invalid input"
   if not isinstance(list1, list):
       return 'only lists are allowed'
   for i in range(lower, upper):
       if i not in list1:
           missing_values_list.append(i)

   return missing_values_list


if __name__ == '__main__':
   list1 = [1, 2, 3, 5, 6, 7, 9, 10, 11]
   print(missing_number_list(list1))