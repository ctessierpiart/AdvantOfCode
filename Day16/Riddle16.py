with open('Day16/Packets.csv', 'r') as file:
            line = file.read().strip('\n')
            bit_packets = bin(int(line, 16))[2:]

class Packet():
    def __init__(self, bit_packet):
        self.subpackets = []
        self.Version = 0
        self.Type = 0
        ##Literal value
        self.Value = 0
        ##Operator
        self.Length_ID = 0
        self.Length = 0
        self.Packet_decode(bit_packet)
        
    def Packet_decode(self, bit_packet):
        index = 0
        self.Version = int(bit_packet[index:index+3], 2)
        index += 3
        self.Type = int(bit_packet[index:index+3], 2)
        index += 3
        
        if self.Type == 4:
            bit = bit_packet[index]
            index += 1
            stringValue = ''
            while bit == '1':
                stringValue = ''.join([stringValue, bit_packet[index:index+4]])
                index+= 4
                bit = bit_packet[index]
                index += 1
            stringValue = ''.join([stringValue, bit_packet[index:index+4]])
            index += 4
            self.Value += int(stringValue, 2)
            
        
        else:
            self.Length_ID = (bit_packet[index] == '1')
            index += 1
            if self.Length_ID == True: ##Number of subpackets
                TotalSubpacketNumber = int(bit_packet[index:index+11],2)
                index += 11
                SubpacketNumber = 0
                LeftoversBit = bit_packet[index:]
                while SubpacketNumber != TotalSubpacketNumber:
                    SubpacketNumber += 1
                    LeftoversBit, Packetlenght = Packet(LeftoversBit)
                    self.Length += Packetlenght
                    
            else:                      ##Bits of subpackets
                self.Length = int(bit_packet[index:index+15],2)
                index += 15
                TotalLength = 0
                LeftoversBit = bit_packet[index:]
                while TotalLength != self.Length:
                    LeftoversBit, Packetlenght = Packet(LeftoversBit)
                
        return bit_packet[index:], self.Length
                

test = '110100101111111000101000'
test2 = '00111000000000000110111101000101001010010001001000000000'

test_packet = Packet(test)
test_packet2 = Packet(test2)

print(test_packet.Value)