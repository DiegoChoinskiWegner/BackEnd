import requests

def fetch_platforms(access_token):
    platforms = []
    page = 1
    url = f"https://sidebar.stract.to/api/platforms"
    headers = {"Authorization": f"Bearer {access_token}"}

    while True:
        params = {"page": page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            platforms.extend(data['platforms'])
            
            current_page = data.get("pagination", {}).get("current", page)
            total_pages = data.get("pagination", {}).get("total", page)
            
            if 'pagination' not in data or data["pagination"] == None or current_page >= total_pages:
                break
        page += 1

    if platforms != None:
        return platforms
    return {"error": "Falha ao buscar contas"}


