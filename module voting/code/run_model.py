
import os
from rouge import Rouge
from model_Voting import Voting
def danh_gia(summary_path,test_paths):
    tamp1 = dict.fromkeys(['f','p','r'],0)
    tamp2 = dict.fromkeys(['f','p','r'],0)
    tamp3 = dict.fromkeys(['f','p','r'],0)
    avg_scores ={}
    count = 0
    for paths in os.listdir(summary_path):
        path = os.path.join(summary_path,paths)
        for file_summary in os.listdir(path):
            file_summarys = os.path.join(path,file_summary)
            summary = open(file_summarys , encoding='utf-8').read()
            for file_tests in os.listdir(test_paths):
                if file_tests == paths:
                    file_test = os.path.join(test_paths,file_tests)   
                    for test_summary in os.listdir(file_test):
                        if test_summary == file_summary:
                            test_summary = os.path.join(file_test,test_summary)
                            test = open(test_summary , encoding='utf-8').read()
                            scores = rouge.get_scores(summary,test)
                            for key in scores:
                                for indx , val in key.items():
                                    if indx =="rouge-1":
                                        for var,gt in val.items():
                                            tamp1[var] +=gt
                                        avg_scores[indx]=tamp1
                                    if indx=="rouge-2":
                                        for var,gt in val.items():
                                            tamp2[var] +=gt
                                        avg_scores[indx] =tamp2
                                    if indx=="rouge-l":
                                        for var,gt in val.items():
                                            tamp3[var] +=gt
                                        avg_scores[indx] =tamp3 
            count +=1
    for index ,val in avg_scores.items():
        for ind1,val1 in val.items():
            avg_scores[index][ind1] = val1 / float(count) 
    return avg_scores



dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'module voting\\data')
test_paths = os.path.join(dir_path,'test')
train_paths = os.path.join(dir_path, 'train')
summary_voing_path = os.path.join(dir_path, 'voting summary')
summary_pp1_path = os.path.join(dir_path, 'pp1 summary')
summary_pp2_path = os.path.join(dir_path, 'pp2 summary')
summary_pp3_path = os.path.join(dir_path, 'pp3 summary')


# chạy model tạo folder summary của từng phương pháp
#Voting.run_model(train_paths,dir_path)

#---------------------thực hiện đánh giá ROUGE ------------------------
rouge = Rouge()
# điểm đánh giá của từng phương pháp
pp1 = danh_gia(summary_pp1_path,test_paths)               
pp2 = danh_gia(summary_pp2_path,test_paths)
pp3 = danh_gia(summary_pp3_path,test_paths)
voting = danh_gia(summary_voing_path,test_paths)


print(pp1)
print("\n")
print(pp2)
print("\n")
print(pp3)
print("\n")

print(voting)
