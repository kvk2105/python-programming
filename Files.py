input_file = './sampleFile.txt'

# Explicit try-catch for file handling
try:
    file = open(input_file, 'r')
    content = file.read()
    print(content)
except Exception as error:
    print(error)
finally:
    print('closing the file')
    file.close()
    
# Using 'with', try-catch are implicitly taken care during file handling to close the file
with open(input_file, 'r') as file:
    print('Using \'with\'')
    print(file.read())