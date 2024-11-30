from concurrent.futures.thread import ThreadPoolExecutor


def print_number(number):
    print(number)

numbers = [1,2,3,4,5,6,7,8,9,4,3,7,8,3]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(print_number, numbers)

# When the workers doesnt have any data to operate then they return None
for result in results:
    print(result)