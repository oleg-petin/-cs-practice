def count_by_extension(paths):
    res = {}
    for path in paths:
        filename = path.split('/')[-1]
        if '.' in filename and not filename.startswith('.'):
            ext= filename.rsplit('.', 1)[-1].lower()
        else:
            ext= ''
        if ext in res:
            res[ext]+=1
        else:
            res[ext] =1
    return res


def deepest_path(paths):
    if len(paths) ==0:
        return ''
    best =paths[0]  
    for i in paths:
        depth = i.count('/')        
        bdepth  = best.count('/')   
        if depth > bdepth:
            best = i
        elif depth == bdepth and i < best:
            best =i
    return best

def human_size(size_in_bytes):
    units= ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    s = size_in_bytes
    u =0
    while s >=1024 and u < len(units) - 1:
        s = s / 1024
        u  +=1
    if u  == 0:
        return f'{s} {units[u]}'
    else:
        return f'{s:.1f} {units[u]}'