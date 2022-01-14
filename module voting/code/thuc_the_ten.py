import numpy as np
from pyvi import ViTokenizer,ViPosTagger
class danh_tu_rieng:
    def tinh_thuc_the_ten(sentences):
        X = []
        for sent in sentences:
            sent = ViPosTagger.postagging(sent)
            X.append(sent)
        list_cau = []
        list_nhan = []
        for x in X:
            for y in range(len(x)):
                if(y % 2 == 0):
                    list_cau.append(x[y])
                else:
                    list_nhan.append(x[y])

        # tính số thực thể tên có trong câu s
        N_name = []
        Nw = []  # số thực từ có trong câu
        for loai in list_nhan:
            lent = len(loai)
            if("Np" in loai) or ("Ny" in loai):
                dem_in= loai.count('Np')+loai.count('Ny')
            else: dem_in = 0
            N_name.append(dem_in)
            Nw.append(lent)
        # tính trọng số câu dựa vào thực thể tên
        trong_so_cau = np.array(N_name)/np.array(Nw)
        return trong_so_cau


