
from selenium import webdriver
import time
from bs4 import BeautifulSoup
#mở trình duyệt
driver = webdriver.Firefox()
driver.get("https://fptshop.com.vn/may-tinh-xach-tay")
driver.implicitly_wait(10) # đợi tối đa 10 giây cho trang web tải xong
# hoặc
time.sleep(10) # đợi đúng 10 giây
html = driver.page_source
# Phân tích HTML với BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Lấy tất cả các phần tử có cùng một lớp (ví dụ: class 'your_class')
elements_with_class = soup.find_all('div',
                                    {'class': 'cdt-product prd-lap product-sale'})  # Thay thế 'your_class' bằng class thực tế của các phần tử

# In thông tin từ tất cả các phần tử
for element in elements_with_class:
    # Lấy văn bản trong phần tử
    element_name = element.find('a',class_='cdt-product__name').text.strip()
    element_cost = element.find('div',class_='progress').text.strip()

    # In ra thông tin lấy được
    print("Tên sản phẩm:", element_name)
    print("Giá bán:", element_cost)
    #print("Cấu hình:", product_specs)
    print("-" * 30)
# Lưu nội dung HTML vào một tệp
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html)
print(driver.title)
driver.quit()



