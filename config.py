import configparser as parser
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
            print('Found section: ' + section)
            dictionary[section] = {}
            for option in config.options(section):
                dictionary[section][option] = config.get(section, option).splitlines()

        self.phrases = dictionary['phrases']

        if 'defaults' in dictionary and 'subjects' in dictionary:
            self.has_subjects = True
            self.defaults = dictionary['defaults']
            self.subjects = dictionary['subjects']

            for subject in self.subjects:
                self.subjects[subject] = self.subjects[subject][0].split(',')

            print('loaded defaults and subjects')

        else:
            self.has_subjects = False

    def create_subjects(self, number = 0):
        if number == 0:
            number = int(self.defaults['num_subjects'][0])


        if self.has_subjects:
            first_subject = random.choice(list(self.subjects))
            subjects = [first_subject]

            for i in range(1,number):
                subjects.append(self.get_adjacent_subject(subjects[i-1]))

            self.current_subjects = subjects
        else:
            pass

    def get_adjacent_subject(self, subject):
        node = self.subjects[subject]
        return random.choice(node)

    def get_subject(self):
        return random.choice(self.current_subjects)

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
