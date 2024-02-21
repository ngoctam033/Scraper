from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import sys

def get_product_info():
    try:
        driver = webdriver.Firefox() # Khởi tạo trình duyệt Firefox
    except WebDriverException:
        print("Could not start the WebDriver.") # In ra thông báo lỗi
    sys.exit(1)# Thoát chương trình nếu không thể khởi tạo trình duyệt
    
    try:
        driver.get("https://fptshop.com.vn/may-tinh-xach-tay") # Mở trang web
    except WebDriverException:
        print("Could not access the URL.") # In ra thông báo lỗi
    driver.quit()# Đóng trình duyệt
    
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Cuộn trang web xuống dưới cùng
    element = driver.find_element(By.CSS_SELECTOR, '.btn.btn-light') # Tìm nút "Xem thêm" bằng CSS Selector
    
    while True: # Lặp lại việc nhấn nút "Xem thêm" cho đến khi nào không còn nút đó nữa
        try:
            element = driver.find_element(By.CSS_SELECTOR, '.btn.btn-light') # Tìm nút "Xem thêm" bằng CSS Selector
            element.click() # Nhấn nút "Xem thêm"
            driver.implicitly_wait(3) # wait for the page to load
        except NoSuchElementException:
            break  # exit the loop if the button is not found
    
    html = driver.page_source # Lấy mã nguồn trang web

    # Phân tích HTML với BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser') # Chuyển mã nguồn trang web thành đối tượng BeautifulSoup

    # Lấy tất cả các phần tử có cùng một lớp
    elements_with_class = soup.find_all('div', {'class': 'cdt-product prd-lap product-sale'}) # Lấy tất cả các phần tử có class là 'cdt-product prd-lap product-sale'

    # Tạo danh sách chứa thông tin sản phẩm
    product_info_list = []

    # Lấy thông tin từ tất cả các phần tử
    for element in elements_with_class: # Duyệt qua từng phần tử
        # Lấy văn bản trong phần tử
        element_name = element.find('a', class_='cdt-product__name').text.strip() # Lấy tên sản phẩm
        element_cost = element.find('div', class_='progress').text.strip() # Lấy giá bán
        # Thêm thông tin vào danh sách
        product_info_list.append((element_name, element_cost))

    driver.quit() # Đóng trình duyệt

    return product_info_list

# Lấy thông tin sản phẩm và in ra
product_info_list = get_product_info()
count = 0
for product_info in product_info_list:
    
    element_name, element_cost = product_info
    print("Tên sản phẩm:", element_name) # In tên sản phẩm
    print("Giá bán:", element_cost) # In giá bán
    # cho biết danh sách có bao nhiêu sản phẩm bằng cách đếm số phần tử product_info
    print("Số sản phẩm:", len(product_info_list))
    print("-" * 30) # In dấu gạch ngang

#bạn hãy chạy code trên và xem kết quả nhé
#bạn có thể tham khảo thêm tại https://www.selenium.dev/documentation/en/ và https://www.crummy.com/software/BeautifulSoup/bs4/doc/
