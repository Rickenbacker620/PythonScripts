import os
import zipfile
from zipfile import ZipFile
import re

def extract_link(file: ZipFile):
    for name in file.namelist():
        content = file.read(name).decode("utf-8")
        reg = re.compile(r'(?<=秒传链接：\s)((.|\n)*)tar')
        return reg.search(content).group(0).strip().split()

links_all = []
count = 0

for root, dirs, files in os.walk("/mnt/c/Users/paras/Desktop/smallzips"):
    for file in files:
        filepath = os.path.join(root, file)
        zf = zipfile.ZipFile(filepath, "r")
        links = extract_link(zf)
        print(zf.filename)
        print(links)
        count += 1
        links_all += links

with open("result.txt", "w") as file:
    for link in links_all:
        file.write(link+"\n")

print(f"已完成{count}个\n")

for link in links_all:
    print(link)