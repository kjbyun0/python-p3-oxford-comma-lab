def oxford_comma(items):
    res_str = ', '.join(items)
    l_idx = res_str.find(', ')
    r_idx = res_str.rfind(', ')

    if l_idx != -1:
        if l_idx == r_idx:
            res_str = res_str[:l_idx] + ' and ' + res_str[l_idx+2:]
        else:
            res_str = res_str[:r_idx+2] + 'and ' + res_str[r_idx+2:]

    return res_str
