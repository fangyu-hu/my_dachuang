import time

from googletrans import Translator
import pandas
# 创建翻译器对象
translator = Translator()

filename='FVEWnOrsKW0.xlsx'
frame=pandas.read_excel(filename)
columns=frame.columns
alldata=[]
for i in frame.values:
    try:
        rowdata = list(i)
        # 要翻译的文本
        text_to_translate = rowdata[-1]

        # 指定源语言（如果不指定，默认会自动检测源语言）
        source_language = "en"  # 英语

        # 目标语言
        target_language = "zh-CN"  # 中文（简体）

        # 进行翻译
        translated_text = translator.translate(text_to_translate, src=source_language, dest=target_language)

        text = translated_text.text
        rowdata[-1] = text
        print(rowdata)
        alldata.append(rowdata)
        time.sleep(1)
    except:
        pass
dataframe=pandas.DataFrame(data=alldata,columns=columns)
dataframe.to_excel(filename.replace('.xlsx','_翻译后.xlsx'),index=False)