# 문제
# 문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

# 출력
# 첫째 줄에 S의 SHA-256 해시값을 출력한다.


# 문제 풀이 핵심 아이디어
# 1. hashlilb의 sha256 함수를 이용하면 구할 수 있다.
# 2. hashlib.sha256(문자열 바이트 객체).hexdigest() : 해시 결과 문자열

import hashlib

input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()

print(result)