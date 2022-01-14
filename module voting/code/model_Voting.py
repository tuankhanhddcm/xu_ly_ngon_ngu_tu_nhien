import numpy as np
from tienxulyvannban import load_data
from thuc_the_ten import danh_tu_rieng
from tf_isf import TF_ISF
from xac_suat_tu import xac_suat
import os

class Voting:
#---------Tính các Phương pháp ------------------------#
    def phuong_phap(dac_trung_1, dac_trung_2,data):
        PP = np.array(dac_trung_1)*np.array(dac_trung_2)
        # sắp xếp
        sentence_dict = dict.fromkeys(data, 0)
        n = 0
        for cau in sentence_dict.keys():
            if(n < len(PP)):
                sentence_dict[cau] = PP[n]
                n += 1
        PP_dict = {}
        for ts in sorted(PP, reverse=True):
            for cau_n, gt in sentence_dict.items():
                if (gt == ts):
                    PP_dict[cau_n] = gt
        sort_PP = []
        for key in PP_dict.keys():
                sort_PP.append(key)
        
        ## tóm tắt văn bản bằng phương pháp 1:
        cau_pp = []
        so_cau_tom_tat = 3
        for key in PP_dict.keys():
            if(len(cau_pp) < so_cau_tom_tat):
                cau_pp.append(key)
        tom_tat = []
        for cau_n in data:
                if(cau_n in cau_pp):
                    cau_n=cau_n.replace("_"," ")
                    tom_tat.append(cau_n)
        return sort_PP, tom_tat
    #------------------------------TÍNH THỨ TỰ ƯU TIÊN---------------------
    def uu_tien(phuong_phap_n,sentence):
        thu_tu = []
        n = len(phuong_phap_n)
        for sent in sentence:
            if sent in phuong_phap_n:
                thu_tu.append(n-phuong_phap_n.index(sent))
        return thu_tu

# -------------------MODEL VOTING(BORDA)-------------------------------------------
    def model_voting(pp1,pp2,pp3,data_train):
        thu_tu_1 = Voting.uu_tien(pp1,data_train)
        thu_tu_2 = Voting.uu_tien(pp2,data_train)
        thu_tu_3 = Voting.uu_tien(pp3,data_train)
        
        voting = np.array(thu_tu_1) + np.array(thu_tu_2) + np.array(thu_tu_3)
        voting_dict = dict.fromkeys(data_train, 0)
        n = 0
        for cau in data_train:
            if n < len(voting):
                voting_dict[cau] = voting[n]
                n += 1
        cau_dict = {}
        for ts in sorted(voting, reverse=True):
            for cau, gt in voting_dict.items():
                if (gt == ts):
                    cau_dict[cau] = gt
        sort_cau_voting=[]
        so_cau_tom_tat = 3 #số câu cần tóm tắt
        for key in cau_dict.keys():
            if(len(sort_cau_voting) < so_cau_tom_tat):
                sort_cau_voting.append(key)
        tom_tat = []
        for cau_n in data_train:
                if(cau_n in sort_cau_voting):
                    cau_n=cau_n.replace("_"," ")
                    tom_tat.append(cau_n)
        return tom_tat

    def run_model( train_paths,dir_path):
        count = 0
        for f in os.listdir(train_paths):
            path_dir =os.path.join(train_paths,f)
            #kiểm tra thư mục chứa file tóm tắt
            if os.path.exists(dir_path +"\\voting summary") == 0:
                os.mkdir(dir_path +"\\voting summary")
            os.mkdir(dir_path +"\\voting summary\\"+ f)

            if os.path.exists(dir_path +"\\pp1 summary") ==0:
                os.mkdir(dir_path +"\\pp1 summary")
            os.mkdir(dir_path +"\\pp1 summary\\"+f)

            if os.path.exists(dir_path +"\\pp2 summary") ==0:
                os.mkdir(dir_path +"\\pp2 summary")
            os.mkdir(dir_path +"\\pp2 summary\\"+f)

            if os.path.exists(dir_path +"\\pp3 summary") ==0:
                os.mkdir(dir_path +"\\pp3 summary")
            os.mkdir(dir_path +"\\pp3 summary\\"+f)
            for path in os.listdir(path_dir):
                if path != ".DS_Store":
                    file_path = os.path.join(path_dir, path)
                    for data in os.listdir(file_path):
                        sentences = []
                        txt = os.path.join(file_path, data)
                        data = load_data.read_data_train(txt)

                        for sent in data:
                            sentences.append(sent)
                        tf_isf = TF_ISF.tinh_TF_ISF(sentences)
                        xac_suat_tu = xac_suat.xac_suat_tu(sentences)
                        thuc_the_ten = danh_tu_rieng.tinh_thuc_the_ten(sentences)

                        sort_pp1,tom_tat_pp1 = Voting.phuong_phap(tf_isf, thuc_the_ten,sentences)
                        sort_pp2,tom_tat_pp2 = Voting.phuong_phap(tf_isf, xac_suat_tu,sentences)
                        sort_pp3,tom_tat_pp3 = Voting.phuong_phap(thuc_the_ten, xac_suat_tu,sentences)
                        tom_tat_voting = Voting.model_voting(sort_pp1,sort_pp2,sort_pp3,sentences)
                        count +=1
                        with open("./data/voting summary/"+ f + "/"+str(count) + ".txt",'w', encoding='utf-8') as f1:
                            f1.write(".\n".join(tom_tat_voting))
                        with open("./data/pp1 summary/"+ f + "/"+str(count) + ".txt",'w', encoding='utf-8') as f2:
                            f2.write(".\n".join(tom_tat_pp1))
                        with open("./data/pp2 summary/"+ f + "/"+str(count) + ".txt",'w', encoding='utf-8') as f3:
                            f3.write(".\n".join(tom_tat_pp2))
                        with open("./data/pp3 summary/"+ f + "/"+str(count) + ".txt",'w', encoding='utf-8') as f4:
                            f4.write(".\n".join(tom_tat_pp3))


        