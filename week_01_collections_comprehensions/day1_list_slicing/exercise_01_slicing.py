# Audio sample data (simulated amplitude values)
samples = [0.1, 0.3, 0.5, 0.8, 1.0, 0.9, 0.7, 0.4, 0.2, 0.05]

# 1. Get the first 4 samples
first_four = samples[:4]

# 2. Get the last 3 samples
last_three = samples[-3:]

# 3. Get every other sample starting from index 0
every_other = samples[::2]

# 4. Reverse the entire list
reversed_samples = samples[::-1]

print(f"First four: {first_four}")
print(f"Last three: {last_three}")
print(f"Every other: {every_other}")
print(f"Reversed: {reversed_samples}")
