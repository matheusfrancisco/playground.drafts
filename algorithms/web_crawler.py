from typing import List

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split('/')[2]
        stack = [startUrl]
        visited = set()
        visited.add(startUrl)  # OR: visited = {startUrl}

        while stack:
            curr_url = stack.pop()
            for next_url in htmlParser.getUrls(curr_url):
                if hostname not in next_url:
                    continue
                if next_url in visited:
                    continue

                stack.append(next_url)
                visited.add(next_url)

        return visited
