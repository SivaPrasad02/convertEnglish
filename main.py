from written_english.convert import convert
import written_english

obj = convert()

if __name__ == '__main__':
    inp = input('Enter the Spoken English Text :  ')
    result = obj.convert_(inp)
    print("spoken english ' {} '  Conversion to written english ' {} '".format(inp, result))
