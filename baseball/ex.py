arr='0101000001100101011100000110010101110010011011110010000001101001011100110010000001100001001000000110001101101111011011110110101101101001011001010010000001110011011101000110100101100011011010110010110000100000011001000110100101110000011100000110010101100100001000000110100101101110001000000110001101101111011011010111000001101111011101010110111001100100001000000110001101101000011011110110001101101111011011000110000101110100011001010010110000100000011011010110000101101110011101010110011001100001011000110111010001110101011100100110010101100100001000000110001001111001001000000011111100111111001111110011111100111111001000000100001101101111011011100110011001100101011000110111010001101001011011110110111001100101011100100111100100100000011010010110111000100000010100110110111101110101011101000110100000100000010010110110111101110010011001010110000100100000010100000110010101110000011001010111001001101111001000000100010001100001011110010010000001101001011100110010000001101000011001010110110001100100001000000110000101101110011011100111010101100001011011000110110001111001001000000110111101101110001000000100111001101111011101100110010101101101011000100110010101110010001000000011000100110001'

arr2=[0b010100, 0b000110, 0b010101, 0b110000, 0b011001, 0b010111, 0b001001, 0b101111, 0b001000, 0b000110, 0b100101, 0b110011, 0b001000, 0b000110, 0b000100, 0b100000, 0b011000, 0b110110, 0b111101, 0b101111, 0b011010, 0b110110, 0b100101, 0b100101, 0b001000, 0b000111, 0b001101, 0b110100, 0b011010, 0b010110, 0b001101, 0b101011, 0b001011, 0b000010, 0b000001, 0b100100, 0b011010, 0b010111, 0b000001, 0b110000, 0b011001, 0b010110, 0b010000, 0b100000, 0b011010, 0b010110, 0b111000, 0b100000, 0b011000, 0b110110, 0b111101, 0b101101, 0b011100, 0b000110, 0b111101, 0b110101, 0b011011, 0b100110, 0b010000, 0b100000, 0b011000, 0b110110, 0b100001, 0b101111, 0b011000, 0b110110, 0b111101, 0b101100, 0b011000, 0b010111, 0b010001, 0b100101, 0b001011, 0b000010, 0b000001, 0b101101, 0b011000, 0b010110, 0b111001, 0b110101, 0b011001, 0b100110, 0b000101, 0b100011, 0b011101, 0b000111, 0b010101, 0b110010, 0b011001, 0b010110, 0b010000, 0b100000, 0b011000, 0b100111, 0b100100, 0b100000, 0b001111, 0b110011, 0b111100, 0b111111, 0b001111, 0b110011, 0b111100, 0b100000, 0b010000, 0b110110, 0b111101, 0b101110, 0b011001, 0b100110, 0b010101, 0b100011, 0b011101, 0b000110, 0b100101, 0b101111, 0b011011, 0b100110, 0b010101, 0b110010, 0b011110, 0b010010, 0b000001, 0b101001, 0b011011, 0b100010, 0b000001, 0b010011, 0b011011, 0b110111, 0b010101, 0b110100, 0b011010, 0b000010, 0b000001, 0b001011, 0b011011, 0b110111, 0b001001, 0b100101, 0b011000, 0b010000, 0b101001, 0b010000, 0b011001, 0b010111, 0b000001, 0b100101, 0b011100, 0b100110, 0b111100, 0b100000, 0b010001, 0b000110, 0b000101, 0b111001, 0b001000, 0b000110, 0b100101, 0b110011, 0b001000, 0b000110, 0b100001, 0b100101, 0b011011, 0b000110, 0b010000, 0b100000, 0b011000, 0b010110, 0b111001, 0b101110, 0b011101, 0b010110, 0b000101, 0b101100, 0b011011, 0b000111, 0b100100, 0b100000, 0b011011, 0b110110, 0b111000, 0b100000, 0b010011, 0b100110, 0b111101, 0b110110, 0b011001, 0b010110, 0b110101, 0b100010, 0b011001, 0b010111, 0b001000, 0b100000, 0b001100, 0b010011, 0b000100, 0b000000]
txt_out = '7/OkZQIau/jou/R1by9acyjjutd0cUdlWshecQhkZUn1cUH1by9g4/9qNAn1byGaby9pbQSjWshgbUmqZAF+JtOBZUn1b8e1YoMPYoM1ny95ZAO+J/jaNAOB2vhrNLhVNDO0cshWNDIjbnrnZQhj4AM1S/Fmu/jou/GjN/n1bUm5JUFpNte1NyH1VA9yZUqLZQu13VR='
table=[''for i in range(0, 64)]
print(len(txt_out))
for i in range(0, len(txt_out)):
    table[arr2[i]] = txt_out[i]
print(table)
flag_out = 'S/jeutjaJvhlNA9Du/GaJBhLbQdjd+n1Jy9BcD3='
flag_in = [0 for i in range(0, len(flag_out))]
for j in range(0, len(flag_out)):
    for i in range(0, 64):
        if(flag_out[j] == table[i]):
            flag_in[j] = i

print(flag_in)
