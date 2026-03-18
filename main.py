from parser import parser
from model import Outlet
from db_config import create_table,insert_into_db
from lxml import html
import time
from utils import load


file=r"C:\Users\beerva.joshi\Downloads\Burger King Locator _ Ahmedabad _ Fast Food Restaurant.html"
table_name="Outlets"

def main():
    create_table(table_name)
    raw=load(file)
    result=parser(raw)
    validated=[]
    for outlet in result:
        try:
            validated.append(Outlet(**outlet))
        except Exception as e:
            print("Validation Error: ",e)
    if validated:
        insert_into_db(table_name,validated)

if __name__=="__main__":
    st=time.time()
    main()
    et=time.time()
    print(et-st)
