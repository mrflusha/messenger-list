import pymysql.cursors
from PyQt5.QtWidgets import QMessageBox as qmb




#Строка бд
#Названия таблиц
db_messengers_forQ = "all_messengers"
db_manufactures_forQ = "manufactures"
db_messengers = "messenger_name"
db_os_forQ = "os_sup"
db_maxupload_forQ = "uploadmax"
db_yesorno_forQ = "yesorno"
#Колонки из главной таблицы
db_group_voice_chat = "supgc"
db_voice_messages = "supvs"
db_support_video = "supvideo"
db_support_os = "supos"
db_upload_max ="upmax"
db_manufacture = "manufact"

zapyaya = ","
all_db = db_group_voice_chat+zapyaya+db_voice_messages+zapyaya+db_support_os+zapyaya+db_support_video
print(all_db)






#Списки



result = []
operatingSyS = []

manufact = []
oneOrZero = []
allin=[]
test_array = []
maxsize = []
db_array = []


tg_upload = []



"""
Сравнить текст из комбобокса с выводом из базы

"""









conn = pymysql.connect(host='yourhost',user = 'youruser', password'yourpassword',db='dbmame',cursorclass=pymysql.cursors.SSCursor)
#соединение с базой
try:
  
 
    with conn.cursor() as cursor:

        print ("connect successful!!")
        conn.autocommit(True)



















#Тестовые запросы к бд, messAll останется так как используется в основном окне
        qFromDB = "SELECT name, manufact, upmax, supos, supvideo, supvs, supgc FROM gb_56105.all_messengers LIMIT 0, 30 ";
        sql = "SELECT messenger_title FROM messenger_name"
        messAll = "SELECT * FROM all_messengers"
        manuf = "SELECT manufactures_title FROM manufactures"


        ye_ne_znau_test_arrayuya = "SELECT supos,manufact  FROM all_messengers WHERE `name`=" +" 'Telegram'"
        test_select = "`supos`,`manufact`,`supvs`"
        test_from = "`all_messengers`"


        listchoise =  "SELECT yesorno_title FROM yesorno" 
        listupload =  "SELECT uploadmax_mb FROM uploadmax" 
        supportOS = "SELECT `os_sup_title` FROM `os_sup` LIMIT 0 , 30"


        

#Функция добавления
        def ins_db(in_db, val):
            facepalm = "INSERT INTO " + in_db + " VALUES ('" + val + "')"
            print(facepalm)
            cursor.execute(facepalm)
        #ins_db("manufactures(manufactures_id,manufactures_title)","(11,'test')")
#Функция удаления
        def del_db(tb_name,tb_id):
            with conn:
                con = conn.cursor()
                facepalm = "DELETE FROM " + tb_name +" WHERE name ='" + tb_id+"'"
                print(facepalm)
                con.execute(facepalm)
                cursor.close()

                #con.close()
        #del_db("manufactures ","manufactures_id = 10")







       # addTodb("test")
         
        # Выполнить команду запроса (Execute Query).
        #cursor.execute(sql)
 
#Функции взятия списка из базы 
        array = []
        def ex_db(checkdb,array):
            cursor.execute(checkdb)

            
            for row in cursor:
              #  print(row)
                array.append(row [0])

                #print (array)
                #print (array)
            return array
            #Test Function RETURN ARRAY [,]
        def exe_ALL(checkdb,array):
            cursor.execute(checkdb)


            for row in cursor:
                array.append(row)
                print("\n", array, "\n")
            return array
#SELECT
     
        def max_upload(db_where, db_array):
            db_string = "SELECT " + db_upload_max + " FROM "+ db_messengers_forQ + " WHERE name = '"+ db_where+"' "
            print(db_string)

            cursor = conn.cursor()

            db_array = cursor.execute(db_string)
            
            conn.close()
            return db_array
            print ("TRUE",db_array)
        #max_upload("Telegram",db_array)
        #db_array=db_array[0][0]
        #print(db_array)
        #print(db_array)




#Функция взятия данных из главной таблицы
        def get_values(currentSelect,currentName, currentMessenger,array):
            rage = str("SELECT "+currentSelect +" FROM " + currentName + " WHERE `name` = '"+ currentMessenger +"' LIMIT 0,30")
            print(rage)
            exe_ALL(rage , array)#--Вложеный список
            array = array[0]#--Вложеный список

            print(currentMessenger,array)
            
            return array


        get_values(test_select,db_messengers_forQ,"Telegram",test_array)
        print (test_array)
        get_values(db_upload_max,db_messengers_forQ,"Telegram",tg_upload)
        print(tg_upload)
        tg_upload = tg_upload[0]
        print(tg_upload)

#Вызовы функций
       # get_values(ye_ne_znau_test_arrayuya,test_array)
        #print("\n", test_array)
        print("\n")
        ex_db(supportOS,operatingSyS)
        print("\noperatingSyS:",operatingSyS,"\n")

        ex_db(sql,result)
        print(result,"\nex")
        ex_db(messAll,array)
        print(array,"\nex")
        ex_db(manuf,manufact)
        print("manufactures =", manufact)
        ex_db(listchoise,oneOrZero)
        print(oneOrZero)
        ex_db(listupload,maxsize)
        print("maxuploadlist : \n",maxsize)
        exe_ALL(qFromDB,allin)
        print("\n\n\t",allin,"\n\n")
        

        #max_upload("Telegram",db_array)
        #print("lol",maxsize[db_array[0][0]])


#        for i in result[2:10]:
#            i=str(i)
#            print(i)
            #ins_db(db_messengers_forQ+"(name)",i)
        #qq=[]
            #db_array = []


                                            
                                     

         
                                #db_array +=(cursor.execute("SELECT uploadmax_mb FROM "+db_upload_max+" WHERE uploadmax_id = "+db_array[0]))



        #max_upload("Telegram", qq)

        
        #print()
       # cursor.execute(messAll)




 #   code, message = error.args
#    qmb.information(self, "Info about "+ import_name, import_name + "\nПроизводитель:"+ import_manufact, QMessageBox.Ok)

#        test_instert = "INSERT INTO manufactures(manufactures_id, manufactures_title) VALUES (" + str((len(manufact))) + ", 'VK')"
#        print (test_instert)
#        cursor.execute(test_instert)
        
 
             
   
finally:


    # Закрыть соединение (Close connection).      
    cursor.close()
    print (qFromDB)
    #test_array = test_array[0]

    print (len(result))
    s = "Telegram"

    
    if array == s:
        print (array[0])
    #print('done...','\n',result,'\n', ebl, "\n", array)


    #print(db_string)
    
    #ex_db(db_string,db_array)
    #print(db_array)
            
#conn.close()        



#    for i in range(len(allin)):
#        print (db_array)
        #print(db_array[0])
#        print(allin[1][1]) 
#        conn.close()


#    for i in range(len(operatingSyS)):
#        print("\n\tBULLSHIT", operatingSyS[i][1])





                    #db_array = listupload[db_array]
                #print (maxsize[db_array[0][0]])
                    #print (db_array)


            

            #print (now)
