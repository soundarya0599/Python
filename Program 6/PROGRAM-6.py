#!/usr/bin/env python
# coding: utf-8

# # <CENTER> PROGRAM 6: PANDAS IN PYTHON</CENTER>
# ---

# **Requirement:**
# 
#         After the death of Mr. Jagmohan Dalmia BCCI is worried about the performance of Indian team in the worldcup as they didn’t qualify for the finals in the last season.They believe that legendary cricketer, Prince of Kolkata, Mr. Sourav Ganguly (Dada) can do some magic to bring the worldcup back in India. BCCI appointed him as the35th Chairman. Dada feels that there will be a cut throat competition in coming worldcup. He wants you, the future data analysts to help him perform criclytics by analyzing the data and come up with patterns which will help us in bring the cup to home this time. I am sure you will do the needful. ALL THE BEST!
# 
# **Note:** You need to make use of Pandas to perform the CRICLYTICS on the given cricket dataset and come up with potential patterns.
# 
# ---

# # CRICKET WORLD CUP 2023

# ### The 2023 Men's ICC Cricket World Cup will be the 13th edition of the ICC Men's Cricket World Cup, scheduled to be hosted by India during October and November 2023. 
# 
# This will be the first time the competition is held completely in India.

# #### NOTE: The analysis is done on previous year's 2019 dataset cosidering the venue of Cricket World Cup 2023

# In[1]:


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import seaborn as sns
import matplotlib.pyplot as plt


# ### IMPORTING DATASETS

# In[2]:


batsman_data      = pd.read_csv('Batsman_Data.csv')
bowlers_data      = pd.read_csv('Bowler_data.csv')
ground_avg        = pd.read_csv('Ground_Averages.csv')
odi_match_results = pd.read_csv('ODI_Match_Results.csv')
odi_match_totals  = pd.read_csv('ODI_Match_Totals.csv')
wc_players        = pd.read_csv('WC_players.csv')


# ### LIST OF INDIAN PLAYERS

# In[3]:


df = wc_players[(wc_players['Country']=='India')]
df


# ### BOWLING PERFORMANCE

# In[4]:


IndianPlayers_ID = [253802, 34102, 28235, 422108, 477021, 28081, 290716, 
                    30045, 430246,559235, 326016, 625383, 625371, 234675, 481896]
indianbowler_id = bowlers_data[(bowlers_data['Player_ID'].isin(IndianPlayers_ID))]

IndianGround = ['Nagpur','Kolkata','Delhi','Dharamsala','Visakhapatnam','Guwahati','Thiruvananthapuram','Chennai',
                'Cuttack','Ahmedabad','Indore','Kochi','Pune','Mumbai (BS)','Kanpur','Rajkot','Jaipur','Mumbai',
                'Hyderabad (Deccan)','Ranchi','Hyderabad (Sind)','Bengaluru','Chandigarh','Dehradun']
indianground = bowlers_data[(bowlers_data['Ground'].isin(IndianGround))]

overs_notnull = bowlers_data[(bowlers_data['Overs'] != '-')]

opp_india = bowlers_data[(bowlers_data['Opposition'] == 'v India')]

wkts_notzero = bowlers_data[(bowlers_data['Wkts']!= 0)]


# #### Indian Bolwers

# In[5]:


b1 = indianbowler_id.iloc[:]
b2 = indianground.iloc[:]
b3 = overs_notnull.iloc[:]

BO1 = pd.merge(b1,b2,how='inner')
Indian_Bowler_Stats = pd.merge(BO1,b3,how='inner')

Indian_Bowler_Stats


# In[6]:


fig = go.Figure(go.Bar(
    x = [Indian_Bowler_Stats['Opposition'],Indian_Bowler_Stats['Wkts']],
    y = Indian_Bowler_Stats['Bowler']     
))

fig.update_yaxes(
    title = 'INDIAN BOWLERS & GROUND',
    showgrid=True,
)
fig.update_layout( 
    title = 'WICKETS OVER INDIAN GROUND'
)
fig.show()


# In[7]:


