import connectdb


def yesorno(param,item):
	param.addItem(item)



def getCombo(dbgetlist):       
            for i in range(len(connectdb.array)):
                dbgetlist.addItem(connectdb.array[i])


def getCombolist(box_get_list,list_check):
	for i in range(len(list_check)):
		box_get_list.addItem(list_check[i])

def max_upload(db_where, db_array):
	db_string = "SELECT " + connectdb.db_upload_max + " FROM "+ connectdb.db_messengers_forQ + " WHERE name = '"+ db_where+"' LIMIT 0,30"

	print(db_string)
                                        
	print("connect")
    

