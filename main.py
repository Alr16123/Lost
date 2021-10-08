from sys import getallocatedblocks
from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup
from requests.api import get
import json

global lst_of_name_turn
lst_of_name_turn = ""

global headers
headers = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"}

####### ЧЕМПИОНАТ АНГЛИИ ########
def get_angl():    
    
    url = "https://news.sportbox.ru/Vidy_sporta/Futbol/Evropejskie_chempionaty/Angliya"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_ ="grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock")
    
    angl_ftb_games = {}
    
    angl_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock").find("a", href = \
            "/Vidy_sporta/Futbol/Evropejskie_chempionaty/Angliya/stats/turnir_18885").string

    while "  " in angl_nm_turn:
        angl_nm_turn = angl_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = angl_nm_turn

    for lst in tegs:
        teams = lst.find_all("a", class_ = "_Sportbox_Spb2015_Components_GameRow_GameRow")
        scr = lst.find_all("span", class_ = "score")
        tm = lst.find_all("span", class_ = "time")

    
    hm_t,gs_t,tm_scr,corr_tm,corr_scr = [],[],[],[],[]
    for i in teams:
        hm_t.append(i["data-rates-event-home-team"])
        gs_t.append(i["data-rates-event-guest-team"])
    

    for i in scr:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    
    for i in corr_tm:
        corr_scr.append(i)
    
    for l,(k,i,j) in enumerate(zip(hm_t,gs_t,corr_scr)):
        angl_ftb_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
    
    with open("ftb_res/angl_ftb_games.json","w") as fl:
        json.dump(angl_ftb_games,fl,indent=4)

####### ЧЕМПИОНАТ ИСПАНИИ ########
def get_isp():   
    
    url = "https://news.sportbox.ru/Vidy_sporta/Futbol/Evropejskie_chempionaty/Ispaniya"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_ ="grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock")
    
    isp_ftb_games = {}
    
    isp_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock").find("a", href = \
            "/Vidy_sporta/Futbol/Evropejskie_chempionaty/Ispaniya/stats").string

    while "  " in isp_nm_turn:
        isp_nm_turn = isp_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = isp_nm_turn

    for lst in tegs:
        teams = lst.find_all("a", class_ = "_Sportbox_Spb2015_Components_GameRow_GameRow")
        scr = lst.find_all("span", class_ = "score")
        tm = lst.find_all("span", class_ = "time")

    
    hm_t,gs_t,tm_scr,corr_tm,corr_scr = [],[],[],[],[]
    for i in teams:
        hm_t.append(i["data-rates-event-home-team"])
        gs_t.append(i["data-rates-event-guest-team"])
    

    for i in scr:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    
    for i in corr_tm:
        corr_scr.append(i)
    
    for l,(k,i,j) in enumerate(zip(hm_t,gs_t,corr_scr)):
        isp_ftb_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
        
    with open("ftb_res/isp_ftb_games.json","w") as fl:
        json.dump(isp_ftb_games,fl,indent=4)

####### ЧЕМПИОНАТ ГЕРМАНИИ ########
def get_germ():

    url = "https://news.sportbox.ru/Vidy_sporta/Futbol/Evropejskie_chempionaty/Germaniya"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_ ="grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock")
    
    germ_ftb_games = {}
    
    germ_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock").find("a", href = \
            "/Vidy_sporta/Futbol/Evropejskie_chempionaty/Germaniya/stats").string

    while "  " in germ_nm_turn:
        germ_nm_turn = germ_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = germ_nm_turn

    for lst in tegs:
        teams = lst.find_all("a", class_ = "_Sportbox_Spb2015_Components_GameRow_GameRow")
        scr = lst.find_all("span", class_ = "score")
        tm = lst.find_all("span", class_ = "time")

    
    hm_t,gs_t,tm_scr,corr_tm,corr_scr = [],[],[],[],[]
    for i in teams:
        hm_t.append(i["data-rates-event-home-team"])
        gs_t.append(i["data-rates-event-guest-team"])
    

    for i in scr:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    for i in corr_tm:
        corr_scr.append(i)
    
    for l,(k,i,j) in enumerate(zip(hm_t,gs_t,corr_scr)):
        germ_ftb_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
        
    with open("ftb_res/germ_ftb_games.json","w") as fl:
        json.dump(germ_ftb_games,fl,indent=4)


