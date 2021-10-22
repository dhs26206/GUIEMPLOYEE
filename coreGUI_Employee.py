
import PySimpleGUI as sg
import time
import pickle as pick
import random
import os
import pygame
import threading
show_name = '               '
show_gender = '              '
show_BasicPay = '             '
show_Martial = '               '
show_Post = '                 '
show_Rank = '                  '
contine = 1
contines = 5
themes = sg.theme_list()
musicstop = 1






lay1 = [[sg.Text('Username :'),sg.InputText()],[sg.Text('Password'),sg.InputText(password_char='*')],[sg.Button('Submit'),sg.Button('Exit')]]
welcome = sg.Window('Log In',lay1)
while True:
    event,values = welcome.read()

    if event == 'Submit':

        if values[0] == 'ddks' and values[1]=='kumar':
            contines = 1
            for i in range(400000):
                sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)
            sg.PopupAnimated(None)
            welcome.close()
        else:
            sg.Popup('INVALID USERNAME AND PASSWORD !',keep_on_top = True)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        contine = 0
        welcome.close()
        break
        
welcome.close()

def New(X):
    try:
        db = open('data97506.txt','rb')
        E =  pick.load(db)
        db.close()
    except:
        E = []
    E.append(X)
    db = open('data97506.txt','wb')
    pick.dump(E,db)
    db.close()

def Show(V):
    db = open('data97506.txt','rb')
    E = pick.load(db)
    db.close()
    Emp_no = []
    for i in range(len(E)):
        Emp_no.append(E[i][6])
    if Emp_no.count(int(V)) == 1:
        ind = Emp_no.index(int(V))
        show_name = E[ind][0]
        show_gender = E[ind][1]
        show_BasicPay = E[ind][2]
        show_Martial = E[ind][3]
        show_Post = E[ind][4]
        show_Rank = E[ind][5]
        return [show_name,show_gender,show_BasicPay,show_Martial,show_Post,show_Rank]
    else:
        return False
                          

def Check(G):
    db = open('data97506.txt','rb')
    E = pick.load(db)
    db.close()
    Emp_no = []
    for i in range(len(E)):
        Emp_no.append(E[i][6])
    
    if Emp_no.count(int(G))==0:
        return True
    else:
        return False
def Delota(Y):
    db = open('data97506.txt','rb')
    E = pick.load(db)
    db.close()
    Emp_no = []
    for i in range(len(E)):
        Emp_no.append(E[i][6])
    if Emp_no.count(int(Y)) == 1:
        T = Emp_no.index(int(Y))
        del E[T]
        db = open('data97506.txt','wb')
        pick.dump(E,db)
        db.close()
        dr = open('data534609.txt','rb')
        T = pick.load(dr)
        dr.close()
        for k in T:
            if k[0] == int(Y):
                h = T.index(k)
                del T[h]
        dk = open('data534609.txt','wb')
        pick.dump(T,dk)
        dk.close()
        return True
    else:
        return False

def Sal(A,B,C):
    if C == 'A':
        d = 10000
    if C == 'B':
        d = 6000
    if C == 'C':
        d = 3000
    if C == 'D':
        d = 1500
    TY = [int(A),C,int(B),int(d),0]
    dr = open('data534609.txt','rb')
    R = pick.load(dr)
    dr.close()
    R.append(TY)
    dr = open('data534609.txt','wb')
    pick.dump(R,dr)
    dr.close()

