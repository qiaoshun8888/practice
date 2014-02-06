def is_palindrome(s):
    for i in range(len(s) / 2):
        j = len(s) - 1 - i
        if not s[i] == s[j]:
            return False
    return True


def main():
    print is_palindrome('123212')


if __name__ == '__main__':
    main()
