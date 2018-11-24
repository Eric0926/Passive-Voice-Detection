import nltk
from methods import DeleteMisleadingParenthesis as dmp #删除混淆插入语的方法
from methods import SplitSentence as ss #切分分句
from methods import PassiveVoiceDetection as pvd #找是否有被动语态
from methods import clause_marker #从句标志语
fhand=open("test.txt")
for sent in fhand:
    sent=sent.rstrip("\n")
    sent=dmp(sent) #删除句子中的混淆插入语
    sub_sents=ss(sent) #切分分句
    print(sent)
    finded=False
    #判断各个分句是否包含被动语态
    for sub_sent in sub_sents:
        if pvd(sub_sent):
            finded=True
            break
    if finded:
        print('Y')
        continue
    #判断第N个与第N+1个分句结合的句子是否包含被动语态
    for i in (range(len(sub_sents)-2)):
        if sub_sents[i].lower().split()[0] not in clause_marker:
            if pvd(sub_sents[i]+" "+sub_sents[i+2]):
                finded=True
                break
    if finded:
        print('Y')
        continue
    print('N')
fhand.close()
