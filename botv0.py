import vk_api
'''
1.найти id постов  GetLastComminityIDPosts
2.найти единожды id людей лайкнувших посты CreateListOfActiveUsers уже юзает GetLastComminityIDPosts также юзает CheckLikes
3.фильтруем найденных пользователей FiltrUser
'''
login = '79536894935'
password = 'balisu81'
def WallInfo(vk, owner_id = 40620395, domain = ''):
    '''Информация о стене пользователя'''
    #пример использования WallInfo(vk,'',"nestondart")
    response = vk.wall.get(owner_id = owner_id)  # Используем метод wall.get
    print("постов на стене " + str(response['count']))
    print("постов удалено " + str(response['items'][0]['id'] - response['count']))
    response = vk.wall.get(owner_id=owner_id, count=100)
    for i in response:
        print(response['count'])
        print(response['items'])
    return [response['count'] ,response['items'][0]['id'] - response['count'] ]

def CheckLikes(vk,type,owner_id,item_id):
    '''функция возвращает список пользователей лайкнувших пост'''
    #CheckLikes(vk,"post", 40620395,1652)
    like = vk.likes.getList(type = type,owner_id = owner_id, item_id = item_id)
    return like['items']

def GetLastComminityIDPosts(vk,  owner_id = -64529860, count = 100):
    '''функция возвращает список id указанного количества постов'''
    #GetLastComminityIDPosts(vk)

    if(count <= 100 ):
        response = vk.wall.get(owner_id = owner_id, count = count)
    else:
        print("count:=100")
        response = vk.wall.get(owner_id=owner_id,count = 100)#todo:разобраться со срезами

    idPostsList = []
    for i in response['items']:
        if('marked_as_ads' in i):
            if (i['marked_as_ads'] == 0):
                idPostsList.append(i['id'])
        else:
            idPostsList.append(i['id'])
    '''все параметры которые можно вытащитьid from_id owner_id date marked_as_ads post_type text attachments post_source comments likes  reposts views is_favorite'''
    return idPostsList
def ShowUserInfo(vk, id = 40620395, paramList = ["sex","bdate","site","education","activity","relation","online"]):
    '''вывод информации о пользователе'''
    #print(ShowUserInfo(vk,513511410))
    info = vk.users.get(user_ids=id, fields=paramList)
    print(info)
    correctParamInfo = []
    for i in range(info.__len__()):
        if 'first_name' in info[i]:
            if info[i]['first_name'] != '':
                correctParamInfo.append(info[i]['first_name'])
        if 'last_name' in info[i]:
            if info[i]['last_name'] != '':
                correctParamInfo.append(info[i]['last_name'])
        if 'sex' in info[i]:
            if(info[i]['sex'] == 0):
                correctParamInfo.append("none")
            if ((info[i]['sex'] == 1)):
                correctParamInfo.append("female")
            if (info[i]['sex'] == 2):
                correctParamInfo.append("male")
        if ('relation' in info[i]):
                correctParamInfo.append("relation"+str(info[i]['relation']))
        if 'bdate' in info[i]:
            if info[i]['bdate'] != '':
                correctParamInfo.append("bdate:"+str(info[i]['bdate']))
        if 'site' in info[i]:
            if info[i]['site'] != '':
                correctParamInfo.append(str(info[i]['site']))
        if 'university_name' in info[i]:
            if (info[i]['university_name'] != ''):
                correctParamInfo.append(str(info[i]['university_name']))
        if 'online' in info[i]:
            if(info[i]['online'] == 1):
                correctParamInfo.append("online")
            else:
                correctParamInfo.append("offline")
        if 'activity' in info[i]:
            if (info[i]['activity'] != ''):
                correctParamInfo.append("activity " + str(info[i]['activity']))
    return correctParamInfo
def CalculateAge(birthday):
    '''требуемый формат даты DD.MM.YYYY'''
    '''допустимый формат даты D.M.YYYY'''
    if( birthday.find('.') == 1):
        birthday = "0" + birthday
    import datetime
    curDay = datetime.datetime.today()
    A = birthday
    A = A[-4:]
    numYear =int(curDay.year)- int(A)
    A = birthday
    A = A[3:5]
    if(A.endswith('.') == True):
        A = "0"+A
        A = A[0:-1]
    if(int(curDay.month) < int(A)):
        numYear-=1
    if (int(curDay.month) == int(A)):
        A= birthday
        A = A[0:2]
        if(int(curDay.day) < int(A)):
            numYear-=1
    return numYear
def DaiFotoZakritogoPolzovatelyaOchenNadoOtvechayu(vk,ID):
    paramList = ["photo_max","photo_max_orig"]
    info = vk.users.get(user_ids= ID, fields=paramList)
    print(info)
    for i in info:
        print(i)
def StealPhoto(vk,ID):
    paramList = ["photo_max"]
    info = vk.users.get(user_ids=ID, fields=paramList)
    result = []
    result.append(info[0]['first_name'])
    result.append(info[0]['photo_max'])
    return result
