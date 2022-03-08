import pandas
import requests
import math

def GetUserDetails(userhandles):
    apiUrl = "https://api.twitter.com/2/users/by?usernames=[]&user.fields=description,verified,created_at,protected,location,url,withheld,public_metrics"
    bearerToken = "AAAAAAAAAAAAAAAAAAAAAFzxYAEAAAAASAnmxjiLpo53ujFzugIxfHkvPuQ%3DpfImoFLh0hnQ7tdkm1cXolrxzBoKml5KkYHXuyFKni0P4hwOb6"
    headers = headers = {"Authorization": f"Bearer {bearerToken}"}
    usernameLimitPerHit = 100
    numberOfRounds = math.ceil(len(userhandles) / usernameLimitPerHit)
    df = pandas.DataFrame()
    errors = pandas.DataFrame()
    for i in range(numberOfRounds):
        start = i * 100
        userNames = userhandles[start : start + usernameLimitPerHit]
        newApi = apiUrl.replace('[]', ",".join(userNames))
        response = requests.get(newApi, headers=headers).json()
        df = df.append(pandas.DataFrame.from_dict(response['data']))
        if()
        errors = errors.append(pandas.DataFrame.from_dict(response['errors']))
    with pandas.ExcelWriter('userData.xlsx', mode='w') as writer:  
        df.to_excel(writer, sheet_name='user_data')
        errors.to_excel(writer, sheet_name='errors')

df = pandas.read_excel('Twitter Handles.xlsx')
df['Twitter Handle'] = df['Twitter Handle'].str.replace('"','')
df['Twitter Handle'] = df['Twitter Handle'].str.replace('@','')
df['Twitter Handle'] = df['Twitter Handle'].str.replace("\((.*?)\)",'', regex=True)
df['Twitter Handle'] = df['Twitter Handle'].str.strip()
df['Twitter Handle'] = df['Twitter Handle'].apply(str)

GetUserDetails(df['Twitter Handle'].values)