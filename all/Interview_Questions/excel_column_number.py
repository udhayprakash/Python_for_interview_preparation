#!/usr/bin/python3
"""
Purpose: For the given numeric column number,
    display the Excel Column label
"""
from string import ascii_uppercase

mapping = {index: char for index, char in enumerate(ascii_uppercase)}
print(mapping)


def get_excel_col_label(colNum):
    if colNum < 1:
        return "INvalid column Number"
    # colName = ''
    # while colNum:
    #     colIndex = (colNum  if colNum <= 26 else colNum // 26) - 1
    #     print('\t', colNum, colIndex, mapping[colIndex],  colName)
    #     colName += mapping[colIndex]
    #     colNum = colIndex
    # return colName
    colName = ""
    while colNum >= 0:
        print(colNum // 26, colNum % 26, colName)
        colName = str(colNum % 26) + colName
        colNum -= colNum % 26
    # return mapping[(colNum // 26) - 1] + mapping[colNum % 26]


if __name__ == "__main__":
    # for i in range(1, 50):
    #     print(i, '-->', get_excel_col_label(i))
    get_excel_col_label(30)
    # assert get_excel_col_label(77) == 'BZ'
