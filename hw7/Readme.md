Задание разделено на 2 части: 
С помощью библиотеки selenium открыли сайт, перешли в категорию Travel, с помощью библитотеки BeautifulSoup произвели парсинг данных книг, относящейся к данной категории. 
В качестве элементов парсинга указаны: название книги, ссылка, цена и наличие. 
С помощью тулбара (на сайте включается клавишей F12) нашли тег, где расположены книги. Потом повторили эту процедуру для всех книг категории. 
Сформировали словарь, который записали в json и csv файлs. Использовали метод try-except. 
Основные трудности, это нахождение нужных тегов, так как очень много дублируемых тегов на исследуемом сайте. 
Поиск методом велся подбора: брал теги и тестровал, находятся нужные данные или нет.