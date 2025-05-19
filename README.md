put dataset.jsonl in 'dataset'
(exist an example)


download java21 and add to $PATH

python jsonl2o.py
all jsonl in 'dataset' turns into 'PIE_Preprocessed/index/{src.cpp,tgt.cpp,original.jsonl,{src,tgt}_o[0,3].{o,output}}'


python o2c.py
'PIE_Preprocessed/index' turns to
'PIE_Preprocessed_g/index/{src,tgt}_O[0,3]_decompiled.c}'
