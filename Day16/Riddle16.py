with open('Day16/Packets.csv', 'r') as file:
            line = file.read().strip('\n')
            bit_packets = bin(int(line, 16))[2:]

class Packet():
    
    def __init__(self, bit_packet):
        self.subpacket = []
        index = 0
        self.Version = int(bit_packet[index:index+3], 2)
        index += 3
        self.Type = int(bit_packet[index:index+3], 2)
        index += 3
        
        if self.Type == 4:
            bit = bit_packet[index]
            while bit == '0':
                index += 1
                bit = bit_packet[index]
            while bit == '1':
                index += 1
                self.subpacket.append(bit_packet[index:index+4])
                index+= 4
                bit = bit_packet[index]
            index += 1
            self.subpacket.append(bit_packet[index:index+4])
            index+= 4
        
        else:
            self.Length_ID = (bit_packet[index] == '1')
            index += 1
            if self.Length_ID == True:
                number_of_subpacket = int(bit_packet[index:index+11],2)
                index += 11
                self.subpacket = Packet(bit_packet[index:])
            else:
                number_of_bits = int(bit_packet[index:index+15],2)
                index += 15
                self.subpacket = Packet(bit_packet[index:])
                
    def operator(self, bit_packet):
        self.subpacket = []
        index = 0
        self.Version = int(bit_packet[index:index+3], 2)
        index += 3
        self.Type = int(bit_packet[index:index+3], 2)
        index += 3

test = '110100101111111000101000'

def Define_First_Packet(bit_string):
    index = 0
    Version = int(bit_string[index:index+3], 2)
    index += 3
    Type = int(bit_string[index:index+3], 2)
    index += 3
    Length_ID = (bit_string[index] == '1')
    index += 1
    if Length_ID == True:
        number_of_subpacket = int(bit_string[index:index+11],2)
        index += 11
        subpacket = Packet(bit_string[index:])
    else:
        number_of_bits = int(bit_string[index:index+15],2)
        index += 15
        subpacket = Packet(bit_string[index:])
    return bit_string[index:index+]