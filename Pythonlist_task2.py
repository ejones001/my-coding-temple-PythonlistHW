submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = set(submitted) & set(attended)
print("Students who both submitted assignments and attended the class:", list(common_students))
