import requests

def shorten_link(full_link):
    API_KEY = 'e83d5497075207c00a1b0a04ea922edc7032c'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {"key": API_KEY, "short": full_link}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    # print(data)
    return(data)


# shorten_link('https://www.youtube.com/watch?v=lYMM7egm_9M&ab_channel=CodePalace')
