class LinearPolynomial():

    def __init__(self, m, b):
        self.m = m
        self.b = b
        
    def __str__(self, m, b):
        return f'{self.m}x + {self.b}'

    def __add__(self, other):
        
        """
        This function adds the other instance of LinearPolynomial
        to the instance referenced by self.

        Returns
        -------
        The sum of this instance of LinearPolynomial with another
        instance of LinearPolynomial. This sum will not change either
        of the instances reference by self or other. It returns the
        sum as a new instance of LinearPolynomial, instantiated with
        the newly calculated sum.


        """
        other = LinearPolynomial
      
    
#         return f"{self.m + other.m}x +  {self.b + other.b}"



# polynom1 = LinearPolynomial(5, 6)
# # polynom2 = LinearPolynomial(2, 3)
# # polynom_result = polynom1 + polynom2
# print(polynom1)


