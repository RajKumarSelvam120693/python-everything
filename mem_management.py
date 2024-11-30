# Memory managemt in Python involves combination of automatic garbage collection, reference counting
# amd various internal optimisations to efficiently manage memory allocation
# and deallocation.
# Understanding these mechanisms can help developers write more efficient and robust apps.
#     1. Key concepts in Python Memory Management
#     2. Memory allocation and deallocation.
#     3. Reference counting
#     4. Garbage collection
#     5. gc module
#     6. Best practices

# Reference counting
# It is the primary method Python uses to manage memory. Each object in Python maintains count of reference
# pointing to it. When the reference ount drops to zero, the memory occupied by the object is dellocated.
import sys
a=[]
# 2 because of one reference is from a and one from getrefcount()
print(sys.getrefcount(a))

b=a
print(sys.getrefcount(b))

# Garbage collection
# Python includes a cyclic garbage collector to handle reference cycles. Reference cycles
# occur when objects reference each other, preventing their reference counts from reaching zero

import gc

gc.enable()

gc.disable()
print(gc.collect())

print(gc.get_stats())









