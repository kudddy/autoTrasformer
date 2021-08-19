def is_true(val):
    if val:
        return val


def generate_city_str(citys_id: list):
    city_str = ""
    for city in citys_id:
        city_str += "&city={}".format(city)
    return city_str

