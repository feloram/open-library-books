import requests
import csv

url = "https://openlibrary.org/search.json"

params = {
    "q": "fiction",
    "fields": "title,author_name,first_publish_year",
    "limit": 50
}

response = requests.get(url, params=params)
data = response.json()
# print(data)

my_books = []

for book in data['docs']:
    
    year = book.get('first_publish_year')
    
    if year and year > 2000:
        
        authors = book.get('author_name', ['نامشخص'])
        
        book_info = {
            'Title': book['title'],
            'Author':", ". join(authors),
            'Year': year
        }
        
        my_books.append(book_info)

        
# print(my_books)
print("تعداد کتاب‌های پیدا شده بعد 2000:", len(my_books))

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
    writer.writeheader()
    writer.writerows(my_books)

print("فایل books.csv ساخته شد.")