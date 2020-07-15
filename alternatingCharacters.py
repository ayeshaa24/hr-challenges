def alternatingCharacters(s):
    ans = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans += 1
    return ans

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)
