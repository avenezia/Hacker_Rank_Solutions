test_cases = int(raw_input().strip())
processed_cases = 0

while processed_cases < test_cases:
    array_length = int(raw_input().strip())
    array = map(int, raw_input().strip().split(' '))
    assert len(array) == array_length
        
    index_exists = False
    index = 0
    left = []
    right = array[index + 1 :]
    left_sum = sum(left)
    right_sum = sum(right)
    while (index < array_length - 1 or len(array) == 1) and not index_exists:
        if left_sum == right_sum:
            index_exists = True
        else:
            value = array[index]
            left.append(value)
            left_sum += value
            right_sum -= array[index + 1]
        index += 1
    print "YES" if index_exists else "NO"
    processed_cases += 1
