import matplotlib.pyplot as plt

# Sample data for visualization
test_cases = [
    "Login Test", "Search Test", "Skip Ad Test", "Play/Pause Test",
    "Like/Dislike Test", "Subscribe Test", "Comment Test", "Share Test", "Integrated Test"
]

# Assuming all tests passed for this example
execution_status = [1] * len(test_cases)  # 1 for pass, 0 for fail

# Sample execution times in seconds
execution_times = [12, 15, 10, 14, 13, 16, 20, 18, 30]

# Plotting execution status
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.barh(test_cases, execution_status, color='green')
plt.xlabel('Execution Status (1: Pass, 0: Fail)')
plt.title('Test Case Execution Status')
plt.grid(axis='x')

# Plotting execution times
plt.subplot(1, 2, 2)
plt.barh(test_cases, execution_times, color='blue')
plt.xlabel('Execution Time (seconds)')
plt.title('Test Case Execution Time')
plt.grid(axis='x')

plt.tight_layout()
plt.show()
