from itertools import combinations 
 
def find_combinations(arr, target_sum): 
    return [combo for r in range(1, len(arr) + 1) for combo in combinations(arr, r) if sum(combo) == target_sum] 
 
# Example usage 
numbers = [1, 2, 3, 4, 5] 
target = 7 
combinations_list = find_combinations(numbers, target) 
print(combinations_list) 