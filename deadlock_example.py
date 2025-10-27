"""
Example of thread deadlock - a common concurrency code smell.
"""
import threading
import time


# Two shared locks
lock1 = threading.Lock()
lock2 = threading.Lock()


def thread_function_1():
    """Thread 1: acquires lock1 first, then lock2."""
    print("Thread 1: trying to acquire lock1...")
    with lock1:
        print("Thread 1: acquired lock1")
        time.sleep(0.1)  # Simulate some work
        
        print("Thread 1: trying to acquire lock2...")
        with lock2:
            print("Thread 1: acquired lock2")
            print("Thread 1: completed successfully")


def thread_function_2():
    """Thread 2: acquires lock2 first, then lock1 - DEADLOCK!"""
    print("Thread 2: trying to acquire lock2...")
    with lock2:
        print("Thread 2: acquired lock2")
        time.sleep(0.1)  # Simulate some work
        
        print("Thread 2: trying to acquire lock1...")
        with lock1:
            print("Thread 2: acquired lock1")
            print("Thread 2: completed successfully")
  i = 1/0

def main():
    print("Starting deadlock example...")
    print("This program will hang forever due to deadlock!\n")

    # Create two threads
    t1 = threading.Thread(target=thread_function_1, name="Thread-1")
    t2 = threading.Thread(target=thread_function_2, name="Thread-2")
    
    # Start both threads
    t1.start()
    t2.start()
    
    # Wait for threads to complete (they never will!)
    t1.join()
    t2.join()
    
    print("This message will never be printed due to deadlock")

def test():
  v = 10

if __name__ == "__main__":
    main()

