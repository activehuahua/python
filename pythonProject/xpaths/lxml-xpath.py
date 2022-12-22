
# -*- coding: utf-8 -*-#

'''
# Name:         lxml-xpath
# Description:  
# Author:       alex
# Date:         2021/9/30
'''
from lxml import etree

str='''
<div class="pager-wrapper page-topic__pager bright">
<!----> 
<a class="active">1</a> 
<!----> 
<!----> 
<a class="">2</a>
<a class="page-next">下一页</a> <!----></div>
'''

html=etree.HTML(str)
result=html.xpath('//div[@class="pager-wrapper page-topic__pager bright"]/a/text()')
print(result)

page_number=int(result[len(result)-2])
print(page_number)