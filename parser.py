from pprint import pprint
from lxml import html
import re
import time

def parser(text):
    tree = html.fromstring(text)
    result=[]

    for outlets in tree.xpath('//div[@class="store-info-box"]'):
        address = outlets.xpath('string(.//li[contains(@class,"outlet-address")])').strip()
        pincode=re.search(r'\b(\d{6})\b', address)
        landmark=outlets.xpath('string(.//li[not(@class)]//div[contains(@class,"info-text")])').strip() or "No Landmark available"
        outlets_dict={
            "Outletname":outlets.xpath('string(.//li[contains(@class,"outlet-name")])').strip(),
            "OutletAddress":address,
            "pincode":pincode.group(1),
            "landmark":landmark,
            "OutletCity":outlets.xpath('string(//*[@id="OutletCity"]/option[2])').strip(),
            "OutletState" :outlets.xpath('string(//*[@id="OutletState"]/option[10])').strip(),
            "Phone":outlets.xpath('string(.//li[contains(@class,"outlet-phone")])').strip(),
            "timings":outlets.xpath('string(.//li[contains(@class,"outlet-timings")])').strip(),
            "MapUrl":outlets.xpath('string(.//a[contains(@class,"map")]/@href)').strip(),
            "OutletUrl":outlets.xpath('string(.//a[contains(@class,"website")]/@href)').strip()
        }
        result.append(outlets_dict)
    return result
