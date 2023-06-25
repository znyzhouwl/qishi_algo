def make_largest_special(s: str) -> str:

    count, i = 0, 0
    res = []
    for j, char in enumerate(s):

        if char == "1":
            count += 1
        else:
            count -= 1
        if count == 0:
            res.append("1" + make_largest_special(s[i+1:j]) + "0")
            i = j + 1

    return "".join(sorted(res, reverse=True))


if __name__ == '__main__':
    print(make_largest_special("110100111000"))
