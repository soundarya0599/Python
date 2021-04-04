#!/usr/bin/env python
# coding: utf-8

# # <center> PROGRAM 8: PIVOTING USING PANDAS IN PYTHON </center>
# 
# ---

# ## DESCRIPTION:	
#     Mr. Jeff Bezos, the CEO of Amazon wants an immediate report of sales of products from Amazon for the fiscal year 2019-2020 (only for the USA). He is looking forward towards you, the emerging data analysts to help him in analyzing the data and come up with potential observations that can help him in improving his business. Do lend a helping hand so that your report helps him in better decision making.
#         
#     NOTE: Use the concept of pivot_table(), query() and aggregation mandatorily to accomplish the task.

# ## Importing required library & data.!

# In[2]:


import calendar
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.io as pio
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# In[3]:


Data = pd.read_excel(open('test.xlsx','rb'),sheet_name='Sheet1')
Original = Data
Data.head(7)


# ## Data Cleaning,Data Transformation,Combining Data

# In[4]:


# Distinct

DistinctCount_Data = Data.nunique(axis=0) 
print(DistinctCount_Data)


# In[5]:


# Checking NaN

Checking_NaN = Data[Data.isna().any(axis=1)]
Checking_NaN.head()


# In[6]:


# Converting sales amount, Calculating Unit price, Month format and Adding Location info.

Data["Sales"] = round(Data.Sales_in_M * 1000000)
Data["Unit_Price"] = round(Data.Sales/Data.Qty,2)
Data["loc"] = Data.City+'('+Data.Code+')'
Data.drop(Data.columns[[2]], axis = 1, inplace = True)
Data['Month'] = Data['Month'].apply(lambda x: calendar.month_abbr[x])
Data.head(5)


# In[7]:


Data.drop(Data.columns[[9]], axis = 1, inplace = True) 
Original = Data
Data.keys()


# ## Data Exploration, Analysis & Presentation 

# In[8]:


# Segment

report_a = pd.pivot_table(Data,index=["Segment"])
report_a


# In[9]:


height = report_a["Sales_in_M"]
bars = ("Consumer","Corporate","Home Office")
y_pos = np.arange(len(bars))

plt.bar(y_pos, height, color=(0.7, 0.3, 0.4, 0.6))
plt.xticks(y_pos, bars)
plt.title("Segment wise annual report",fontweight="bold")
plt.ylabel("Sales in USD ($)")
plt.show()


# ###        Interpretation for Segment wise annual report:
#                 Highest Turnover    - Home Office
#                 Average Turnover    - Corporate
#                 Lowest  Turnover    - Consumer

# In[10]:


# Sales Mean value by double indexing Segment & Category.

report_b = pd.pivot_table(Data,
                          index=["Segment","Category"],
                          values=["Sales_in_M"],
                          aggfunc=[np.sum,np.mean,np.std]
                         )
report_b


# In[11]:


report_b = report_b.reset_index()
report_b.columns=["Segment","Category","Sales_Sum","Sales_mean","Sales_std"]
fig = px.line(report_b, 
              x="Segment", y="Sales_mean",
              height=350, color='Category',
              title='Sales Mean value'
             )
fig.show()


# ###        Interpretation for Sales Mean-Values
#                 Notably products under:- 
#                 
#                     Technology Category under every segments proving higher revenue in sales.
#                     Where,
#                     Office Supplies left idle and Furniture sales remains consistance.
#                     
#                     Comparision wise Furniture is falling down but Office supplies remains constant.
#                 

# In[12]:


# Segment & Category in details

report_c = pd.pivot_table(Data,
                          index=["Segment","Category"],
                          values=["Qty"],
                          aggfunc=[np.sum,np.max,np.min]
                         )
report_c


# In[13]:


report_c = report_c.reset_index()  
report_c.columns=["Segment","Category","Total_Quantity","Max_Quantity","Min_Quantity"]

fig = px.bar(report_c, x="Segment", y="Total_Quantity",
             color='Category', barmode='group',
             title="Segment-wise Category Report", height=350)
fig.show()


# ###         Insight form products and their sales quantity
# 
#                As per previous figure interpretation, we concluded that Technology lead on company revenue. 
#                But here, Technology pulled to bottom.
#                
#                It's clearly shoes that's Quantity wise Technology based products sold very less comparatively.
#                But Technology was been expensive then other category. 
#                

# In[14]:


# State wise, Category profit aggregation

