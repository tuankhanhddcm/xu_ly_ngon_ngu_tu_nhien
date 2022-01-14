import numpy as np
from tienxulyvannban import load_data

class TF_ISF:
    def tinh_TF_ISF(sentence):

        # tạo danh sách số từ trong văn bản,số từ của 1 câu,số câu trong văn bản
        list_word, word_in_sentence, list_sentence = load_data.tao_danh_sach(sentence)
        # Tính TF
        TF = np.array(word_in_sentence)

        # -------------Tính ISF------------------------
        SF_dict = dict.fromkeys(list_word, 0)
        # tổng số câu (SF) có chứa từ X
        for key in SF_dict.keys():
            count = 0
            for n_cau in list_sentence:
                dem_in_cau = n_cau.count(key)
                if(dem_in_cau > 0):
                    count += 1
                SF_dict[key] = count

        # tinh ISF
        import math
        ISF_word_dict = {}
        for k, v in SF_dict.items():
            s_f = math.log10(len(list_sentence)/v)
            ISF_word_dict[k] = s_f
        #tinh ISF của câu
        ISF_sentence = []
        for n_cau in list_sentence:
            tong = 0
            for k, v in ISF_word_dict.items():
                if(k in n_cau):
                    if(n_cau.count(k) > 1):
                        v = v*2
                    tong += v
            ISF_sentence.append(tong)
        # tính trọng số
        trong_so_TFISF = (np.array(TF)*np.array(ISF_sentence)) /np.array(word_in_sentence)
        # trọng số của 1 câu tính theo TF-ISF
        if (max(trong_so_TFISF)):
            trong_so_cau = np.array(trong_so_TFISF)/max(trong_so_TFISF)
        else: trong_so_cau = np.array(trong_so_TFISF)
        return trong_so_cau

