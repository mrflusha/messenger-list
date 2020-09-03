import pymysql
from time import sleep as freeze


#Названия таблиц
db_messengers_forQ = "all_messengers"
db_manufactures_forQ = "manufactures"
db_messengers = "messenger_name"
db_os_forQ = "os_sup"
db_maxupload_forQ = "uploadmax.id"
db_yesorno_forQ = "yesorno"
#Колонки из главной таблицы
db_group_voice_chat = "supgc"
db_voice_messages = "supvs"
db_support_video = "supvideo"
db_support_os = "supos"
db_upload_max ="upmax"
db_manufacture = "manufact"
db_title = "name"
mf_id="manufactures_id"

z = ","

a = " AND "
w = " WHERE "
o = " OR "

arr = []

refresh_select = "SELECT * FROM all_messengers"

array = []
try:
	db = pymysql.connect(host='',user = '',\
							 password='',\
							 db='',\
							 cursorclass=pymysql.cursors.SSCursor)

	def max_upload(db_where, db_array):
		with db.cursor() as cursor:
			db.autocommit(True)
			db_string = "SELECT " \
								+ db_upload_max+","+db_group_voice_chat+","+db_voice_messages+","+db_support_video+","+db_support_os +","+db_manufacture+ \
								" FROM "+ db_messengers_forQ + \
								" WHERE name = '"+ db_where+"' LIMIT 0,30"
				    
			cursor.execute(db_string)

			for row in cursor:
				db_array.append(row)
		cursor.close()
		return db_array



				    


	def insert_db(db_array,man_value):
		with db.cursor() as cursor:
			db.autocommit(True)			
			db_str = "INSERT INTO " + db_messengers_forQ+\
									"("+db_title+z+db_manufacture+z+db_upload_max+z+db_support_os+z+db_voice_messages+z+db_group_voice_chat+z+db_support_video+")" \
									+ " VALUES "+ db_array 							    
			cursor.execute(db_str)

		cursor.close()
		return db_array

	def ex_sort(value,max_file, array):
		with db.cursor() as cursor:
			arr =[]
			freeze(1)

			sort_str = "SELECT " + db_title + " FROM " + db_messengers_forQ + w + value +" LIMIT 0,30"

			ex_db(sort_str,arr)
			array.append(arr)
		cursor.close()
		return array
		



	def sort_func(vm,os,gc,vc,mf,array):

			array.clear()
			arr.clear()
			voice_messages =  "("+db_voice_messages + " = " + vm + ")"
			group_voice_chat =   "(" + db_group_voice_chat + " = " + gc + ")"
			video_calls =   "("+db_support_video + " = " + vc +")"  
			max_file =  db_upload_max +" <= "+ mf

			ex_sort(voice_messages,max_file,array)
			ex_sort(group_voice_chat,max_file,array)
			ex_sort(video_calls,max_file,array)
			ex_db("SELECT "+db_title+" FROM "+db_messengers_forQ+w+max_file,arr)
			array.append(arr)
			for j in range(len(array)):
				if len(array[j]) == 0:
					array[j].append("Мессенджеры с заданной характеристикой отсутствуют в базе")


			
			
			return array


	def ex_db(checkdb,array):
		with db.cursor() as cursor:
	            cursor.execute(checkdb)            
	            for row in cursor:
	                array.append(row [0])
		cursor.close()
		return array







except:
	pass
