# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:16:19 2024

@author: Admin
"""

s = ('Đại học Quốc gia, \nKhu phố 6, \nP. Linh Trung, \nQ. Thủ Đức, \nTp. HCM')
s = s.replace(',','')
s = s.replace('P. ','')
s = s.replace('Q. ','')
s = s.replace('Tp. ','')
print(s)