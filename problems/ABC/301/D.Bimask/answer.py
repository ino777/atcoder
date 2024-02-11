S = input()
N = int(input())


def n_to_digit(n, d):
    digit = [0]*d
    i = 1
    if n == 0:
        return digit
    if n == 1:
        digit[-1] = 1
        return digit
    while True:
        q = n // 2
        r = n % 2
        digit[-i] = r
        if q == 1:
            digit[-(i+1)] = q
            break
        n = q
        i += 1
    return digit

def digit_to_n(digit):
    n = 0
    for i in range(len(digit)):
        n += 2**i*int(digit[-(i+1)])
    return n

def plus(digit1, digit2):
    result = []
    c = 0
    for i in range(len(digit1)):
        d1 = digit1[-(i+1)]
        d2 = digit2[-(i+1)]
        if type(d1) == str and '?' in d1:
            num_d1 = int(d1.split('+')[1]) if '+' in d1 else 0
            a = (num_d1 + int(d2) + c) % 2
            c = (num_d1 + int(d2) + c) // 2
            a = '?' + '+' + str(a) if a == 1 else '?'
        else:
            a = (int(d1) + int(d2) + c) % 2
            c = (int(d1) + int(d2) + c) // 2
        result = [a] + result[:]
    return result


def main():
    # Nがmin_sより小さければ解なし
    min_s = digit_to_n(S.replace('?', '0'))
    if N < min_s:
        print(-1)
        return

    # Nがmax_sより大きければSの最大が解
    max_s = digit_to_n(S.replace('?', '1'))
    if N >= max_s:
        print(max_s)
        return

    # それ以外の場合
    # N - S >= 0 となるSの最大のもの
    n_digit = n_to_digit(N, len(S))
    # Sをビット反転 0 -> 2, 1 -> 3にしてから、2 -> 1, 3 -> 0とする
    r_s = S.replace('0', '2').replace('1', '3').replace('2', '1').replace('3', '0')
    # +1
    r_p_s = plus(list(r_s), n_to_digit(1, len(S)))
    # r = N-S
    r = plus(r_p_s, n_digit)

    # 一番indexが小さい?+1を探す
    index = 0
    for i, v in enumerate(r):
        if v == '?+1':
            index = i
        if v == 0:
            break
    zero_index = []
    one_index = []
    for i, v in enumerate(r):
        if (v == '?' and i < index) or (v == '?+1' and i == index):
            zero_index.append(i)
        elif v == '?' or v == '?+1':
            one_index.append(i)
    # 元のSに対してindex以下の?は0に、indexより後の?は1にする
    new_S = list(S)
    for i in zero_index:
        new_S[i] = 0
    for i in one_index:
        new_S[i] = 1
    print(digit_to_n(new_S))

main()
