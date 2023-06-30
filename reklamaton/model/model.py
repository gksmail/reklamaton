#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def make_lists(df): 
    all_mes = []
    for i in range(len(df)):

        data = df.loc[i, 'messages']
        alll = []
        views = data['views']
        react_list = data['reactions']

        alll.append(views)
#         alll.append(part_count)
        list_emo = []
#             if react_list is not None:
#                 for h in react_list:
#                     emotion = h['emoticon']
#                     count_for_emo = h['count']
#                     list_emo.append([emotion, count_for_emo])
#                 alll.append(list_emo)
        all_mes.append(alll)
    
    return all_mes

def convert(message, file,is_rek):
    
    new = pd.read_json(file)
    par_c = new['participants_count']
    

    dff = make_lists(new)
    
    r = 0
    for i in dff:
        r += i[0]
    st_v = r / len(dff)
    
    for_pr = pd.DataFrame({ 'message': message,
                           'views': st_v,
                           'part' : par_c,
                           'is_reklama': is_rek})

    for_pr = for_pr.loc[1]
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(for_pr)
    return prediction
 





    

