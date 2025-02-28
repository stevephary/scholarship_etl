from extract.scraping import wemakescholar_scholarships
from common.save_to_csv import save_to_csv


scholar = wemakescholar_scholarships()
save_to_csv(scholar,"test.csv")
# print(scholar)
