import requests as req
import recipieVideoExtractor as rcv
import re

base_url = "https://www.indianhealthyrecipes.com/recipes/hyderabadi-restaurant-styles/"
data = req.get(base_url)
inner_elements = re.findall('<article(.*?)</article>', str(data.content))
delimiter = "^"


def get_data():
    data_holder = []
    for element in inner_elements:
        cnt = re.sub('class="(.*?)"', "", element).replace("aria-label=", "").replace('><div ><a  href="',
                                                                                      delimiter).replace(
            '" aria-hidden="true" tabindex="-1"><img width="500" height="500" src="', delimiter).replace('"  alt="',
                                                                                                         delimiter)
        filter_cnt = cnt.split(delimiter)
        dictionary = {
            "title": filter_cnt[0],
            "recipe_url": filter_cnt[1],
            "recipe_video": rcv.fetch_recipe_url(filter_cnt[1]),
            "img ::": filter_cnt[2],
        }
        data_holder.append(dictionary)
    return data_holder

# print(data_holder)
