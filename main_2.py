
import numpy as np

filePath1 = ""
filePath2 = ""
outFilePath1 = ""
outFilePath2 = ""
outFilePath3 = ""
signStr = ""


filePath1 = "MaskWords.txt"
filePath2 = "MaskWords4399.txt"
outFilePath1 = "text1.txt"
outFilePath2 = "text2.txt"
outFilePath3 = "text3.txt"
signStr = "◆"

# filePath1 = input("请输入需要去重合并的文件1路径（相对路径）: ")
# filePath2 = input("请输入需要去重合并的文件2路径（相对路径）: ")
# outFilePath = input("请输入输出文件路径（相对路径）: ")
# signStr = input("请输入分隔符: ")

# while filePath1 == "" or filePath2 == "" or outFilePath == "" or signStr == "":
#     if filePath1 == "":
#         filePath1 = input("请输入需要去重合并的文件1路径（相对路径）: ")
#     if filePath2 == "":
#         filePath2 = input("请输入需要去重合并的文件2路径（相对路径）: ")
#     if outFilePath == "":
#         outFilePath = input("请输入输出文件路径（相对路径）: ")
#     if signStr == "":
#         signStr = input("请输入分隔符 : ")

f1 = open(filePath1, encoding='utf-8')
f2 = open(filePath2, encoding='utf-8')
outFile1 = open(outFilePath1, "w", encoding="utf-8")
outFile2 = open(outFilePath2, "w", encoding="utf-8")
outFile3 = open(outFilePath3, "w", encoding="utf-8")

##比较两个列表，如果都有，则删除后一个列表中的对应元素
def CompareContent():
    lines1 = f1.readlines()[0]
    lines2 = f2.readlines()[0]
    str1List = set(Deduplication(lines1).split(signStr))
    str2List = set(Deduplication(lines2).split(signStr))
    commonList = str1List & str2List

    for str in str1List:
        if str in str2List:
            str2List.remove(str)

    return listToString(str1List)##,listToString(str2List),listToString(commonList)


def listToString(setList):
    last_word = ""
    listofSet = list(setList)
    for word in setList:
        if word.find("\n") > -1:
            index = word.find("n")
            word = word[0:index]
        last_word += word + signStr
    listofSet.sort()
    listofSet.reverse()
    len_listofset = len(listofSet)-1
    arr = quickSort(listofSet, 0, len_listofset)
    str = combineSign(arr)
    return str


def Deduplication(str):
    word_list = set(str.split(signStr))

    last_word = ""
    for word in word_list:
        if word.find("\n") > -1:
            index = word.find("n")
            word = word[0:index]
        last_word += word + signStr

    return last_word


def quickSort(arr, left, right):
    if left >= right:
        return
    index_i = left
    index_j = right
    desc = arr[left]
    while index_i < index_j:
        while index_i < index_j and len(arr[index_j]) < len(desc):
            index_j -= 1
        if index_i < index_j:
            arr[index_i] = arr[index_j]
            index_i += 1
        while index_i < index_j and len(arr[index_i]) > len(desc):
            index_i += 1
        if index_i < index_j:
            arr[index_j] = arr[index_i]
            index_j -= 1
    arr[index_i] = desc
    quickSort(arr, left, index_i-1)
    quickSort(arr, index_i+1, right)
    return arr


def combineSign(arr):
    str = ""
    for word in arr:
        str = str + signStr +word
    return str


str1 = CompareContent()
outFile1.write("".join(str1))
