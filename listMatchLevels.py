"""
LIST : MATCH LEVELS
-
a dynamoPython script, visit the website for more details
https://github.com/Amoursol/dynamoPython
"""
__author__ = 'Kenzo Bird - birdkenzo@gmail.com'
__dynamoforum__ = 'Kennyb6'
__version__ = '1.0'

"""
Script to match structure of one list to another.
IN[0] must be completely flattened prior to this script.
Empty lists in either inputs may give unwanted results.
"""


def recCount(_lists, c):
    # Count all elements in the structure list (IN[1])
    for _list in _lists:
        if isinstance(_list, list):
            c = recCount(_list, c)
        else:
            c += 1
    return c


def recMatch(_list, _matches, _out, c):
    """
    Recreate the value list (IN[0]) according to the structure list (IN[1])
    _list = entire value list
    _matches = the current list level of the structure list
    _out = value list matching the structure list to be passed on
    c = count to be used as the current index of the value list
    """
    for _match in _matches:
        if isinstance(_match, list):  # if list, recurse another level deeper
            outTemp, c = recMatch(_list, _match, [], c)
            _out.append(outTemp)
        else:
            _out.append(_list[c])
            c += 1
    return _out, c


# Inputs:
mList = IN[0]  # List of values, flattened to single level
toMatch = IN[1]  # Original structured list
outList = []  # Need blank list to be appended, will be new value list
c = 0
mC = 0

# Checks that both lists are equal value to prevent invalid index errors
if len(mList) == recCount(toMatch, c):
    OUT = recMatch(mList, toMatch, outList, mC)[0]
else:
    in0Len = "IN[0] length = " + str(len(mList))
    in1Len = "IN[1] length = " + str(recCount(toMatch, c))
    OUT = ["List lengths do not match.", in0Len, in1Len]
