import mysql.connector
import json
from mysql.connector import Error

def update_json_column():
    connection = None
    try:
        #1.connect to db
        connection = mysql.connector.connect(
            host='localhost',
            database='parts',
            user='root',
            password='root_1234',
            auth_plugin='mysql_native_password'
        )
    
        #2.iterate rows
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            table_name = 'project_data_accessories_draft_old'
            id_column = 'project_data_id'
            json_column_name = 'rtm_segments'
            select_query = f"select {id_column}, {json_column_name} from {table_name}"
            cursor.execute(select_query)
            records = cursor.fetchall()
        
            #3.parse the json column
            for row in records:
                json_data = row[json_column_name]
                id_data = row[id_column]

                json_dict = json.loads(json_data)
                for channel, cvalue in json_dict.items():
                    for business_model, bvalue in cvalue.items():
                        for rtm_segment, rvalue in bvalue.items():
                            json_dict[channel][business_model][rtm_segment]['isBlocked'] = True
                            json_dict[channel][business_model][rtm_segment]['date'] = ''
                
                #4.update the data
                update_query = f"UPDATE {table_name} set {json_column_name} = %s WHERE {id_column} = %s"
                updated_json_string = json.dumps(json_dict)
                cursor.execute(update_query, (updated_json_string, id_data))

            connection.commit()
            print("All changes committed successfully")
    except Error as e:
        #Handling the db connection error
        print(f"Error while connecting to database: {e}")
        if connection and connection.is_connected():
            connection.rollback()
    
    finally:
        #closing the db connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySql connection is closed")

if __name__ == "__main__":
    update_json_column()