fig = px.line(Indian_Bowler_Stats, 
              x = 'Econ', 
              y = 'Bowler', 
              title='INDIAN BOLWER ECONOMIC RATE')
fig.show()


# #### Bowlers Against Indian Team :Overseas Bowlers

# In[8]:


d1 = opp_india.iloc[:]
d2 = overs_notnull.iloc[:]
d3 = wkts_notzero.iloc[:]
d4 = indianground.iloc[:]

D1 = pd.merge(d1,d2,how='inner')
D2 = pd.merge(D1,d3,how='inner')
Overseas_Bowler_Stats = pd.merge(D2,d4,how='inner')

Overseas_Bowler_Stats


# In[9]:


fig = go.Figure(go.Bar(
    x = Overseas_Bowler_Stats['Bowler'],
    y = [Overseas_Bowler_Stats['Wkts'],Overseas_Bowler_Stats['Ground']],
))

fig.update_xaxes( title = 'Overseas Bowler')
fig.update_yaxes( title = 'Wickets Per Match')
fig.update_layout( title = '<b>OVERSEAS BOWLERS WICKETS RATE TOWARDS INDIAN GROUND<b>')
fig.show()


# In[10]:


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=Overseas_Bowler_Stats['Bowler'],
        y=Overseas_Bowler_Stats['Mdns'],
        name="Maiden Over"
    ))

fig.add_trace(
    go.Bar(
        x=Overseas_Bowler_Stats['Bowler'],
        y=Overseas_Bowler_Stats['Wkts'],
        name="Wickets"
    ))
fig.update_layout( 
    title = 'DIFF ON WICKETS & MAIDEN'
)
fig.update_yaxes( 
    title = 'WICKETS & MAIDEN'
)
fig.show()


# ### BATTING PERFORMANCE 

# In[11]:


IndianPlayers_ID = [253802, 34102, 28235, 422108, 477021, 28081, 290716, 30045, 
                    430246, 559235, 326016, 625383, 625371, 234675, 481896]
indianbatter_id = batsman_data[(batsman_data['Player_ID'].isin(IndianPlayers_ID))]

IndianGround = ['Nagpur','Kolkata','Delhi','Dharamsala','Visakhapatnam','Guwahati','Thiruvananthapuram','Chennai',
                'Cuttack','Ahmedabad','Indore','Kochi','Pune','Mumbai (BS)','Kanpur','Rajkot','Jaipur','Mumbai',
                'Hyderabad (Deccan)','Ranchi','Hyderabad (Sind)','Bengaluru','Chandigarh','Dehradun']
indianground = batsman_data[(batsman_data['Ground'].isin(IndianGround))]

Bat1=['DNB','TDNB','absent','sub']
bat1_notnull = batsman_data[(~batsman_data['Bat1'].isin(Bat1))]

opp_india = batsman_data[(batsman_data['Opposition'] == 'v India')]


# #### Indian Batsman

# In[12]:


ba1 = indianbatter_id.iloc[:]
ba2 = indianground.iloc[:]
ba3 = bat1_notnull.iloc[:]

BA1 = pd.merge(ba1,ba2,how='inner')
Batsman_indian = pd.merge(BA1,ba3,how='inner')

Batsman_indian


# In[13]:


fig = go.Figure(go.Bar(
    x = Batsman_indian['Batsman'],
    y = [Batsman_indian['Opposition'],Batsman_indian['SR']],
))

fig.update_xaxes( title = 'Indian Players')
fig.update_yaxes( title = 'Opposition Teams')
fig.update_layout(title = '<b>INDIAN BATSMAN STRIKE RATE WITH OPPOSITION TEAMS<b>')
fig.show()


# In[14]:


subject = Batsman_indian["Batsman"]
score = Batsman_indian["Runs"]
aggs = ["count","sum","avg","median","stddev","min","max"] 

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)

data = [dict(
  type = 'bar',     
  x = subject,
  y = score,
  mode = 'markers',
  marker=dict(size=[40, 60, 80, 100],
                color=[0,1,2,3]),
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>INDIAN BATSMAN STATISTICAL RECORDS</b><br>Descriptive statistical dropdown menu',
  xaxis = dict(title = 'Indian players'),
  yaxis = dict(title = 'Score statistics', range = [0,190]),
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = agg_func
  )]
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)