def SAL(A,B,C):
    dr = open('data534609.txt','rb')
    R = pick.load(dr)
    dr.close()
    
    UY = []
    
    kj = len(R)
    hn = []
    
    for list in R:
        if list[1] == str(A):
            UY.append(list)
            y = R.index(list)
            hn.append(list)
    
    for k in hn:
        R.remove(k)
       
    
    if B == 'P':
        for i in range(len(UY)):
            ck = UY[i][2]
            ck = ck + (ck/100)*int(C)
            UY[i][2] = ck
    if B == 'M':
        for i in range(len(UY)):
            ck = UY[i][2]
            ck = ck + int(C)
            UY[i][2] = ck

    for i in range(len(UY)):
        R.append(UY[i])

    dr = open('data534609.txt','wb')
    pick.dump(R,dr)
    dr.close()
    db = open('data97506.txt','rb')
    T = pick.load(db)
    db.close()
    TR = []
    for i in range(len(T)):
        if T[i][5] == A:
            if B == 'P':
                hkg = int(T[i][2])
                hkg = hkg + int((h/100)*int(C))
                T[i][2] = hkg
            if B == 'M':
                hkg = int(T[i][2])
                hkg = hkg + int(C)
                T[i][2] = hkg
    db = open('data97506.txt','wb')
    pick.dump(T,db)
    db.close()
                

def SAN(T):
    dr = open('data534609.txt','rb')
    R = pick.load(dr)
    dr.close()
    for i in range(len(R)):
        if R[i][0] == int(T):
            a = R[i][2]
            b = R[i][3]
            c = R[i][4]
            d = ''
            return a,b,c,d

def SALARYCHANGER(B):
    if Check(int(B))== True:
        return 'tghj@re'
    if Check(int(B))== False:
        dr = open('data534609.txt','rb')
        GH = pick.load(dr)
        dr.close()
        x,y,z,k = SAN(B)
        return z

def SALARYUPDATER(T,I):
    dr = open('data534609.txt','rb')
    YU= pick.load(dr)
    dr.close()
    for list in YU:
        if list[0] == int(T):
            list[4] = int(I)
    dr = open('data534609.txt','wb')
    pick.dump(YU,dr)
    dr.close()
    return True


def About():
    dr= open('about67894','rb')
    I = pick.load(dr)
    dr.close()
    return I

I = About()

def ThemeReader():
    dr = open('mcsr3','rb')
    j = pick.load(dr)
    dr.close()
    J = j[0]
    return J
def ThemeChanger(U):
    dr = open('mcsr3','wb')
    pick.dump(U,dr)
    dr.close()

sg.theme(ThemeReader())
    
        
    
def Music():    
    path = 'Music'
    files = os.listdir(path)
    d = random.choice(files)
    List = []
    s = 'Music\\'+d
    pygame.mixer.init()
    pygame.mixer.music.load(s)
    pygame.mixer.music.play()
    
Music()

def Another():
    while musicstop == 1:
        time.sleep(3)
        if pygame.mixer.music.get_busy():
            pass
        else:
            pygame.time.Clock().tick(5)
            Music()
    if musicstop == 2:
        pygame.mixer.music.stop()

t1 = threading.Thread(target= Another,name='background')
t1.start()



main_tab1 = [[sg.T(' New Employee')],[sg.Text('Name of the Employee :'),sg.InputText(key='-NAME-')],
             [sg.Radio('Male',"GENDER",key='-GEN-'),sg.Radio('Female',"GENDER")],
             [sg.Text('Basic Pay'),sg.InputText(key='-PAY-')],
             [sg.Text('Martial Status'),sg.Radio('Married',"MAR",key='-MAR1-'),sg.Radio('UnMarried',"MAR",key='-MAR2-'),sg.Radio('Other',"MAR",key='-MAR3-')],
             [sg.Text('Post of the Employee'),sg.InputText(key='-POST-')],
             [sg.Text('Group of Rank'),sg.Radio('Group:A',"RANK",key='-GRA-'),sg.Radio('Group:B',"RANK",key='-GRB-'),sg.Radio('GROUP:C',"RANK",key='-GRC-'),sg.Radio('GROUP:D',"RANK",key='-GRD-')],
             [sg.Button('Submit')]]

