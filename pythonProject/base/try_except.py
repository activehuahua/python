class ShortInputException(Exception):
    def __init__(self,length,atlease):
        Exception.__init__(self)
        self.length=length
        self.atlease=atlease

try:
    text=input('Enter something---->')
    if len(text)<3:
        raise ShortInputException(len(text),3)

except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
except ShortInputException as ex:
    print('ShorInputException The length is', ex.length, ',the atlease is', ex.atlease )
else:
    print('You entered {0}'.format(text))