# In[15]:


import plotly.express as px

fig = px.bar(Batsman_indian, y='Opposition', x="Batsman", color='Opposition', orientation="v", hover_name="SR",
             #color_discrete_map={
                #"v Australia": "red",
                #"v Pakistan": "green",
                #"v Bangladesh": "blue"},
             
             title="Indian Batsmans Strike Rate [SR]"
            )

fig.show()


# #### Batsman against Indian team : Overseas Batsman

# In[16]:


da1 = opp_india.iloc[:]
da2 = indianground.iloc[:]
da3 = bat1_notnull.iloc[:]

DA1 = pd.merge(da1,da2,how='inner')
Batsman_Against_India = pd.merge(DA1,da3,how='inner')

Batsman_Against_India


# In[17]:



my_count=Batsman_Against_India["Ground"]
df = pd.DataFrame({
                "Ground": Batsman_Against_India["Ground"],
                "Runs": Batsman_Against_India["Runs"],
                "Bat1": Batsman_Against_India["Bat1"]
                })
 
# Create a grid : initialize it
g = sns.FacetGrid(df, col='Ground', hue='Ground', col_wrap=4, )
 
# Add the line over the area with the plot function
g = g.map(plt.plot, 'Runs', 'Bat1')
 
# Fill the area with fill_between
g = g.map(plt.fill_between, 'Runs', 'Bat1', alpha=0.5).set_titles("{col_name} Ground")
 
# Control the title of each facet
g = g.set_titles("{col_name}")
 
# Add a title for the whole plo
plt.subplots_adjust(top=0.92)
g = g.fig.suptitle('Evolution Boundaries in different ground')


# ### GROUND PERFORMANCE

# In[18]:


ground_avg


# In[19]:


fig = go.Figure(go.Scatter(
    x = ground_avg['Ground'],
    y = ground_avg['Runs'],
))

fig.update_layout(
    title = 'RUNS OVER DIFFERENT GROUND',
    #xaxis_tickformat = '%d %B (%a)<br>%Y'
)

fig.show()


# In[20]:


fig = go.Figure(go.Bar(
    x = ground_avg['Ground'],
    y = ground_avg['Wkts'],
))

fig.update_layout(
    title = 'WICKETS OVER DIFFERENT GROUND',
    
)

fig.show()


# In[21]:


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=ground_avg['Ground'],
        y=ground_avg['RPO'],
        name="Runs Per Over"
    ))

fig.add_trace(
    go.Bar(
        x=ground_avg['Ground'],
        y=ground_avg['Ave'],
        name="Runs Per Wickets"
    ))

fig.update_layout(
    title = 'Runs Per Over Vs Runs Per Wickets in Different Grounds',
    
)

fig.show()


# In[22]:


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=ground_avg['Span'],
        y=ground_avg['RPO'],
        name="Runs Per Over"
    ))

fig.add_trace(
    go.Bar(
        x=ground_avg['Span'],
        y=ground_avg['Ave'],
        name="Runs Per Wickets"
    ))

fig.update_layout(
    title = 'Runs Per Over Vs Runs Per Wickets in Different Spans',
    
)

fig.show()


# In[23]:


df=ground_avg
fig = px.scatter(ground_avg, 
                 x=ground_avg['Mat'], 
                 y=ground_avg['Won'], 
                 size="Tied", 
                 color="Won",
           hover_name="Span", log_x=True, size_max=60)

fig.update_layout(
    title = 'Year wise Number of matches and winning & Tied matches count',
    
)
fig.show()


# In[24]:


df = ground_avg
fig = px.scatter(df, x="Mat", y="Runs", animation_frame="Span", animation_group="Runs",
                     size="Runs",color="Runs", hover_name="Won")
fig.show()


# In[25]:



fig = px.bar_polar(ground_avg, r="Mat", theta="Runs", color="Span",
                   color_discrete_sequence= px.colors.sequential.Plasma_r,
                   title="Part of a continuous color scale used as a discrete sequence"
                  )
fig.show()


