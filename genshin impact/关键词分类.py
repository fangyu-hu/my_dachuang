import pandas

keywords='角色，文化，京剧，音乐，故事'.split('，')
keyword_dict={}
for i in keywords:
    keyword_dict[i]=[]
dataframe=pandas.read_excel('8svl0sQXDLI_翻译后.xlsx')
columns=dataframe.columns
for i in dataframe.values:
    for keyword in keywords:
        if keyword in i[-1]:
            keyword_dict[keyword].append(i)
dataframe=pandas.read_excel('EiAhMr6IJTQ_翻译后.xlsx')
columns=dataframe.columns
for i in dataframe.values:
    for keyword in keywords:
        if keyword in i[-1]:
            keyword_dict[keyword].append(i)
dataframe=pandas.read_excel('FVEWnOrsKW0_翻译后.xlsx')
columns=dataframe.columns
for i in dataframe.values:
    for keyword in keywords:
        if keyword in i[-1]:
            keyword_dict[keyword].append(i)

for i in keyword_dict.items():
    alldata=i[1]
    filename=i[0]
    dataframe=pandas.DataFrame(data=alldata,columns=columns)
    dataframe.to_excel('{}.xlsx'.format(filename),index=False)