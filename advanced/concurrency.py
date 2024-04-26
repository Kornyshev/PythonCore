import asyncio
import multiprocessing
import threading
import time


# Threading example for I/O-bound tasks
def thread_worker(number):
    """
    Simulates an I/O-bound task by sleeping and then printing a message.
    """
    print(f"Thread {number} starting.")
    time.sleep(2)  # Simulate a delay, e.g., waiting for a network response
    print(f"Thread {number} finished.")


def run_threads():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=thread_worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Multiprocessing example for CPU-bound tasks
def cpu_bound_worker(number):
    """
    Simulates a CPU-bound task that performs heavy calculations.
    """
    print(f"Process {number} starting.")
    result = sum(i * i for i in range(10000000))
    print(f"Process {number} finished with result {result}.")


def run_processes():
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=cpu_bound_worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# Asyncio example for asynchronous I/O operations
async def async_task(name, delay):
    """
    Simulates an asynchronous I/O-bound task.
    """
    print(f"Task {name} started.")
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay}s delay.")


async def run_async_tasks():
    tasks = [async_task(f"Task{i}", i) for i in range(5, 0, -1)]
    await asyncio.gather(*tasks)


# Main function to run all examples
def main():
    print("Running threading example...")
    run_threads()

    print("\nRunning multiprocessing example...")
    run_processes()

    print("\nRunning asyncio example...")
    asyncio.run(run_async_tasks())


if __name__ == "__main__":
    main()