# # FINAL TEAM SELECTION TO PLAY ON FIELD BASED ON ALL FACTORS

# In[26]:


bowler = pd.read_excel('data/Bowler_data.xlsx')
player= pd.read_csv('data/WC_players.csv')
batsman=pd.read_csv('data/Batsman_data.csv')
newteam=pd.read_csv('data/Players.csv')


# In[27]:


indian=player.loc[player['Country'] =='India']
indian


# ### BATSMEN PERFORMANCE

# In[28]:


cricket_batsman={}


# In[29]:


# Removing null values
bowler=bowler.dropna()
batsman=batsman.dropna()


# In[30]:


# Adding details to dict about batsman
for i in indian['ID']:
    for j in batsman['Player_ID']:
        if i==j:
            a=batsman.loc[batsman['Player_ID'] == i]
            run=a['Runs'].mean()
            fours=a['4s'].sum()
            sixs=a['6s'].sum()
            sr=a['SR'].mean()
            cricket_batsman[i]=[run,fours,sixs,sr]


# In[31]:


cricket_batsman


# In[32]:


bats=pd.DataFrame.from_dict(cricket_batsman).T


# In[33]:


bats=bats.rename(columns={0:"Runs",1:"4s",2:"6s",3:"SR"})
bats


# ### BOWLERS PERFORMANCE

# In[34]:


#empty dict for bowlers
cricket_bowler={}


# In[35]:


#addding details of bowlers to dict
for i in indian['ID']:
    for j in bowler['Player_ID']:
        if i==j:
            a=bowler.loc[bowler['Player_ID'] == i]
            over=a['Overs'].sum()
            mdns=a['Mdns'].sum()
            runs=a['Runs'].sum()
            wkts=a['Wkts'].sum()
            eco=a['Econ'].mean()
            ave=a['Ave'].mean()
            sr=a['SR'].mean()
            cricket_bowler[i]=[over,mdns,runs,wkts,eco,ave,sr]
balls=pd.DataFrame.from_dict(cricket_bowler).T
balls=balls.rename(columns={0:"Overs",1:"MDNS",2:"Runs",3:"WKTS",4:"ECO",5:"AVE",6:"SR"})
balls


# ### SELECTION

# In[36]:


# Selecting Top 6 batsman
bats=bats.sort_values(['6s','SR'],ascending=False)
bats=bats.head(6)
bats


# In[37]:


# Selecting Top 6 bowlers
balls=balls.sort_values(['ECO'],ascending=True)
balls=balls.head(6)
balls


# In[38]:


# Common players 
playerid_bats=bats.index
bats_list=set(playerid_bats)
playerid_balls=balls.index
balls_list=set(playerid_balls)
bats_list.intersection(balls_list)


# In[39]:


# Making list of playres
players=[]
bats_list=list(playerid_bats)
balls_list=list(playerid_balls)
for i in bats_list:
    if i not in players:
        players.append(i)
for i in balls_list:
    if i not in players:
        players.append(i)


# ### LIST OF PLAYERS ON FIELD FOR 2023 WORLD CUP

# In[40]:


f_l=[]
for i in players:
    for j in list(indian['ID']):
        if i==j:
            a=indian.loc[indian['ID'] == i]
            a=a.drop(['ID','Country'],axis=1)
            k= a.to_string(index=False,header=False)
            f_l.append(k)


# In[41]:


import numpy as np
S=pd.DataFrame(np.array(f_l).reshape(len(f_l)))
S.columns=['Player']
S
#pd.DataFrame(np.array(f_l).reshape(-1,len(f_l)))


# ## INFERENCES:
# 
# #### Based on the performance of the team members we need a change in the team.
# 
# * MS Dhoni has taken retirement
# 
# * Dinesh Kartik and Vijay Shankar can be removed
# 
# * New young members can be included like Shreyas Iyer, Prithvi Shaw, Washington Sundar, Navdeep Saini, Devdutt Padikalal,Varun Chakravorthy
# 
# * Virat Kohli(Captain)
# 
# * Rohit Sharma(Vice Captain)

# In[42]:


TEAM_2023=pd.DataFrame(newteam)
TEAM_2023

