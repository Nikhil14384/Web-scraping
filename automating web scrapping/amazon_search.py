# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:30:42 2021

@author: Nikhil Reddy
"""

from autoscraper import AutoScraper


Scrap= AutoScraper()


amzn_url="https://www.amazon.in/s?k=iphones"

req_list_amzn=["₹58,400","New Apple iPhone 11 (128GB) - Black"]
Scrap_amzn=Scrap.build(amzn_url,req_list_amzn)
res_amzn=Scrap.get_result_similar(amzn_url,grouped=True)

dyk=list(res_amzn.keys())
print(dyk)
Scrap.set_rule_aliases({dyk[len(dyk)-1]:'Title',dyk[0]:'Price'})
Scrap.keep_rules([dyk[len(dyk)-1],dyk[0]])
Scrap.save('amazon-search3')
