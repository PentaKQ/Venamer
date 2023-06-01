from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget
import os
from datetime import date
from datetime import datetime
import time
import io
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
from chitiet_doiten import Ui_Form_doiten
from chitiet_doi import Ui_Form_doi
from chitiet_xoa import Ui_Form_xoa
from chitiet_thay import Ui_Form_thay
from chitiet_them import Ui_Form_them
now = datetime.now()
vitriType = 'dau'
doi_coso = True
doi_gioihan = False
xoa_gioihan = False
them_gioihan = False
thay_gioihan = False




Venamer.setWindowIcon(QtGui.QIcon('logo.png'))



#####################################################################################################################################
        self.pushButton_undo.setEnabled(False)

        self.pushButton_file.clicked.connect(self.run_open_file)

        self.JobTab.tabBarClicked['int'].connect(self.reset_pb)

        self.pushButton_doiten.clicked.connect(self.run_doiten)
        self.pushButton_xoa.clicked.connect(self.run_xoa)
        self.pushButton_them.clicked.connect(self.run_them)
        self.pushButton_doi.clicked.connect(self.run_doiduoi)
        self.pushButton_thay.clicked.connect(self.run_thay)

        self.pushButton_doiten_xemtruoc.clicked.connect(self.run_doiten_xemtruoc)
        self.pushButton_them_xemtruoc.clicked.connect(self.run_them_xemtruoc)
        self.pushButton_xoa_xemtruoc.clicked.connect(self.run_xoa_xemtruoc)
        self.pushButton_doi_xemtruoc.clicked.connect(self.run_doiduoi_xemtruoc)
        self.pushButton_thay_xemtruoc.clicked.connect(self.run_thay_xemtruoc)

        self.pushButton_lichsu.clicked.connect(self.run_lichsu)

        self.pushButton_doiten_chitiet.clicked.connect(self.moCuaSo_doiten)
        self.pushButton_them_chitiet.clicked.connect(self.moCuaSo_them)
        self.pushButton_thay_chitiet.clicked.connect(self.moCuaSo_thay)
        self.pushButton_xoa_chitiet.clicked.connect(self.moCuaSo_xoa)
        self.pushButton_doi_chitiet.clicked.connect(self.moCuaSo_doi)

        self.pushButton_undo.clicked.connect(self.undo)

        self.radioButton_them_dau.clicked.connect(self.them_dau)
        self.radioButton_them_cuoi.clicked.connect(self.them_cuoi)
        self.radioButton_them_tuychinh.clicked.connect(self.them_tuychinh)

        self.checkBox_doi_gioihan.clicked.connect(self.run_doi_gioihan)
        self.checkBox_thay_gioihan.clicked.connect(self.run_thay_gioihan)
        self.checkBox_xoa_gioihan.clicked.connect(self.run_xoa_gioihan)
        self.checkBox_them_gioihan.clicked.connect(self.run_them_gioihan)

        self.radioButton_coso.clicked.connect(self.run_doi_coso)
        self.radioButton_khongso.clicked.connect(self.run_doi_khongso)

        




    def moCuaSo_doiten(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_doiten()
        self.ui.setupUi(self.window)
        startFrom = int(self.spinBox_doiten.text())
        duoiFile = self.lineEdit_doiten_duoi.text()
        specialName = self.lineEdit_doiten_ktdt.text()
        gioihan = self.lineEdit_doi_gioihan.text()
        path = self.duongdan.text()
        
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_doiten().loaddata(self.window, files, doi_coso, doi_gioihan, specialName, duoiFile, startFrom, gioihan)
            self.window.show()

    def moCuaSo_them(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_them()
        self.ui.setupUi(self.window)
        path = self.duongdan.text()
        kituthem = self.lineEdit_them_kitu.text()
        count = 1
        gioihan = self.lineEdit_them_gioihan.text()
        try:
            cach_n = self.spinBox_them_tuychinh.text()
            tinh_tu = self.comboBox_them_tuychinh.currentText()
        except Exception():
            cach_n = '0'
            tinh_tu = ''


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_them().loaddata(self.window, files, kituthem, gioihan, count, vitriType, cach_n, tinh_tu, them_gioihan)
            self.window.show()

    def moCuaSo_thay(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_thay()
        self.ui.setupUi(self.window)
        gioihan = self.lineEdit_thay_gioihan.text()
        thay = self.lineEdit_thay_thay.text()
        thay_thanh = self.lineEdit_thay_thanh.text()
        path = self.duongdan.text()
        count = 1


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_thay().loaddata(self.window, files, gioihan, thay, thay_thanh, count, thay_gioihan)
            self.window.show()

    def moCuaSo_xoa(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_xoa()
        self.ui.setupUi(self.window)
        kitucanxoa = self.lineEdit_xoa_kitu.text()
        path = self.duongdan.text()
        count = 1
        gioihan = self.lineEdit_xoa_gioihan.text()


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_xoa().loaddata(self.window, files, kitucanxoa, gioihan, count, xoa_gioihan)
            self.window.show()

    def moCuaSo_doi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form_doi()
        self.ui.setupUi(self.window)
        path = self.duongdan.text()
        doi = kituthem = self.lineEdit_doi_doi.text()
        doithanh = self.lineEdit_doi_doithanh.text()
        count=1


        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            Ui_Form_doi().loaddata(self.window, files, doi, kituthem, doithanh, count)
            self.window.show()




    def run_open_file(self):
        path = str(QFileDialog.getExistingDirectory(None, "Chọn Đường Dẫn"))
        self.duongdan.setText(path)

    def run_lichsu(self):
        try:
            os.startfile('logs.txt')
        except Exception:
            with io.open('logs.txt','a+', encoding='utf-8') as f:
                pass
            f.close()
            os.startfile('logs.txt')
            
    def undo(self):
        
        path = self.duongdan.text()
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp muốn hoàn tác không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            self.pushButton_undo.setEnabled(False)
            try:
                count = 1
                with io.open('before.txt','r', encoding='utf-8') as f:
                    before_list = f.readlines()
                f.close()
                with io.open('after.txt','r', encoding='utf-8') as f:
                    after_list = f.readlines()
                f.close()
                for i in range(len(before_list)):
                    self.progressBar.setProperty("value", round(count*100/len(before_list)))
                    QApplication.processEvents()
                    count = count + 1
                    before_list[i] = before_list[i][0:len(before_list[i])-1]
                    after_list[i] = after_list[i][0:len(after_list[i])-1]
                    for file in files:
                        if file == after_list[i]:
                            os.rename(path+'\\'+file,path+'\\'+before_list[i])
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Hoàn Tác [{file}] -> ['+before_list[i]+']\n')
                            f.close()
                            break
                done = QMessageBox()
                done.setWindowTitle('Hoàn Tất')
                done.setText(f'Đã hoàn tác thành công {len(files)} tệp')
                done.setIcon(QMessageBox.Information)
                x = done.exec_()

            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Không tìm thấy dữ liệu để hoàn tác!')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()

                



    def run_doi_gioihan(self):
        global doi_gioihan
        if doi_gioihan == False:
            self.lineEdit_doi_gioihan.setEnabled(True)
            doi_gioihan = True
        else:
            self.lineEdit_doi_gioihan.setEnabled(False)
            doi_gioihan = False

    def run_xoa_gioihan(self):
        global xoa_gioihan
        if xoa_gioihan == False:
            self.lineEdit_xoa_gioihan.setEnabled(True)
            xoa_gioihan = True
        else:
            self.lineEdit_xoa_gioihan.setEnabled(False)
            xoa_gioihan = False

    def run_them_gioihan(self):
        global them_gioihan
        if them_gioihan == False:
            self.lineEdit_them_gioihan.setEnabled(True)
            them_gioihan = True
        else:
            self.lineEdit_them_gioihan.setEnabled(False)
            them_gioihan = False

    def run_thay_gioihan(self):
        global thay_gioihan
        if thay_gioihan == False:
            self.lineEdit_thay_gioihan.setEnabled(True)
            thay_gioihan = True
        else:
            self.lineEdit_thay_gioihan.setEnabled(False)
            thay_gioihan = False





    def reset_pb(self):
        self.progressBar.setProperty("value", 0)

    def run_doi_coso(self):
        global doi_coso
        doi_coso = True 


    def run_doi_khongso(self):
        global doi_coso
        doi_coso = False



        

    def them_dau(self):
        global vitriType
        vitriType = 'dau'
        self.spinBox_them_tuychinh.setEnabled(False)
        self.comboBox_them_tuychinh.setEnabled(False)
    def them_cuoi(self):
        global vitriType
        vitriType = 'cuoi'
        self.spinBox_them_tuychinh.setEnabled(False)
        self.comboBox_them_tuychinh.setEnabled(False)
    def them_tuychinh(self):
        global vitriType
        vitriType = 'tuychinh'
        self.spinBox_them_tuychinh.setEnabled(True)
        self.comboBox_them_tuychinh.setEnabled(True)


    def run_doiten(self):
        self.pushButton_undo.setEnabled(True)
        path = self.duongdan.text()
        startFrom = int(self.spinBox_doiten.text())
        duoiFile = self.lineEdit_doiten_duoi.text()
        specialName = self.lineEdit_doiten_ktdt.text()
        gioihan = self.lineEdit_doi_gioihan.text()
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        i = startFrom
        count = 1
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác!')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:


            if doi_coso == True:
                try:
                    for file in files:
                        
                        file = str(file)
                        if doi_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                if specialName != '':
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+str(i)+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(str(specialName)+str(i)+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+str(specialName)+str(i)+'.'+duoiFile)
                                else:
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(i)+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(str(i)+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+str(i)+'.'+duoiFile)

                        else:
                            if specialName != '':
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+str(i)+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(specialName)+str(i)+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(specialName)+str(i)+'.'+duoiFile)
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(i)+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(i)+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(i)+'.'+duoiFile)
                        i = i + 1
                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1
                        
                    f.close()

                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_()

                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)


                except PermissionError:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra, không có quyền truy cập vào thư mục')
                    msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra, tên các file trước khi đổi và sau khi đổi không được trùng nhau và không được có kí tự đặc biệt!')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

            else:
                try:
                    mang_file = ''
                    mang_so = ['0','1','2','3','4','5','6','7','8','9']


                    for file in files:
                        
                        file = str(file)
                        mang_file = ''
                        for i in range(len(file)):
                            if file[i] in mang_so:
                                mang_file = mang_file + str(file[i])

                        if doi_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):

                                if specialName != '':
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+mang_file+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(str(specialName)+mang_file+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+str(specialName)+mang_file+'.'+duoiFile)
                                else:
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+mang_file+'.'+duoiFile+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(mang_file+'.'+duoiFile+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+mang_file+'.'+duoiFile)

                        else:
                            if specialName != '':
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(specialName)+mang_file+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(specialName)+mang_file+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(specialName)+mang_file+'.'+duoiFile)
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+mang_file+'.'+duoiFile+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(mang_file+'.'+duoiFile+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+mang_file+'.'+duoiFile)

                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1

                        

                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_()                    
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)

                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến tên được đổi, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

    
       
    def run_xoa(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        kitucanxoa = self.lineEdit_xoa_kitu.text()
        path = self.duongdan.text()
        count = 1
        gioihan = self.lineEdit_xoa_gioihan.text()
        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            try:
                for file in files:
                    file = str(file)
                    
                    if xoa_gioihan == True:
                        if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                            if file.find(str(kitucanxoa)) != -1:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(kitucanxoa),'')+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file.replace(str(kitucanxoa),'')+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file.replace(str(kitucanxoa),''))
                    else:
                        if file.find(str(kitucanxoa)) != -1:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(kitucanxoa),'')+']\n')
                            with io.open('before.txt','a+', encoding='utf-8') as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(file.replace(str(kitucanxoa),'')+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+file.replace(str(kitucanxoa),''))

                    self.progressBar.setProperty("value", round(count*100/len(files)))
                    QApplication.processEvents()
                    count = count + 1

                f.close()
                done = QMessageBox()
                done.setWindowTitle('Hoàn Tất')
                done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                done.setIcon(QMessageBox.Information)
                x = done.exec_() 
                if len(files) == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra, thư mục rỗng')
                    msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)
            except Exception:
                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Có lỗi liên quan đến tên tệp sau khi xóa, vui lòng thử lại')
                msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
                self.progressBar.setProperty("value", 0)



    def run_them(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        path = self.duongdan.text()
        kituthem = self.lineEdit_them_kitu.text()
        count = 1
        gioihan = self.lineEdit_them_gioihan.text()

        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        else:
            if vitriType == 'dau':

                try:
                    for file in files:
                        file = str(file)
                        
                        if them_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(kituthem)+file+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(str(kituthem)+file+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+str(kituthem)+file)
                        else:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+str(kituthem)+file+']\n')
                            with io.open('before.txt','a+', encoding='utf-8',) as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(str(kituthem)+file+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+str(kituthem)+file)

                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1

                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến kí tự được thêm hoặc lỗi không xác định liên quan đến vị trí thêm đầu, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

            elif vitriType == 'cuoi':
                try:
                    for file in files:
                        file = str(file)
                        
                        if them_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file+str(kituthem)+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file+str(kituthem)+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file+str(kituthem))
                        else:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file+str(kituthem)+']\n')
                            with io.open('before.txt','a+', encoding='utf-8') as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(file+str(kituthem)+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+file+str(kituthem))

                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1

                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến kí tự được thêm hoặc lỗi không xác định liên quan đến vị trí thêm cuối, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

            else:
                try:
                    cach_n = self.spinBox_them_tuychinh.text()
                    tinh_tu = self.comboBox_them_tuychinh.currentText()
                    if tinh_tu == 'vị trí đầu':
                        for file in files:
                            file = str(file)
                            
                            if them_gioihan == True:
                                if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)])
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)]+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(cach_n)]+str(kituthem)+file[int(cach_n):len(file)])

                            self.progressBar.setProperty("value", round(count*100/len(files)))
                            QApplication.processEvents()
                            count = count + 1
                        done = QMessageBox()
                        done.setWindowTitle('Hoàn Tất')
                        done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                        done.setIcon(QMessageBox.Information)
                        x = done.exec_() 
                        if len(files) == 0:
                            msg = QMessageBox()
                            msg.setWindowTitle('Lỗi')
                            msg.setText('Có lỗi xảy ra, thư mục rỗng')
                            msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                            self.progressBar.setProperty("value", 0)
                    else:
                        for file in files:
                            file = str(file)
                            
                            if them_gioihan == True:
                                if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                    with io.open('logs.txt','a+', encoding='utf-8') as f:
                                        f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+']\n')
                                    with io.open('before.txt','a+', encoding='utf-8') as f:
                                        f.write(file+'\n')
                                    with io.open('after.txt','a+', encoding='utf-8') as f:
                                        f.write(file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+'\n')
                                    f.close()
                                    os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)])
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)]+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(cach_n)]+str(kituthem)+file[int(len(file))-int(cach_n):len(file)])
                            self.progressBar.setProperty("value", round(count*100/len(files)))
                            QApplication.processEvents()
                            count = count + 1
                        f.close()
                        done = QMessageBox()
                        done.setWindowTitle('Hoàn Tất')
                        done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                        done.setIcon(QMessageBox.Information)
                        x = done.exec_() 
                        if len(files) == 0:
                            msg = QMessageBox()
                            msg.setWindowTitle('Lỗi')
                            msg.setText('Có lỗi xảy ra, thư mục rỗng')
                            msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                            self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến kí tự được thêm hoặc lỗi không xác định liên quan đến vị trí thêm tùy chỉnh, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)


        

    def run_doiduoi(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        path = self.duongdan.text()
        doi = kituthem = self.lineEdit_doi_doi.text()
        doithanh = self.lineEdit_doi_doithanh.text()
        count=1

        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        else:
            if doi == '' and doithanh == '':

                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Không thể để trống cả 2 ô!')
                msg.setIcon(QMessageBox.Warning)

                x = msg.exec_()
            else:

                try:

                    for file in files:
                        
                        file = str(file)
                        if file[len(file)-len(doi):len(file)] == str(doi):
                            
                            if doi != '':
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(len(doi))]+doithanh+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(len(file))-int(len(doi))]+doithanh+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(len(doi))]+doithanh)
                            else:
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file[0:int(len(file))-int(len(doi))]+'.'+doithanh+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file[0:int(len(file))-int(len(doi))]+'.'+doithanh+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file[0:int(len(file))-int(len(doi))]+'.'+doithanh)
                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1
                    f.close()
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)
                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến cách đặt phần mở rộng, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)

    def run_thay(self):
        self.pushButton_undo.setEnabled(True)
        with io.open('before.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        with io.open('after.txt','w+', encoding='utf-8') as f:
            pass
        f.close()
        gioihan = self.lineEdit_thay_gioihan.text()
        thay = self.lineEdit_thay_thay.text()
        thay_thanh = self.lineEdit_thay_thanh.text()
        path = self.duongdan.text()
        count = 1

        try:
            files = os.listdir(path)
        except Exception:
            msg = QMessageBox()
            msg.setWindowTitle('Lỗi')
            msg.setText('Địa chỉ tệp không chính xác')
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

        else:

            if thay != '':

                try:
                    for file in files:
                        file = str(file)
                        if thay_gioihan == True:
                            if file[len(file)-len(gioihan):len(file)] == str(gioihan):
                                with io.open('logs.txt','a+', encoding='utf-8') as f:
                                    f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(thay),str(thay_thanh))+']\n')
                                with io.open('before.txt','a+', encoding='utf-8') as f:
                                    f.write(file+'\n')
                                with io.open('after.txt','a+', encoding='utf-8') as f:
                                    f.write(file.replace(str(thay),str(thay_thanh))+'\n')
                                f.close()
                                os.rename(path+'\\'+file,path+'\\'+file.replace(str(thay),str(thay_thanh)))
                        else:
                            with io.open('logs.txt','a+', encoding='utf-8') as f:
                                f.write(f'{datetime.now()}: Đổi [{file}] -> ['+file.replace(str(thay),str(thay_thanh))+']\n')
                            with io.open('before.txt','a+', encoding='utf-8') as f:
                                f.write(file+'\n')
                            with io.open('after.txt','a+', encoding='utf-8') as f:
                                f.write(file.replace(str(thay),str(thay_thanh))+'\n')
                            f.close()
                            os.rename(path+'\\'+file,path+'\\'+file.replace(str(thay),str(thay_thanh)))
                        self.progressBar.setProperty("value", round(count*100/len(files)))
                        QApplication.processEvents()
                        count = count + 1
                    done = QMessageBox()
                    done.setWindowTitle('Hoàn Tất')
                    done.setText(f'Đã thay đổi thành công {len(files)} tệp')
                    done.setIcon(QMessageBox.Information)
                    x = done.exec_() 
                    if len(files) == 0:
                        msg = QMessageBox()
                        msg.setWindowTitle('Lỗi')
                        msg.setText('Có lỗi xảy ra, thư mục rỗng')
                        msg.setInformativeText(f'Địa chỉ thư mục hiện tại: {path}')
                        msg.setIcon(QMessageBox.Warning)
                        x = msg.exec_()
                        self.progressBar.setProperty("value", 0)

                except Exception:
                    msg = QMessageBox()
                    msg.setWindowTitle('Lỗi')
                    msg.setText('Có lỗi xảy ra liên quan đến cách đặt tên thay thế, vui lòng thử lại')
                    msg.setInformativeText(f'Lỗi tại tệp: {file} - Đã đổi {count-1}/{len(files)}')
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
                    self.progressBar.setProperty("value", 0)
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Lỗi')
                msg.setText('Tên thay thế không được để trống!')
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()


    def run_doiten_xemtruoc(self):
        specialName = self.lineEdit_doiten_ktdt.text()
        startFrom = int(self.spinBox_doiten.text())
        duoiFile = self.lineEdit_doiten_duoi.text()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        if duoiFile == '':
            self.lineEdit_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: " + str(specialName) + str(startFrom) + str(duoiFile)+ ", " + str(specialName) + str(startFrom+1) + str(duoiFile) +", ..."))
        else:
            self.lineEdit_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: " + str(specialName) + str(startFrom)+"." + str(duoiFile)+ ", " + str(specialName) + str(startFrom+1) + "."+ str(duoiFile) +", ..."))


    def run_xoa_xemtruoc(self):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        kitucanxoa = self.lineEdit_xoa_kitu.text()
        self.lineEdit_xoa_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: "+str(kitucanxoa)+"abcdef.xyz ---> abcdef.xyz"))
       

    def run_them_xemtruoc(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        kituthem = self.lineEdit_them_kitu.text()
        if vitriType == 'dau':
            self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef.xyz ---> "+str(kituthem)+"abcdef.xyz"))
        elif vitriType == 'cuoi':
           self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef.xyz ---> abcdef.xyz"+str(kituthem))) 
        else:
            self.lineEdit_them_xemtruoc.setPlaceholderText(_translate("Venamer", "Không có bản xem trước")) 

        

    def run_doiduoi_xemtruoc(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        doi = kituthem = self.lineEdit_doi_doi.text()
        doithanh = self.lineEdit_doi_doithanh.text()
        if doi != '' and doithanh != '':
            self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef."+str(doi)+" ---> abcdef."+str(doithanh)))
        elif doi != '' and doithanh == '':
            self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef."+str(doi)+" ---> abcdef"))
        elif doi == '' and doithanh != '':
            self.lineEdit_doi_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: abcdef ---> abcdef."+str(doithanh)))
    def run_thay_xemtruoc(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Venamer", "Venamer"))
        thay = self.lineEdit_thay_thay.text()
        thay_thanh = self.lineEdit_thay_thanh.text()
        self.lineEdit_thay_xemtruoc.setPlaceholderText(_translate("Venamer", "tệp sẽ có dạng: "+str(thay)+"abcdef.xyz ---> "+str(thay_thanh)+"abcdef.xyz"))


###########################################################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Venamer()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())