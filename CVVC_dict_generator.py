import re
#讀取配置設定
with open('cvvc_dict_conf.ini') as conf_file:
    config = {}
    for line in conf_file.readlines():
        if line[0] != '[':
            line = line.replace('\n', '')
            index = line.find('=')
            config.setdefault(line[:index], line[index+1:])
    
with open(config['presamp']) as presamp_file:
    tag = ''
    data_list = []
    tmp_dict = {}
    #tmp_dict{cv:[vc, cv, vc]...}
    #忽略的前輟與後輟
    #移除reg特殊字元
    ignore_head = r'^[%s]' % ''.join([re.sub(r'([\^\$\(\*\+\?\.\[\\\{\|])', r'\\\1', s) for s in config['ignore_head'].split(',')])
    ignore_foot = r'[%s]$' % ''.join([re.sub(r'([\^\$\(\*\+\?\.\[\\\{\|])', r'\\\1', s) for s in config['ignore_foot'].split(',')])
    #讀取發音
    for line in presamp_file.readlines():
        if line.find('[VOWEL]') != -1:
            #標示所在tag
            tag = 'VOWEL'
        elif line.find('[CONSONANT]') != -1:
            #標示所在tag
            tag = 'CONSONANT'
        elif tag == 'VOWEL' and line != '':
            #將vowel發音加入tmp_dict
            tmp_list = re.split(r'[=,]', line)
            for v in tmp_list[2:-1]:
                #如果符合ignore_head或ignore_foot就跳過
                if re.search(ignore_head, v) or re.search(ignore_foot, v):
                    #print('ignore v:%s' % v)
                    continue
                #填入tmp_dict
                tmp_dict.setdefault(v, [None, v, tmp_list[0]])
        elif tag == 'CONSONANT' and line != '':
            #將consonant發音加入tmp_dict
            tmp_list = re.split(r'[=,]', line)
            for c in tmp_list[1:-1]:
                #如果符合ignore_head或ignore_foot就跳過
                if re.search(ignore_head, c) or re.search(ignore_foot, c):
                    #print('ignore c:%s' % c)
                    continue
                #前方vc部分
                if tmp_dict.get(c):
                    tmp_dict[c][0] = tmp_list[0]
    data_list = [tmp_dict[x] for x in tmp_dict]

with open(config['output'], 'w', encoding='utf-16') as xia:
    xia.write('[Setting]\nName=%s\nStaticHead=%s\nStaticLength=%s\nIgnoreMaxR=%s\n' % (config['Name'], config['StaticHead'], config['StaticLength'], config['IgnoreMaxR']))
    xia.write('[TwoNote]\n')
    #發音交錯生成
    for word1 in data_list:
        for word2 in data_list:
            if word1[2] and word2[0]:
                #print('%s,%s=%s,%s %s' % (word1[1], word2[1], word1[1], word1[2], word2[0]))
                xia.write('%s,%s=%s,%s %s\n' % (word1[1], word2[1], word1[1], word1[2], word2[0]))
