import csv 
import json

#read csv file
csv_filepath = open("/Users/yoshikiuchida/Desktop/Python_csv/csv2gatsby_code/csv_files/timetable.csv","r")



reader = csv.reader(csv_filepath)
line_csv_file = [row for row in reader]
content_month1 = line_csv_file[1][0]
content_day1 = line_csv_file[1][1]
content_dayofweek1 = line_csv_file[1][2]
content_place1 = line_csv_file[1][3]
content_event1 = line_csv_file[1][4]
content_start_time1 = line_csv_file[1][5]
content_end_time1 = line_csv_file[1][6]
content_session_name1 = line_csv_file[1][7]
content_presnter1 = line_csv_file[1][8]
content_room_name1 = line_csv_file[1][9]
content_room_url1 = line_csv_file[1][10]
content_slack_name1 = line_csv_file[1][11]
content_slack_url1 = line_csv_file[1][12]
content_log_url1 = line_csv_file[1][13]
content_slide_url1 = line_csv_file[1][14]
content_flyer1 = line_csv_file[1][15]


content_event2 = line_csv_file[2][4]

class TimetableCodeGenerator:
    """
    タイムテーブルのGatsbyコードを生成する
    """
    

    def __init__(self):
        pass

    def parse_csv(self):
        """
        CSVファイルをパースして、1行ずつリストにしたものを返す
        """
        
        
        session_data_lists = []
        return session_data_lists

    def create_jajson_file(self):
        """
        parse_csvから受け取ったデータをもとにja.jsonファイルを生成する
        """
        json_response = {
                    "programs": {
                        content_event1: {
                            "title": content_session_name1,
                            "presenter": content_presnter1
                        },
                        content_event2: {
                            "title": content_event2
                        }
                    }
                }

        a = open('/Users/yoshikiuchida/Desktop/Python_csv/csv2gatsby_code/output/ja_result.json' , 'w')
        json.dump(json_response,a)
        
        pass

    def create_timetabletsx_file(self):
        """
        parse_csvから受け取ったデータをもとにtimetable.tsxファイルを生成する
        """
        tsx_response =  {
                            {
                                "start": content_start_time1,
                                "end": content_end_time1,
                                "intlKey": content_event1,
                                "roomUrl": content_room_url1,
                                "roomName": content_room_name1,
                                "slackUrl": content_slack_url1,
                                "slackName": content_slack_name1,
                                "logUrl": content_log_url1,
                                "slidesUrl": content_slide_url1,
                            },
                        }     
        b = open('/Users/yoshikiuchida/Desktop/Python_csv/csv2gatsby_code/tsx_test.tsx','w')
        
                
    
        
        
        pass


if __name__ == '__main__':
    obj = TimetableCodeGenerator()
    session_data_lists = obj.parse_csv()
    obj.create_jajson_file()
    obj.create_timetabletsx_file()