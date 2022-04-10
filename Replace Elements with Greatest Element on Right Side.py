class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lst = [-1]
        cur_max = arr[len(arr)-1]
        for i in range(len(arr)-2, -1, -1):
            lst.append(cur_max)
            if cur_max < arr[i]:
                cur_max = arr[i]    
        return lst[::-1]