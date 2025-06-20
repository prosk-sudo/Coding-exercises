if __name__ == '__main__':
    lst = []
    N = int(input())
    for _ in range(N):
        command, *nums = input().split()
        match command:
            case 'insert':
                lst.insert(int(nums[0]), int(nums[1]))
            case 'print':
                print(lst)
            case 'remove':
                lst.remove(int(nums[0]))
            case 'append':
                lst.append(int(nums[0]))
            case 'sort':
                lst.sort()
            case 'pop':
                lst.pop()
            case 'reverse':
                lst.reverse()
            case _:
                print(":P")
