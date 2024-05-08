submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended = list(set(attended) & set(submitted))
print("Updated attended list:", attended)
