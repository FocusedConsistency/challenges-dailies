def decode_qr(qr_code):
    code = [[0 for _ in range(len(qr_code[0]))] for _ in range(len(qr_code))]
    for i in range(len(code)):
        for j in range(len(code[0])):
            code[i][j] = int(qr_code[i][j])

    rotated = [row[:] for row in code]
    rotations = 0

    for line in rotated:
        print(line)
    print("INITIAL")

    while not (int(code[0][0]) and int(code[0][1]) and int(code[0][-2]) and int(code[0][-1]) and int(code[1][0]) and int(code[1][1]) and int(code[1][-2]) and int(code[1][-1]) and int(code[-2][0]) and int(code[-2][1]) and int(code[-1][0]) and int(code[-1][1])) and rotations < 4:
        for i in range(len(code)):
            for j in range(len(code[0])):
                rotated[j][-1-i] = int(code[i][j])
                print(rotated[j])
            print("---")
        code = [row[:] for row in rotated]
        rotations += 1
        print("Rotation finished--------------")
    print(rotations)

    result = []
    skipped = [(0,0), (0,1), (0,4), (0,5), (1,0), (1,1), (1,4), (1,5), (4,0), (4,1), (5,0), (5,1)]
    for i in range(len(code)):
        for j in range(len(code[0])):
            if not (i,j) in skipped:
                result.append(str(rotated[i][j]))
    print(''.join(result))
    return ''.join(result)

decode_qr([
    "011011", 
    "101011", 
    "101000", 
    "100010", 
    "110011", 
    "111011"])
# 010001000100010101010110
