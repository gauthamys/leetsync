class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        initial = [[1]]
        if numRows == 1:
            return initial
        
        for i in range(1, numRows):
            j = 0
            top = initial[-1]
            to_push = []
            while j < len(top):
                left = 0 if j - 1 < 0 else top[j - 1]
                to_push.append(left + top[j])
                j += 1

            to_push.append(1)
            initial.append(to_push)

        return initial