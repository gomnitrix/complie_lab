# f1 = open("./SDT.txt", "r",encoding='UTF-8')
# f2 = open("./semantic_grammar.txt", "r",encoding='UTF-8')
# f3 = open("./SDT.txt","w+",encoding='UTF-8')
# try:
#     lines1 = f1.readlines()
#     lines2 = f2.readlines()
#     temp = []
#     for i in range(len(lines1)):
#         line1 = lines1[i]
#         line2 = lines2[i].strip()
#         line = line2+'?'+line1
#         temp.append(line)
#     f3.writelines(temp)
# except Exception as e:
#     raise e
# finally:
#     f1.close()
#     f2.close()
#     f3.close()


def test():
    offset=None
    exec("print(offset)")

if __name__ == '__main__':
    test()