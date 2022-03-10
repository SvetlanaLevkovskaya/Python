""""1,2,3"      =>  "2"
"1,2,3,4"    =>  "2 3"
"1,2,3,4,5"  =>  "2 3 4"

""     =>  NULL
"1"    =>  NULL
"1,2"  =>  NULL"""


def array(string):
    s = ' '.join(string.split(',')[1:-1])
    return s if s else None


print(array('1,2,3'))
print(array(''))
print(array('1'))
print(array('1,2'))


def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None


print(array('1,2,3'))
print(array(''))
print(array('1'))
print(array('1,2'))