main_tab2 = [[sg.T('Editing Details')],[sg.Text('Enter the Index Number of the Employee :'),sg.InputText(key='-EDITEMP-'),sg.Button('Search Employee')],
             [sg.Text('',key='-LOAD-')],
             [sg.Text('____________________________________________________________________________')],
             [sg.Text('Name'),sg.InputText(key='-UP_NAME-')],
             [sg.Radio('Male',"GENDER_UP",key='-GEN_UP-'),sg.Radio('Female',"GENDER_UP",key='-GENE_DUP-')],
             [sg.Text('Basic Pay'),sg.InputText(key='-PAY_UP-')],
             [sg.Text('Martial Status'),sg.Radio('Married',"MAR_UP",key='-MAR1_UP-'),sg.Radio('UnMarried',"MAR_UP",key='-MAR2_UP-'),sg.Radio('Other',"MAR_UP",key='-MAR3_UP-')],
             [sg.Text('Post of the Employee'),sg.InputText(key='-POST_UP-')],
             [sg.Text('Group of Rank'),sg.Radio('Group:A',"RANK_UP",key='-GRA_UP-'),sg.Radio('Group:B',"RANK_UP",key='-GRB_UP-'),sg.Radio('GROUP:C',"RANK_UP",key='-GRC_UP-'),sg.Radio('GROUP:D',"RANK_UP",key='-GRD_UP-')],
             [sg.Text('_____________________________________________________________________________')],
             [sg.Text('MAKE SURE TO COLLECT VALID PROOF FOR THE CORRECTION DONE IN EMPLOYEE \'S DETAILS')],
             [sg.Button('Edit')]]

main_tab3 = [[sg.T('Deleting Employee')],
             [sg.Text('Enter the Index Number of the Employee'),sg.InputText(key='-DELEMP-'),sg.Button('Show Details')],
             [sg.Text('',key='-LOAD1-')],
             [sg.Text('Name of the Employee :'),sg.Text('                                   ',key = '-DEL_N-')],
             [sg.Text('Rank :'),sg.Text('       ',key = '-DEL_R-')],
             [sg.Text('Post of the Employee :'),sg.Text('                                  ',key = '-DEL_P-')],
             [sg.Text('')],
             [sg.Text('')],
             [sg.Button('Delete This Employee')]]


             
main_layout=[[sg.TabGroup([[sg.Tab('Entering Details of Employee',main_tab1)],
                           [sg.Tab('Editing Details of Employee',main_tab2)],
                           [sg.Tab('Deleting Employee',main_tab3)]]),sg.Button('Advanced')],[sg.Button('Settings & Help')]]
def advancecr():
    advancelay1=[[sg.T('Salary Incrementor')],
                 [sg.Text('Please Select the Group')],
                 [sg.Radio('Group:A',"GRP",key = 'GRA'),sg.Radio('Group:B',"GRP",key='GRB'),sg.Radio('Group:C',"GRP",key='GRC'),sg.Radio('Group:D',"GRP",key='GRD')],
                 [sg.Text('Salary Increase Criteria :'),sg.Radio('By Percentage(%)',"CHH",key='%'),sg.Radio('Manual Increase(in Rupees)',"CHH",key='Rs')],
                 [sg.Text('By How Much :'),sg.InputText('',key='INC')],
                 [sg.Text()],
                 [sg.Button('Increase')]]
    salarylay=[[sg.T('Salary Overview')],
               [sg.Text('Enter Employee Number'),sg.InputText(key='EMPSAL'),sg.Button('Show')],
               [sg.Text('Name of the Employee'),sg.Text('                       ',key='EMPSAN')],
               [sg.Text('Basic Pay'),sg.Text('              ',key='BPSAL')],
               [sg.Text('Grade Pay'),sg.Text('               ',key='GPSAL')],
               [sg.Text('AOW Pay'),sg.Text('                  ',key='AOWSAL')],
               [sg.Text('Total Salary Payable :'),sg.Text('                    ',key='TSSAL')]]

    emplay1 = [[sg.T('Special Employee Salary Changer')],
               [sg.Text('Enter Employee Number :'),sg.InputText(key='EMPSAL1'),sg.Button('Search')],
               [sg.Text('Name of the Employee : '),sg.Text('                         ',key = 'RTYU')],
               [sg.Text('AOW Pay'),sg.InputText(key='AOWSAL1')],
               [sg.Text()],
               [sg.Text()],
               [sg.Button('Update')]]

    advance1 = [[sg.TabGroup([[sg.Tab('Bulk Salary Incrementor',advancelay1)],
                           [sg.Tab('Salary Over View',salarylay)],
                           [sg.Tab('Employee Salary Changer',emplay1)]])]]
    return advance1

