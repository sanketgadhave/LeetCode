class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       
       for i in range(0, len(flowerbed)):
            if n == 0:
                return True
            else:
                if flowerbed[i] == 0 and len(flowerbed) == 1:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i] == 0 and i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and i == len(flowerbed)-1:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                if n == 0:
                    break
        
       if n == 0:
        return True
       else:
        return False