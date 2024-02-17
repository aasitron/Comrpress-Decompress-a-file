import zlib, base64
def compress(inputfile,oputputfile):
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data,'utf-8') #Converting String into bytes
    compressed_data = base64.b64encode(zlib.compress(data_bytes,9))  #Encoding the compressed data , 0-9(belongs to zlib) is the level of compression higher the number higher the compression
    decoded_data = compressed_data.decode('utf-8') # Converting bytes back to string
    compressed_file = open(oputputfile,'w')
    compressed_file.write(decoded_data)

compress('demo.txt','ot.txt')
    
def decompress(inputfile,oputputfile):
    file_content = open(inputfile, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data)) #First Decoding happens and then decompressing
    decoded_data = decompressed_data.decode('utf-8')
    file = open(oputputfile,'w')
    file.write(decoded_data)
    file.close()

decompress('ot.txt','dec1.txt')