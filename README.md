# cvvc-incision-dict-generator
# 本程式是幫朋友代管

自動從cvvc的presamp.ini產生UTAU Incision Plugin格式的拆音字典  
此程式產生的成品配布:[CVVC夏語遙v3拆音字點檔](https://bowlroll.net/file/245265)

配置要從旁邊的cvvc_dict_conf.ini調整:  
<pre>
[Dict_Setting]
Name=字典檔名稱
StaticHead=False
StaticLength=120
IgnoreMaxR=60
[Config]
presamp=輸入的presamp.ini位置
output=輸出檔案名稱
ignore_head=要忽略的音素前輟(逗號分隔)
ignore_foot=要忽略的音素後輟(逗號分隔)
ignore_element=要忽略的音素(逗號分隔)
ignore_vowel=要忽略的連續音前半部(逗號分隔)
ignore_consonant=要忽略的連續音後半部(逗號分隔)
</pre>
Dict_Setting的設定請參考UTAU Incision的範例檔案說明
