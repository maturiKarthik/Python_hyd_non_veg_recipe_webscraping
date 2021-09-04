import requests as req
import re


# This script fetch the video of the recipie
def fetch_recipe_url(url):
    response = req.get(url)
    video = re.findall('<script type="application/ld\+json" class="yoast-schema-graph">(.*?)</script>',
                       str(response.content))
    video_url = re.findall('"embedUrl":"(.*?)"', str(video))
    if len(video_url) > 0:
        return video_url[0]
    else:
        return video_url
