def get_longest_palindrome(origin: str) -> str:
    longest_palindrome = ""

    for i in range(len(origin)):
        for j in range(i + 1, len(origin) + 1):
            substring = origin[i:j]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome
# We check results
input_str1 = "0123219"
input_str2 = "1012210"
result1 = get_longest_palindrome(input_str1)
result2 = get_longest_palindrome(input_str2)
print("The longest palindrom for '0123219':", result1)
print("THe longest palindrom for  '1012210':", result2)


