submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

are_identical = set(submitted) == set(attended)
print("Are the two lists identical in terms of content?", are_identical)