def FiltrUser(vk,sex,idList,minAge =18,maxAge = 22, allowNotBF = False, needPhone = False):
    '''функция принимает список id и возвращает список только удовлетворяющих выборке пользователей'''
    paramList = ["sex", "bdate", "relation","photo","contacts"]
    roadToLen = 0
    resultList = []
    while(roadToLen != idList.__len__()):
        currentCheck = []
        currentI = 0
        while((currentI!= 100) and (roadToLen != idList.__len__())):
            currentCheck.append(idList[roadToLen])
            currentI+=1
            roadToLen+=1
        info = vk.users.get(user_ids=currentCheck, fields=paramList)
        for i in range(info.__len__()):
            approvedFlag = True
            if(sex != "none"):
                if 'sex' in info[i]:
                    if (info[i]['sex'] == 2):
                        if(sex == "female"):
                            approvedFlag = False
                    if (info[i]['sex'] == 1):
                        if(sex == "male"):
                            approvedFlag = False
                else:
                    approvedFlag = False
            if(needPhone == True):
                if( "mobile_phone" in info[i]):
                    if(info[i]['mobile_phone'] == ""):
                        approvedFlag = False
                    if(info[i]['mobile_phone'].__len__() != 11):
                        approvedFlag = False
                    if(info[i]['mobile_phone'].find('*')!= -1):
                        approvedFlag = False
                else:
                    approvedFlag = False
            if not ('photo' in info[i]):
                approvedFlag = False
            if ('relation' in info[i]):
                if ((info[i]['relation'] == 0) or (info[i]['relation'] == 1) or (info[i]['relation'] == 6)) == False:
                    approvedFlag = False
            if 'bdate' in info[i]:
                if (info[i]['bdate'].count('.') == 2):  # count кого?!
                    Age = CalculateAge(info[i]['bdate'])
                    if( (Age <= minAge) or (Age >= maxAge)):
                        approvedFlag = False
                else:
                    if(allowNotBF == False):
                        approvedFlag = False
            else:  # В данный момент убираем всех кто не указал год рождения
                if (allowNotBF == False):
                    approvedFlag = False
            if approvedFlag == True:
                resultList.append(info[i]['id'])
    return resultList

def CreateListOfActiveUsers(vk, count = 100,owner_id = -64529860):
    '''возвращает список списков [id_user, id_post]  ид пользователя и лайкнутый пост'''

    idPostList = GetLastComminityIDPosts(vk,owner_id,count)
    listIDUsers= []
    listUserAndPostID = []
    for i in idPostList:
        likedCurrentPost = CheckLikes(vk,"post",owner_id, i)
        for j in likedCurrentPost:
            if not (j in listIDUsers):
                listIDUsers.append(j)
                listUserAndPostID.append([j,i])#cначала id_user potom id_post
    return [listIDUsers,listUserAndPostID]

def StartActiveSearching(vk,minAge = 18,maxAge = 22, allowNotBD = False,count = 100, owner_id =-64529860):
    listActive = CreateListOfActiveUsers(vk,count,owner_id)
    print("всего различных пользователей: " + str(listActive[0].__len__()))
    listActive1 = FiltrUser(vk,"female",listActive[0],minAge,maxAge,allowNotBD)
    print("пользователей после фильтрации: " + str(listActive1.__len__()))
    for i in range(listActive1.__len__()):
        print("https://vk.com/id" +str(listActive1[i]))
        DaiFotoZakritogoPolzovatelyaOchenNadoOtvechayu(vk, listActive1[i])
        for j in range(listActive[1].__len__()):
            if(listActive1[i] == listActive[1][j][0]):
                sendIDPost = str(owner_id) +"_"+ str(listActive[1][j][1])
                res = vk.wall.getById(posts=sendIDPost)
                print(res[0]['text'])
                print("id posta: " + str(listActive[1][j][1]))

def ReturnUserInfo(SearchingParams):
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return 0
    vk = vk_session.get_api()
    result=[]
    listActive = CreateListOfActiveUsers(vk, int(SearchingParams[1]), int(SearchingParams[0]))
    import wind
    wind.pointAllSearching.configure(text= "всего различных пользователей: " + str(listActive[0].__len__()))
    listActive1 = FiltrUser(vk, SearchingParams[2], listActive[0], int(SearchingParams[4]), int(SearchingParams[5]), SearchingParams[3], SearchingParams[6])#вот сюда новые параметры
    wind.pointSearching.configure(text ="пользователей после фильтрации: " + str(listActive1.__len__()) )
    for i in range(listActive1.__len__()):
        resultmin = []
        resultmin.append("https://vk.com/id" + str(listActive1[i]))
        resultmin.append(StealPhoto(vk, listActive1[i]))
        for j in range(listActive[1].__len__()):
            if (listActive1[i] == listActive[1][j][0]):
                sendIDPost = str(SearchingParams[0]) + "_" + str(listActive[1][j][1])
                res = vk.wall.getById(posts=sendIDPost)
                resultmin.append(res[0]['text'])
        paramList = ["bdate"]
        info = vk.users.get(user_ids= listActive1[i], fields=paramList)
        if 'bdate' in info[0]:
            if (info[0]['bdate'].count('.') == 2):
                age = CalculateAge(info[0]['bdate'])
                resultmin.append(age)
            else:
                resultmin.append("-")
        else:
            resultmin.append("-")
        result.append(resultmin)
    result[0].append(str(listActive1.__len__()))
    return result




def main():
    '''vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return 0
    vk = vk_session.get_api()'''
    #StartActiveSearching(vk,18,22,False,10)
    #DaiFotoZakritogoPolzovatelyaOchenNadoOtvechayu(vk,198231777)
    import wind
    wind.CreateWindow()
if __name__ == '__main__':
    main()