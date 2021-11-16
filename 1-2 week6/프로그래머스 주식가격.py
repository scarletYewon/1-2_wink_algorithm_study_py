def solution(prices):
    answer = [0]*len(prices)
    count = []
    
    for i, price in enumerate(prices):
        while count and price < prices[count[-1]]:
            j = count.pop()
            answer[j] = i - j
        count.append(i)
        
    while count:
        j = count.pop()
        answer[j] = len(prices) - j - 1
        
    return answer