report_d = pd.pivot_table(Data,
               index=["Segment","State"],
               values=["Sales_in_M"],
               columns=["Category"],
               aggfunc=[np.sum, np.max, np.min],fill_value=0)
report_d


# In[15]:


report_d.query('Segment == ["Corporate"] & State == ["New Jersey","New Mexico","New York"]')


# In[16]:


report_d.query('State == ["California","Georgia","Texas","Washington"]')


# ### Insights:
# 
#         Segment & State-wise indexing,
#         Over Categories-wise SUM, MAX, MIN sales report. 
#         
#         Insight will be used to analysis data through diffferent perspective
# 

# In[17]:


# Sub-Category level

report_e = pd.pivot_table(Data,
                          index=["Category","SubCategory"],
                          values=["Sales_in_M","Qty"],
                          aggfunc=[np.sum]
                         )
report_e


# In[18]:


report_e = report_e.reset_index()  
report_e.columns=["Category","SubCategory","TotalQuantity","TotalSales"]
fig = px.bar(report_e, 
             x="Category", y="TotalQuantity", 
             color="SubCategory",
             title="Category"
            )
fig.show()


# ### Interpretation for Category and sub category wise annual report:
# 
#             Furnishings from Furniture & Binders, Paper from Office Supplies sold higher by product units.
#             Accessories and Phones from Technology category shows higher in product sales.
#             
#             So considering future earth and eco-friendly environment,
#             we promote valueable #GoGreen methods among every dealers and customers. 
#             Tech gaint Apple Inc. announced their revised policy. 
#     

# In[19]:


# Customer geographics analysis

report_f = pd.pivot_table(Data,
                          index=["State","Code"],
                          values=["CustomerName"],
                          aggfunc=[np.count_nonzero]
                         )
report_f


# In[20]:


report_f = report_f.reset_index()  
report_f.columns=["State","Code","TotalCustomers"]
report_f.sort_values(by=['TotalCustomers'], inplace=True, ascending=False)
df = report_f
report_f.head(7)


# In[21]:



fig = go.Figure(data=go.Choropleth(
locations=df['Code'],                   # Spatial coordinates
z = df['TotalCustomers'].astype(float), # Data to be color-coded
locationmode = 'USA-states',            # set of locations match entries in `locations`
colorscale = 'sunset',
text=df['State'] ,                      # hover text
colorbar_title = "No. of Customer's",
))
fig.update_layout(
    title_text = 'Total number of Customers by State',
    geo_scope='usa', # limite map scope to USA
)
fig.show()


# In[ ]:





# In[22]:


# Geographical based Quantity analysis

report_g = pd.pivot_table(Data,
                          index=["State","Code"],
                          values=["Qty"],
                          aggfunc=[np.sum]
                         )
report_g


# In[23]:


report_g = report_g.reset_index()  
report_g.columns=["State","Code","Qty"]
report_g.sort_values(by=['Qty'], inplace=True, ascending=False)
df = report_g
report_g


# In[24]:


fig = go.Figure(data=go.Choropleth(
    locations=df["Code"],           # Spatial coordinates
    z = df['Qty'].astype(float),    # Data to be color-coded
    locationmode = 'USA-states',    # set of locations match entries in `locations`
    colorscale = 'ylorrd',
    #text=df['loc'] ,                # hover text
    colorbar_title = "Product-wise Quantity in Millions",
))
fig.update_layout(
    title_text = 'Total number of products sold by State',
    geo_scope='usa',                # limite map scope to USA
)
fig.show()


# In[25]:


# Geographical based Sales analysis

report_h = pd.pivot_table(Data,
                          index=["State","Code"],
                          values=["Sales_in_M"],
                          aggfunc=[np.sum]
                         )
report_h.head(10)


# In[26]:


report_h = report_h.reset_index()  
report_h.columns=["State","Code","Sales_in_M"]
report_h.sort_values(by=["Sales_in_M"], inplace=True, ascending=False)
df = report_h
report_h.head()


# In[27]:


fig = go.Figure(data=go.Choropleth(
    locations=df["Code"],           # Spatial coordinates
    z = df['Sales_in_M'].astype(float),    # Data to be color-coded
    locationmode = 'USA-states',    # set of locations match entries in `locations`
    colorscale = 'plotly3',
    #text=df['loc'] ,                # hover text
    colorbar_title = "Product-wise Quantity in Millions",
))
fig.update_layout(
    title_text = 'Sales by State',
    geo_scope='usa',                # limite map scope to USA
)
fig.show()


