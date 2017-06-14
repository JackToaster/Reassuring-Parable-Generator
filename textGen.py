
import time
from config import config



def fixFormat(input_string):
    return input_string

#evaluate and replace a string
def evaluatePhrase(inputString, config):
    if inputString.find('{') == -1:
        return inputString
    else:
        index1 = inputString.find('{')
        index2 = inputString.find('}')
        key = inputString[index1 + 1:index2]
        phrase = config.get_phrase(key)
        inputString = inputString[:index1] + phrase + inputString[index2 + 1:]
        inputString = fixFormat(inputString)
        return evaluatePhrase(inputString, config)

#generate a phrase
def gen_phrase(config):
    output_string = config.get_phrase('starter')
    return evaluatePhrase(output_string, config)

filename = raw_input("Enter config filename to use for text generation:")
loaded_config = config(filename)
number_of_outputs = int(raw_input('Enter number of strings to generate:'))
current_time = time.time()
for i in range(0,number_of_outputs):
    print(gen_phrase(loaded_config))

time_dif = time.time() - current_time
print('Generated ' + str(number_of_outputs) + ' strings in ' + str(time_dif) + " seconds.")