################### NHL #######################
def get_nhl():
    
    url = "https://news.sportbox.ru/Vidy_sporta/Hokkej/NHL"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_ ="grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock")
    
    nhl_hkk_games = {}
    
    nhl_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock").find("a", href = \
            "/Vidy_sporta/Hokkej/NHL/stats").string

    while "  " in nhl_nm_turn:
        nhl_nm_turn = nhl_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = nhl_nm_turn

    for lst in tegs:
        teams = lst.find_all("a", class_ = "_Sportbox_Spb2015_Components_GameRow_GameRow")
        scr = lst.find_all("span", class_ = "score")
        tm = lst.find_all("span", class_ = "time")

    
    hm_t,gs_t,tm_scr,corr_tm,corr_scr = [],[],[],[],[]
    for i in teams:
        hm_t.append(i["data-rates-event-home-team"])
        gs_t.append(i["data-rates-event-guest-team"])
    

    for i in scr:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    for i in corr_tm:
        corr_scr.append(i)
    
    for l,(k,i,j) in enumerate(zip(hm_t,gs_t,corr_scr)):
        nhl_hkk_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
        
    with open("hkk_res/nhl_hkk_games.json","w") as fl:
        json.dump(nhl_hkk_games,fl,indent=4)

################### КХЛ #######################
def get_khl(): 

    url = "https://news.sportbox.ru/Vidy_sporta/Hokkej/KHL"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    khl_hkk_games = {}
    
    khl_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_ComponentsStandings_StandingsInSeasonBlock_StandingsInSeasonBlock").find("a", href = \
            "/Vidy_sporta/Hokkej/KHL/stats").string

    while "  " in khl_nm_turn:
        khl_nm_turn = khl_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = khl_nm_turn

    url = "https://news.sportbox.ru/Vidy_sporta/Hokkej/KHL/stats"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_="_Sportbox_Spb2015_Components_TableGames_TableGames")

    
    for lst in tegs:
        teams_h_firs= lst.find_all("div", class_ = "box-left")
        teams_g_firs= lst.find_all("div", class_ = "box-right")
        scr_firs = lst.find_all("span", class_ = "score")
        tm_firs = lst.find_all("span", class_ = "time")
        break

    for lst in tegs:
        teams_h_last= lst.find_all("div", class_ = "box-left")
        teams_g_last= lst.find_all("div", class_ = "box-right")
        scr_last = lst.find_all("span", class_ = "score")
        tm_last = lst.find_all("span", class_ = "time")
    

    tm_h,tm_g = [],[]
    corr_scr, corr_tm, tm_scr  = [], [], []

    # хозяева(название)
    for lst in teams_h_firs:
        tm_h.append(lst.find_all("div", class_ = "name"))

    for lst in teams_h_last:
        tm_h.append(lst.find_all("div", class_ = "name")) 

    for k,lst in enumerate(tm_h):
        tm_h[k] = str(lst)[19:-7]

    # гости(название)
    for lst in teams_g_firs:
        tm_g.append(lst.find_all("div", class_ = "name"))

    for lst in teams_g_last:
        tm_g.append(lst.find_all("div", class_ = "name")) 

    for k,lst in enumerate(tm_g):
        tm_g[k] = str(lst)[19:-7]
     

    for i in scr_firs:
        tm_scr.append(i.contents[0].string)


    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    

    # формат времени 00:00 или 01 янв
    for k in tm_firs:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)    
    
    for i in corr_tm:
        corr_scr.append(i)


    for i in scr_last:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm_last:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    for i in corr_tm:
        corr_scr.append(i)

    
    for l,(k,i,j) in enumerate(zip(tm_h,tm_g,corr_scr)):
        khl_hkk_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
        
    with open("hkk_res/khl_hkk_games.json","w") as fl:
        json.dump(khl_hkk_games,fl,indent=4)


################### ВХЛ #######################
def get_vhl():    
  
    url = "https://news.sportbox.ru/Vidy_sporta/Hokkej/VHL"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_ ="grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock")
    
    vhl_hkk_games = {}
    
    vhl_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_TourGamesBlock_TourGamesBlock").find("a", href = \
            "/Vidy_sporta/Hokkej/VHL/stats").string

    while "  " in vhl_nm_turn:
        vhl_nm_turn = vhl_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = vhl_nm_turn

    for lst in tegs:
        teams = lst.find_all("a", class_ = "_Sportbox_Spb2015_Components_GameRow_GameRow")
        scr = lst.find_all("span", class_ = "score")
        tm = lst.find_all("span", class_ = "time")

    
    hm_t,gs_t,tm_scr,corr_tm,corr_scr = [],[],[],[],[]
    for i in teams:
        hm_t.append(i["data-rates-event-home-team"])
        gs_t.append(i["data-rates-event-guest-team"])
    
    corr_scr, corr_tm, tm_scr  = [], [], []

    for i in scr:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    for i in corr_tm:
        corr_scr.append(i)
    
    for l,(k,i,j) in enumerate(zip(hm_t,gs_t,corr_scr)):
        vhl_hkk_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
        
    with open("hkk_res/vhl_hkk_games.json","w") as fl:
        json.dump(vhl_hkk_games,fl,indent=4)

