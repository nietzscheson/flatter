flatter = lambda obj: [element for item in obj for element in flatter(item)] if isinstance(obj, list) else [obj]
