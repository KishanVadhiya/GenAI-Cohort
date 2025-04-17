import tiktoken 

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Size of vocabulory : ",encoder.n_vocab)

text="Hasta la vista"

encoded= encoder.encode(text)

print("Encoded tokens : ",encoded)

decodedToken= [101235, 557, 22932]

decoded=encoder.decode(decodedToken)

print("Tokens decoded : ",decoded)