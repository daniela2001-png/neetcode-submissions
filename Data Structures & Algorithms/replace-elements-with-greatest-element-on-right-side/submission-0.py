class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        lenght = len(arr)
        maxi = 0
        while i < lenght - 1:
            maxi = max(arr[i+1:])
            if arr[i] < maxi:
                arr[i] = maxi
            if arr[i] > maxi:
                arr[i] = maxi
            i += 1
        arr[i] = -1
        return arr