#   

# ### Interpretation on Location (State & sales)
# 
#     Total number of Customers by State
#                Highest: California(CA)-1946
#                Lowest : Wyoming(WY)-1
#          
#     Total number of products sold by State
#                Highest: California(CA)-19153871
#                Lowest: Wyoming(WY)-16608       
#          
#     Sales by State
#                Highest sales:California	(CA)-446306.4635 M
#                Lowest sales: North Dakota (ND)-919.9100 M

# In[28]:


report_i = pd.pivot_table(Data,
                          index=["CustomerName"],
                          values=["Qty"],
                          aggfunc=[np.sum]
                         )
report_i.head(10)


# In[29]:


pd.pivot_table(Data,index=['CustomerName'],values=['Qty'],aggfunc=[np.sum]).sort_values([('sum','Qty')],ascending=False).head().plot(kind='bar',color='pink')


# In[30]:


### Sales_in_M


# In[31]:


pd.pivot_table(Data,index=['CustomerName'],values=['Sales_in_M'],aggfunc=[np.sum]).sort_values([('sum','Sales_in_M')],ascending=False).head().plot(kind='bar',color='green')


# ### Interpretation on Customer
# 
#      Hightest amount of purchase of products was done by William Brown.
#      More number of products were purchased by Sean Miller

# In[ ]:





# #  REPORT FOR FISCAL YEAR 2019-20 FINANCIAL ANALYTICS
# ### Only for the USA

# #### There are 4 main categories to analyse sales of product : 
# * segments
# * categories of product
# * location(state)
# * customer
# 
# #### Insights based on Segment:
# 
#          Highest Turnover    - Home Office
#          Average Turnover    - Corporate
#          Lowest  Turnover    - Consumer      
# 
#          Company can focus more on Consumer segment for increasing turnover.
#          
# #### Insights based on Categories of product:
#          
#          *Furnishings from Furniture & Binders, Paper from Office Supplies sold higher by product units.
#          Accessories and Phones from Technology category shows higher in product sales.
# 
#          So considering future earth and eco-friendly environment,
#          we promote valueable #GoGreen methods among every dealers and customers. 
#          Tech gaint Apple Inc. announced their revised policy. 
# 
#          *Technology Category under every segments proving higher revenue in sales.
#          Where,
#          Office Supplies left idle and Furniture sales remains consistance.
# 
#          Individually Furniture, Office Supplies and technology are idle for consumer and corporate segment.
#          But from corporate to home office segment,
#          there is falling down for furniture and increase for technology while furniture stays constant.         
#                 
#          *It's clearly shoes that's Quantity wise Technology based products sold very less comparatively.
#          But Technology was been expensive then other category. 
#          
# #### Insights based on location (state wise):
#           
#          Sales by State
#                Highest sales:California	(CA)-446306.4635 M
#                Lowest sales: North Dakota (ND)-919.9100 M
#                
#          Total number of products sold by State
#                Highest: California(CA)-19153871
#                Lowest: Wyoming(WY)-16608
#                
#          Total number of Customers by State
#                Highest: California(CA)-1946
#                Lowest : Wyoming(WY)-1
#          
# #### Insights based on customer:       
#           
#          Sales in Million : William Brown
#          Qty : Sean Miller

# ### Decisions that can be taken

# In the **Category** the company should focus on increasing the technological equipments ordered quantity by more advertising and creating a demand in the market and also the focus can be on the increasing of sales in terms of money of office supplies by increasing the profit margin so that the company can grow as whole
# 
# In the **State** company should focus on Wyoming to sale more in terms of quantity and the company should sale more and more in the state like North Dakota
# 
# In the **City**  company should focus on Cedar Rapids to sale more in terms of quantity and the company should sale more and more in the City like Abilene
# 
# In the **Segment**  company should focus on Home Office products to sale more in terms of quantity and the company should sale more and more in the segment like Home Office only

# ---

# #### Color set for graph:
# 'aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
# 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
# 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
# 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
# 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
# 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
# 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
# 'orrd', 'oryel', 'peach', 'phase', 'picnic', 'pinkyl', 'piyg',
# 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn', 'puor',
# 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
# 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar', 'spectral',
# 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn', 'tealrose',
# 'tempo', 'temps', 'thermal', 'tropic', 'turbid', 'twilight',
# 'viridis', 'ylgn', 'ylgnbu', 'ylorbr', 'ylorrd'
