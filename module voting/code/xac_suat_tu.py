import numpy as np
from tienxulyvannban import load_data
class xac_suat:
    #build từ điển số lần suất hiện của từ trong văn bản
    def word_dict(sentences,list_word):
        #tạo từ điển từ
        wordict=dict.fromkeys(list_word,0)
        #số lần xuất hiện của từ trong toàn bộ văn bản
        for n_cau in sentences:
            #n_cau=n_cau.lower()
            for tu in n_cau.split(" "):
                wordict[tu]+=1
        return wordict
    
    #tống số lần xuất hiện
    def sum_lan_xuat_hien_tu_in_cau(wordict,list_sentence):
        solanxuathien=[]
        for sentence in list_sentence:
            dem=0
            for words, count in wordict.items():
                if (words in sentence):
                    if(sentence.count(words) > 1):
                        count=count*2
                    dem+=count
            solanxuathien.append(dem)
        return solanxuathien

    def xac_suat_tu(sentences):
        # tạo danh sách số từ trong văn bản,số từ của 1 câu,số câu trong văn bản
        list_word, word_in_sentence, list_sentence = load_data.tao_danh_sach(sentences)
        #tạo từ điển
        wordict=xac_suat.word_dict(sentences,list_word)
        #tính tổng lần xuất hiện của 1 từ
        solanxuathien=xac_suat.sum_lan_xuat_hien_tu_in_cau(wordict,list_sentence)
        #tính xác xuất thực thực từ
        trongso=np.array(solanxuathien)/len(list_word)/np.array(word_in_sentence)
        return trongso
