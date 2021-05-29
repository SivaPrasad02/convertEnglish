class convert:
    """
    Create a reusable library and a REST API based service that can convert a
    paragraph of spoken english to written english. For example, "two dollars" should
    be converted to $2. Abbreviations spoken as "H T M L" or "Triple A" should be
    written as "HTML" and "AAA" respectively. Note that we are not asking you to
    convert audio to text; just convert a raw transcript from spoken English to
    written English.
    """
    def __init__(self):
        self.help_keys = {
                            'one': 1,
                            'two': 2,
                            'three': 3,
                            'four': 4,
                            'five': 5,
                            'six': 6,
                            'seven': 7,
                            'eight': 8,
                            'nine': 9,
                            'zero' : 0,
                            'double' : 2,
                            'triple' : 3
                        }
        self.number = ''

    def convert_(self,Input):
        '''Input : Spoken english word
           output : written english word'''
        if len(Input.split(' ')) == 2:
            key, repeat = Input.split(' ')[0].lower(), Input.split(' ')[1]
            if key in self.help_keys.keys():
                number = self.help_keys[key]
            second = ['$'+str(number) if repeat.lower()=='dollor' or repeat.lower()=='dollors' else repeat*number]
            return second[0]
        else:
            result = Input.split(' ')
            return ''.join(result)
        


