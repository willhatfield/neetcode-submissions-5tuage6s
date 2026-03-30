class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First binary search: find the correct row
        top, bottom = 0, len(matrix) - 1
        row = 0

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                row = mid_row
                break
        else:
            # Target is outside the range of any row
            return False
            
        # Second binary search: find target in the identified row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            num = matrix[row][mid]

            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False