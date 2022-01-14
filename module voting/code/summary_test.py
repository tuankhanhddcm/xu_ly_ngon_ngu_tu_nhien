import os
from tienxulyvannban import load_data

dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
dir_path = os.path.join(dir_path, 'module voting\\data')
train_paths = os.path.join(dir_path, 'train')
count = 0
for f in os.listdir(train_paths):
    path_dir =os.path.join(train_paths,f)
    if os.path.exists(dir_path+"\\test")==0:
        os.mkdir(dir_path+"\\test")
    os.mkdir(dir_path +"\\test\\"+f)
    for path in os.listdir(path_dir):
        if path != ".DS_Store":
            file_path = os.path.join(path_dir, path)
            for data in os.listdir(file_path):
                sentences = []
                txt = os.path.join(file_path, data)
                data1 = load_data.read_data_test(txt)
                for sent in data1:
                    sent=sent.replace("_"," ")
                    sentences.append(sent)
                count +=1  
                with open("./data/test/"+ f + "/"+str(count) + ".txt",'w', encoding='utf-8') as f1:
                            f1.write(".\n".join(sentences))
