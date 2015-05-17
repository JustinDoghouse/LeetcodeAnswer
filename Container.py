__author__ = 'burger'


class Container:
    # @param height, an integer[]
    # @return an integer

    def maxArea(self, height):
        return self.xArea(height)

    def axArea(self, height, lo, hi):  # my own way which is exceed memory
        if (height[lo] > height[hi]):
            return self.axArea(height, hi, lo)
        lgh = hi - lo
        sgn = int(lgh / abs(lgh))
        lgh *= sgn
        area = lgh * height[lo]
        for i in range(1, lgh - 1):
            crt = lgh * height[lo] / (lgh - i)
            if ( crt < height[hi]):
                if (height[lo + i * sgn] > crt):
                    return self.axArea(height, lo + i * sgn, hi)
            elif (height[lo + i * sgn] > height[hi]):
                return max(self.axArea(height, hi, lo + i * sgn), area)
        return area

    def xArea(selfself, height):
        lo = 0
        hi = len(height) - 1
        maxarea = 0
        while (hi > lo):
            maxarea = max(maxarea, (hi - lo) * min(height[lo], height[hi]))
            if (height[lo] <= height[hi]):
                lo += 1
            else:
                hi -= 1
        return maxarea


if __name__ == '__main__':
    height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    h2 = [9, 6, 14, 11, 2, 2, 4, 9, 3, 8]
    s = Container()
    print(s.maxArea(h2))