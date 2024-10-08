程序说明
本程序旨在从南京地区的安居客网(https://nj.fang.anjuke.com/loupan/all/)抓取楼盘信息，包括楼盘名称、房价、区域和户型，并将这些信息保存到Excel文件和文本文件中。以下是详细的程序说明：
1. 导入必要的库
time：用于在请求之间添加延迟，以遵守网站的请求频率限制。
requests：用于发送HTTP请求。
BeautifulSoup：从bs4库中导入，用于解析HTML内容。
re：虽然本程序未直接使用，但通常用于正则表达式匹配。
openpyxl：用于将DataFrame写入Excel文件。
os：用于获取当前工作目录等操作系统相关的功能。
pandas：用于数据处理，将抓取的数据转换为DataFrame并保存到Excel。
fake_useragent.UserAgent：用于生成随机的User-Agent，模拟不同浏览器访问网站，以应对可能的反爬虫机制。
2. 定义函数
open_url(url)
功能：发送GET请求到指定URL，并返回响应对象。
参数：url（要请求的网址）。
使用fake_useragent生成随机的User-Agent，并设置到请求头中。
打印请求的URL和响应状态码。
find_data(res)
功能：解析HTML响应内容，提取楼盘信息。
参数：res（HTTP响应对象）。
使用BeautifulSoup解析HTML，查找并提取楼盘名称、价格、区域和户型信息。
如果未能找到任何数据或发生异常，则返回空列表和相应的状态信息。
main()
主函数，控制程序的执行流程。
初始化URL和存储所有数据的列表。
循环遍历指定页码的URL（假设从1到24页），发送请求，解析数据。
如果数据提取失败，则重试最多10次。
将每页的数据添加到总数据列表中。
使用pandas将总数据转换为DataFrame，并保存到Excel文件。
同时，将总数据写入文本文件，每行包含楼盘名称、房价、区域和户型信息。
3. 执行程序
当直接运行此脚本时（if __name__ == "__main__":），调用main()函数开始执行。
程序首先打印当前工作目录，然后按照上述流程抓取数据并保存到文件。
注意事项
本程序假设了网页的结构是固定的，并且使用了特定的类名来查找元素。如果网页结构发生变化，可能需要更新选择器。
由于本网站有反爬虫机制，爬虫过程中遇到了IP封锁、验证码等状况，因此程序中加入了重试机制，并对降低请求频率，生成随机的User-Agent，模拟不同浏览器访问网站，应对可能的反爬虫机制
