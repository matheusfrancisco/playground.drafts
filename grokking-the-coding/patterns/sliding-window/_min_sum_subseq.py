
def min_window(str1, str2):
    size_str1, size_str2 = len(str1), len(str2)
    length = float('inf')
    index_s1, index_s2 = 0, 0
    min_subsequence = ""

    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1
            if index_s2 == size_str2:
                start, end = index_s1, index_s1+1
                index_s2 -= 1
                while index_s2 >= 0:
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    start -= 1
                start += 1
                # by start and end pointers is less than current min length
                if end - start < length:
                    length = end - start
                    min_subsequence = str1[start:end]

                index_s1 = start
                index_s2 = 0

        index_s1 += 1

    return min_subsequence


min_window("abcdebdde", "bde")
