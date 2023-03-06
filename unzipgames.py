import os
import zipfile
from zipfile import ZipFile
import re

def extract_link(file: ZipFile):
    for old_name in file.namelist():
        new_name = old_name.encode('cp437').decode('gbk')
        if "百度网盘" in new_name:
            print("-"*24 + new_name +"-"*24)
            content = file.read(old_name).decode("utf-8")
            reg = re.compile(r'(?<=备用百度秒传链接：\s)((.|\n)*)(?=\s+-+\s+注意)')
            return reg.search(content).group(0).strip().split()

links_all = []

for root, dirs, files in os.walk("/mnt/c/Users/paras/Desktop/smallzips"):
    for file in files:
        filepath = os.path.join(root, file)
        zf = zipfile.ZipFile(filepath, "r")
        links = extract_link(zf)
        print(links)
        links_all += links

with open("result.txt", "w") as file:
    for link in links_all:
        file.write(link+"\n")
