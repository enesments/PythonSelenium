#Ogrenci Kayit Sistemi
students=["Enes Mentese","Ekrem Erdem"]
def ShowStudent():
    print("Ögrenci Listesi")
    for student in students:
        print (student)
def AddStudent():
    name = input("Ogrenci adi : ")
    surname = input("Ogrenci Soyadi : ")
    students.append(name +" "+ surname)
    print(name+" " +surname + " listeye eklendi.")
def RemoveStudent():
    name = input("Ogrenci adi : ")
    surname = input("Ogrenci Soyadi : ")
    for student in students:
        if(student==name+" "+surname):
            students.remove(name+" "+surname)
            print(student + " listeden silindi.")
            if (len(students)==0):
                print("Listede öğrenci yok.")
            else:
                ShowStudent()
                break
        else:
            print(name+" "+surname +" adlı kişi listede yok.")
            ShowStudent()
            break
            
def AddMultipleStudents():
    sayi= print(input("Kaç adet öğrenci girmek istediğinizi giriniz."))
    a=0
    while a<sayi:
        name=input(str(a)+"Ogrenci adi : ")
        surname=input(str(a)+"Ogrenci soyadi : ")
        students.append(name +" "+ surname)
        a+=1
        print(sayi+" adet öğrenci eklenmiştir.")
def RemoveMultipleStudents():
    sayi= print(input("Kaç adet öğrenci girmek istediğinizi giriniz."))
    a=0
    while a<sayi:
        name=input(str(a)+"Ogrenci adi : ")
        surname=input(str(a)+"Ogrenci soyadi : ")
        students.remove(name +" "+ surname)
        a+=1
        print(sayi+" adet öğrenci silinmiştir.")
def StudentNo():
   name=input("Öğrenci adi : ")
   surname=input("Ogrenci soyadi : ")
   for i in range (len(students)):
       if students[i]==name+" "+surname:
            no=i
            break 
   SN = StudentNo()
   print(name+" "+surname+f" numarası: {no+1}")



print ("Öğrenci Ekleme: 1\nÖğrenci Silme: 2\nÇoklu Öğrenci Ekleme: 3\nÇoklu Öğrenci Silme: 4\nÖğrenci Numarası Öğrenme: 5\n")
calt=int(input("İstenilen işlem numarasını girin: "))
if(calt==1):
    AddStudent()
elif(calt==2):
    RemoveStudent()
elif(calt==3):
    AddMultipleStudents()
elif(calt==4):
    RemoveMultipleStudents()
elif(calt==5):
    ShowStudent()
else:
    print("Secim yanlış!!!")





       
    
        
     
   

