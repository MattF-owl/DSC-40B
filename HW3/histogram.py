def histogram(points, bins):

    result = []
    idx_c = 0
    idx_b = 0
    for bin in bins:

        bin_diff = bin[1] - bin[0]

        while idx_c < len(points) and points[idx_c] < bin[1]:
            idx_c += 1
        
        result.append((idx_c - idx_b) / len(points) / bin_diff)
        idx_b = idx_c
    return result


#test
# if __name__ == "__main__":
#     points = [1, 2,3,6,7,9,10,11]
#     bins = [(0, 4), (4,8), (8,12)]
#     print(histogram(points, bins))