##filePath1,filepath2是需要去重合并的文件路径，outFilePath是合并后输出文件
##signStr是文件中的分割符

# filePath1 = "masknew.txt"
# filePath2 = "masknew2.txt"
# outFilePath = "MaskWord.txt"
# signStr = "◆"
filePath1 = ""
filePath2 = ""
outFilePath = ""
signStr = ""

filePath1 = input("请输入需要去重合并的文件1路径（相对路径）: ")
filePath2 = input("请输入需要去重合并的文件2路径（相对路径）: ")
outFilePath = input("请输入输出文件路径（相对路径）: ")
signStr = input("请输入分隔符: ")


while filePath1 == "" or filePath2 == "" or outFilePath == "" or signStr == "":
    if filePath1 == "":
        filePath1 = input("请输入需要去重合并的文件1路径（相对路径）: ")
    if filePath2 == "":
        filePath2 = input("请输入需要去重合并的文件2路径（相对路径）: ")
    if outFilePath == "":
        outFilePath = input("请输入输出文件路径（相对路径）: ")
    if signStr == "":
        signStr = input("请输入分隔符 : ")

f1 = open(filePath1, encoding='utf-8')
f2 = open(filePath2, encoding='utf-8')
outFile = open(outFilePath, "w")
newF = open(outFilePath, "w", encoding='utf-8')


def combineFile(path1, path2):
    combine_content = ""
    file_content1 = path1.readlines()
    file_content2 = path2.readlines()
    for fc1 in file_content1:
        if fc1.rfind("\n") > -1:
            index = fc1.rfind("\n")
            combine_content = combine_content[0:index]
        combine_content += fc1
    combine_content = quChong(combine_content)
    path1.close()
    for fc2 in file_content2:
        combine_content += signStr + fc2
    combine_content = quChong(combine_content)
    path2.close()
    line = quChong(combine_content)
    line = line[line.find(signStr) + 1:line.rfind(signStr)]
    newF.write("".join(line))
    print("处理完成！")


def quChong(str):
    word_list = set(str.split(signStr))
    last_word = ""
    for word in word_list:
        if word.find("\n") > -1:
            index = word.find("n")
            word = word[0:index]
        last_word += word + signStr
    return last_word


combineFile(f1, f2)
