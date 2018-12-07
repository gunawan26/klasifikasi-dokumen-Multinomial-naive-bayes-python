from datetime import time

import noname
import wx
import pandas as pd
from cleanse_data import TrainingData
import csv
from Dataset import Dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import io
from sklearn.naive_bayes import MultinomialNB
import re
import ComboBox
import numpy as np
import sklearn
variables =[]
labels = []


class resultPanel(noname.MyFrame3):

    def __init__(self,parent,judul_args,abstrak_args,hasil_stemming_args,result_args,cross_args):
        noname.MyFrame3.__init__(self,parent)



        self.m_judul_result.AppendText(judul_args)
        self.m_abstrak_result.AppendText(abstrak_args)
        self.m_stem_result.AppendText(hasil_stemming_args)
        self.m_result.AppendText(str(result_args))

        self.m_result.AppendText("Akurasi : {0}".format(cross_args[0]))
        self.m_result.AppendText(cross_args[1])











        self.Show()







class errorDialog(noname.MyDialog1):

    def __init__(self,parent):
        noname.MyDialog1.__init__(self,parent)
        self.Show()

class DetailTrainingData(noname.MyFrame2):

    def __init__(self,parent,count_training):
        self.cnt_train = count_training
        noname.MyFrame2.__init__(self,parent)
        self.show_data_training(count_training)
        self.Bind(wx.EVT_BUTTON,self.onExit,self.m_button4_exit)

        #self.Bind(wx.EVT_UPDATE_UI, lambda event:self.show_data_training(count_training))
        self.Show()


    def show_data_training(self,count_training):

       for x,item in enumerate(count_training,start=1):
            new_val = list(item)
            new_val.insert(0,x)
            self.m_dataViewListCtrl1.AppendItem(new_val)
            print(count_training)


    def onExit(self,event):

        self.Close()
        pass



