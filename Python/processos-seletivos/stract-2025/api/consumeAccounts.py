import requests

def fetch_accounts(access_token, platform):
    accounts = []
    page = 1
    url = f"https://sidebar.stract.to/api/accounts"
    headers = {"Authorization": f"Bearer {access_token}"}

    while True:
        params = {"platform": platform,"page": page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            accounts.extend(data['accounts'])
            
            current_page = data.get("pagination", {}).get("current", page)
            total_pages = data.get("pagination", {}).get("total", page)
            
            if 'pagination' not in data or data["pagination"] == None or current_page >= total_pages:
                break
        page += 1

    if accounts != None:
        return accounts
    return {"error": "Falha ao buscar contas"}


