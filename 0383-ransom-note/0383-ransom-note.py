class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for c in magazine:
            if magazine_dict.get(c):
                magazine_dict[c]+=1
            else:
                magazine_dict[c]=1
        count=0
        for c in ransomNote:
            if not magazine_dict.get(c):
                break
            elif magazine_dict.get(c)==0:
                break
            else:
                magazine_dict[c]-=1
                count+=1
        return count==len(ransomNote)
