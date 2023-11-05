class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""]*n
        for i in range(1,n+1):
            if i%3==0:
                answer[i-1]+="Fizz"
            if i%5==0:
                answer[i-1]+="Buzz"
            if answer[i-1]=="":
                answer[i-1]=str(i)
        return answer
        