################### ЛигаВТБ #######################
def get_vtb():
    
    url = "https://news.sportbox.ru/Vidy_sporta/Basketbol/vtb-league"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    vtb_bkst_games = {}
    
    vtb_nm_turn = soup.find("div", class_ = \
        "grid-padding-20-15 _Sportbox_Spb2015_Components_ComponentsStandings_StandingsInSeasonBlock_StandingsInSeasonBlock").find("a", href = \
            "/Vidy_sporta/Basketbol/vtb-league/stats").string

    while "  " in vtb_nm_turn:
        vtb_nm_turn = vtb_nm_turn.replace("  ", " ")

    global lst_of_name_turn
    lst_of_name_turn = vtb_nm_turn

    url = "https://news.sportbox.ru/Vidy_sporta/Basketbol/vtb-league/stats"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    tegs = soup.find_all("div", class_="_Sportbox_Spb2015_Components_TableGames_TableGames")

    for lst in tegs:
        teams_h= lst.find_all("div", class_ = "box-left")
        teams_g= lst.find_all("div", class_ = "box-right")
        scr = lst.find_all("span", class_ = "score")
        tm = lst.find_all("span", class_ = "time")
    

    tm_h,tm_g = [],[]
    # хозяева(название)
    for lst in teams_h:
        tm_h.append(lst.find_all("div", class_ = "name"))

    for lst in teams_h:
        tm_h.append(lst.find_all("div", class_ = "name")) 

    for k,lst in enumerate(tm_h):
        tm_h[k] = str(lst)[19:-7]

    # гости(название)
    for lst in teams_g:
        tm_g.append(lst.find_all("div", class_ = "name"))

    for lst in teams_h:
        tm_g.append(lst.find_all("div", class_ = "name")) 

    for k,lst in enumerate(tm_g):
        tm_g[k] = str(lst)[26:-7]

    
    corr_scr, corr_tm, tm_scr  = [], [], []

    for i in scr:
        tm_scr.append(i.contents[0].string)

    # формат счета 0-0
    for i in tm_scr:
        i = i.replace(":","-")
        corr_scr.append(i)
    
    # формат времени 00:00 или 01 янв
    for k in tm:
        if len(k.contents[0]) == 2:
            corr_tm.append(k.text[:2] + ":" + k.text[2:4])    
        else:
            corr_tm.append(k.text)
            
    for i in corr_tm:
        corr_scr.append(i)
    
    for l,(k,i,j) in enumerate(zip(tm_h,tm_g,corr_scr)):
        vtb_bkst_games[l+1] = {
            "home_team" : k,
            "guest_team" : i,
            "score" : j
        }
    

    with open("bskt_res/vtb_bkst_games.json","w") as fl:
        json.dump(vtb_bkst_games,fl,indent=4)

################### НОВОСТИ #######################
def get_news():

    url = "https://www.gazeta.ru/sport/news/"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    news_st = {}
    
    st_links = soup.find_all("div", id = "_id_article_listing")

    # время
    for i in st_links:
        tm = i.find_all("time")

    tm_1 = []
    for l in tm:
        tm_1.append(l.text)    

    time = []  
    for k,i in enumerate(tm_1):
        time.append(i.replace("\n",""))
        if k == 14:
            time = time[::-1]
            break
    
    # заголовок статьи
    for i in st_links:
        nm = i.find_all("a")

    nm_1 = []
    for k in nm:
        nm_1.append(k.text)
    
    name = []
    for k,i in enumerate(nm_1):    
        if len(i) > 2:
            name.append(i.replace("\n","").replace("\xa0"," "))
        if k == 29:
            name = name[::-1]
            break
    
    for i in st_links:
        img = i.find_all("img", loading = "lazy")
    
    image = []
    for k in img:
        image.append(k["src"])

    
    for i in st_links:
        lnk = i.find_all("a", class_ = "b_ear-image")
    
    links = []
    for k,i in enumerate(lnk):
        links.append("https://www.gazeta.ru"+i["href"])
        if k == 14:
            links = links[::-1]
            break
    

    for l,(k,j,i,m) in enumerate(zip(time,name, image, links)):
        news_st[l] ={
            "time" : k,
            "name" : j,
            "image" : i,
            "link" : m
        }

    with open("news.json","w") as fl:
        json.dump(news_st,fl,indent=4)
    
    