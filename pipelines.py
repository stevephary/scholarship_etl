from extract.scraping import wemakescholar_scholarships
from common.save_to_csv import save_to_csv
from extract.upload_to_s3 import upload_to_s3
import json


scholar = wemakescholar_scholarships()
save_to_csv(scholar,"test.csv")
# print(scholar)
json_data = json.dumps(scholar)
upload_to_s3(json_data,"test")