class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid_row = (t + b) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                break
            if matrix[mid_row][0] > target:
                b = mid_row - 1
            else:
                t = mid_row + 1
        
        if t > b:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid_row][mid] == target:
                return True
            if matrix[mid_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            