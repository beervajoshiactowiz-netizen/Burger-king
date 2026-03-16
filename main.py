from parser import parser
from model import Outlet
from db_config import create_table,insert_into_db
from lxml import html

file=r"C:\Users\beerva.joshi\Downloads\Burger King Locator _ Ahmedabad _ Fast Food Restaurant.html"
table_name="Outlets"
def load(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        return content

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
    main()