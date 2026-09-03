nums = [10,20,"Test",None,3.2,[10,[40,[60,[90]]]]]


result_list = []

def is_numeric(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def total_sum(nums):
    for val in nums:
        if isinstance(val,list):
            total_sum(val)
        elif is_numeric(val):
            result_list.append(val)
    return set(result_list)

result_set = total_sum(nums)
print(result_set)

sum_val = 0
for v in result_set:
    sum_val += v

print(sum_val)


# Output
# {3.2, 40, 10, 20, 90, 60}
# 223.2