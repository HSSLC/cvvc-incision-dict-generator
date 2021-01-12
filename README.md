# cvvc-incision-dict-generator

自動從cvvc的presamp.ini產生UTAU Incision Plugin格式的拆音字典  

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
</pre>
Dict_Setting的設定請參考UTAU Incision的範例檔案說明
