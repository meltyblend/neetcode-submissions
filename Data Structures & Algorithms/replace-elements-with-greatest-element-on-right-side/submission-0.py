class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        best = arr[-1]
        for i in range(len(arr) -1 , -1, -1):
            if arr[i] < best:
                arr[i] = best
            if arr[i] > best:
                best = arr[i]
        arr.append(-1)
        arr.remove(arr[0])


        return arr
