def sum_array(array):
    '''Return sum of all items in array
       Args :
             array:
             a list or an array-like object that contains numerical values.

       Returns:  sum of all items in array or list
       Examples  >>> sum_array([1,2,3,4,5,6,7]) = 28
      '''
    array_sum=0
    for i in (array):
        array_sum+=i
    return array_sum


def fibonacci(n):

    '''calculates nth term in fibonacci sequence
    Args :
         n (int): is the nth number of fibonacci sequence that we want to calculate

    Returns:
         int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(5)
        5
        >> fibonacci(8)
        21
    '''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    '''calculates the factorial of n
       Args :
            n (int) is the factorial number you want to calculate
       Returns n!, which is the factorial of n(int)

       Examples:
        >>> factorial(0)
        1
        >> factorial(2)
        2
        >> factorial(3)
        6

    '''
    if n==1 or n==0:
        return 1
    else :
        return n * factorial(n-1)

def reverse(word):

    '''Returns a word in reverse
       Args:
           word(string) a string word without any spaces
           def reverse(word):
       Return:
              string word in reverse
               Examples:
        >>> reverse('trevor')

        >> reverse(1)
        2
        >> factorial(3)
        6

              '''

    if len(word)<=1:
        return word
    else:
        return reverse(word[1:])+ word[0]
