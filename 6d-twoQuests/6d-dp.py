def solution(a, b):
    
    dp = [[[0,0] for j in range(2003)] for i in range(2003)]

    dp[0][0][0] = 100000000
    dp[0][0][1] = 100000000

    dp[0][1][0] = a[0]
    dp[0][1][1] = 100000000
    dp[1][0][1] = b[0]
    dp[1][0][0] = 100000000

    for i in range(2,len(a)+1):
        dp[0][i][0] = dp[0][i-1][0] + abs(a[i-1]-a[i-2])
        dp[0][i][1] = 100000000

    for i in range(2,len(b)+1):
        dp[i][0][1] = dp[i-1][0][1] + abs(b[i-1]-b[i-2])
        dp[i][0][0] = 100000000

    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if(j == 1):
                dp[i][j][0] = min(dp[i][j-1][0]+abs(a[j-1]-0),dp[i][j-1][1]+abs(a[j-1]-b[i-1]))
            if(i == 1):
                dp[i][j][1] = min(dp[i-1][j][0]+abs(b[i-1]-a[j-1]),dp[i-1][j][1]+abs(b[i-1]-0))
            dp[i][j][0] = min(dp[i][j-1][0]+abs(a[j-1]-a[j-2]),dp[i][j-1][1]+abs(a[j-1]-b[i-1]))
            dp[i][j][1] = min(dp[i-1][j][0]+abs(b[i-1]-a[j-1]),dp[i-1][j][1]+abs(b[i-1]-b[i-2]))

    return min(dp[len(b)][len(a)][0],dp[len(b)][len(a)][1])

