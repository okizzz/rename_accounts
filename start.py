#!/usr/bin/env python3.8
import os

#функция парсинга всех имен с расширением txt
def parsename():
    path = "./in"
    names = [f for f in os.listdir(path) if f.endswith('.txt')]
    return(names)

def main():
    names = parsename()
    for index, name in  enumerate(names) :
    	clear_name = name.split(".")[0]
    	os.rename(f'./in/{name}', f'./out/{clear_name}.aezakmi')
    	print(f'{index} {name} rename to {clear_name}.aezakmi')

if __name__ == '__main__':
    main()
