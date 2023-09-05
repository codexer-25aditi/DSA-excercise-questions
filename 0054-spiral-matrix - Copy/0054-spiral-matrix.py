class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        round = 1
        while matrix and matrix[0]:
            if round == 1:
                res.extend(matrix[0])
                matrix[0:1] = []
                round += 1
            elif round == 2:
                for i in matrix:
                    res.append(i.pop())
                round += 1
            elif round == 3:
                res.extend(matrix[-1][::-1])
                matrix[-1:] = []
                round += 1
            elif round == 4 and len(matrix[0]):
                for i in matrix[::-1]:
                    res.append(i.pop(0))
                round = 1
        return res