class Solution:

    def encode(self, strs: List[str]) -> str:

        code = ""
        for i in range(len(strs)):
            code += strs[i]
            code += "."
        
        return code

    def decode(self, s: str) -> List[str]:
        res = s.split(".")
        res.pop(-1)
        return res

        
        

            



