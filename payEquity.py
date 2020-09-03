import sys
import os
import sqlite3
import cerberus
import string
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from payEquityEditorUI import Ui_MainWindow
from jobIDexist import Ui_Dialog
from loginDialog import Ui_loginDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButtonUpdatePayScale.clicked.connect(self.SavePayScale)
        self.ui.pushButtonFetchJobDescription.clicked.connect(self.fetchJobDescription)
        self.ui.pushButtonCreateJobDescription.clicked.connect(self.createJobDescription)

        
    #def fetchPayScale(self):

    def updateJobDescription(self):
        jobID = self.ui.entryJobID.text()
        jobTitle = self.ui.entryJobTitle.text()
        payScaleID = self.ui.entryPayScaleID_2.text()
        jobDescriptionResponsabilities = self.ui.entryJobDescriptionResponsabilities.toPlainText()
        jobLevel = self.ui.entryJobLevel.text()
        jobLevelCode = self.ui.entryJobLevelCode.text()
        L1Manager = self.ui.entryFirstLevelManager.text()
        businessUnit = self.ui.entryBusinessUnit.text()
        functionUnit = self.ui.entryFunctionUnit.text()
        isUnionisable = self.ui.isUnionisable.isChecked()
        jobDescriptionQualifications = self.ui.entryJobDescriptionQualifications.toPlainText()
        jobDescriptionWorkingConditions = self.ui.entryJobDescriptionWorkingConditions.toPlainText()        
        sql_query = """UPDATE jobDescriptionTable 
        SET 
        jobTitle = ?, 
        jobLevel = ?, 
        jobLevelCode = ?, 
        L1Manager = ?, 
        businessUnit = ?, 
        functionUnit = ?, 
        isUnionisable = ?, 
        jobDescriptionResponsabilities = ?, 
        jobDescriptionQualifications = ?, 
        jobDescriptionWorkingConditions = ?
        WHERE
        jobID = ?;"""
        keyValues = [jobTitle, payScaleID, jobLevel, jobLevelCode, L1Manager, businessUnit, functionUnit, isUnionisable, jobDescriptionResponsabilities, jobDescriptionQualifications, jobDescriptionWorkingConditions, jobID]
        self.curr.execute(sql_query, (keyValues,))
    def fetchJobDescription(self):
        jobID = str(self.ui.entryJobID.text())
        
        sql_select_query_first_check = """select jobID from jobDescriptionTable where jobID = ?"""
        sql_query_fill = """select jobTitle, jobLevel, jobLevelCode, L1Manager, businessUnit, functionUnit, isUnionisable, jobDescriptionResponsabilities, jobDescriptionQualifications, jobDescriptionWorkingConditions from jobDescriptionTable where jobID = ?"""
        
        
        self.curr.execute(sql_query_fill, (jobID,))
        queryResult = self.curr.fetchone()
        self.ui.entryJobTitle.setText(str(queryResult[0]))
        self.ui.entryJobLevel.setText(str(queryResult[1]))
        self.ui.entryJobLevelCode.setText(str(queryResult[2]))
        self.ui.entryFirstLevelManager.setText(str(queryResult[3]))
        self.ui.entryBusinessUnit.setText(str(queryResult[4]))
        self.ui.entryFunctionUnit.setText(str(queryResult[5]))
        self.ui.isUnionisable.setChecked(bool(queryResult[6]))
        self.ui.entryJobDescriptionResponsabilities.setPlainText(str(queryResult[7]))
        self.ui.entryJobDescriptionQualifications.setPlainText(str(queryResult[8]))
        self.ui.entryJobDescriptionWorkingConditions.setPlainText(str(queryResult[9]))
        
    def createJobDescription(self):
        self.jobIDExist()
                    
        if self.jobIDexist == None:
            jobID = self.ui.entryJobID.text()
            jobTitle = self.ui.entryJobTitle.text()
            payScaleID = self.ui.entryPayScaleID_2.text()
            jobDescriptionResponsabilities = self.ui.entryJobDescriptionResponsabilities.toPlainText()
            jobLevel = self.ui.entryJobLevel.text()
            jobLevelCode = self.ui.entryJobLevelCode.text()
            L1Manager = self.ui.entryFirstLevelManager.text()
            businessUnit = self.ui.entryBusinessUnit.text()
            functionUnit = self.ui.entryFunctionUnit.text()
            isUnionisable = self.ui.isUnionisable.isChecked()
            jobDescriptionQualifications = self.ui.entryJobDescriptionQualifications.toPlainText()
            jobDescriptionWorkingConditions = self.ui.entryJobDescriptionWorkingConditions.toPlainText()
            
            values = [jobID, jobTitle, payScaleID, jobLevel, jobLevelCode, L1Manager, businessUnit, functionUnit, isUnionisable, jobDescriptionResponsabilities, jobDescriptionQualifications, jobDescriptionWorkingConditions]
            self.curr.execute("INSERT INTO jobDescriptionTable (jobID, jobTitle, payScaleID, jobLevel, jobLevelCode, L1Manager, businessUnit, functionUnit, isUnionisable, jobDescriptionResponsabilities, jobDescriptionQualifications, jobDescriptionWorkingConditions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
                    
            self.conn.commit()
        if self.jobIDexist != None:
           self.dialog = jobIDexistDialog()
           self.dialog.show()
           
               
        self.ui.entryJobID.clear()
        self.ui.entryJobTitle.clear()
        self.ui.entryPayScaleID.clear()
        self.ui.entryJobLevel.clear()
        self.ui.entryJobLevelCode.clear()
        self.ui.entryFirstLevelManager.clear()
        self.ui.entryBusinessUnit.clear()
        self.ui.entryFunctionUnit.clear()
        self.ui.isUnionisable.setCheckState(False)
        self.ui.entryJobDescriptionWorkingConditions.clear()
        self.ui.entryJobDescriptionQualifications.clear()
        self.ui.entryJobDescriptionResponsabilities.clear()
        
    def connectSQL(self):
        
        dataBaseName = "payEquityDataBase.sqlite3"
        self.conn = sqlite3.connect(dataBaseName)
        self.curr = self.conn.cursor()
       
    def executeSQL(self):
        
        self.command = "INSERT INTO"
        self.table = "jobDescriptionTable"
        self.curr.execute()
        self.conn.commit()

    def jobIDExist(self):
        jobID = self.ui.entryJobID.text()
        
        sql_select_query = """select jobID from jobDescriptionTable where jobID = ?"""
        self.curr.execute(sql_select_query, (jobID,))
        
        self.jobIDexist = self.curr.fetchone()
        
                    
        self.conn.commit()
        

class jobIDexistDialog(QDialog):
    def __init__(self):
        super(jobIDexistDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
"""class loginDialog(Qdialog):
    def __init__(self):
        super(loginDialog, self).__init__()
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)"""
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    #login = loginDialog()
    #login.show()
    window = MainWindow()
    window.connectSQL()
    window.show()

    sys.exit(app.exec_())