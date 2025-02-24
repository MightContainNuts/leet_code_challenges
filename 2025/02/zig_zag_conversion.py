class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        counting_down = False

        for letter in s:
            print(f"current row {current_row} : {letter}")
            rows[current_row] += letter

            if current_row ==  numRows -1 or current_row == 0:
                counting_down = not counting_down

            current_row +=1 if counting_down else -1

        return "".join(rows)










if __name__ == '__main__':
    test_1 = "AB"
    row_num = 1
    exp_output ="PAHNAPLSIIGYIR"
    s = Solution()
    print(s.convert(test_1, row_num))
