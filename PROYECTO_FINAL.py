from huffman import HuffmanCoding
import sys
import numpy as np
import sounddevice as sd
from scipy.io import wavfile
from rice_coder import rice_encoder, rice_decoder


print("-- COMPRESOR Y DESCOMPRESOR DE ARCHIVOS DE SONIDO Y TEXTO --")
op=int("¿QUE TIPO DE ARCHIVO VAS A USAR? 1)SONIDO (wav) 2)TEXTO")

#ARCHIVO DE SONIDO
if op ==1:
    # Read the audio file to encode
    filepath = input("¿CUAL ES TU ARCHIVO?") #Sound1.wav
    sample_rate, audio = wavfile.read(filepath)

    # Play original audio
    print('Playing original audio...!')
    sd.play(audio, sample_rate)


    op2=int("¿QUIERES 1-COMPRIMIR O 2-DESCOMPRIMIR?")

    if op2 == 1:
        # Encode the audio file and write as .exx2
        idx = filepath.find(".wav")
        encoded_file = filepath[:idx] + "_Enc.exx2"
        M = 4
        with open(encoded_file, 'wb') as codedfile:
            for i in range(len(audio)):
                e = rice_encoder(audio[i], M) + '\n'
                codedfile.write(e.encode())
        codedfile.close()

    
    if op2 == 2:
        # Decode the encoded audio file
        decoded_audio = []
        with open(encoded_file, 'rb') as codedfile:
            for i in codedfile:
                decoded_audio.append(rice_decoder(i.decode('utf8').strip(), M))
        codedfile.close()
        decoded_audio = np.array(decoded_audio, dtype='int16')
    

    # Play decoded audio
    print('Playing decoded audio...!')
    sd.play(decoded_audio, sample_rate)

    # Write decoded audio file in .wav format
    idx = encoded_file.find(".exx2")
    decoded_file = encoded_file[:idx] + "_Dec.wav"
    wavfile.write(decoded_file, sample_rate, decoded_audio)



#ARCHIVO DE TEXTO
if op == 2:
    op3 = int(input("¿QUIERES COMPRIMIR O DESCOPRIMIR? \n 1)COMPRIMIR \n 2)DESCOMPRIMIR ->>"))

    if op3 ==1:
        path=input("¿QUE ARCHIVO QUIERES COMPRIMIR?->> ")#"sample.txt"
        h = HuffmanCoding(path)
        output_path = h.compress()
        print("Compressed file path: " + output_path)
    
    
    if op3 == 2:    
        path=input("¿QUE ARCHIVO QUIERES DESCOMPRIMIR?->> ")#"sample.txt"
        h = HuffmanCoding(path)
        decom_path = h.decompress(output_path)
        print("Decompressed file path: " + decom_path)



