from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestCheckAmazonAddToCart(BaseTest):
    def test_check_amazon_addToCart(self):
        home_page = HomePage(self.driver)
        home_page.access_home_page()  # ana sayfaya gidilir (sayfaya ulaşıncaya kadar sayfa yenilenir)
        home_page.reject_cookies()  # cookieler reddedilir
        self.assertEqual(self.base_url, home_page.get_current_url(),
                         "Amazon anasayfa açılamadı!")  # amazon ana sayfasına gidildiği doğrulanır
        home_page.search_text()  # search box'a değer girilir ve arama yapılır

        search_page = SearchPage(self.driver)
        self.assertIn(home_page.textToSearch, search_page.return_text_first_element(),
                      "Arama sonucundaki ilk ürün Samsung ürünü değil!")
        # arama sonucunda açılan sayfada gelen ilk ürünün Samsung ürünü olduğu doğrulanır
        search_page.click_second_page_button()  # ikinci sayfa butonuna tıklanır
        self.assertIn("pg_2", home_page.get_current_url(),
                      "İkinci sayfaya erişim sağlanamadı!")  # ikinci sayfada olunduğu doğrulanır
        search_page.click_to_product()  # ürüne tıklama yapılır

        product_page = ProductPage(self.driver)
        product_page.is_product_present()  # ürün sayfasında olunduğu doğrulanır
        product_page.click_add_to_cart_button()  # sepete ekle butonuna tıklanır

        cart_page = CartPage(self.driver)
        self.assertIn("https://www.amazon.com.tr/cart", home_page.get_current_url(),
                      "Sepet sayfasına erişim sağlanamadı!")  # sepet sayfasıne erişim sağlandığı doğrulanır
        cart_page.click_amazon_logo()  # amazon logosuna tıklanarak ana sayfaya gidilir
