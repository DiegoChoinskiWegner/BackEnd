import requests

def fetch_insights(access_token, platform, account, userToken, *fields):
    insights = []
    page = 1
    url = f"https://sidebar.stract.to/api/insights"
    headers = {"Authorization": f"Bearer {access_token}"}

    while True:
        params = {"platform": platform,"account": account,"token": userToken,"fields": list(fields),"page": page}
        params["fields"] = ",".join(fields)
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            insights.extend(data['insights'])
            
            current_page = data.get("pagination", {}).get("current", page)
            total_pages = data.get("pagination", {}).get("total", page)
            
            if 'pagination' not in data or data["pagination"] == None or current_page >= total_pages:
                break
        page += 1

    if insights != None:
        return insights
    return {"error": "Falha ao buscar contas"}


