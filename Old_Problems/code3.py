
def generate_chakravyuha(size):
    battlefield = [[0] * size for _ in range(size)]
    total_power_points = 0
    power_point_locations = []

    unit_number = 1

    for level in range(size // 2 + 1):
        for i in range(level, size - level):
            battlefield[level][i] = unit_number
            if unit_number % 11 == 0:
                total_power_points += 1
                power_point_locations.append((level, i))
            unit_number += 1

        for i in range(level + 1, size - level):
            battlefield[i][size - level - 1] = unit_number
            if unit_number % 11 == 0:
                total_power_points += 1
                power_point_locations.append((i, size - level - 1))
            unit_number += 1

        for i in range(size - level - 2, level - 1, -1):
            battlefield[size - level - 1][i] = unit_number
            if unit_number % 11 == 0:
                total_power_points += 1
                power_point_locations.append((size - level - 1, i))
            unit_number += 1

        for i in range(size - level - 2, level, -1):
            battlefield[i][level] = unit_number
            if unit_number % 11 == 0:
                total_power_points += 1
                power_point_locations.append((i, level))
            unit_number += 1

    return battlefield, total_power_points, power_point_locations


def print_battlefield(battlefield):
    for row in battlefield:
        print('\t'.join(map(str, row)))


# Example Usage
chakravyuha_size = 10
battlefield_matrix, collected_power_points, power_point_positions = generate_chakravyuha(chakravyuha_size)

print_battlefield(battlefield_matrix)
print(f"Total Collected Power Points : {collected_power_points}")
for position in power_point_positions:
    print(position)
