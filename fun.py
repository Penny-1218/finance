#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:35:33 2024

@author: penny
"""

import pandas as pd
import numpy as np

data=pd.read_excel("/Users/penny/Desktop/finance/数据字典.xlsx",sheet_name="库表关系")
data_table=pd.read_excel("/Users/penny/Desktop/finance/数据字典.xlsx",sheet_name="表字段信息").rename(columns={"table_name":"表英文"})

data_final=pd.merge(data,data_table,how='inner',on='表英文')[['库名中文','表中文', '表描述', 'column_name',
       'column_description', '注释']]

def get_all_table_names():
    return list(data['表中文'].unique())

def get_table_schema(x):
    return data_final[data_final['表中文']==x]


    
    