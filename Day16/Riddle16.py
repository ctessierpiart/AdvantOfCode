from math import prod


with open('Day16/Packets.csv', 'r') as file:
            line = file.read().strip('\n')
            bit_packets = bin(int(line, 16))[2:]

class Packet():
    def __init__(self, bit_packet):
        self.Leftovers = []
        self.Version = 0
        self.sumVersion = 0
        self.Type = 0
        ##Literal value
        self.Value = 0
        ##Operator
        self.Length_ID = 0
        self.Length = 0
        self.subpacketValues = []
        self.Packet_decode(bit_packet)
        
    def Packet_decode(self, bit_packet):
        index = 0
        self.Version = int(bit_packet[index:index+3], 2)
        self.sumVersion = self.Version
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
            self.Length = index
            self.Leftovers = bit_packet[index:]
        
        else:
            self.Length_ID = (bit_packet[index] == '1')
            index += 1
            if self.Length_ID == True: ##Number of subpackets
                TotalSubpacketNumber = int(bit_packet[index:index+11],2)
                index += 11
                self.Length = index
                SubpacketNumber = 0
                self.Leftovers = bit_packet[index:]
                while SubpacketNumber != TotalSubpacketNumber:
                    SubpacketNumber += 1
                    Subpacket = Packet(self.Leftovers)
                    self.subpacketValues.append(Subpacket.Value)
                    self.Length    += Subpacket.Length
                    self.Leftovers  = Subpacket.Leftovers
                    self.sumVersion += Subpacket.sumVersion
                    
            else:                      ##Bits of subpackets
                self.Length = index + 15 + int(bit_packet[index:index+15],2)
                SubpacketLength = int(bit_packet[index:index+15],2)
                index += 15
                TotalLength = 0
                self.Leftovers = bit_packet[index:]
                while TotalLength != SubpacketLength:
                    Subpacket = Packet(self.Leftovers)
                    TotalLength    += Subpacket.Length
                    self.Leftovers  = Subpacket.Leftovers
                    self.sumVersion += Subpacket.sumVersion
                    self.subpacketValues.append(Subpacket.Value)
                    
            match(self.Type):
                case(0):
                    self.Value = sum(self.subpacketValues)
                case(1):
                    self.Value = prod(self.subpacketValues)
                case(2):
                    self.Value = min(self.subpacketValues)
                case(3):
                    self.Value = max(self.subpacketValues)
                case(5):
                    self.Value = (self.subpacketValues[0] > self.subpacketValues[1])
                case(6):
                    self.Value = (self.subpacketValues[0] < self.subpacketValues[1])
                case(7):
                    self.Value = (self.subpacketValues[0] == self.subpacketValues[1])
                    
            a = 0

                

test = '110100101111111000101000'
test2 = '00111000000000000110111101000101001010010001001000000000'

test_packet = Packet(test)
test_packet2 = Packet(test2)

Realdeal = Packet(bit_packets)

print(Realdeal.sumVersion)
print(Realdeal.Value)