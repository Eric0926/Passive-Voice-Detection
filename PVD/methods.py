import nltk

#导入引起倒装的句首标志
inversion_initials=[]
fhand=open("inversion_initials.txt")
inversion_initials=fhand.readlines()
for i in range(len(inversion_initials)):
    inversion_initials[i]=inversion_initials[i].rstrip("\n")
fhand.close()

#将倒装句转换为陈述语序
def InvertedToDeclarative(sent):
    for words in inversion_initials:
        if sent.startswith(words):
            sent=sent.lstrip(words+" ")
            break
    return sent

#导入混淆插入语
misleading_parenthesis=[]
fhand=open("misleading_parenthesis.txt")
misleading_parenthesis=fhand.readlines()
for i in range(len(misleading_parenthesis)):
    misleading_parenthesis[i]=misleading_parenthesis[i].rstrip("\n")
fhand.close()

#删除混淆插入语
def DeleteMisleadingParenthesis(sent):
    for words in misleading_parenthesis:
        pos=sent.find(words)
        if (pos!=-1):
            sent=sent[0:pos-1]+sent[pos+len(words):]
    return sent

#切分分句
def SplitSentence(sent):
    pos=sent.find(",")
    sub_sents=[]
    if (pos==-1):
        sub_sents.append(sent)
    else:
        while (pos!=-1):
            sub_sents.append(sent[:pos])
            sent=sent[pos+2:]
            pos=sent.find(",")
        sub_sents.append(sent)
    return sub_sents

#导入过去完成时可作形容词的动词
jj_vbn=[]
fhand=open("jj_vbn.txt")
jj_vbn=fhand.readlines()
for i in range(len(jj_vbn)):
    jj_vbn[i]=jj_vbn[i].rstrip("\n")
fhand.close()

#识别被动语态
def PassiveVoiceDetection(sent):
    be_get_list=["be","am","is","are","was","were","been","being","get","gets","got","getting"]
    sent_list=nltk.word_tokenize(sent)
    sent_words_tags=nltk.pos_tag(sent_list)
    sent_tags=[]
    for word,tag in sent_words_tags:
        sent_tags.append(tag)
    #print(sent_words_tags)
    #print(sent_tags)
    find_pv=False
    for i in range(len(sent_tags)):
        if (sent_tags[i]=="VBN" or sent_tags[i]=="VBD"):
            if sent_list[i] in jj_vbn:
                find_by=False
                for j in sent_list[i+1:]:
                    if j=="by":
                        find_by=True
                        break
                if not find_by:
                    sent_tags[i]="JJ"
                    continue
            find_be_get=False
            j=i-1
            while (j>=0):
                if (sent_list[j] in be_get_list):
                    find_be_get=True
                    break
                j-=1
            if find_be_get:
                find_pv=True
                break
    return find_pv

clause_marker=["which","that","when","where","if","whether","once"]
