def tribonacci(signature, n):
    if n > 3:
        for i in range(3, n):
            signature.append(sum(signature[-3:]))
    return signature[:n]
