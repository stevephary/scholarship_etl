import requests
from bs4 import BeautifulSoup
import logging
import re
from typing import List, Optional, Dict



logging.basicConfig(
    level=logging.DEBUG,  
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def wemakescholar_scholarships() -> Optional[List[Dict]]:
    base_url = "https://www.wemakescholars.com"
    url = f"{base_url}/scholarship"
    
    logging.info(f"scraping {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div_tags = soup.find_all('div', class_='col-md-6 col-sm-6 col-xs-6 p0')
    scholarship_links = [div.find('a').get('href') for div in div_tags]
    logging.info(f"Found {len(scholarship_links)} scholarship links")
    
    
    scholarships = []
    for link in scholarship_links:
        scholarship_url = f"{base_url}{link}"
        
        scholarship_response = requests.get(scholarship_url)
        scholarship_soup = BeautifulSoup(scholarship_response.text, "html.parser")
        
        #fetching scholarship infos
        scholarship_name = scholarship_soup.find('h1', class_='clrwms fw4 font18')
        eligible_degree = scholarship_soup.find('a', class_='clrblue')
        application_link = scholarship_soup.find('article', class_='more-about-scholarship').find('a', text='here').get('href')
        
        p_tags = scholarship_soup.find_all('p')
        deadline = "N/A"  
        funding_type = "N/A"
        field_of_study = "N/A"
        university = "N/A"
        eligible_to = "N/A"
                    
        for p in p_tags:
            p_text = p.get_text(strip=True).lower()
            span = p.find_next_sibling('span', class_='text-line-value')
            if not span:
                continue 
            if 'deadline' in p_text:
                if re.match(r"\d{1,2} [A-Za-z]{3}, \d{4}", span.text.strip()):
                    deadline = span.text.strip()
            elif 'funding' in p_text:
                funding_type = span.text.strip()
            elif 'eligible courses' in p_text:
                field_of_study = span.text.strip()
            elif 'can be taken at' in p_text:
                university_spans = p.find_next_siblings('span', class_='text-line-value')
                if university_spans:
                    university = university_spans[1].text.strip()
            elif 'eligible nationalities' in p_text:
                eligible_to = span.text.strip()
        
        scholarship_details = {
            "name": scholarship_name.text.strip() if scholarship_name else "N/A",
            "eligible_degree": eligible_degree.text.strip() if eligible_degree else "N/A",
            "deadline": deadline,
            "funding_type":funding_type,
            "field_of_study": field_of_study,
            "university": university,
            "eligible_to": eligible_to,
            "application_link": application_link,
            "url": scholarship_url
        }
        scholarships.append(scholarship_details)
        
        logging.info(f"Scraped details for {len(scholarships)} scholarships.")
        
    return scholarships
        
    
    
    

# def get_scholarship_names(base_url: str) -> Optional[List[str]]:

#     all_scholarships = []
#     page = 1
#     max_pages = 10

#     try:
#         while page <= max_pages: 
#             page_url = f"{base_url}?page={page}"
#             logging.info(f"Fetching page {page}: {page_url}")
#             response = requests.get(page_url)
#             response.raise_for_status()
#             soup = BeautifulSoup(response.text, "html.parser")

#             names = soup.find_all("h2", class_="post-title")
#             if names:
#                 scholarship_names = [name.get_text(strip=True) for name in names]
#                 all_scholarships.extend(scholarship_names)
#                 logging.info(f"Found {len(scholarship_names)} scholarships on page {page}.")
#                 page += 1 
#             else:
#                 logging.warning(f"No scholarship names found on page {page}. Stopping.")
#                 break  

#         logging.info("All scholarship names retrieved successfully!")
#         return all_scholarships

#     except requests.RequestException as e:
#         logging.error(f"Error fetching URL: {e}")
#         return None
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")
#         return None
    
    
# def scholarship_info(scholarships: List[str]) -> Optional[dataframe]: