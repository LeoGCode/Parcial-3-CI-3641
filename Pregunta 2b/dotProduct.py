# Given two vectors of the same size (represented as an array), perform the dot product.
# the dot product.

# The computation must be done concurrently, taking advantage of the mechanisms provided in the language for this purpose.
# mechanisms provided in the language for this purpose.

import threading

result = 0
# Create the vectors
vector_a = [1 for i in range(0, 10000000)]
vector_b = [1 for j in range(0, 10000000)]

def dot_product(a:list, b:list, lock:threading.Lock):
    r = 0
    for i in range(0, len(a)):
        r += a[i] * b[i]
    lock.acquire()
    global result
    result += r
    lock.release()

if __name__ == '__main__':
    
    num_threads = 20

    # Create lock
    lock = threading.Lock()

    slice_vec = len(vector_a) // num_threads

    # Create the threads
    threads = []
    for i in range(0, num_threads):
        threads.append(threading.Thread(target=dot_product, args=(vector_a[i*slice_vec:(i+1)*slice_vec], vector_b[i*slice_vec:(i+1)*slice_vec], lock)))

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the result
    print(result)

