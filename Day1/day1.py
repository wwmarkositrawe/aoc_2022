from itertools import groupby


input_data = open("Day1\data.txt").read().rstrip().split("\n")

li = [list(group) for k, group in groupby(input_data, bool) if k]

def conv_to_int(x):
    if isinstance(x, list):
        return list(map(conv_to_int, x))
    else: return int(x)
    
li_int = conv_to_int(li)


def sumator(lst):
    li_int_summed_vals_in_nested_list = []
    for nested_list in lst:
        li_int_summed_vals_in_nested_list.append(sum(nested_list))
    return li_int_summed_vals_in_nested_list

summed_vals = sumator(li_int)

    
def max_val(lst):
    return max(lst)

result = max_val(summed_vals)


def main(): 
    print(result)
    
    
if __name__ == "__main__":    
    main()
    




