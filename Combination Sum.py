__author__ = 'burger'


def find(candidates, start, target):
    # if start < 0:
    #   return None
    if candidates[start] > target:
        return None
        #find(candidates,start - 1, target)
    if candidates[start] == target:
        return [[target]]
    else:
        result = []
        for i in range(start, -1, -1):
            x = find(candidates, i, target - candidates[i])
            while not x:
                x = find(candidates, i, target - candidates[i])
            if x != None:
                for y in x:
                    y.append(candidates[i])
                    result.append(y)
                    #result.append([y.append(candidates[i]) for y in x])
            else:
                continue
        return result


def recurse(candidates, rsary, tmp, start, target):
    if target == 0:
        rsary.append(tmp)
        return
    for i in range(start, len(candidates)):
        ntg = target - candidates[i]
        if ntg < 0:
            break
        else:
            ntmp = tmp[:]
            ntmp.append(candidates[i])
            recurse(candidates, rsary, ntmp, i, ntg)


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        recurse(candidates, result, [], 0, target)
        return result
        # return find(candidates,len(candidates) - 1, target)


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))

