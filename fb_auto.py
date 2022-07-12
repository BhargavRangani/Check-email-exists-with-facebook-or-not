import requests

facebook_page = requests.get("https://www.facebook.com/")
email_input = str(input("Please enter an email : "))
if "privacy_mutation_token" in facebook_page.text:
    print("\n###############################################")
    print("Anti CSRF parameters detected!!!")
    test_str=facebook_page.text
    test_str=test_str.split("privacy_mutation_token")
    #print(test_str[1])
    test_str=str(test_str[1])
    
    test_str=test_str.split("=")
    #print(test_str[1])
    
    test_str=str(test_str[1])
    test_str=test_str.split('"')
    #print(test_str[0])
    
    privacy_mutation_token = test_str[0]
    print("privacy_mutation_token is : "+privacy_mutation_token)
    
    jazoest = facebook_page.text
    jazoest = jazoest.split('name="jazoest" ')
    jazoest = str(jazoest[1])
    
    jazoest = jazoest.split('value="')
    jazoest=jazoest[1]
    
    jazoest = jazoest.split('"')
    jazoest = jazoest[0]
    print("jazoest param is : "+jazoest)
    
    lsd = facebook_page.text
    lsd = lsd.split('name="lsd" ')
    lsd = str(lsd[1])
    
    lsd = lsd.split('value="')
    lsd=lsd[1]
    
    lsd = lsd.split('"')
    lsd = lsd[0]
    print("lsd param is : "+lsd)
    
    headers = {"Host": "www.facebook.com", "Cookie": "sb=HkogYsPKjFwQdes_VmcxGW6R; datr=HkogYhwiaBFih6kHqTL28kOk; fr=0wAlHB3leDSlwZ8c1..BiIEoe.9W.AAA.0.0.BiLJMy.AWUCODn1rQ4; wd=681x647", "Content-Length": "301","Cache-Control": "max-age=0","Sec-Ch-Ua-Mobile": "?0","Sec-Ch-Ua-Platform": "Windows","Upgrade-Insecure-Requests": "1","Origin": "https://www.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://www.facebook.com/","Accept-Encoding": "gzip, deflate","Accept-Language": "en-US,en;q=0.9"}
    
    params={"jazoest":str(jazoest),"lsd":"AVpEyVLkc2s","email":email_input,"login_source":"comet_headerless_login","next":'',"encpass":"%23PWD_BROWSER%3A5%3A1647088456%3AAedQAPYuWckZPe04LJxXHn%2Bvo6icfqQuF1G%2BgCq5890fb2IZ3w%2BEl1y8UDQbFEyVP0mEmcyS6x0mlD5nqM7ZQliCgJVlPiJlIxW02Z4V7D299UESLTzMyYKzhRVfazlfcksJdiQyZhG3gg%3D%3D"}
    
    print("\n\nSending a POST request to : https://www.facebook.com//login/?privacy_mutation_token="+str(privacy_mutation_token))
    login_response = requests.post("https://www.facebook.com//login/?privacy_mutation_token="+str(privacy_mutation_token), data=params, headers=headers)
    print("Response received with status code : "+str(login_response.status_code))
    
    if("The email address you entered isn&#039;t connected to an account" in login_response.text):
        print("\n\nThe entered email is not registered on facebook")
        print(1)
    else:
        print("\n\nThe entered email is registered!")
        print(login_response.text)
    
    #print(login_response.text)
    
    
