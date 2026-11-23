class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []

        top = 0
        bottom = m - 1
        left = 0 
        right = n - 1

        while top<=bottom and left<=right:
            res.extend(matrix[top][left:right+1])
            top+=1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top<=bottom:
                res.extend(reversed(matrix[bottom][left:right+1]))
                bottom -=1
            
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left +=1
        return res
