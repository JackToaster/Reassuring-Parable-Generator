import random, ConfigParser as parser, time

#load the configuration file
def loadConfig(config_filename):
    #create a config parser
    config = parser.ConfigParser()
    #read the file
    config.read(config_filename)
    #read the values
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option).splitlines()

    return dictionary['phrases']

def fixFormat(input_string):
    return input_string

#evaluate and replace a string
def evaluatePhrase(inputString, phrases):
    if inputString.find('{') == -1:
        return inputString
    else:
        index1 = inputString.find('{')
        index2 = inputString.find('}')
        key = inputString[index1 + 1:index2]
        phrase = random.choice(phrases[key])
        if phrase == '[none]':
            phrase = ''
        inputString = inputString[:index1] + phrase + inputString[index2 + 1:]
        inputString = fixFormat(inputString)
        return evaluatePhrase(inputString, phrases)

#generate a phrase
def gen_phrase(phrases):
    output_string = random.choice(phrases['starter'])
    return evaluatePhrase(output_string, phrases)

filename = raw_input("Enter config filename to use for text generation:")
loaded_config = loadConfig(filename)
number_of_outputs = int(raw_input('Enter number of strings to generate:'))
current_time = time.time()
for i in range(0,number_of_outputs):
    print(gen_phrase(loaded_config))

time_dif = time.time() - current_time
print('Generated ' + str(number_of_outputs) + ' strings in ' + str(time_dif) + " seconds.")
