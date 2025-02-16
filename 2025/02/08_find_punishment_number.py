class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishment_nums = []

        for num in range(n + 1):
            squared_num = self.squared_num(num)
            if self.is_part_punishment_num(squared_num, num):
                punishment_nums.append(squared_num)
                print(f" {num} is a punishment number")

        total_punishment_num = sum(punishment_nums)
        print(f"Total of punishment nums: {total_punishment_num}")
        return total_punishment_num

    def squared_num(self, num) -> int:
        return num ** 2

    def is_part_punishment_num(self, squared_num, target):
        print(f"Checking if {squared_num} is a punishment number of {target}")
        return self.create_parts_and_check_sum(str(squared_num), target)

    def create_parts_and_check_sum(self, squared_num_str, target):
        def get_splits(start, parts):
            if start == len(squared_num_str):
                total_sum = sum(
                    int(part) for part in parts)
                print(f"Checking split: {parts}, Total sum: {total_sum}")
                if total_sum == target:
                    return True
                return False

            for i in range(start + 1, len(squared_num_str) + 1):
                if get_splits(i, parts + [squared_num_str[start:i]]):
                    return True
            return False

        return get_splits(0, [])



if __name__ == '__main__':
    n = 10
    exp_ans = 182

    s= Solution()
    s.punishmentNumber(n)
