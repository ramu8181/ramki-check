#### Bubble Sort Exercise
#Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

#elements = [
##        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#    ]
#bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

#bubble_sort(elements, key='transaction_amount')
#This will sort elements by transaction_amount and your sorted list will look like,
#
#elements = [
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#    ]
#But if you call it like this,
#
#bubble_sort(elements, key='name')
#output will be,
#
#elements = [
#        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#    ]
###
# you can use this to sort strings too


class bubble_sort_yymethods():

  def __init__(self):
     return

  def bubble_sort(self,elements):
      size = len(elements)
      for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            return elements
            break
     
  def bubble_sort_dict1 (self,elements):
      if type(elements) == list :
         for each  in elements:
            for  key,value in each:
               print ( key , value)
      

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    #elements = [1,2,3,4,2]
    #elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    elements_dict1 = [        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    elements_dict2 = [
       { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
       { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},   ]

    if ( input("Enter the sort") == "dict"):
         obj = bubble_sort_yymethods()
         print (obj.bubble_sort(elements_dict1))
    else:
        obj = bubble_sort_yymethods()
        print (obj.bubble_sort(elements))
    print ( elements_dict1)

