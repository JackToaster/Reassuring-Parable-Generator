import ConfigParser as parser
import random

class config:
    # load the configuration file
    def __init__(self, config_filename):
        self.load_config(config_filename)

    def load_config(self, config_filename):
        # create a config parser
        config = parser.ConfigParser()
        # read the file
        config.read(config_filename)
        # read the values
        dictionary = {}
        for section in config.sections():
            dictionary[section] = {}
            for option in config.options(section):
                dictionary[section][option] = config.get(section, option).splitlines()

        self.phrases = dictionary['phrases']

        if dictionary.has_key('defaults') & dictionary.has_key('subjects'):
            self.has_subjects = True
            self.defaults = dictionary['defaults']
            self.subjects = dictionary['subjects']
            print 'loaded defaults and subjects'
        else:
            self.has_subjects = False

    def create_subjecs(self):
        if self.has_subjects:
            first_subject = random.choice(self.subjects.keys())


    def get_phrase(self, key):
        try:
            string_to_return = random.choice(self.phrases[key])
            if string_to_return == 'none':
                return ''
            else:
                return string_to_return
        except:
            print('Could not find phrases with key ' + key)
            return ''
