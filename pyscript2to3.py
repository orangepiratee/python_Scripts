import sys,os

def load_script(path):
    print_info('loading file {}'.format(path))
    with open(path,'r',encoding='utf8') as file:
        lines =  file.readlines()
        return lines
    pass

def modify_print(lines):
    for line in lines:
        index = lines.index(line)
        line = line.strip('\n')
        #print_info('{} {}'.format(index,line))
        if 'print' in line.strip('\n') and not line.strip(' ').startswith('#'):
            newline = '{}({})\n'.format(line,lines[index+1].strip(' ').strip('\n'))
            #print_good('{} {}'.format(index,newline))
            lines[index] = newline
            del lines[index+1]
    return lines

def getnewpath(path):
    fname = path.rsplit('.',1)[0]
    print(fname)
    fname = '{}{}.py'.format(fname,'_py3')
    print(fname)
    return fname

def write2file(lines,newpath):
    f = open(newpath,'w+',encoding='utf8')
    for line in lines:
        f.write(line)
    f.close()
    print_good('saved.')
    return 1

def modify_modules(lines):
    for line in lines:
        if 'print' not in line:
            modules = line.replace('urllib2','urllib.request')
            modules = modules.replace('httplib','http.client')
            newline = modules
            lines[lines.index(line)] = newline
    return lines

def main(path):
    lines = load_script(path)
    lines_print3 = modify_print(lines)
    lines_import3 = modify_modules(lines_print3)
    result = lines_import3
    newpath = getnewpath(path)
    write2file(result,newpath)


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)

def print_info(txt):
    print('[i]{}'.format(txt))

def print_good(txt):
    print('[+]{}'.format(txt))