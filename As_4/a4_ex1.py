# K11720457
# Aral Cimcim

# Write a function split_list(lst: list, num_sublists: int) -> list that splits a given list into (mostly) equally-sized sublists

def split_list(lst: list, num_sublists: int) -> list:
    result = []
    if num_sublists == 0:
        return lst  
    else:
        for i in range(num_sublists):
            sublist = lst[i::num_sublists]
            result.append(sublist)
    
    return result

