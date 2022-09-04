

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K=5


"""
Brute force
time complexity: O(N*K)
N is the number of elements in the array


"""
def find_averages_of_sub_brute(k, arr):
    res = []
    for i in range(len(arr)-k+1):
        s = 0.0
        for j in range(i, i+k):
            s += arr[j]

        res.append(s/k)

    return res
    

def solution(k, arr):
    out = []
    win_sum, win_start = 0.0, 0
    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        if win_end  >= k - 1:
            out.append(win_sum/k)
            win_sum -= arr[win_start]
            win_start += 1
        
    return out  

    

assert [2.2, 2.8, 2.4, 3.6, 2.8] == find_averages_of_sub_brute(K, arr)
assert [2.2, 2.8, 2.4, 3.6, 2.8] == solution(K, arr)

