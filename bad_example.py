from triangle_area import calculate_area_by_base_height, calculate_area_by_three_sides

# Bad code with code smells
def calc(x, y, z):
    # Magic numbers
    result = calculate_area_by_base_height(10, 5)

    # No error handling - potential crash
    data = None
    result2 = calculate_area_by_three_sides(data, 4, 5)
    
    # Magic numbers and hardcoded values
    # Poor variable naming and duplicate code
    for i in range(5):
        t = calculate_area_by_base_height(i, i)
        t2 = calculate_area_by_base_height(i, i)
        t3 = calculate_area_by_base_height(i, i)
    c = 4/0



    j= 2/0
    # Unnecessary complexity
    return result if result != None else 0

calc(1, 2, 3)

