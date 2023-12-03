# Using the build in filter function

nums = range(1,1000)

def is_prime(num):
    for i in range(2,num):
        if(num % i) == 0:
            return False
    return True

# We can use the filter built in method to pass a filter and an item to be filtered
primes=filter(is_prime, nums)

# This is stored as a filter object to conserve memory.
print(primes)

# However it can be converted to other objects such as a list
primes = list(primes)
print(primes)
