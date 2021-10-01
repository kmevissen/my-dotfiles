import numpy

size = 10000000

users_a = 14381
users_b = 14315
success_a = 7976
success_b = 7811

a = numpy.random.beta(success_a, users_a-success_a, size)
b = numpy.random.beta(success_b, users_b-success_b, size)

result = numpy.sum(a > b)/size

print(result)