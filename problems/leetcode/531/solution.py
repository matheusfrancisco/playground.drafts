from typing import List

class Solution:
    #     def check(self, picture, x, y):
    #         n = len(picture)
    #         m = len(picture[0])
    #         cnt = 0
    #         for i in range(n):
    #             cnt += (picture[i][y] == "B")

    #         for j in range(m):
    #             if(j != y):
    #               cnt += (picture[x][j] == "B")

    #         return picture[x][y] == 'B' and cnt == 1;

    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        #       n = len(picture)
        #       m = len(picture[0])
        #       ans = 0
        #       for j in range(m):
        #           ans += self.check(picture, 0, j)
        #       for i in range(m):
        #           ans += self.check(picture, i, 0)

        #       for j in range(m):
        #           picture[0][j] = (1 if picture[0][j] == 'B' else 0)

        #       for i in range(n):
        #           picture[i][0] = (1 if picture[i][0] == 'B' else 0)

        #       for i in range(n):
        #           for j in range(m):
        #               if (picture[i][j] == 'B'):
        #                   picture[i][0] += 1
        #                   picture[0][j] += 1

        #       for i in range(n):
        #           for j in range(m):
        #               if (picture[i][j] == 'B'):
        #                   if picture[0][j] == '1' and picture[i][0] == '1':
        #                     ans += 1

        #       return ans

        m, n = len(picture[0]), len(picture)
        ans = 0
        for i in range(n):
            row_black = 0
            row_black_idx = 0
            for j in range(m):
                if picture[i][j] == 'B':
                    row_black += 1
                    row_black_idx = j
                    if row_black > 1:
                        break

            if row_black == 1:
                col_black = 0
                for k in range(n):
                    if picture[k][row_black_idx] == "B":
                        col_black += 1
                        if col_black > 1:
                            break
                if col_black == 1:
                    ans += 1
        return ans
