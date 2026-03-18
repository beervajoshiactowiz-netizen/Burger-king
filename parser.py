from pprint import pprint
from lxml import html
import re
import json


with open("xpaths.json", "r") as f:
    XPATHS = json.load(f)

def parser(text):
    tree = html.fromstring(text)
    result=[]
    city  = tree.xpath(f'string({XPATHS["OutletCity"]})').strip()
    state = tree.xpath(f'string({XPATHS["OutletState"]})').strip()
    store=tree.xpath(XPATHS["store_box"])
    for outlets in store:
        address = outlets.xpath(f'string({XPATHS["OutletAddress"]})').strip()
        pincode=re.search(r'\b(\d{6})\b', address)
        landmark=outlets.xpath(f'string({XPATHS["landmark"]})').strip() or "No Landmark available"
        outletUrl=outlets.xpath(f'string({XPATHS["OutletUrl"]})').strip()
        storeid=re.search(r'-(\d+)',outletUrl)
        outlets_dict={
            "Outletname":outlets.xpath(f'string({XPATHS["Outletname"]})').strip(),
            "storeId": int(storeid.group(1)),
            "OutletAddress":address,
            "pincode":pincode.group(1),
            "landmark":landmark,
            "OutletCity":city,
            "OutletState" :state,
            "Phone":outlets.xpath(f'string({XPATHS["Phone"]})').strip(),
            "timings":outlets.xpath(f'string({XPATHS["timings"]})').strip(),
            "MapUrl": outlets.xpath(f'string({XPATHS["MapUrl"]})').strip(),
            "OutletUrl":outletUrl
        }
        result.append(outlets_dict)
    return result
