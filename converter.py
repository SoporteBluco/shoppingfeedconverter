from bs4 import BeautifulSoup

input_file = "nombre del acchivo" + ".html"
output_file = "nombre del archivo" + ".txt"

def extract_categories_from_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'lxml')
        categories = []
        for ul in soup.find_all('ul'):
            for li in ul.find_all('li'):
                categories.append(li.get_text(strip=True).replace('>', ' > '))
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for category in categories:
            out_file.write(category + '\n')
        print(f"Categories were exported succefully in {output_file}")
        
extract_categories_from_html(input_file, output_file)