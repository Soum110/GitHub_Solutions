class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        s, out = [], []
        i = 0
        x = 1
        while(i < len(target)):
            s.append(x)
            out.append("Push")
            if x == target[i]:
                i += 1
            else:
                s.pop()
                out.append("Pop")
            x += 1
        return out
            
