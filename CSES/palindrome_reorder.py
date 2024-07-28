def main():
    user_input = input()
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    occurence = [0] * 26
    odd = []
    answer = [''] * len(user_input)

    for char in user_input:
        occurence[ord(char) - ord('A')] += 1

    for i, count in enumerate(occurence):
        if count % 2 == 1:
            odd.append(i)

    if len(odd) > 1:
        print("NO SOLUTION")
        return

    left = 0
    right = len(user_input) - 1
    
    for i, count in enumerate(occurence):
        while count > 1:
            answer[left] = chars[i]
            answer[right] = chars[i]
            left += 1
            right -= 1
            count -= 2
    
    if len(odd) == 1:
        answer[len(user_input) // 2] = chars[odd[0]]
    
    print("".join(answer))

if __name__ == "__main__":
    main()
