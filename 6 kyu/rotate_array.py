def rotate(arr, n):
    dex = -(n % len(arr))
    return arr[dex:] + arr[:dex]

data = [1, 2, 3, 4, 5]
assert rotate(data, 1) == [5, 1, 2, 3, 4]
assert rotate(data, 2) == [4, 5, 1, 2, 3]
assert rotate(data, 3) == [3, 4, 5, 1, 2]
assert rotate(data, 4) == [2, 3, 4, 5, 1]
assert rotate(data, 5) == [1, 2, 3, 4, 5]
assert rotate(data, 0) == [1, 2, 3, 4, 5]
assert rotate(data, -1) == [2, 3, 4, 5, 1]
assert rotate(data, -2) == [3, 4, 5, 1, 2]
assert rotate(data, -3) == [4, 5, 1, 2, 3]
assert rotate(data, -4) == [5, 1, 2, 3, 4]
assert rotate(data, -5) == [1, 2, 3, 4, 5]
assert rotate(data, 7) == [4, 5, 1, 2, 3]
assert rotate(data, 11) == [5, 1, 2, 3, 4]
assert rotate(data, 12478) == [3, 4, 5, 1, 2]
assert rotate(['a', 'b', 'c'], 1) == ['c', 'a', 'b']
assert rotate([1.0, 2.0, 3.0], 1) == [3.0, 1.0, 2.0]
assert rotate([True, True, False], 1) == [False, True, True]
