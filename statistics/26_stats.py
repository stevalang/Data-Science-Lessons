def greet_customer(firstName, customerData):
    
    res = ''

    if firstName not in customerData:

        res = 'Welcome! Is this your first time?'
        customerData[firstName]={'visits': 0}
    
    elif customerData[firstName]['visits'] == 1:
        res = f'Welcome back, {firstName}! We\'re glad you liked us the first time!'
    
    else:
        res = f'Welcome back, {firstName}! So glad to see you again!'
    
    customerData[firstName]['visits'] +=1
    
    return res
    
customerData = {'Joe': {'visits': 1},
  'Carol': {'visits': 2},
  'Howard': {'visits': 3},
  'Carrie': {'visits': 4}}

output = greet_customer('Terrance', customerData)
print(output) # --> 'Welcome! Is this your first time?'
