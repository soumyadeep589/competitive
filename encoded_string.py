def encode_string(s):
    temp = ''
    out = ''
    count = 1
    for i in range(0, len(s)):
        if i == 0:
            temp = s[i]
            out += s[i]
        else:
            if s[i] == temp:
                count += 1
            else:
                out += str(count) + s[i]
                count = 1
                temp = s[i]
    return out + str(count)

print(encode_string("wwwwaaadexxxxxxabb"))
