# save og_color(to check if tobecolored coordinate shares this color), total rows and cols
# save direction movements, and colored set
# take the src cordinates in dfs check if they are in range 
# # put the coordinated in stack and while stack:
# pop first if color == og color - color it
# visit its neighbors if they have og color and are not in colored add them to stack
# TC, SC = O(n) and O(n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        og_color = image[sr][sc]
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        color_this = []
        colored = set()
        def color_dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0:
                return image
            color_this.append((r,c))
            while color_this:
                curr_r, curr_c = color_this.pop()
                #print("Curr: ", curr_r, curr_c)
                image[curr_r][curr_c] = color
                for mv_r, mv_c in directions:
                    #print(mv_r, mv_c)                 
                    r = curr_r + mv_r
                    c = curr_c + mv_c
                    #print("New Co",r,c)
                    if r < rows and r >= 0 and c < cols and c >= 0:
                        if image[r][c] == og_color and (r,c) not in colored:
                            add = (r,c)
                            color_this.append(add)
                            colored.add(add)
            return image

        return color_dfs(sr, sc)
        