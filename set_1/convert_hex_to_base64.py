#TODO - There's got to be an easier way to do this....
import sys
hex = sys.argv[1]

def createBinaryStr(hex):
	bin_s = ""
	for i in range(int(len(hex)/2)):
		start = i*2
		end = start+2
		h = hex[start:end]
		b = bin(int(h,16))[2:].zfill(8)
		bin_s += b
	return bin_s

def padBinString(bin_s):
	return bin_s.ljust((len(bin_s) % 6), "0")

def splitToSixBits(padded_s):
	start = 0
	end = 6
	sixBits = int(len(padded_s)/6)
	sixBitArr = []
	for i in range(sixBits):
		sixBitArr.append(padded_s[start:end])
		tmp = end
		end = end + 6
		start = tmp
	return sixBitArr

def bitsArrToDecimal(arr):
	decimalArr = []
	for bits in arr:
		decimalArr.append(int(bits,2))
	return decimalArr

def createMapping():
	b64Map = []
	for i in range(26):
		letter = chr(65+i)
		b64Map.append(letter)

	for i in range(26):
		letter = chr(97+i)
		b64Map.append(letter)

	for i in range(10):
		b64Map.append(str(i))

	b64Map.append("+")
	b64Map.append("/")
	return b64Map

def convertToB64(arr, b64Map):
	b64Str = ""
	for dec in arr:
		l = b64Map[dec]
		b64Str += l
	return b64Str

binary = createBinaryStr(hex)
padded_str = padBinString(binary)
sixBitArr = splitToSixBits(padded_str)
decimalArr = bitsArrToDecimal(sixBitArr)
b64Map = createMapping()
b64 = convertToB64(decimalArr, b64Map)

print(b64)


