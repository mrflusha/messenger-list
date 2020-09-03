import pymysql.cursors,pymysql.err
import sys



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

z = ","
all_db = db_group_voice_chat+z+db_voice_messages+z+db_support_os+z+db_support_video






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








try:
    conn = pymysql.connect(host='',user = '', password='',db='',cursorclass=pymysql.cursors.SSCursor)

#соединение с базой
  
 
    with conn.cursor() as cursor:

        print ("connect successful!!")
        conn.autocommit(True)



















#Тестовые запросы к бд, messAll останется так как используется в основном окне
        qFromDB = "SELECT name, manufact, upmax, supos, supvideo, supvs, supgc FROM gb_56105.all_messengers LIMIT 0, 30 ";
        sql = "SELECT messenger_title FROM messenger_name"
        messAll = "SELECT * FROM all_messengers"
        manuf = "SELECT manufactures_title FROM manufactures"



        test_select = "`supos`,`manufact`,`supvs`"
        test_from = "`all_messengers`"


        listchoise =  "SELECT yesorno_title FROM yesorno" 
        listupload =  "SELECT uploadmax_mb FROM uploadmax" 
        supportOS = "SELECT `os_sup_title` FROM `os_sup` LIMIT 0 , 30"


        

#Функция добавления
        def ins_db(in_db, val):
            facepalm = "INSERT INTO " + in_db + " VALUES ('" + val + "')"
            cursor.execute(facepalm)

#Функция удаления
        def del_db(tb_name,tb_id):
            with conn:
                con = conn.cursor()
                facepalm = "DELETE FROM " + tb_name +" WHERE name ='" + tb_id+"'"
                con.execute(facepalm)
            cursor.close()





#Функции взятия списка из базы 

        array = []
        def ex_db(checkdb,array):
            cursor.execute(checkdb)            
            for row in cursor:
                array.append(row [0])
            return array

        def exe_ALL(checkdb,array):
            cursor.execute(checkdb)
            for row in cursor:
                array.append(row)
            return array

#SELECT
     
        def max_upload(db_where, db_array):
            db_string = "SELECT " + db_upload_max + " FROM " + db_messengers_forQ + " WHERE name = '" + db_where + "' "
            cursor = conn.cursor()
            db_array = cursor.execute(db_string)
            
            conn.close()
            return db_array
            


#Функция взятия данных из главной таблицы
        def get_values(currentSelect,currentName, currentMessenger,array):
            rage = str("SELECT "+currentSelect +" FROM " + currentName + " WHERE `name` = '"+ currentMessenger +"' LIMIT 0,30")
            exe_ALL(rage , array)#--Вложеный список
            array = array[0]#--Вложеный список            
            return array


        get_values(test_select,db_messengers_forQ,"Telegram",test_array)
        get_values(db_upload_max,db_messengers_forQ,"Telegram",tg_upload)
        tg_upload = tg_upload[0]


#Вызовы функций
        ex_db(supportOS,operatingSyS)
        ex_db(messAll,array)
        ex_db(manuf,manufact)
        ex_db(listchoise,oneOrZero)
        ex_db(listupload,maxsize)


 

        cursor.close()


except pymysql.err.OperationalError as e:
    print (e)


finally:
    if pymysql.err.OperationalError:
        print(pymysql.err)
        pass
    # Закрыть соединение (Close connection). 
    else:
        cursor.close()   
