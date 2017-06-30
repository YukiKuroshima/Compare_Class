import pandas as pd
import numpy as np
import re
# df = pd.read_excel("Allan Hancock College.xlsx", skiprows=6, parse_cols="G, H").dropna()
df = pd.read_excel("/Users/yukikuroshima/Desktop/Comp/Allan\ Hancock\ College.xlsx", skiprows=6, parse_cols="B, E, G, H")
df.columns = ['SJSU_Class', 'SJSU_Unit', 'Class', 'Unit']
# df.set_index('SJSU_Class', inplace=True)
# df.replace('', np.NaN, inplace=True)
df.dropna(how='all', inplace=True)
# df = df[Class == NaN]
print(df)

# with open('Allan Hancock College.txt') as f:
#     textDf = f.readlines()

f = open('/Users/yukikuroshima/Desktop/Comp/Allan\ Hancock\ College.txt')
text = f.readlines()
f.close()

# f = open( "Allan Hancock College.txt", "r" )
# textDf = []
# for line in f:
#     textDf.append(line)
# textDf = pd.read_table('Allan Hancock College.txt')
# print(textDf)

#
# p = re.compile('^[A-Z]+ [0-9]+')
#
# for l in textDf.iterrows():
#     m = re.search(p, l)
#     print(m)
#     if m:
#         className.append(m.group(0))

temp = []

for l in text:
    # print(l)
    match = re.search('^([A-Z]+ [0-9]+[A-Z]?)', l)
    if match:
        sjsuClass = match.group(0)
    else:
        sjsuClass = np.NaN

    match = re.search('\((\d)\)\|', l)
    if match:
        sjsuUnit = match.group(1)
    else:
        sjsuUnit = np.NaN

    match = re.search('\|([A-Z]+ [0-9]+[A-Z]?)', l)
    if match:
        className = match.group(1)
    else:
        className = np.NaN

    match = re.search('\s+\((\d)\)$', l)
    if match:
        unit = match.group(1)
    else:
        unit = np.NaN

    temp.append([sjsuClass, sjsuUnit, className, unit])


columns = ['SJSU_Class', 'SJSU_Unit', 'Class', 'Unit']
sjsu_df = pd.DataFrame(temp, columns=columns).dropna(how='all')
print(sjsu_df)

# text = 'gfgfdAAA1234ZZZuijjk'
#
# m = re.search('AAA(.+?)ZZZ', text)
# if m:
#     found = m.group(1)
#     print(found)


# print(className)
