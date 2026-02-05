



from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # sr and sc is the coordinate system
        height = len(image) - 1
        witdth = len(image[0]) - 1
        # we make use of the call stack instead of a normal stack by making the function recursive

        def dfs(w: int, h: int, c: int) -> None:
            if 0 < w < witdth or 0 < h < height:
                directions = [(1 + w,h), (w - 1,h), (w,1 + h), (w,h-1)]
                for wi, he in directions:
                    if 0 <= wi <= witdth and 0 <= he <= height:
                        if image[he][wi] == c:
                            image[he][wi] = color
                            dfs(wi, he, c) # adds a recursive call
            

        dfs(sr, sc, image[sr][sc])
        return image
    

im = [[1,1,1],[1,1,0],[1,0,1]]
r = 1
c = 1
co = 2

inp = Solution()

print(inp.floodFill(im,r,c,co))

