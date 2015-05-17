__author__ = 'burger'


class Solution:
    def fourSum_nnlogn(self, num, target):
        # 250 ms
        hashset = {}
        result = []
        num.sort()

        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                sum = num[i] + num[j]
                if target - sum in hashset:
                    for (a, b) in hashset[target - sum]:
                        if b < i and [num[a], num[b], num[i], num[j]] not in result:
                            result.append([num[a], num[b], num[i], num[j]])
                if sum in hashset:
                    hashset[sum].append((i, j))
                else:
                    hashset[sum] = [(i, j)]
        return result

    def fourSum_200ms(self, num, target):
        if len(num) < 4:
            return []
        lst = []
        num.sort()
        for left_out in range(len(num) - 3):
            if num[left_out] > target / 4.0:
                break
            if left_out > 0 and num[left_out] == num[left_out - 1]:
                continue
            target2 = target - num[left_out]
            for left_in in range(left_out + 1, len(num) - 2):
                if (num[left_in] > target2 / 3.0):
                    break
                if left_in > left_out + 1 and num[left_in] == num[left_in - 1]:
                    continue
                target3 = target2 - num[left_in]

                right_in = left_in + 1
                right_out = len(num) - 1
                if num[right_in] > target3 / 2.0:
                    continue
                if num[right_out] < target3 / 2.0:
                    continue
                while right_in < right_out:
                    sum = num[right_out] + num[right_in]
                    if right_in > left_in + 1 and num[right_in] == num[right_in - 1]:
                        right_in += 1
                        continue
                    if right_out < len(num) - 1 and num[right_out] == num[right_out + 1]:
                        right_out -= 1
                        continue
                    if sum == target3:
                        lst.append([num[left_out], num[left_in], num[right_in], num[right_out]])
                        right_in += 1
                        right_out -= 1
                    elif sum > target3:
                        right_out -= 1
                    else:
                        right_in += 1
        return lst

    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum_1000ms(self, num, target):  ##1000ms
        if len(num) < 4:
            return []
        lst = set()
        num.sort()

        left_right = [(x, y) for x in range(len(num) - 2) for y in range(x, len(num))]
        for left_out, right_out in left_right:
            if (num[left_out] > target // 4):
                break
            left_in = left_out + 1
            right_in = right_out - 1
            nt = target - num[left_out] - num[right_out]
            while (left_in < right_in):
                if num[left_in] + num[right_in] > nt:
                    right_in -= 1
                elif num[left_in] + num[right_in] < nt:
                    left_in += 1
                else:
                    lst.add((num[left_out], num[left_in], num[right_in], num[right_out]))
                    left_in += 1
                    right_in -= 1

        return [list(x) for x in lst]


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum_nnlogn([1, 0, -1, 0, -2, 2], 0))
