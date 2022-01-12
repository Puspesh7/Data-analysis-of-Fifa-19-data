#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:14:51 2022

@author: hsjhinkwan
"""
#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px

#%%
import warnings
warnings.simplefilter(action='ignore',category=Warning)

pd.set_option('display.max_columns',None)

fifa = pd.read_csv('/Users/hsjhinkwan/Desktop/Fifa 19 analysis/data.csv')

fifa.head()

#%%

fifa.info()

#%%

# Dropping unaccessary features from the dataset.

fifa.drop(['ID','Photo','Flag','Club Logo','Real Face','Jersey Number','Loaned From'],axis=1,inplace=True)

#%%
# Data Cleaning

# For numerical features, the missing values will be replaced by mean value of the feature column

fifa['International Reputation'].fillna(fifa['International Reputation'].mean(),inplace=True)
fifa['Weak Foot'].fillna(fifa['Weak Foot'].mean(),inplace=True)
fifa['Skill Moves'].fillna(fifa['Skill Moves'].mean(),inplace=True)
fifa['Crossing'].fillna(fifa['Crossing'].mean(),inplace=True)
fifa['Finishing'].fillna(fifa['Finishing'].mean(),inplace=True)
fifa['HeadingAccuracy'].fillna(fifa['HeadingAccuracy'].mean(),inplace=True)
fifa['ShortPassing'].fillna(fifa['ShortPassing'].mean(),inplace=True)
fifa['Volleys'].fillna(fifa['Volleys'].mean(),inplace=True)
fifa['Dribbling'].fillna(fifa['Dribbling'].mean(),inplace=True)
fifa['Curve'].fillna(fifa['Curve'].mean(),inplace=True)
fifa['FKAccuracy'].fillna(fifa['FKAccuracy'].mean(),inplace=True)
fifa['LongPassing'].fillna(fifa['BallControl'].mean(),inplace=True)
fifa['Acceleration'].fillna(fifa['Acceleration'].mean(),inplace=True)
fifa['SprintSpeed'].fillna(fifa['SprintSpeed'].mean(),inplace=True)
fifa['Agility'].fillna(fifa['Agility'].mean(),inplace=True)
fifa['Reactions'].fillna(fifa['Reactions'].mean(),inplace=True)
fifa['Balance'].fillna(fifa['Balance'].mean(),inplace=True)
fifa['ShotPower'].fillna(fifa['ShotPower'].mean(),inplace=True)
fifa['Jumping'].fillna(fifa['Jumping'].mean(),inplace=True)
fifa['Stamina'].fillna(fifa['Stamina'].mean(),inplace=True)
fifa['Strength'].fillna(fifa['Strength'].mean(),inplace=True)
fifa['LongShots'].fillna(fifa['LongShots'].mean(),inplace=True)
fifa['Aggression'].fillna(fifa['Aggression'].mean(),inplace=True)
fifa['Interceptions'].fillna(fifa['Interceptions'].mean(),inplace=True)
fifa['Positioning'].fillna(fifa['Positioning'].mean(),inplace=True)
fifa['Vision'].fillna(fifa['Vision'].mean(),inplace=True)
fifa['Penalties'].fillna(fifa['Penalties'].mean(),inplace=True)
fifa['Composure'].fillna(fifa['Composure'].mean(),inplace=True)
fifa['Marking'].fillna(fifa['Marking'].mean(),inplace=True)
fifa['StandingTackle'].fillna(fifa['StandingTackle'].mean(),inplace=True)
fifa['SlidingTackle'].fillna(fifa['SlidingTackle'].mean(),inplace=True)
fifa['GKDiving'].fillna(fifa['GKDiving'].mean(),inplace=True)
fifa['GKHandling'].fillna(fifa['GKHandling'].mean(),inplace=True)
fifa['GKKicking'].fillna(fifa['GKKicking'].mean(),inplace=True)
fifa['GKPositioning'].fillna(fifa['GKPositioning'].mean(),inplace=True)
fifa['GKReflexes'].fillna(fifa['GKReflexes'].mean(),inplace=True)

#%%

# preprocessing for value, wage and release clause conversion

def value_wage_conversion(value):
  if(isinstance(value,str)):
    out = value.replace('€','')
    if 'M' in out:
      out = float(out.replace('M',''))*1000000
    elif 'K' in out:
      out = float(out.replace('K',''))*1000
    return float(out)

fifa['Value'] = fifa['Value'].apply(lambda x : value_wage_conversion(x))
fifa['Wage'] = fifa['Wage'].apply(lambda x : value_wage_conversion(x))
fifa['Release Clause'] = fifa['Release Clause'].apply(lambda x : value_wage_conversion(x))
fifa['Release Clause'].fillna(fifa['Release Clause'].mean(),inplace=True)

#%%

# dealing with club and position, categorical
fifa['Club'].fillna('No Club',inplace=True)
fifa['Position'].fillna('unknown',inplace=True)

#%%
# dealing with joining date
def convert_date(value):
  l=[]
  if isinstance(value,str):
    l = value.split(',')
    return l[-1]

fifa['Joined'] = fifa['Joined'].replace(np.nan,"NA")
fifa['Joined'] = fifa['Joined'].apply(lambda x : convert_date(x))

#%%

def height_converter(value):
  l=[]
  if isinstance(value,str):
    l = value.split("'")
    return (float(l[0])*30.4)+(float(l[1])*2.5)

def weight_converter(value):
  if isinstance(value,str):
    value = value.replace("lbs","")
    return float(value)*0.45

fifa['Height'] = fifa['Height'].apply(lambda x : height_converter(x))
fifa['Height'].fillna(fifa['Height'].mean(),inplace=True)
fifa['Weight'] = fifa['Weight'].apply(lambda x : weight_converter(x))
fifa['Weight'].fillna(fifa['Weight'].mean(),inplace=True)

#%%
fifa.head()

#%%

fifa['Work Rate'].fillna("Medium/Medium",inplace=True)
fifa['Preferred Foot'].fillna("Right",inplace=True)

#%%

fifa['Body Type'].value_counts()

#%%
fifa['Body Type'][fifa['Body Type']== 'Messi'] = 'Normal'
fifa['Body Type'][fifa['Body Type']== 'Neymar'] = 'Normal'
fifa['Body Type'][fifa['Body Type']== 'Afinfenwa'] = 'Normal'
fifa['Body Type'][fifa['Body Type']== 'Courtois'] = 'Normal'
fifa['Body Type'][fifa['Body Type']== 'Shaqiri'] = 'Normal'
fifa['Body Type'][fifa['Body Type']== 'C. Ronaldo'] = 'Normal'
fifa['Body Type'][fifa['Body Type']== 'PLAYER_BODY_TYPE_25'] = 'Normal'

#%%

def skill_converter(s):
    if isinstance(s,str):
        return float(s[0:2])+float(s[-1])

skill_columns = ['LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']
for i in skill_columns:
    fifa[i] = fifa[i].apply(lambda x : skill_converter(x))
    fifa[i].fillna(0.0,inplace=True)
    
fifa['Body Type'].fillna('Normal',inplace=True)

#%%

fifa['LS']

#%%

fifa.info()

#%%

# Distribution of age for eah players

ages = fifa['Age']
plt.figure(figsize=(10,8))
ax = sns.countplot(ages,color='#00ffff')
ax.set_xlabel(xlabel="Age of players",fontsize=16)
ax.set_title(label="Distribution of Age of Players",fontsize=20)
plt.show()


#%%

# Distribution of Age vs Overall and Age vs Potential of Players

overall_1 = pd.DataFrame(fifa.groupby(['Age'])['Overall'].mean())
potential_1 = pd.DataFrame(fifa.groupby(['Age'])['Potential'].mean())

merged = pd.merge(overall_1,potential_1,on='Age',how='inner')
merged['Age'] = merged.index
plt.plot(merged['Age'],merged['Overall'],marker='.',label='Overall')
plt.plot(merged['Age'],merged['Potential'],marker='.',label='Potential')
plt.xlabel(xlabel='Age')
plt.ylabel(ylabel='Value')
plt.title(label='Age vs Overall and Potetial Distribution')
plt.legend()
plt.show()

#%%


# Distribution of Clubs and their average value of players

club_1 = fifa.groupby('Club')['Value'].mean()

clubs_2 = pd.DataFrame(club_1)
clubs_2.sort_values('Value',ascending=False,inplace=True)

clubs_2['Club'] = clubs_2.index

plt.figure(figsize=(20,8))

plt.barh(clubs_2['Club'].head(10),clubs_2['Value'].head(10))
plt.xlabel(xlabel='Value')
plt.ylabel(ylabel='Club')
plt.title(label='Average value of players by club')
plt.show()


#%%

# distribution of Clubs and their average overall ratinf of players

test = fifa.groupby('Club')['Overall'].mean()
clubs_overall = pd.DataFrame(test)
clubs_overall.sort_values('Overall',ascending=False,inplace=True)

clubs_overall['Club'] = clubs_overall.index

plt.figure(figsize=(20,8))

plt.barh(clubs_overall['Club'].head(10),clubs_overall['Overall'].head(10))
plt.xlabel(xlabel='Overall')
plt.ylabel(ylabel='Club')
plt.title(label='Average overall by clubs')
plt.show()

#%%

player_features = ['Crossing', 'Finishing', 'HeadingAccuracy',
       'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
       'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
       'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping',
       'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions',
       'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking',
       'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes']
df_postion  = pd.DataFrame()
for position_name, features in fifa.groupby(fifa['Position'])[player_features].mean().iterrows():
    top_features = dict(features.nlargest(5))
    df_postion[position_name] = tuple(top_features)
df_postion.head()

#%%

# best team formation

position = []
player = []
club_l = []
for col in df_postion.columns:
    tmp_df = pd.DataFrame()
    l = [df_postion[col].values]
    l = l[0]
    l = list(l)
    l.append('Name')
    tmp_df = pd.DataFrame.copy(fifa[fifa['Position'] == col][l])
    tmp_df['mean'] = np.mean(tmp_df.iloc[: , :-1] , axis = 1)
    name = tmp_df['Name'][tmp_df['mean'] == tmp_df['mean'].max()].values[0]
    club = fifa['Club'][fifa['Name'] == str(name)].values[0]
    position.append(col)
    player.append(name)
    club_l.append(club)
    
gk = ['GK']
forward = ['LS', 'ST', 'RS','LF', 'CF', 'RF']
midfeilder = ['LW','RW', 'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM',
              'RCM', 'RM', 'LDM', 'CDM', 'RDM' ]
defenders = ['LWB','RWB', 'LB', 'LCB', 'CB',]

print('GoalKeeper : ')
for p , n , c in zip(position , player , club_l):
    if p in gk:
        print('{} [Club : {} , Position : {}]'.format(n , c , p))
print('\nFORWARD : ')
for p , n , c in zip(position , player , club_l):
    if p in forward:
        print('{} [Club : {} , Position : {}]'.format(n , c , p))
print('\nMIDFEILDER : ')
for p , n , c in zip(position , player , club_l):
    if p in midfeilder:
        print('{} [Club : {} , Position : {}]'.format(n , c , p))
print('\nDEFENDER : ')
for p , n , c in zip(position , player , club_l):
    if p in defenders:
        print('{} [Club : {} , Position : {}]'.format(n , c , p))
        

        
#%%
        
CAM = 'H. Nakagawa'
CB = 'D. Godín'
CDM = 'Casemiro'
CF = 'S. Giovinco'
CM = 'N. Keïta'
GK = 'De Gea'
LAM = 'Paulo Daineiro'
LB = 'Jordi Alba'
LCB = 'G. Chiellini'
LCM = 'David Silva'
LDM = 'N. Kanté' 
LF = 'E. Hazard' 
LM = 'Douglas Costa' 
LS = 'J. Martínez' 
LW = 'Neymar Jr' 
LWB = 'M. Pedersen' 
RAM = 'J. Cuadrado' 
RB = 'Nélson Semedo' 
RCB = 'Sergio Ramos' 
RCM = 'L. Modrić' 
RDM = 'P. Pogba' 
RF = 'L. Messi' 
RM = 'Gelson Martins' 
RS = 'A. Saint-Maximin' 
RW = 'R. Sterling' 
RWB = 'M. Millar' 
ST = 'Cristiano Ronaldo' 

#%%

def create_football_formation(formation = [] , label_1 = None ,
                              label_2 = None , label_3 = None ,
                              label_4 = None,label_4W = None ,
                              label_5 = None , label_3W = None):
    
    plt.scatter(x = [1] , y = [6] , s = 300 , color = 'blue')
    plt.annotate('De Gea \n(Manchester United)' , (1 - 0.5 , 6 + 0.5))
    plt.plot(np.ones((11 , ))*1.5 , np.arange(1 , 12) , 'w-')
    plt.plot(np.ones((5 , ))*0.5 , np.arange(4 , 9) , 'w-')
    
    n = 0
    for posi in formation:
        if posi ==  1:
            n += 3
            dot = plt.scatter(x = [n]  , y = [6] , s = 400 , color = 'white')
            plt.scatter(x = [n]  , y = [6] , s = 300 , color = 'red')
            for i, txt in enumerate(label_1):
                txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')')
                plt.annotate(txt, ( n-0.5 , 6+0.5))
            
        elif posi == 2:
            n += 3
            y = [5 , 7.5]
            x = [ n , n ]
            plt.scatter(x  , y , s = 400 , color = 'white')
            plt.scatter(x  , y , s = 300 , color = 'red')
            for i, txt in enumerate(label_2):
                txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')') 
                plt.annotate(txt, (x[i] - 0.5, y[i]+0.5))
        elif posi == 3:
            n+=3
            y = [3.333 , 6.666 , 9.999]
            x = [n , n  , n ]
            plt.scatter(x  , y , s = 400 , color = 'white')
            plt.scatter(x  , y , s = 300 , color = 'red')
            for i, txt in enumerate(label_3):
                txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')')
                plt.annotate(txt, (x[i] - 0.5, y[i]+0.5))
            
            if not label_3W == None:
                n+=3
                y = [3.333 , 6.666 , 9.999]
                x = [n , n  , n ]
                plt.scatter(x  , y , s = 400 , color = 'white')
                plt.scatter(x  , y , s = 300 , color = 'red')
                for i, txt in enumerate(label_3W):
                    txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')')
                    plt.annotate(txt, (x[i] - 0.5, y[i]+0.5))
            
        elif posi == 4 and not label_4 == None:
            n+=3
            y = [2.5 , 5 , 7.5 , 10]
            x = [n , n  , n , n ]
            plt.scatter(x  , y , s = 400 , color = 'white')
            plt.scatter(x  , y , s = 300 , color = 'red')
            for i, txt in enumerate(label_4):
                txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')')
                plt.annotate(txt, (x[i] - 0.5, y[i]+0.5))
                
            if not label_4W == None:
                n+=3
                y = [2.5 , 5 , 7.5 , 10]
                x = [n , n  , n , n ]
                plt.scatter(x  , y , s = 400 , color = 'white')
                plt.scatter(x  , y , s = 300 , color = 'red')
                for i, txt in enumerate(label_4W):
                    txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')')
                    plt.annotate(txt, (x[i] - 0.5, y[i]+0.5))
                
                
        elif posi == 5:
            n+=3
            y = [2 , 4 , 6 , 8 , 10]
            x = [n , n , n  , n  , n]
            plt.scatter(x  , y , s = 400 , color = 'white')
            plt.scatter(x  , y , s = 300 , color = 'red')
            for i, txt in enumerate(label_5):
                txt = str(txt+'\n('+fifa['Club'][fifa['Name'] == txt].values[0]+')')
                plt.annotate(txt, (x[i] - 0.5, y[i]+0.5))
            
    plt.plot(np.ones((5 , ))*(n+0.5) , np.arange(4 , 9) , 'w-')
    plt.plot(np.ones((11 , ))*(n/2) , np.arange(1 , 12) , 'w-')
    plt.yticks([])
    plt.xticks([])
    ax = plt.gca()
    ax.set_facecolor('#28fc03')
                     
#%%
    
plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 ] , 
                         label_4 = [LWB , LCB , RCB , RWB],
                         label_4W = [LW , LCM , CM , RW],
                         label_2 = [LF , RF],
                         )
plt.title('Best Fit for formation 4-4-2')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 ] , 
                         label_4 = [LB , CB , RCB , RB],
                         label_4W = [LAM , LDM , RDM , RAM],
                         label_2 = [LS , RS],
                         )
plt.title('OR\nBest Fit for formation 4-4-2')
plt.show()


plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 ] , 
                         label_4 = [LB , CB , RCB , RB],
                         label_4W = [LW , LDM , RDM , RW],
                         label_2 = [CF , ST],
                         )
plt.title('OR\nBest Fit for formation 4-4-2')
plt.show()


plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 ] , 
                         label_4 = [LB , CB , RCB , RB],
                         label_4W = [LW , LCM , RCM , RW],
                         label_2 = [CF , ST],
                         )
plt.title('OR\nBest Fit for formation 4-4-2')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 ] , 
                         label_4 = [LWB , LCB , RCB , RWB],
                         label_4W = [LW , LCM , CM , RW],
                         label_2 = [LF , RF],
                         )
plt.title('OR\nBest Fit for formation 4-4-2')
plt.show()


plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 , 3 , 1] , 
                         label_4 = [LWB , LCB , RCB , RWB],
                         label_2 = [LCM , RCM],
                         label_3 = [LF , CAM , RF],
                         label_1 = [ST])
plt.title('Best Fit for formation 4-2-3-1')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 , 3 , 1] , 
                         label_4 = [LWB , LB , RB , RWB],
                         label_2 = [LAM , RAM],
                         label_3 = [LW , CF , RW],
                         label_1 = [ST])
plt.title('OR\nBest Fit for formation 4-2-3-1')
plt.show()

plt.figure(1 , figsize = (15 , 7))
create_football_formation(formation = [ 4 , 2 , 3 , 1] , 
                         label_4 = [LWB , CB , RCB , RWB],
                         label_2 = [CM , CAM],
                         label_3 = [LF , CM , RF],
                         label_1 = [ST])
plt.title('OR\nBest Fit for formation 4-2-3-1')

plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 2 , 3 , 1] , 
                         label_4 = [LWB , LCB , RCB , RWB],
                         label_2 = [LCM , RCM],
                         label_3 = [LDM , CAM , RDM],
                         label_1 = [ST])
plt.title('OR\nBest Fit for formation 4-2-3-1')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 5, 4 , 1 ] , 
                         label_5 = [LWB , LCB , CB , RCB , RWB],
                         label_4 = [LW, LDM , RDM , RW],
                         label_1 = [ST])
plt.title('Best Fit for formation 5-4-1')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 3 ] , 
                         label_4 = [LWB , LCB , RCB , RWB],
                         label_3 = [LW, CAM , RW],
                         label_3W = [LF , ST , RF])
plt.title('Best Fit for formation 4-3-3')
plt.show()


plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 3 ] , 
                         label_4 = [LWB , CB , RB , RWB],
                         label_3 = [LAM, CM , RAM],
                         label_3W = [LS , CF , RS])
plt.title('OR\nBest Fit for formation 4-3-3')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 3 ] , 
                         label_4 = [LB , LCB , RCB , RB],
                         label_3 = [LDM, CDM , RDM],
                         label_3W = [LF , CF , RF])
plt.title('OR\nBest Fit for formation 4-3-3')
plt.show()

plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 3] , 
                         label_4 = [LWB , CB , RB , RWB],
                         label_3 = [LAM, CAM , RAM],
                         label_3W = [LS , ST , RS])
plt.title('OR\nBest Fit for formation 4-3-3')
plt.show()


plt.figure(1 , figsize = (15 , 7))           
create_football_formation(formation = [ 4 , 3] , 
                         label_4 = [LWB , CB , RB , RWB],
                         label_3 = [LCM, CAM , RCM],
                         label_3W = [LF , ST , RF])
plt.title('OR\nBest Fit for formation 4-3-3')
plt.show()

        