def settingcr():
    setting1 = [[sg.T('SETTING')],
                [sg.Text()],
                [sg.Text('___________________________________________________')],
                [sg.Text('Change Theme :'),sg.Listbox(themes,size=(20,4),enable_events = True,key='-THEME-'),sg.Button('Apply Theme')],
                [sg.Text()],
                [sg.Text('___________________________________________________')],
                [sg.Text('Add Sound while you work :')],
                [sg.Text('To Play  Music while playing \n Simply Copy the music file in the Music Folder')]]
    about = [[sg.T('About this Application')],
             [sg.Text(I)]]
    rtyu = [[sg.TabGroup([[sg.Tab('SETTING',setting1)],
                      [sg.Tab('About this Application',about)]])]]
    return rtyu

                    
         
            
            
             
              
              


main_window = sg.Window('Employee Data Management',main_layout)

while True :
    if contine == 0 and contines != 1:
        break
    event,values = main_window.read()
    if event == 'Submit':
        a = values['-NAME-']
        if values['-GEN-'] == True:
            b = 'M'
        else:
            b = 'F'
        d = int(values['-PAY-'])
        if values['-MAR1-'] == True:
            e = 'M'
        if values['-MAR2-'] == True:
            e = 'NM'
        if values['-MAR3-'] == True:
            e = 'OTH'
        f = values['-POST-']
        if values['-GRA-'] == True:
            g = 'A'
        if values['-GRB-'] == True:
            g = 'B'
        if values['-GRC-'] == True:
            g = 'C'
        if values['-GRD-'] == True:
            g = 'D'
        h = random.randint(1000,9999)
        while Check(h) == 'true':
            h = random.randint(1000,9999)
            
        ZX = [a,b,d,e,f,g,h]
        sg.Popup('The Employee Number of this Employee is :',h,'\n Please Tell this to Employee and memorise it')
        New(ZX)
        Sal(h,d,g)
    if event == 'Search Employee':
        if values['-EDITEMP-'].isnumeric() == True:
            XV = Show(values['-EDITEMP-'])
            if XV == False:
                sg.Popup('Employee Doesn\'t Exist')
            else:
                main_window['-UP_NAME-'].update(XV[0])
                if XV[1] == 'M':
                    main_window['-GEN_UP-'].update(True)
                else:
                    main_window['-GENE_DUP-'].update(True)
                main_window['-PAY_UP-'].update(XV[2])
                if XV[3] == 'M':
                    main_window['-MAR1_UP-'].update(True)
                if XV[3] == 'NM':
                    main_window['-MAR2_UP-'].update(True)
                if XV[3] == 'OTH':
                    main_window['-MAR3_UP-'].update(True)
                main_window['-POST_UP-'].update(XV[4])
                if XV[5] == 'A':
                    main_window['-GRA_UP-'].update(True)
                if XV[5] == 'B':
                    main_window['-GRB_UP-'].update(True)
                if XV[5] == 'C':
                    main_window['-GRC_UP-'].update(True)
                if XV[5] == 'D':
                    main_window['-GRD_UP-'].update(True)
            
    if event == 'Edit':
        a = values['-UP_NAME-']
        if values['-GEN_UP-'] == True:
            b = 'M'
        else:
            b = 'F'
        d = int(values['-PAY_UP-'])
        if values['-MAR1_UP-'] == True:
            e = 'M'
        if values['-MAR2_UP-'] == True:
                e = 'NM'
        if values['-MAR3_UP-'] == True:
            e = 'OTH'
        f = values['-POST_UP-']
        if values['-GRA_UP-'] == True:
            g = 'A'
        if values['-GRB_UP-'] == True:
            g = 'B'
        if values['-GRC_UP-'] == True:
            g = 'C'
        if values['-GRD_UP-'] == True:
            g = 'D'
        h = int(values['-EDITEMP-'])
        ZV = [a,b,d,e,f,g,h]
        
        Delota(h)
        
        New(ZV)
        Sal(h,d,g)
        sg.Popup('Details Updated Successfully')
    if event == 'Show Details':
        if values['-DELEMP-'].isnumeric() == True:
            R = Show(values['-DELEMP-'])
            if R == False:
                sg.Popup('Employee Doesn\'t Exist',auto_close = True, auto_close_duration=1.5)
            else:
                main_window['-DEL_N-'].update(R[0])
                main_window['-DEL_R-'].update(R[5])
                main_window['-DEL_P-'].update(R[4])
    if event == 'Delete This Employee':
        sg.Popup('Make Sure to collect Resign Application and NOC with the Concerned Authority')
        time.sleep(4)
        if Delota(values['-DELEMP-'])== True:
                    
            sg.Popup('Employee Record Deleted Successfully')
        else:
            sg.Popup('Enter the Index Number !')
    if event == sg.WIN_CLOSED:
        musicstop = 2
        sg.Popup('Log Out Successfully')
        main_window.close()
        break

    if event == 'Advanced':
        advance12 = advancecr()
        advance = sg.Window('Advanced',advance12)
        while True:
            event,values = advance.read()
            if event == sg.WIN_CLOSED:
                advance.close()
                break
            if event == 'Increase':
                if values['GRA']== True:
                    a = 'A'
                if values['GRB']== True:
                    a= 'B'
                if values['GRC']== True:
                    a = 'C'
                if values['GRD']== True:
                    a = 'D'
                if values['%'] == True:
                    b = 'P'
                if values['Rs'] == True:
                    b = 'M'
                c = values['INC']
                sg.Popup('Remember to take Increment Order from Concerned Authority\n Starting Action in 4 seconds !',keep_on_top = True)
                time.sleep(4)
                for i in range(200000):
                    sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)
                SAL(a,b,c)
                sg.PopupAnimated(None)
                sg.Popup('Salary Updated Successfully !')

            if event == 'Show':
                R = Show(values['EMPSAL'])
                if R == False:
                    sg.Popup('Employee Doesn\'t Exist')
                else:
                    a = R[0]
                    advance['EMPSAN'].update(a)
                    T,Y,Z,X = SAN(int(values['EMPSAL']))
                    advance['BPSAL'].update(T)
                    advance['GPSAL'].update(Y)
                    advance['AOWSAL'].update(Z)
                    advance['TSSAL'].update(int(T)+int(Y)+int(Z))

            if event == 'Search':
                y = SALARYCHANGER(int(values['EMPSAL1']))
                yo = SALARYCHANGER(int(values['EMPSAL1']))
                if yo == 'tghj@re':
                    sg.Popup('Employee doesn\'t Exist')
                if yo != 'tghj@re':
                    Y = Show(int(values['EMPSAL1']))
                    advance['AOWSAL1'].update(y)
                    advance['RTYU'].update(Y[0])
            if event == 'Update':
                if int(values['EMPSAL1']) == None or False:
                    sg.Popup('Please Enter the Employee Number')
                else:
                    jk = int(values['EMPSAL1'])
                    n = int(values['AOWSAL1'])
                    if SALARYUPDATER(jk,n) == True:
                        sg.Popup('Employee Salary Updated Succesfully !')

    if event == 'Settings & Help':
        rtss = settingcr()
        set_window = sg.Window('Settings & Help',rtss)
        while True:
            e,v = set_window.read()
            if e == 'Apply Theme' :
                if v['-THEME-']== None:
                    pass
                else:
                    z = v['-THEME-']
                    ThemeChanger(z)
                    sg.Popup('Theme will be applied next time \n when you run this Application')

            if e == sg.WIN_CLOSED:
                set_window.close()
                break
      
            
        
        
        
              
        
                    
                   

            
                    
                            
                    
                
                
                    
        
        
        
        
                
            
            
              
                
                
                
            
        
        
     
             
             
            

    
    
    
    

    
    