class myEvent(noname.MyFrame1):


    def __init__(self,parent):
        self.val_kategori = Dataset.combo_text(Dataset())
        noname.MyFrame1.__init__(self, parent,self.val_kategori)
        self.Add_training.Bind(wx.EVT_BUTTON,self.create_data_set)
        self.proses_training.Bind(wx.EVT_BUTTON,self.training_data)
        self.proses_testing.Bind(wx.EVT_BUTTON,self.testing_prediction)
        self.vectorizer = TfidfVectorizer()
        self.vector_cross_val = TfidfVectorizer()
        self.Bind(wx.EVT_MENU,self.onClickDataTraing,self.m_menuItem_training)
        self.Bind(wx.EVT_MENU,self.onClickExitApp,self.m_menuItem1)

        pass






    def onClickDataTraing(self,event):
        countDTraining = Dataset.count_kategori(Dataset)
        print(countDTraining)
        DetailTrainingData(None,countDTraining)
        pass

    def onClickExitApp(self,event):

        self.Close()

        pass

    def onClickAddUpdateCat(self,event):

        noname.MyFrame1.choices = Dataset.combo_text(Dataset)
        noname.MyFrame1.reload_choice(noname.MyFrame1)
        pass

    def validate_data_input(self, *data_input_args):

        for arg in data_input_args:
            arg = re.sub("[^a-zA-Z]*", "", arg)

            if(arg == "" or arg == " "):
                print("data_kosong")
                return False

        return True


    def create_data_set(self,event):

        judul = self.m_training_judul.GetValue()
        kategori =  self.m_training_topik.GetValue()
        abstrak = self.m_training_abstrak.GetValue()
        validate = self.validate_data_input(kategori,abstrak,judul)

        if(validate):
            print("masuk")
            # melakukan preprocessing pada abstrak sebelum masuk ke data set.
            abstrak = TrainingData.clean_words(abstrak)
            #kategori = TrainingData.clean_words(kategori)
            print(abstrak+" "+kategori)
            new_dataset = Dataset()

            kategori_id = new_dataset.set_kat(kategori)

            new_dataset.insert_training(judul,abstrak,kategori_id)

            with open('data_set.csv', 'a') as f:
                w = csv.writer(f)
                w.writerow([kategori, abstrak])
                pass

            self.m_training_judul.Clear()
            self.m_training_topik.SetLabelText(" ")
            self.m_training_abstrak.Clear()
            val = new_dataset.combo_text()
            self.m_training_topik.Clear()
            self.m_training_topik.Append(val)
            wx.MessageBox('Dataset berhasil di tambahkan', 'Sukses', wx.OK)
        else:
            wx.MessageBox('Input yang anda masukan tidak lengkap', 'Error', wx.OK | wx.ICON_ERROR)

    def training_data(self,event):
        global variables
        global labels
        global variables_test_cros
        global labels_test_cros
        dataset_val = Dataset()
        #=================================================================#
        q = "SELECT tb_kategori.nama_kategori as kategori,abstract as text FROM tb_training inner join tb_kategori using (id_kategori)"
        #=================================================================#

        new = pd.read_sql(q,dataset_val.connect)
        job_df_new = new
        job_df_new.columns = ['kategori', 'text']

        cat_count = {x: 0 for x in set(job_df_new["kategori"])}
        for cat in job_df_new["kategori"]:
            cat_count[cat] += 1
        corpus = job_df_new.text
        words = [w for w in corpus]

        tfidf_matrix = self.vectorizer.fit_transform(words).todense()
        tfidf_names = self.vectorizer.get_feature_names()
        tfidf_mat_test = self.vector_cross_val.fit_transform(words).todense()
        tfidf_name_test = self.vectorizer.get_feature_names()

        #make variable global
        variables = tfidf_matrix
        labels = job_df_new.kategori
        variables_test_cros = tfidf_mat_test
        labels_test_cros = job_df_new.kategori


        with open('variable_set.txt','w') as f:
            f.write(str(variables))

        with open('label_set.txt','w') as f:
            f.write(str(labels))

        wx.MessageBox('Proses Training Selesai', 'Sukses', wx.OK)


        pass


    def testing_prediction(self,event):

        judul_testing = self.m_ctrl_test_judul.GetValue()
        abstrak_testing = self.m_judul_text_abstrak.GetValue()
        validate_testing = self.validate_data_input(judul_testing,abstrak_testing)
        if(validate_testing):

            if(len(variables) > 0):
                clean_abstrak = TrainingData.clean_words(abstrak_testing)

                #cross validation
                #variables_train, variables_test, labels_train, labels_test = train_test_split(variables, labels, test_size=.1)
                myvectorizer = TfidfVectorizer()
                mn_bayes = MultinomialNB()

                data_tes = pd.read_csv(io.StringIO(clean_abstrak))


                test_data = self.vectorizer.transform(data_tes)

                mn_bayes_fit =mn_bayes.fit(variables,labels)

                prediction_mn = mn_bayes_fit.predict(test_data)
                #mn_ascore = sklearn.metrics.accuracy_score(labels_test, prediction_mn)
                #print(mn_ascore)

                #print(prediction_mn)
                #print(sklearn.metrics.confusion_matrix(test))
                print(labels)

                cros_val = self.cross_validation()
                print(cros_val)
                mypanel = resultPanel(None,judul_testing,abstrak_testing,clean_abstrak,prediction_mn,cros_val)


            else:
                wx.MessageBox('Harap proses Training Terlebih dahulu', 'Warning', wx.OK | wx.ICON_WARNING)

        else:
            wx.MessageBox('Input yang anda masukan tidak lengkap', 'Error', wx.OK | wx.ICON_ERROR)
        pass

    def cross_validation(self):
        mn_bayes2 = MultinomialNB()
        variables_train, variables_test, labels_train, labels_test = train_test_split(variables_test_cros, labels_test_cros, test_size=0.33)

        mn_bayes_fit = mn_bayes2.fit(variables_train, labels_train)
        prediction_mn = mn_bayes_fit.predict(variables_test)
        mn_ascore_accuration = sklearn.metrics.accuracy_score(labels_test, prediction_mn)
        #print("akurasi")
        #print(mn_ascore_accuration)
        #print("Classification Metrics: ")
        classification_metric = sklearn.metrics.classification_report(labels_test, prediction_mn)
        print(classification_metric)
        #print(type(classification_metric))
        print(sklearn.metrics.confusion_matrix(labels_test, prediction_mn))


        return mn_ascore_accuration,classification_metric


    def analysis_text(self,corpus_args):
        print(corpus_args)
