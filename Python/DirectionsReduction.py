def dir_reduc(arr):
    directions_binding = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]

    for i in range(len(arr) - 1):
        if set(arr[i:i+2]) in directions_binding:
            del (arr[i:i+2])
            return dir_reduc(arr)
    return arr
