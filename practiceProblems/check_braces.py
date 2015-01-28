def check_braces(expressions):
    l = len(expressions)
    braces = {
        'curly': {
            "}": "cr",
            "{": "cl",
            "count": 0
            },
        'paren': {
            ")": "pr",
            "(": "pl",
            "count": 0
            },  
        'square': {
            "]": "cr",
            "[": "cl",
            "count": 0
            }
        }
    for i in range(l):
        q = len(expressions[i])
        braces['curly']['count'] = 0
        braces['paren']['count'] = 0
        braces['square']['count'] = 0
        for d in range(q):
            t = expressions[i][d]
            if t in braces['curly']:
                braces['curly']['count'] += 1
                continue
            elif t in braces['paren']:
                braces['paren']['count'] += 1
                continue
            elif t in braces['square']:
                braces['square']['count'] += 1
                continue
            else:
                continue
        
        if (braces['curly']['count'] % 2 == 0):
            if (braces['paren']['count'] % 2 == 0):
                if (braces['curly']['count'] % 2 == 0):
                    print 1
                    
        else:
            print 0
check_braces(["()", "[})"])