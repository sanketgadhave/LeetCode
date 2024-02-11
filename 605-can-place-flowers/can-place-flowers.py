class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n
        next_ele = -1
        for i in range(0, len(flowerbed)):
            if count > 0:
                if i == 0:
                    prev_ele = -1
                else:
                    prev_ele = flowerbed[i-1]
                if i == len(flowerbed) - 1:
                    next_ele = -1
                else:
                    next_ele = flowerbed[i+1]
                if (prev_ele == 0 or prev_ele == -1) and flowerbed[i] == 0 and (next_ele == 0 or next_ele == -1):
                    flowerbed[i] = 1
                    count -= 1
                
        if count == 0:
            return True
        else:
            return False