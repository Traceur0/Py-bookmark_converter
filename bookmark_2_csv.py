import csv
from datetime import datetime
import re
from time import strftime




path = input("type the path HTML file stored: ")
t = strftime('%Y%m%d%H%M%S')

def csv_conversion(set_li):
    head = ["URL", "ADD_DATE", "SITENAME"]
    with open(f'{t}_converted.csv', 'w', encoding="utf-8-sig", newline="") as doc_csv:
        w = csv.writer(doc_csv)
        w.writerow(head)
        w.writerows(set_li)
        print("EoF")


with open(path, 'r', encoding="utf-8") as doc_html:
    line_raw = doc_html.readlines()
    line_trimmed = line_raw[8:]
    set_list = []
    regex_str = re.compile(r'\s?<DT><A HREF="(.+)" ADD_DATE="(.+)" ICON=".+">(.+)</A>')
    for line in line_trimmed:
        matched = regex_str.match(line.strip())
        try:
            # ADD_DATE ### AttributeError
            # 첫 행에서는 정규표현식에 해당하는 부분이 존재하지지 않음
                # group() == None 의 경우 Errors
            r_time = datetime.fromtimestamp(int(matched.group(2)))
            set = [matched.group(1),r_time,matched.group(3)]
            set_list.append(set)
        except AttributeError:
            continue
    csv_conversion(set_list)

    # group(2)가 존재할 경우에만 append()
    # 없는경우 pass