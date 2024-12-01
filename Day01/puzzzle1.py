def read_lists_from_file(file_path):
    left_list = []
    right_list = []

    
    with open(file_path, 'r') as file:
        for line in file:
            
            left, right = map(int, line.strip().split())
            # print(left)
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate distances
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    return total_distance

def calculate_similarity(left_list,right_list):
    dict1 = {}
    for val in right_list:
        if val in dict1:
            dict1[val] += 1
        else:
            dict1[val] = 1 
    
    total = 0
    for val in left_list:
        if val in dict1:
            total += val * dict1[val]
    
    return total
        

# Specify your .txt file path
file_path = ".\demo_data.txt"

# Read the lists
left_list, right_list = read_lists_from_file(file_path)
# print(left_list)

# Calculate total distance
# total_distance = calculate_total_distance(left_list, right_list)
# print(f"Total Distance: {total_distance}")


total_similarity = calculate_similarity(left_list,right_list)
print(total_similarity)
