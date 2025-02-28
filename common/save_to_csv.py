import csv
import logging

logging.basicConfig(
    level=logging.DEBUG,  
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def save_to_csv(data, filename):
    if data:
        fieldnames = data[0].keys()
        with open(filename, 'w',newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
            
        logging.info(f"Data successfully saved to {filename}")