

def humming_wight(n):    #counts number of ones in the binary number 5 --> 101 --> 2
    count_ones = 0
    while n > 0:
        b = n & 1
        count_ones += b
        n >>= 1
    return count_ones





def hamming_distance(nr1, nr2): #nr1, nr2 are binary numbers
    xor = nr1 ^ nr2
    distance = humming_wight(xor)
    return distance


# print(hamming_distance(0b101101, 0b100011), "tessst")

def smallest_distance(bin_number, list_of_binarys):
    number =  0

    smallest = hamming_distance(bin_number, list_of_binarys[0])
    for i in range(1, len(list_of_binarys)):
        distance = hamming_distance(bin_number, list_of_binarys[i])
        
        if distance < smallest and distance != 0:
            smallest = distance
            number = "{:015b}".format(list_of_binarys[i])
            
    return smallest, number

def find_word(number, list_of_binrys):
    dist, word = smallest_distance(number, list_of_binrys)


    return word



mots = [
    0b000000000000000,
    0b000010100110111,
    0b000101001101110, 
    0b000111101011001,
    0b001000111101011,
    0b001010011011100,
    0b001101110000101,
    0b001111010110010,
    0b010001111010110,
    0b010011011100001,
    0b010100110111000,
    0b010110010001111,
    0b011001000111101,
    0b011011100001010,
    0b011100001010011,
    0b011110101100100,
    0b100001010011011,
    0b100011110101100,
    0b100100011110101,
    0b100110111000010,
    0b101001101110000,
    0b101011001000111,
    0b101100100011110,
    0b101110000101001,
    0b110000101001101,
    0b110010001111010,
    0b110101100100011,
    0b110111000010100,
    0b111000010100110,
    0b111010110010001,
    0b111101011001000,
    0b111111111111111,
]

#partie 5


solution = find_word(0b000010100110111 ^ 0b10100110111, mots)

print(solution)


