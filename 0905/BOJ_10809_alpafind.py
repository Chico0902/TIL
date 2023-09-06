S = input()

#알파벳 만드는법
alpa_list = []
for i in range(97, 122+1): #{ord 는 문자를 아스키코드로 바까줌/ ord('a') = 97, odr('z')=122}
#chr() = 아스키코드를 문자로 바꿔줌
    alpa_list.append(chr(i))
# print(alpa_list)
#
# alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in alpa_list:
    print(S.find(i), end=' ')