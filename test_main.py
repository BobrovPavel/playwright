from playwright.sync_api import expect

# def test_listen_network(page):
#     page.on("response", lambda response: print("<<", response.status, response.url, response))
#     def route_handler(route):
#         url = route.request.url.lower()
#         is_image = any(url.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"])
#         if route.request.method == "GET" and is_image:
#             route.abort()
#         else:
#             print(">>", route.request.method, route.request.url)
#             route.continue_()
#     page.route("**/*", route_handler)
#     page.goto('https://osinit.ru/')

# def test_replace_from_har(page):
#     page.route_from_har(
#         "example.har",
#         # Применять HAR только к запросам, содержащим этот путь
#         url="**/company_logos.json",
#         # Если в HAR файле нет точного совпадения или это другой запрос — идти в реальную сеть
#         not_found="continue"
#     )
#     page.goto("https://reqres.in/")