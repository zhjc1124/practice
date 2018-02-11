result = []


def queen(status=(), cur=0):
    if cur == 8:
        result.append(status)
    else:
        for i in range(8):
            for index in range(len(status)):
                if abs(status[index]-i) in (0, abs(index-cur)):
                    break
            else:
                queen(status + (i,), cur + 1)


queen()
print(len(result))
