"""
This transform any list object with N dimensions in a flat list
ex: [1,[2,[3]], 4] >>> [1,2,3,4]
obj: list
"""
flatter = (
    lambda obj: [element for item in obj for element in flatter(item)]
    if isinstance(obj, list)
    else [obj]
)
