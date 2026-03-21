def decode_qr(qr_code):
    code = [[0 for _ in range(6)] for _ in range(6)]
    for i in range(len(code)):
        for j in range(len(code[0])):
            code[i][j] = int(qr_code[i][j])

    rotated = [row[:] for row in code]
    rotations = 0

    for line in rotated:
        print(line)
    print("Initial matrix")

    corners_to_skip = [(0,0), (0,1), (0,4), (0,5), (1,0), (1,1), (1,4), (1,5), (4,0), (4,1), (5,0), (5,1)]
    while not all(code[i][j] for i, j in corners_to_skip) and rotations < 4:
        for i in range(len(code)):
            for j in range(len(code[0])):
                rotated[j][-1-i] = int(code[i][j])
                print(rotated[j])
            print("------------------")
        code = [row[:] for row in rotated]
        rotations += 1
        print(f"Rotation {rotations} finished")
        print("------------------")

    result = []
    for i in range(len(code)):
        for j in range(len(code[0])):
            if not (i,j) in corners_to_skip:
                result.append(str(rotated[i][j]))

    return ''.join(result)

print(decode_qr([
    "011011", 
    "101011", 
    "101000", 
    "100010", 
    "110011", 
    "111011"]))
# 010001000100010101010110
