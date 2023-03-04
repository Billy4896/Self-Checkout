import time
from Product import Product
from collections import deque

# Import list to hold the product list imported from the text file.
products = []
imported = []


def init():
    try:
        file = open('products.txt', 'rt')
        for each_line in file:
            barcode, product_name, unit_price = each_line.strip().split(',')
            products.append(Product(barcode, product_name, float(unit_price)))
        file.close()
    except Exception as e:
        print(f"Error {e}")


# Test using a set
def set_test():
    # Create an empty set for testing
    set1 = set()
    # START CLOCK
    startClock = time.time()
    # FOR EACH PRODUCT IN THE LIST
    for i in products:
        set1.add(i)
    # END CLOCK
    endClock = time.time()
    # PRINT TIME ELAPSED
    endTime = float((endClock - startClock) * 1000)
    print(f"The set test total runtime is {endTime} milliseconds.")


# Test using a queue
def queue_test():
    # Create an empty queue
    queue = deque()
    # START CLOCK
    startClock = time.time()
    # FOR EACH PRODUCT IN THE LIST
    for i in products:
        queue.append(i)
    # END CLOCK
    endClock = time.time()
    # PRINT TIME ELAPSED
    endTime = float((endClock - startClock) * 1000)
    print(f"The queue test total runtime is {endTime} milliseconds.")


# Testing a stack
def deque_stack():
    # Create an empty stack
    stack = deque()
    # START CLOCK
    startClock = time.time()
    # FOR EACH PRODUCT IN THE LIST
    for i in products:
        stack.appendleft(i)
    # END CLOCK
    endClock = time.time()
    # PRINT TIME ELAPSED
    endTime = float((endClock - startClock) * 1000)
    print(f"The stack test total runtime is {endTime} milliseconds.")


# Searching Algorithms
# Binary Search
def binary_search(products_list, barcode):
    # Primary key value
    barcode = barcode.get_barcode()
    low = 0
    high = len(products_list) - 1
    mid = 0

    while low <= high:

        mid = (high + low)

        # If x is greater, ignore left half
        if (products_list[mid]).get_barcode() < barcode:
            low = mid + 1

        # If x is smaller, ignore right half
        elif (products_list[mid]).get_barcode() > barcode:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Sequential Search
def sequential_search(products_list, barcode):
    pos = 0
    found = False
    # While the match has not been found.
    while pos < len(products_list) and not found:
        # If the barcode finds a match in the product list return true and break the loop.
        if products_list[pos].get_barcode() == barcode.get_barcode():
            found = True
        # Else increase the position by 1 and continue loop.
        else:
            pos = pos + 1
    # Return if found and the position.
    return found, pos


init()
set_test()
queue_test()
deque_stack()

# Binary Test
barcode_input = input("Enter barcode: ")
new_product = Product(barcode_input)
# START CLOCK
startClock = time.time()
result = binary_search(products, new_product)
if result != -1:
    print("Element can be found at index", str(result))
else:
    print("Element cannot be found in the array")
# END CLOCK
endClock = time.time()
endTime = float((endClock - startClock) * 1000)
# PRINT TIME ELAPSED
print(f"The binary search test total runtime is {endTime} milliseconds")

# Call Sequential
barcode_input = input("Enter barcode: ")
new_product = Product(barcode_input)
# START CLOCK
startClock = time.time()
result2 = sequential_search(products, new_product)
print(result2)
# END CLOCK
endClock = time.time()
endTime = float((endClock - startClock) * 1000)
# PRINT TIME ELAPSED
print(f"The sequential search test total runtime is {endTime} milliseconds")
