import time

def loading_screen(task_name):
    print(f"Doing {task_name}... ", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)  # Adjust the sleep duration as needed
    print("\rdone!", end=' '*20, flush=True)
    for _ in range(2):
        time.sleep(0.5)
    print('this is done', flush=False)

# Example usage
loading_screen("the task")
