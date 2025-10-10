# Create a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Add elements
numbers.append(60)          # Add at end
numbers.insert(2, 25)       # Insert at index 2
print("After adding elements:", numbers)

# Remove elements
numbers.remove(40)          # Remove value 40
numbers.pop()               # Remove last element
print("After removing elements:", numbers)

# Update elements
numbers[1] = 200
print("After updating:", numbers)

# Loop through list
print("List elements are:")
for num in numbers:
    print(num)

# Sort and reverse
numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)