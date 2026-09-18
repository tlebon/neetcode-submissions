class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "BLANK"
        string = ''
        for i, x in enumerate(strs):
            if i == 0:
                string = x
            else:
                string = string + "?/" + x
        return string

    def decode(self, s: str) -> List[str]:
        if s =='BLANK':
            return []
        return s.split('?/')
