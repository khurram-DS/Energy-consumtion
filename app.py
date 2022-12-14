import streamlit as st
# Eda packages

import pandas as pd
import numpy as np

#Data viz packages

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

#function

def main():
    
    title_container1 = st.container()
    col1, col2 ,  = st.columns([6,12])
    from PIL import Image
    image = Image.open('static/asia.jpeg')
    with title_container1:
        with col1:
            st.image(image, width=200)
        with col2:
            st.markdown('<h1 style="color: red;">ASIA Consulting</h1>',
                           unsafe_allow_html=True)
    
    
    
    
    st.sidebar.image("static/BMI.jpg", use_column_width=True)
    activites = ["About","Energy consumption & Analysis"]
    choice =st.sidebar.selectbox("Select Activity",activites)
    
    
    

    if choice == "About":
        st.subheader("About ACS")
        st.text("""ACS is a consulting company specialized in data analysis was established during 2010. Our mission is to clarify the right direction for business owners in order to get better business results using very advanced statistical approaches, also, to support postgraduate students to prove their finding using academic statistical analysis. Providing the work in a high level of quality is one of our important goals. Our future vision is to be a leader in 
business analytics advisor for all successful business owners.
Our qualified staff is our strength of many of our successful projects. 
ACS did more than 100 successful projects since 2010/11. We are focusing on providing a 
sophisticated work with co-operated with our international parter. ACS has an international
agreement with Statistics Solutions (Ltd.) to be authorized for selling a statistical 
package in the GCC region, and that makes ACS more credible in statistical performance.""")
        
        
        st.subheader("About this Project")
        st.write("**A survey of the behavior of citizens and residents towards household energy consumption**")
        st.write("A survey of the behavior of citizens and residents towards household energy consumption")
        st.subheader("**Fill the survey form , from below link**")
        new_title5 = '<p style="font-family:sans-serif; color:black; font-size: 14 px;">Fill this survey <a  href="https://form.jotform.com/223211953851049"> Survey Form </a> </p> ' 
        st.markdown(new_title5, unsafe_allow_html=True)
        
        st.write("**Calculation Behind the energy consumtion to your homes Appliances**")
        st.text("""How do you use energy in your homes? 
We generally require both heat (often directly from fossil fuels) and electric power for appliances, entertainment, etc.
In this class, we'll focus on the electric energy (really electromagnetic energy) used in typical households. 
Recall the basic concepts we learned regarding power and energy:

1.energy = power x time, (units: kWh = W/1000 x hours)
OR

2.power = energy /time (units: W = (kWh)1000 / h)
3.power = volts x amps (P= I V)
- volts: a measure of potential for electricity; such as the height of water behind 
a dam (120 V = standard household voltage in the US).
- current: a measure of the flow of electricity, such as the flow rate of water 
through the dam.

How do we know how much electricity an appliance is consuming?

- Look at the appliance rating – watts? Amps? Watts = amps x volts 
(It is helpful to have examples, such as a hair dryer, to show this.)
- Look at tables of "average" wattage. (Note the age of the appliance, 
such as a refrigerator, and refer to tables in the Home Energy Audit activity.)
- Reinforce concepts:
1.energy = power x time,
2.(kWh = W/1000 x hours)
3.so appliances that are used for a long time but at a lower wattage might consume 
the same energy as appliances used for short time periods at high wattage (power)""")
        
 
        
        st.text('© Asia Consulting for Statistics')
#overall analysis    
    elif choice == "Energy consumption & Analysis":

        st.subheader("Usages of Energy consumption by different appliances")
        

        st.text('------------------------------------------------------------------------------------------------------------------------------')
        
        
       
        
        
    
        def get_df(file):
          # get extension and read file
          extension = file.name.split('.')[1]
          if extension.upper() == 'CSV':
            df = pd.read_csv(file)
          elif extension.upper() == 'XLSX':
            df = pd.read_excel(file)
          
          return df
        file = st.file_uploader("Upload file", type=['csv' 
                                                 ,'xlsx'])
        if not file:
            st.write("Upload a .csv or .xlsx file to get started")
            return
        st.write("**Data has been loaded Successfully**")
        
        df = get_df(file)
        if st.checkbox("Show Raw Data"):
            st.write(df)
        
        
        st.subheader("**Expanding different appliances usages of energy to multiple features**")
        
            
        
            
            
        if st.checkbox("Click to Expand the columns to new features"):
            
            # column 1st

            data=[]
            data = df['Air Conditioner Central Packaged - تكييف مركزي مغلف'].str.split('\n',expand=True)
            
            new=df.join(data)
            new['#1 units owned - Air Conditioner Central Packaged ']=(new[0].str.split('/').str[1])
            new['#1 units owned - Air Conditioner Central Packaged ']=(new['#1 units owned - Air Conditioner Central Packaged '].str.split(':').str[1])
            
            new['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']=(new[1].str.split('/').str[1])
            new['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']=(new['#2 Average temperature (C) setting - Air Conditioner Central Packaged '].str.split(':').str[1])
            
            new['#3 Operating in hours per day - Air Conditioner Central Packaged ']=(new[2].str.split('/').str[1])
            new['#3 Operating in hours per day - Air Conditioner Central Packaged ']=(new['#3 Operating in hours per day - Air Conditioner Central Packaged '].str.split(':').str[1])
            
            new['#4 Unit size in Ton - Air Conditioner Central Packaged ']=(new[3].str.split('/').str[1])
            new['#4 Unit size in Ton - Air Conditioner Central Packaged ']=(new['#4 Unit size in Ton - Air Conditioner Central Packaged '].str.split(':').str[1])
            new['#4 Unit size in Ton - Air Conditioner Central Packaged ']=(new['#4 Unit size in Ton - Air Conditioner Central Packaged '].str.split(' ').str[0])
            
            import re
            new['Air Conditioner Central Packaged  - The estimated Watts consumed per day'] =pd.to_numeric(new[5].str.replace('[^\d.]', ''), errors='coerce')
            
            new=new.drop([0,1,2,3,4,5], axis=1)
            
            col1=new.columns.get_loc('Air Conditioner Central Packaged - تكييف مركزي مغلف')
            
            
            first_newumn = new.pop('#1 units owned - Air Conditioner Central Packaged ')
            second_newumn=new.pop('#2 Average temperature (C) setting - Air Conditioner Central Packaged ')
            third_newumn=new.pop('#3 Operating in hours per day - Air Conditioner Central Packaged ')
            fourth_newumn=new.pop('#4 Unit size in Ton - Air Conditioner Central Packaged ')
            fifth_newumn=new.pop('Air Conditioner Central Packaged  - The estimated Watts consumed per day')
            
            new.insert(col1+1, '#1 units owned - Air Conditioner Central Packaged ', first_newumn)
            new.insert(col1+2, '#2 Average temperature (C) setting - Air Conditioner Central Packaged ', second_newumn)
            new.insert(col1+3, '#3 Operating in hours per day - Air Conditioner Central Packaged ', third_newumn)
            new.insert(col1+4, '#4 Unit size in Ton - Air Conditioner Central Packaged ', fourth_newumn)
            new.insert(col1+5, 'Air Conditioner Central Packaged  - The estimated Watts consumed per day', fifth_newumn)
            
            #column 2nd
            data=[]
            data = df['Air Conditioner Central Split - وحدة تكييف مركزي منفصلة'].str.split('\n',expand=True)
            acss=new.join(data)
            
            acss['#1 units owned - Air Conditioner Central Split ']=(acss[0].str.split('/').str[1])
            acss['#1 units owned - Air Conditioner Central Split ']=(acss['#1 units owned - Air Conditioner Central Split '].str.split(':').str[1])
            
            acss['#2 Average temperature (C) setting - Air Conditioner Central Split ']=(acss[1].str.split('/').str[1])
            acss['#2 Average temperature (C) setting - Air Conditioner Central Split ']=(acss['#2 Average temperature (C) setting - Air Conditioner Central Split '].str.split(':').str[1])
            
            acss['#3 Operating in hours per day - Air Conditioner Central Split ']=(acss[2].str.split('/').str[1])
            acss['#3 Operating in hours per day - Air Conditioner Central Split ']=(acss['#3 Operating in hours per day - Air Conditioner Central Split '].str.split(':').str[1])
            
            acss['#4 Unit size in Ton - Air Conditioner Central Split ']=(acss[3].str.split('/').str[1])
            acss['#4 Unit size in Ton - Air Conditioner Central Split ']=(acss['#4 Unit size in Ton - Air Conditioner Central Split '].str.split(':').str[1])
            acss['#4 Unit size in Ton - Air Conditioner Central Split ']=(acss['#4 Unit size in Ton - Air Conditioner Central Split '].str.split(' ').str[0])
            
            import re
            acss['Air Conditioner Central Split  - The estimated Watts consumed per day'] =pd.to_numeric(acss[5].str.replace('[^\d.]', ''), errors='coerce')
            
            acss=acss.drop([0,1,2,3,4,5], axis=1)
            
            col2=acss.columns.get_loc('Air Conditioner Central Split - وحدة تكييف مركزي منفصلة')
            
            first_acssumn = acss.pop('#1 units owned - Air Conditioner Central Split ')
            second_acssumn=acss.pop('#2 Average temperature (C) setting - Air Conditioner Central Split ')
            third_acssumn=acss.pop('#3 Operating in hours per day - Air Conditioner Central Split ')
            fourth_acssumn=acss.pop('#4 Unit size in Ton - Air Conditioner Central Split ')
            fifth_acssumn=acss.pop('Air Conditioner Central Split  - The estimated Watts consumed per day')
            
            acss.insert(col2+1, '#1 units owned - Air Conditioner Central Split ', first_acssumn)
            acss.insert(col2+2, '#2 Average temperature (C) setting - Air Conditioner Central Split ', second_acssumn)
            acss.insert(col2+3, '#3 Operating in hours per day - Air Conditioner Central Split ', third_acssumn)
            acss.insert(col2+4, '#4 Unit size in Ton - Air Conditioner Central Split ', fourth_acssumn)
            acss.insert(col2+5, 'Air Conditioner Central Split  - The estimated Watts consumed per day', fifth_acssumn)
            
            
            #column 3rd
            data=[]
            data = df['Air conditioning Units Mini split - وحدة تكييف مركزي منفصلة'].str.split('\n',expand=True)
            acum=acss.join(data)
            
            acum['#1 units owned - Air conditioning Units Mini split ']=(acum[0].str.split('/').str[1])
            acum['#1 units owned - Air conditioning Units Mini split ']=(acum['#1 units owned - Air conditioning Units Mini split '].str.split(':').str[1])
            
            acum['#2 Average temperature (C) setting - Air conditioning Units Mini split ']=(acum[1].str.split('/').str[1])
            acum['#2 Average temperature (C) setting - Air conditioning Units Mini split ']=(acum['#2 Average temperature (C) setting - Air conditioning Units Mini split '].str.split(':').str[1])
            
            acum['#3 Operating in hours per day - Air conditioning Units Mini split ']=(acum[2].str.split('/').str[1])
            acum['#3 Operating in hours per day - Air conditioning Units Mini split ']=(acum['#3 Operating in hours per day - Air conditioning Units Mini split '].str.split(':').str[1])
            
            acum['#4 Unit size in Ton - Air conditioning Units Mini split ']=(acum[3].str.split('/').str[1])
            acum['#4 Unit size in Ton - Air conditioning Units Mini split ']=(acum['#4 Unit size in Ton - Air conditioning Units Mini split '].str.split(':').str[1])
            acum['#4 Unit size in Ton - Air conditioning Units Mini split ']=(acum['#4 Unit size in Ton - Air conditioning Units Mini split '].str.split(' ').str[0])
            
            import re
            acum['Air conditioning Units Mini split  - The estimated Watts consumed per day'] =pd.to_numeric(acum[5].str.replace('[^\d.]', ''), errors='coerce')
            
            acum=acum.drop([0,1,2,3,4,5], axis=1)
            
            col3=acum.columns.get_loc('Air conditioning Units Mini split - وحدة تكييف مركزي منفصلة')
            
            first_acumumn = acum.pop('#1 units owned - Air conditioning Units Mini split ')
            second_acumumn=acum.pop('#2 Average temperature (C) setting - Air conditioning Units Mini split ')
            third_acumumn=acum.pop('#3 Operating in hours per day - Air conditioning Units Mini split ')
            fourth_acumumn=acum.pop('#4 Unit size in Ton - Air conditioning Units Mini split ')
            fifth_acumumn=acum.pop('Air conditioning Units Mini split  - The estimated Watts consumed per day')
            
            acum.insert(col3+1, '#1 units owned - Air conditioning Units Mini split ', first_acumumn)
            acum.insert(col3+2, '#2 Average temperature (C) setting - Air conditioning Units Mini split ', second_acumumn)
            acum.insert(col3+3, '#3 Operating in hours per day - Air conditioning Units Mini split ', third_acumumn)
            acum.insert(col3+4, '#4 Unit size in Ton - Air conditioning Units Mini split ', fourth_acumumn)
            acum.insert(col3+5, 'Air conditioning Units Mini split  - The estimated Watts consumed per day', fifth_acumumn)
            
            #column 4th
            data=[]
            data = df['Air conditioning Units Windows - نوافذ وحدات التكييف'].str.split('\n',expand=True)
            acuw=acum.join(data)
            
            acuw['#1 units owned - Air conditioning Units Windows ']=(acuw[0].str.split('/').str[1])
            acuw['#1 units owned - Air conditioning Units Windows ']=(acuw['#1 units owned - Air conditioning Units Windows '].str.split(':').str[1])
            
            acuw['#2 Average temperature (C) setting - Air conditioning Units Windows ']=(acuw[1].str.split('/').str[1])
            acuw['#2 Average temperature (C) setting - Air conditioning Units Windows ']=(acuw['#2 Average temperature (C) setting - Air conditioning Units Windows '].str.split(':').str[1])
            
            acuw['#3 Operating in hours per day - Air conditioning Units Windows ']=(acuw[2].str.split('/').str[1])
            acuw['#3 Operating in hours per day - Air conditioning Units Windows ']=(acuw['#3 Operating in hours per day - Air conditioning Units Windows '].str.split(':').str[1])
            
            acuw['#4 Unit size in Ton - Air conditioning Units Windows ']=(acuw[3].str.split('/').str[1])
            acuw['#4 Unit size in Ton - Air conditioning Units Windows ']=(acuw['#4 Unit size in Ton - Air conditioning Units Windows '].str.split(':').str[1])
            acuw['#4 Unit size in Ton - Air conditioning Units Windows ']=(acuw['#4 Unit size in Ton - Air conditioning Units Windows '].str.split(' ').str[0])
            
            import re
            acuw['Air conditioning Units Windows  - The estimated Watts consumed per day'] =pd.to_numeric(acuw[5].str.replace('[^\d.]', ''), errors='coerce')
            
            acuw=acuw.drop([0,1,2,3,4,5], axis=1)
            
            col4=acuw.columns.get_loc('Air conditioning Units Windows - نوافذ وحدات التكييف')
            
            first_acuwumn = acuw.pop('#1 units owned - Air conditioning Units Windows ')
            second_acuwumn=acuw.pop('#2 Average temperature (C) setting - Air conditioning Units Windows ')
            third_acuwumn=acuw.pop('#3 Operating in hours per day - Air conditioning Units Windows ')
            fourth_acuwumn=acuw.pop('#4 Unit size in Ton - Air conditioning Units Windows ')
            fifth_acuwumn=acuw.pop('Air conditioning Units Windows  - The estimated Watts consumed per day')
            
            acuw.insert(col4+1, '#1 units owned - Air conditioning Units Windows ', first_acuwumn)
            acuw.insert(col4+2, '#2 Average temperature (C) setting - Air conditioning Units Windows ', second_acuwumn)
            acuw.insert(col4+3, '#3 Operating in hours per day - Air conditioning Units Windows ', third_acuwumn)
            acuw.insert(col4+4, '#4 Unit size in Ton - Air conditioning Units Windows ', fourth_acuwumn)
            acuw.insert(col4+5, 'Air conditioning Units Windows  - The estimated Watts consumed per day', fifth_acuwumn)
            
            #column 5th
            data=[]
            data = df['Portable air cooler for single room - مبرد هواء محمول لغرفة فردية'].str.split('\n',expand=True)
            pacsr=acuw.join(data)
            
            
            pacsr['#1 units owned - Portable air cooler for single room']=(pacsr[0].str.split('/').str[1])
            pacsr['#1 units owned - Portable air cooler for single room']=(pacsr['#1 units owned - Portable air cooler for single room'].str.split(':').str[1])
            
            pacsr['#2 Average temperature (C) setting - Portable air cooler for single room']=(pacsr[1].str.split('/').str[1])
            pacsr['#2 Average temperature (C) setting - Portable air cooler for single room']=(pacsr['#2 Average temperature (C) setting - Portable air cooler for single room'].str.split(':').str[1])
            
            pacsr['#3 Operating in hours per day - Portable air cooler for single room']=(pacsr[2].str.split('/').str[1])
            pacsr['#3 Operating in hours per day - Portable air cooler for single room']=(pacsr['#3 Operating in hours per day - Portable air cooler for single room'].str.split(':').str[1])
            
            
            import re
            pacsr['Portable air cooler for single room - The estimated Watts consumed per day'] =pd.to_numeric(pacsr[4].str.replace('[^\d.]', ''), errors='coerce')
            
            pacsr=pacsr.drop([0,1,2,3,4], axis=1)
            
            
            col5=pacsr.columns.get_loc('Portable air cooler for single room - مبرد هواء محمول لغرفة فردية')
            
            first_pacsrumn = pacsr.pop('#1 units owned - Portable air cooler for single room')
            second_pacsrumn=pacsr.pop('#2 Average temperature (C) setting - Portable air cooler for single room')
            third_pacsrumn=pacsr.pop('#3 Operating in hours per day - Portable air cooler for single room')
            
            fifth_pacsrumn=pacsr.pop('Portable air cooler for single room - The estimated Watts consumed per day')
            
            pacsr.insert(col5+1, '#1 units owned - Portable air cooler for single room', first_pacsrumn)
            pacsr.insert(col5+2, '#2 Average temperature (C) setting - Portable air cooler for single room', second_pacsrumn)
            pacsr.insert(col5+3, '#3 Operating in hours per day - Portable air cooler for single room', third_pacsrumn)
            
            pacsr.insert(col5+4, 'Portable air cooler for single room - The estimated Watts consumed per day', fifth_pacsrumn)
            
            #column 6th
            data=[]
            data = df['Air Purifier Device - جهاز تنقية الهواء'].str.split('\n',expand=True)
            apd=pacsr.join(data)
            apd['#1 units owned - Air Purifier Device']=(apd[0].str.split('/').str[1])
            apd['#1 units owned - Air Purifier Device']=(apd['#1 units owned - Air Purifier Device'].str.split(':').str[1])
            
            
            
            apd['#2 Operating in hours per day - Air Purifier Device']=(apd[1].str.split('/').str[1])
            apd['#2 Operating in hours per day - Air Purifier Device']=(apd['#2 Operating in hours per day - Air Purifier Device'].str.split(':').str[1])
            
            
            import re
            apd['Air Purifier Device - The estimated Watts consumed per day'] =pd.to_numeric(apd[3].str.replace('[^\d.]', ''), errors='coerce')
            
            apd=apd.drop([0,1,2,3], axis=1)
            
            col6=apd.columns.get_loc('Air Purifier Device - جهاز تنقية الهواء')
            
            first_apdumn = apd.pop('#1 units owned - Air Purifier Device')
            
            third_apdumn=apd.pop('#2 Operating in hours per day - Air Purifier Device')
            
            fifth_apdumn=apd.pop('Air Purifier Device - The estimated Watts consumed per day')
            
            apd.insert(col6+1, '#1 units owned - Air Purifier Device', first_apdumn)
            
            apd.insert(col6+2, '#2 Operating in hours per day - Air Purifier Device', third_apdumn)
            
            apd.insert(col6+3, 'Air Purifier Device - The estimated Watts consumed per day', fifth_apdumn)
            
            
            #column 7th
            data=[]
            data = df['Electric fan - مروحة كهربائية'].str.split('\n',expand=True)
            ef=apd.join(data)
            ef['#1 units owned - Electric fan']=(ef[0].str.split('/').str[1])
            ef['#1 units owned - Electric fan']=(ef['#1 units owned - Electric fan'].str.split(':').str[1])
            
            
            
            ef['#2 Operating in hours per day - Electric fan']=(ef[1].str.split('/').str[1])
            ef['#2 Operating in hours per day - Electric fan']=(ef['#2 Operating in hours per day - Electric fan'].str.split(':').str[1])
            
            
            import re
            ef['Electric fan - The estimated Watts consumed per day'] =pd.to_numeric(ef[3].str.replace('[^\d.]', ''), errors='coerce')
            
            ef=ef.drop([0,1,2,3], axis=1)
            
            col7=ef.columns.get_loc('Electric fan - مروحة كهربائية')
            
            first_efumn = ef.pop('#1 units owned - Electric fan')
            
            third_efumn=ef.pop('#2 Operating in hours per day - Electric fan')
            
            fifth_efumn=ef.pop('Electric fan - The estimated Watts consumed per day')
            
            ef.insert(col7+1, '#1 units owned - Electric fan', first_efumn)
            
            ef.insert(col7+2, '#2 Operating in hours per day - Electric fan', third_efumn)
            
            ef.insert(col7+3, 'Electric fan - The estimated Watts consumed per day', fifth_efumn)
            
            #column 8th
            data=[]
            data = df['Heater - Central - سخان - مركزي'].str.split('\n',expand=True)
            hc=ef.join(data)
            hc['#1 units owned - Heater - Central ']=(hc[0].str.split('/').str[1])
            hc['#1 units owned - Heater - Central ']=(hc['#1 units owned - Heater - Central '].str.split(':').str[1])
            
            
            
            hc['#2 Operating in hours per day - Heater - Central ']=(hc[1].str.split('/').str[1])
            hc['#2 Operating in hours per day - Heater - Central ']=(hc['#2 Operating in hours per day - Heater - Central '].str.split(':').str[1])
            
            
            import re
            hc['Heater - Central  - The estimated Watts consumed per day'] =pd.to_numeric(hc[3].str.replace('[^\d.]', ''), errors='coerce')
            
            hc=hc.drop([0,1,2,3], axis=1)
            
            col8=hc.columns.get_loc('Heater - Central - سخان - مركزي')
            
            first_hcumn = hc.pop('#1 units owned - Heater - Central ')
            
            third_hcumn=hc.pop('#2 Operating in hours per day - Heater - Central ')
            
            fifth_hcumn=hc.pop('Heater - Central  - The estimated Watts consumed per day')
            
            hc.insert(col8+1, '#1 units owned - Heater - Central ', first_hcumn)
            
            hc.insert(col8+2, '#2 Operating in hours per day - Heater - Central ', third_hcumn)
            
            hc.insert(col8+3, 'Heater - Central  - The estimated Watts consumed per day', fifth_hcumn)
            
            
            #column 9th
            data=[]
            data = df['Heater - Space Heater (Portable, Electric) - المدفأة - سخان الفضاء (محمول ، كهربائي)'].str.split('\n',expand=True)
            hsh=hc.join(data)
            hsh['#1 units owned - Heater - Space Heater (Portable, Electric) ']=(hsh[0].str.split('/').str[1])
            hsh['#1 units owned - Heater - Space Heater (Portable, Electric) ']=(hsh['#1 units owned - Heater - Space Heater (Portable, Electric) '].str.split(':').str[1])
            
            
            
            hsh['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']=(hsh[1].str.split('/').str[1])
            hsh['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']=(hsh['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) '].str.split(':').str[1])
            
            
            import re
            hsh['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day'] =pd.to_numeric(hsh[3].str.replace('[^\d.]', ''), errors='coerce')
            
            hsh=hsh.drop([0,1,2,3], axis=1)
            
            col9=hsh.columns.get_loc('Heater - Space Heater (Portable, Electric) - المدفأة - سخان الفضاء (محمول ، كهربائي)')
            
            first_hshumn = hsh.pop('#1 units owned - Heater - Space Heater (Portable, Electric) ')
            
            third_hshumn=hsh.pop('#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ')
            
            fifth_hshumn=hsh.pop('Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day')
            
            hsh.insert(col9+1, '#1 units owned - Heater - Space Heater (Portable, Electric) ', first_hshumn)
            
            hsh.insert(col9+2, '#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ', third_hshumn)
            
            hsh.insert(col9+3, 'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day', fifth_hshumn)
            
            
            #column 10th
            data=[]
            data = df['Heater - Space Heater (Portable, Oil) - المدفأة - مدفأة الفضاء (المحمولة ، بالزيت)'].str.split('\n',expand=True)
            hso=hsh.join(data)
            hso['#1 units owned - Heater - Space Heater (Portable, Oil) ']=(hso[0].str.split('/').str[1])
            hso['#1 units owned - Heater - Space Heater (Portable, Oil) ']=(hso['#1 units owned - Heater - Space Heater (Portable, Oil) '].str.split(':').str[1])
            
            
            
            hso['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']=(hso[1].str.split('/').str[1])
            hso['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']=(hso['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) '].str.split(':').str[1])
            
            
            import re
            hso['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day'] =pd.to_numeric(hso[3].str.replace('[^\d.]', ''), errors='coerce')
            
            hso=hso.drop([0,1,2,3], axis=1)
            
            col10=hso.columns.get_loc('Heater - Space Heater (Portable, Oil) - المدفأة - مدفأة الفضاء (المحمولة ، بالزيت)')
            
            first_hsoumn = hso.pop('#1 units owned - Heater - Space Heater (Portable, Oil) ')
            
            third_hsoumn=hso.pop('#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ')
            
            fifth_hsoumn=hso.pop('Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day')
            
            hso.insert(col10+1, '#1 units owned - Heater - Space Heater (Portable, Oil) ', first_hsoumn)
            
            hso.insert(col10+2, '#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ', third_hsoumn)
            
            hso.insert(col10+3, 'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day', fifth_hsoumn)
            
            #column 11th
            data=[]
            data = df['Blender/mixer/food processor - الخلاط//طاحن الطعام'].str.split('\n',expand=True)
            mbm=hso.join(data)
            mbm['#1 units owned - Blender/mixer/food processor ']=(mbm[0].str.split('/').str[1])
            mbm['#1 units owned - Blender/mixer/food processor ']=(mbm['#1 units owned - Blender/mixer/food processor '].str.split(':').str[1])
            
            
            
            mbm['#2 Operating in minutes per day - Blender/mixer/food processor ']=(mbm[1].str.split('/').str[1])
            mbm['#2 Operating in minutes per day - Blender/mixer/food processor ']=(mbm['#2 Operating in minutes per day - Blender/mixer/food processor '].str.split(':').str[1])
            
            
            import re
            mbm['Blender/mixer/food processor  - The estimated Watts consumed per day'] =pd.to_numeric(mbm[3].str.replace('[^\d.]', ''), errors='coerce')
            
            mbm=mbm.drop([0,1,2,3], axis=1)
            
            col11=mbm.columns.get_loc('Blender/mixer/food processor - الخلاط//طاحن الطعام')
            
            first_mbmumn = mbm.pop('#1 units owned - Blender/mixer/food processor ')
            
            third_mbmumn=mbm.pop('#2 Operating in minutes per day - Blender/mixer/food processor ')
            
            fifth_mbmumn=mbm.pop('Blender/mixer/food processor  - The estimated Watts consumed per day')
            
            mbm.insert(col11+1, '#1 units owned - Blender/mixer/food processor ', first_mbmumn)
            
            mbm.insert(col11+2, '#2 Operating in minutes per day - Blender/mixer/food processor ', third_mbmumn)
            
            mbm.insert(col11+3, 'Blender/mixer/food processor  - The estimated Watts consumed per day', fifth_mbmumn)
            
            #column 12th
            data=[]
            data = df['Kettle - غلاية الماء'].str.split('\n',expand=True)
            ke=mbm.join(data)
            ke['#1 units owned - kettle ']=(ke[0].str.split('/').str[1])
            ke['#1 units owned - kettle ']=(ke['#1 units owned - kettle '].str.split(':').str[1])
            
            
            
            ke['#2 Operating in minutes per day - kettle ']=(ke[1].str.split('/').str[1])
            ke['#2 Operating in minutes per day - kettle ']=(ke['#2 Operating in minutes per day - kettle '].str.split(':').str[1])
            
            
            import re
            ke['kettle- The estimated Watts consumed per day'] =pd.to_numeric(ke[3].str.replace('[^\d.]', ''), errors='coerce')
            
            ke=ke.drop([0,1,2,3], axis=1)
            
            col12=ke.columns.get_loc('Kettle - غلاية الماء')
            
            first_keumn = ke.pop('#1 units owned - kettle ')
            
            third_keumn=ke.pop('#2 Operating in minutes per day - kettle ')
            
            fifth_keumn=ke.pop('kettle- The estimated Watts consumed per day')
            
            ke.insert(col12+1, '#1 units owned - kettle ', first_keumn)
            
            ke.insert(col12+2, '#2 Operating in minutes per day - kettle ', third_keumn)
            
            ke.insert(col12+3, 'kettle- The estimated Watts consumed per day', fifth_keumn)
            
            #column 13th
            data=[]
            data = df['Toaster - محمصة'].str.split('\n',expand=True)
            toast=ke.join(data)
            toast['#1 units owned - Toaster ']=(toast[0].str.split('/').str[1])
            toast['#1 units owned - Toaster ']=(toast['#1 units owned - Toaster '].str.split(':').str[1])
            
            
            
            toast['#2 Operating in minutes per day - Toaster ']=(toast[1].str.split('/').str[1])
            toast['#2 Operating in minutes per day - Toaster ']=(toast['#2 Operating in minutes per day - Toaster '].str.split(':').str[1])
            
            
            import re
            toast['Toaster- The estimated Watts consumed per day'] =pd.to_numeric(toast[3].str.replace('[^\d.]', ''), errors='coerce')
            
            toast=toast.drop([0,1,2,3], axis=1)
            
            col13=toast.columns.get_loc('Toaster - محمصة')
            
            first_toastumn = toast.pop('#1 units owned - Toaster ')
            
            third_toastumn=toast.pop('#2 Operating in minutes per day - Toaster ')
            
            fifth_toastumn=toast.pop('Toaster- The estimated Watts consumed per day')
            
            toast.insert(col13+1, '#1 units owned - Toaster ', first_toastumn)
            
            toast.insert(col13+2, '#2 Operating in minutes per day - Toaster ', third_toastumn)
            
            toast.insert(col13+3, 'Toaster- The estimated Watts consumed per day', fifth_toastumn)
            
            #column 14th
            data=[]
            data = df['Range - LPG - موقد للطبخ'].str.split('\n',expand=True)
            lpg=toast.join(data)
            lpg['#1 units owned - Range - LPG ']=(lpg[0].str.split('/').str[1])
            lpg['#1 units owned - Range - LPG ']=(lpg['#1 units owned - Range - LPG '].str.split(':').str[1])
            
            
            
            lpg['#2 Operating in minutes per day - Range - LPG ']=(lpg[1].str.split('/').str[1])
            lpg['#2 Operating in minutes per day - Range - LPG ']=(lpg['#2 Operating in minutes per day - Range - LPG '].str.split(':').str[1])
            
            
            import re
            lpg['Range - LPG- The estimated Watts consumed per day'] =pd.to_numeric(lpg[3].str.replace('[^\d.]', ''), errors='coerce')
            
            lpg=lpg.drop([0,1,2,3], axis=1)
            
            col14=lpg.columns.get_loc('Range - LPG - موقد للطبخ')
            
            first_lpgumn = lpg.pop('#1 units owned - Range - LPG ')
            
            third_lpgumn=lpg.pop('#2 Operating in minutes per day - Range - LPG ')
            
            fifth_lpgumn=lpg.pop('Range - LPG- The estimated Watts consumed per day')
            
            lpg.insert(col14+1, '#1 units owned - Range - LPG ', first_lpgumn)
            
            lpg.insert(col14+2, '#2 Operating in minutes per day - Range - LPG ', third_lpgumn)
            
            lpg.insert(col14+3, 'Range - LPG- The estimated Watts consumed per day', fifth_lpgumn)
            
            #column 15th
            data=[]
            data = df['Range - Electric - موقد كهربائي للطبخ'].str.split('\n',expand=True)
            rae=lpg.join(data)
            rae['#1 units owned - Range - Electric ']=(rae[0].str.split('/').str[1])
            rae['#1 units owned - Range - Electric ']=(rae['#1 units owned - Range - Electric '].str.split(':').str[1])
            
            
            
            rae['#2 Operating in minutes per day - Range - Electric ']=(rae[1].str.split('/').str[1])
            rae['#2 Operating in minutes per day - Range - Electric ']=(rae['#2 Operating in minutes per day - Range - Electric '].str.split(':').str[1])
            
            
            import re
            rae['Range - Electric- The estimated Watts consumed per day'] =pd.to_numeric(rae[3].str.replace('[^\d.]', ''), errors='coerce')
            
            rae=rae.drop([0,1,2,3], axis=1)
            
            col15=rae.columns.get_loc('Range - Electric - موقد كهربائي للطبخ')
            
            first_raeumn = rae.pop('#1 units owned - Range - Electric ')
            
            third_raeumn=rae.pop('#2 Operating in minutes per day - Range - Electric ')
            
            fifth_raeumn=rae.pop('Range - Electric- The estimated Watts consumed per day')
            
            rae.insert(col15+1, '#1 units owned - Range - Electric ', first_raeumn)
            
            rae.insert(col15+2, '#2 Operating in minutes per day - Range - Electric ', third_raeumn)
            
            rae.insert(col15+3, 'Range - Electric- The estimated Watts consumed per day', fifth_raeumn)
            
            #column 16th
            data=[]
            data = df['Cooktop - (LPG/Electric/Induction) - موقد كهربائي سطحي للطبخ'].str.split('\n',expand=True)
            celi=rae.join(data)
            celi['#1 units owned - Cooktop - (LPG/Electric/Induction) ']=(celi[0].str.split('/').str[1])
            celi['#1 units owned - Cooktop - (LPG/Electric/Induction) ']=(celi['#1 units owned - Cooktop - (LPG/Electric/Induction) '].str.split(':').str[1])
            
            
            
            celi['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']=(celi[1].str.split('/').str[1])
            celi['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']=(celi['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) '].str.split(':').str[1])
            
            
            import re
            celi['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day'] =pd.to_numeric(celi[3].str.replace('[^\d.]', ''), errors='coerce')
            
            celi=celi.drop([0,1,2,3], axis=1)
            
            col16=celi.columns.get_loc('Cooktop - (LPG/Electric/Induction) - موقد كهربائي سطحي للطبخ')
            
            first_celiumn = celi.pop('#1 units owned - Cooktop - (LPG/Electric/Induction) ')
            
            third_celiumn=celi.pop('#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ')
            
            fifth_celiumn=celi.pop('Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day')
            
            celi.insert(col16+1, '#1 units owned - Cooktop - (LPG/Electric/Induction) ', first_celiumn)
            
            celi.insert(col16+2, '#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ', third_celiumn)
            
            celi.insert(col16+3, 'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day', fifth_celiumn)
            
            #column 17th
            data=[]
            data = df['Oven -(LPG/Electric) - فرن كهربائي للطبخ'].str.split('\n',expand=True)
            ole=celi.join(data)
            ole['#1 units owned - Oven -(LPG/Electric) ']=(ole[0].str.split('/').str[1])
            ole['#1 units owned - Oven -(LPG/Electric) ']=(ole['#1 units owned - Oven -(LPG/Electric) '].str.split(':').str[1])
            
            
            
            ole['#2 Operating in minutes per day - Oven -(LPG/Electric) ']=(ole[1].str.split('/').str[1])
            ole['#2 Operating in minutes per day - Oven -(LPG/Electric) ']=(ole['#2 Operating in minutes per day - Oven -(LPG/Electric) '].str.split(':').str[1])
            
            
            import re
            ole['Oven -(LPG/Electric)- The estimated Watts consumed per day'] =pd.to_numeric(ole[3].str.replace('[^\d.]', ''), errors='coerce')
            
            ole=ole.drop([0,1,2,3], axis=1)
            
            col17=ole.columns.get_loc('Oven -(LPG/Electric) - فرن كهربائي للطبخ')
            
            first_oleumn = ole.pop('#1 units owned - Oven -(LPG/Electric) ')
            
            third_oleumn=ole.pop('#2 Operating in minutes per day - Oven -(LPG/Electric) ')
            
            fifth_oleumn=ole.pop('Oven -(LPG/Electric)- The estimated Watts consumed per day')
            
            ole.insert(col17+1, '#1 units owned - Oven -(LPG/Electric) ', first_oleumn)
            
            ole.insert(col17+2, '#2 Operating in minutes per day - Oven -(LPG/Electric) ', third_oleumn)
            
            ole.insert(col17+3, 'Oven -(LPG/Electric)- The estimated Watts consumed per day', fifth_oleumn)
            
            #column 18th
            data=[]
            data = df['Air fryer - مقلاة الهواء'].str.split('\n',expand=True)
            af=ole.join(data)
            af['#1 units owned - Air fryer ']=(af[0].str.split('/').str[1])
            af['#1 units owned - Air fryer ']=(af['#1 units owned - Air fryer '].str.split(':').str[1])
            
            
            
            af['#2 Operating in minutes per day - Air fryer ']=(af[1].str.split('/').str[1])
            af['#2 Operating in minutes per day - Air fryer ']=(af['#2 Operating in minutes per day - Air fryer '].str.split(':').str[1])
            
            
            import re
            af['Air fryer- The estimated Watts consumed per day'] =pd.to_numeric(af[3].str.replace('[^\d.]', ''), errors='coerce')
            
            af=af.drop([0,1,2,3], axis=1)
            
            col18=af.columns.get_loc('Air fryer - مقلاة الهواء')
            
            first_afumn = af.pop('#1 units owned - Air fryer ')
            
            third_afumn=af.pop('#2 Operating in minutes per day - Air fryer ')
            
            fifth_afumn=af.pop('Air fryer- The estimated Watts consumed per day')
            
            af.insert(col18+1, '#1 units owned - Air fryer ', first_afumn)
            
            af.insert(col18+2, '#2 Operating in minutes per day - Air fryer ', third_afumn)
            
            af.insert(col18+3, 'Air fryer- The estimated Watts consumed per day', fifth_afumn)
            
            #column 19th
            data=[]
            data = df['Coffee Maker - جهاز صانع القهوة'].str.split('\n',expand=True)
            cm=af.join(data)
            cm['#1 units owned - Coffee Maker ']=(cm[0].str.split('/').str[1])
            cm['#1 units owned - Coffee Maker ']=(cm['#1 units owned - Coffee Maker '].str.split(':').str[1])
            
            
            
            cm['#2 Operating in minutes per day - Coffee Maker ']=(cm[1].str.split('/').str[1])
            cm['#2 Operating in minutes per day - Coffee Maker ']=(cm['#2 Operating in minutes per day - Coffee Maker '].str.split(':').str[1])
            
            
            import re
            cm['Coffee Maker- The estimated Watts consumed per day'] =pd.to_numeric(cm[3].str.replace('[^\d.]', ''), errors='coerce')
            
            cm=cm.drop([0,1,2,3], axis=1)
            
            col19=cm.columns.get_loc('Coffee Maker - جهاز صانع القهوة')
            
            first_cmumn = cm.pop('#1 units owned - Coffee Maker ')
            
            third_cmumn=cm.pop('#2 Operating in minutes per day - Coffee Maker ')
            
            fifth_cmumn=cm.pop('Coffee Maker- The estimated Watts consumed per day')
            
            cm.insert(col19+1, '#1 units owned - Coffee Maker ', first_cmumn)
            
            cm.insert(col19+2, '#2 Operating in minutes per day - Coffee Maker ', third_cmumn)
            
            cm.insert(col19+3, 'Coffee Maker- The estimated Watts consumed per day', fifth_cmumn)
            
            #column 20th
            data=[]
            data = df['Water Cooler - مبرد مياه'].str.split('\n',expand=True)
            wc=cm.join(data)
            wc['#1 units owned - Water Cooler  ']=(wc[0].str.split('/').str[1])
            wc['#1 units owned - Water Cooler  ']=(wc['#1 units owned - Water Cooler  '].str.split(':').str[1])
            
            
            
            wc['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']=(wc[1].str.split('/').str[1])
            wc['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']=(wc['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler'].str.split(':').str[1])
            
            
            import re
            wc['Water Cooler - The estimated Watts consumed per day'] =pd.to_numeric(wc[3].str.replace('[^\d.]', ''), errors='coerce')
            
            wc=wc.drop([0,1,2,3], axis=1)
            
            col20=wc.columns.get_loc('Water Cooler - مبرد مياه')
            
            first_wcumn = wc.pop('#1 units owned - Water Cooler  ')
            
            third_wcumn=wc.pop('#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler')
            
            fifth_wcumn=wc.pop('Water Cooler - The estimated Watts consumed per day')
            
            wc.insert(col20+1, '#1 units owned - Water Cooler  ', first_wcumn)
            
            wc.insert(col20+2, '#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler', third_wcumn)
            
            wc.insert(col20+3, 'Water Cooler - The estimated Watts consumed per day', fifth_wcumn)
            
            #column 21th
            data=[]
            data = df['Water Heater - Central - سخان المياه - مركزي'].str.split('\n',expand=True)
            whc=wc.join(data)
            whc['#1 units owned - Water Heater - Central  ']=(whc[0].str.split('/').str[1])
            whc['#1 units owned - Water Heater - Central  ']=(whc['#1 units owned - Water Heater - Central  '].str.split(':').str[1])
            
            
            
            whc['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']=(whc[1].str.split('/').str[1])
            whc['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']=(whc['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central'].str.split(':').str[1])
            
            
            import re
            whc['Water Heater - Central - The estimated Watts consumed per day'] =pd.to_numeric(whc[3].str.replace('[^\d.]', ''), errors='coerce')
            
            whc=whc.drop([0,1,2,3], axis=1)
            
            col21=whc.columns.get_loc('Water Heater - Central - سخان المياه - مركزي')
            
            first_whcumn = whc.pop('#1 units owned - Water Heater - Central  ')
            
            third_whcumn=whc.pop('#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central')
            
            fifth_whcumn=whc.pop('Water Heater - Central - The estimated Watts consumed per day')
            
            whc.insert(col21+1, '#1 units owned - Water Heater - Central  ', first_whcumn)
            
            whc.insert(col21+2, '#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central', third_whcumn)
            
            whc.insert(col21+3, 'Water Heater - Central - The estimated Watts consumed per day', fifth_whcumn)
            
            #column 22th
            data=[]
            data = df['Water Heater - Normal - سخان المياه - عادي'].str.split('\n',expand=True)
            whn=whc.join(data)
            whn['#1 units owned - Water Heater - Normal  ']=(whn[0].str.split('/').str[1])
            whn['#1 units owned - Water Heater - Normal  ']=(whn['#1 units owned - Water Heater - Normal  '].str.split(':').str[1])
            
            
            
            whn['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']=(whn[1].str.split('/').str[1])
            whn['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']=(whn['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal'].str.split(':').str[1])
            
            
            import re
            whn['Water Heater - Normal - The estimated Watts consumed per day'] =pd.to_numeric(whn[3].str.replace('[^\d.]', ''), errors='coerce')
            
            whn=whn.drop([0,1,2,3], axis=1)
            
            col22=whn.columns.get_loc('Water Heater - Normal - سخان المياه - عادي')
            
            first_whnumn = whn.pop('#1 units owned - Water Heater - Normal  ')
            
            third_whnumn=whn.pop('#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal')
            
            fifth_whnumn=whn.pop('Water Heater - Normal - The estimated Watts consumed per day')
            
            whn.insert(col22+1, '#1 units owned - Water Heater - Normal  ', first_whnumn)
            
            whn.insert(col22+2, '#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal', third_whnumn)
            
            whn.insert(col22+3, 'Water Heater - Normal - The estimated Watts consumed per day', fifth_whnumn)
            
            #column 23th
            data=[]
            data = df['Clothes dryer - مجفف الملابس'].str.split('\n',expand=True)
            
            cd=whn.join(data)
            cd['#1 units owned - Clothes dryer  ']=(cd[0].str.split('/').str[1])
            cd['#1 units owned - Clothes dryer  ']=(cd['#1 units owned - Clothes dryer  '].str.split(':').str[1])
            
            
            
            cd['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']=(cd[1].str.split('/').str[1])
            cd['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']=(cd['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer'].str.split(':').str[1])
            
            cd['#3 What is the capacity?']=(cd[2].str.split('/').str[1])
            cd['#3 What is the capacity?']=(cd['#3 What is the capacity?'].str.split(':').str[1])
            cd['#3 What is the capacity?']=(cd['#3 What is the capacity?'].str.split('(').str[0])
            import re
            cd['Clothes dryer - The estimated Watts consumed per day'] =pd.to_numeric(cd[4].str.replace('[^\d.]', ''), errors='coerce')
            
            cd=cd.drop([0,1,2,3,4], axis=1)
            
            col23=cd.columns.get_loc('Clothes dryer - مجفف الملابس')
            
            first_cdumn = cd.pop('#1 units owned - Clothes dryer  ')
            
            third_cdumn=cd.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer')
            second_cdumn=cd.pop('#3 What is the capacity?')
            
            fifth_cdumn=cd.pop('Clothes dryer - The estimated Watts consumed per day')
            
            cd.insert(col23+1, '#1 units owned - Clothes dryer  ', first_cdumn)
            
            cd.insert(col23+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer', third_cdumn)
            cd.insert(col23+3, '#3 What is the capacity? - Clothes dryer', second_cdumn)
            cd.insert(col23+4, 'Clothes dryer - The estimated Watts consumed per day', fifth_cdumn)
            
            #column 24th
            data=[]
            data = df['Front loaded Clothes washer automatic  - غسالة الملابس المحملة الأمامية أوتوماتيكية'].str.split('\n',expand=True)
            
            fcd=cd.join(data)
            fcd['#1 units owned - Front loaded Clothes washer automatic  ']=(fcd[0].str.split('/').str[1])
            fcd['#1 units owned - Front loaded Clothes washer automatic  ']=(fcd['#1 units owned - Front loaded Clothes washer automatic  '].str.split(':').str[1])
            
            
            
            fcd['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']=(fcd[1].str.split('/').str[1])
            fcd['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']=(fcd['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic'].str.split(':').str[1])
            
            fcd['#3 What is the capacity?']=(fcd[2].str.split('/').str[1])
            fcd['#3 What is the capacity?']=(fcd['#3 What is the capacity?'].str.split(':').str[1])
            fcd['#3 What is the capacity?']=(fcd['#3 What is the capacity?'].str.split('(').str[0])
            import re
            fcd['Front loaded Clothes washer automatic - The estimated Watts consumed per day'] =pd.to_numeric(fcd[4].str.replace('[^\d.]', ''), errors='coerce')
            
            fcd=fcd.drop([0,1,2,3,4], axis=1)
            
            col24=fcd.columns.get_loc('Front loaded Clothes washer automatic  - غسالة الملابس المحملة الأمامية أوتوماتيكية')
            
            first_fcdumn = fcd.pop('#1 units owned - Front loaded Clothes washer automatic  ')
            
            third_fcdumn=fcd.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic')
            second_fcdumn=fcd.pop('#3 What is the capacity?')
            
            fifth_fcdumn=fcd.pop('Front loaded Clothes washer automatic - The estimated Watts consumed per day')
            
            fcd.insert(col24+1, '#1 units owned - Front loaded Clothes washer automatic  ', first_fcdumn)
            
            fcd.insert(col24+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic', third_fcdumn)
            fcd.insert(col24+3, '#3 What is the capacity? - Front loaded Clothes washer automatic', second_fcdumn)
            fcd.insert(col24+4, 'Front loaded Clothes washer automatic - The estimated Watts consumed per day', fifth_fcdumn)
            
            #column 25th
            data=[]
            data = df['Top loaded Clothes washer automatic   - أعلى غسالة الملابس المحملة تلقائيًا'].str.split('\n',expand=True)
            
            topl=fcd.join(data)
            topl['#1 units owned - Top loaded Clothes washer automatic  ']=(topl[0].str.split('/').str[1])
            topl['#1 units owned - Top loaded Clothes washer automatic  ']=(topl['#1 units owned - Top loaded Clothes washer automatic  '].str.split(':').str[1])
            
            
            
            topl['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']=(topl[1].str.split('/').str[1])
            topl['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']=(topl['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic'].str.split(':').str[1])
            
            topl['#3 What is the capacity?']=(topl[2].str.split('/').str[1])
            topl['#3 What is the capacity?']=(topl['#3 What is the capacity?'].str.split(':').str[1])
            topl['#3 What is the capacity?']=(topl['#3 What is the capacity?'].str.split('(').str[0])
            import re
            topl['Top loaded Clothes washer automatic - The estimated Watts consumed per day'] =pd.to_numeric(topl[4].str.replace('[^\d.]', ''), errors='coerce')
            
            topl=topl.drop([0,1,2,3,4], axis=1)
            
            col25=topl.columns.get_loc('Top loaded Clothes washer automatic   - أعلى غسالة الملابس المحملة تلقائيًا')
            
            first_toplumn = topl.pop('#1 units owned - Top loaded Clothes washer automatic  ')
            
            third_toplumn=topl.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic')
            second_toplumn=topl.pop('#3 What is the capacity?')
            
            fifth_toplumn=topl.pop('Top loaded Clothes washer automatic - The estimated Watts consumed per day')
            
            topl.insert(col25+1, '#1 units owned - Top loaded Clothes washer automatic  ', first_toplumn)
            
            topl.insert(col25+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic', third_toplumn)
            topl.insert(col25+3, '#3 What is the capacity? - Top loaded Clothes washer automatic', second_toplumn)
            topl.insert(col25+4, 'Top loaded Clothes washer automatic - The estimated Watts consumed per day', fifth_toplumn)
            
            #column 26th
            data=[]
            data = df['Clothes washer normal   - غسالة الملابس عادية'].str.split('\n',expand=True)
            
            cwnl=topl.join(data)
            cwnl['#1 units owned - Clothes washer normal  ']=(cwnl[0].str.split('/').str[1])
            cwnl['#1 units owned - Clothes washer normal  ']=(cwnl['#1 units owned - Clothes washer normal  '].str.split(':').str[1])
            
            
            
            cwnl['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']=(cwnl[1].str.split('/').str[1])
            cwnl['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']=(cwnl['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal'].str.split(':').str[1])
            
            cwnl['#3 What is the capacity?']=(cwnl[2].str.split('/').str[1])
            cwnl['#3 What is the capacity?']=(cwnl['#3 What is the capacity?'].str.split(':').str[1])
            cwnl['#3 What is the capacity?']=(cwnl['#3 What is the capacity?'].str.split('(').str[0])
            import re
            cwnl['Clothes washer normal - The estimated Watts consumed per day'] =pd.to_numeric(cwnl[4].str.replace('[^\d.]', ''), errors='coerce')
            
            cwnl=cwnl.drop([0,1,2,3,4], axis=1)
            
            col26=cwnl.columns.get_loc('Clothes washer normal   - غسالة الملابس عادية')
            
            first_cwnlumn = cwnl.pop('#1 units owned - Clothes washer normal  ')
            
            third_cwnlumn=cwnl.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal')
            second_cwnlumn=cwnl.pop('#3 What is the capacity?')
            
            fifth_cwnlumn=cwnl.pop('Clothes washer normal - The estimated Watts consumed per day')
            
            cwnl.insert(col26+1, '#1 units owned - Clothes washer normal  ', first_cwnlumn)
            
            cwnl.insert(col26+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal', third_cwnlumn)
            cwnl.insert(col26+3, '#3 What is the capacity? - Clothes washer normal', second_cwnlumn)
            cwnl.insert(col26+4, 'Clothes washer normal - The estimated Watts consumed per day', fifth_cwnlumn)
            
            #column 26th
            data=[]
            data = df['Dish Washer - غسالة صحون'].str.split('\n',expand=True)
            
            dw=cwnl.join(data)
            dw['#1 units owned - Dish washer  ']=(dw[0].str.split('/').str[1])
            dw['#1 units owned - Dish washer  ']=(dw['#1 units owned - Dish washer  '].str.split(':').str[1])
            
            
            
            dw['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']=(dw[1].str.split('/').str[1])
            dw['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']=(dw['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer'].str.split(':').str[1])
            
            dw['#3 What is the capacity?']=(dw[2].str.split('/').str[1])
            dw['#3 What is the capacity?']=(dw['#3 What is the capacity?'].str.split(':').str[1])
            dw['#3 What is the capacity?']=(dw['#3 What is the capacity?'].str.split('(').str[0])
            import re
            dw['Dish washer - The estimated Watts consumed per day'] =pd.to_numeric(dw[4].str.replace('[^\d.]', ''), errors='coerce')
            
            dw=dw.drop([0,1,2,3,4], axis=1)
            
            col27=dw.columns.get_loc('Dish Washer - غسالة صحون')
            
            first_dwumn = dw.pop('#1 units owned - Dish washer  ')
            
            third_dwumn=dw.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer')
            second_dwumn=dw.pop('#3 What is the capacity?')
            
            fifth_dwumn=dw.pop('Dish washer - The estimated Watts consumed per day')
            
            dw.insert(col27+1, '#1 units owned - Dish washer  ', first_dwumn)
            
            dw.insert(col27+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer', third_dwumn)
            dw.insert(col27+3, '#3 What is the capacity? - Dish washer', second_dwumn)
            dw.insert(col27+4, 'Dish washer - The estimated Watts consumed per day', fifth_dwumn)
            
            #column 28th
            data=[]
            data = df['Freezer - الفريزر'].str.split('\n',expand=True)
            
            ffff=dw.join(data)
            ffff['#1 units owned - Freezer  ']=(ffff[0].str.split('/').str[1])
            ffff['#1 units owned - Freezer  ']=(ffff['#1 units owned - Freezer  '].str.split(':').str[1])
            
            
            
            ffff['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Freezer']=(ffff[1].str.split('/').str[1])
            ffff['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Freezer']=(ffff['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Freezer'].str.split(':').str[1])
            
            ffff['#3 What is the capacity?']=(ffff[2].str.split('/').str[1])
            ffff['#3 What is the capacity?']=(ffff['#3 What is the capacity?'].str.split(':').str[1])
            ffff['#3 What is the capacity?']=(ffff['#3 What is the capacity?'].str.split('(').str[0])
            import re
            ffff['Freezer - The estimated Watts consumed per day'] =pd.to_numeric(ffff[4].str.replace('[^\d.]', ''), errors='coerce')
            
            ffff=ffff.drop([0,1,2,3,4], axis=1)
            
            col28=ffff.columns.get_loc('Freezer - الفريزر')
            
            first_ffffumn = ffff.pop('#1 units owned - Freezer  ')
            
            third_ffffumn=ffff.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Freezer')
            second_ffffumn=ffff.pop('#3 What is the capacity?')
            
            fifth_ffffumn=ffff.pop('Freezer - The estimated Watts consumed per day')
            
            ffff.insert(col28+1, '#1 units owned - Freezer  ', first_ffffumn)
            
            ffff.insert(col28+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Freezer', third_ffffumn)
            ffff.insert(col28+3, '#3 What is the capacity? - Freezer', second_ffffumn)
            ffff.insert(col28+4, 'Freezer - The estimated Watts consumed per day', fifth_ffffumn)
            
            #column 29th
            data=[]
            data = df['Refrigerator - ثلاجة'].str.split('\n',expand=True)
            
            refri=ffff.join(data)
            refri['#1 units owned - Refrigerator  ']=(refri[0].str.split('/').str[1])
            refri['#1 units owned - Refrigerator  ']=(refri['#1 units owned - Refrigerator  '].str.split(':').str[1])
            
            
            
            refri['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Refrigerator']=(refri[1].str.split('/').str[1])
            refri['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Refrigerator']=(refri['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Refrigerator'].str.split(':').str[1])
            
            refri['#3 What is the capacity?']=(refri[2].str.split('/').str[1])
            refri['#3 What is the capacity?']=(refri['#3 What is the capacity?'].str.split(':').str[1])
            refri['#3 What is the capacity?']=(refri['#3 What is the capacity?'].str.split('(').str[0])
            import re
            refri['Refrigerator - The estimated Watts consumed per day'] =pd.to_numeric(refri[4].str.replace('[^\d.]', ''), errors='coerce')
            
            refri=refri.drop([0,1,2,3,4], axis=1)
            
            col29=refri.columns.get_loc('Refrigerator - ثلاجة')
            
            first_refriumn = refri.pop('#1 units owned - Refrigerator  ')
            
            third_refriumn=refri.pop('#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Refrigerator')
            second_refriumn=refri.pop('#3 What is the capacity?')
            
            fifth_refriumn=refri.pop('Refrigerator - The estimated Watts consumed per day')
            
            refri.insert(col29+1, '#1 units owned - Refrigerator  ', first_refriumn)
            
            refri.insert(col29+2, '#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Refrigerator', third_refriumn)
            refri.insert(col29+3, '#3 What is the capacity? - Refrigerator', second_refriumn)
            refri.insert(col29+4, 'Refrigerator - The estimated Watts consumed per day', fifth_refriumn)

            if st.checkbox("click to see the data with new features"):
                st.write(refri)
            
            

            
            
            import base64
            import io
            towrite = io.BytesIO()
            downloaded_file = refri.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
            towrite.seek(0)  # reset pointer
            b64 = base64.b64encode(towrite.read()).decode() 
            linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="Energy_consumption.xlsx">Download excel file</a>'
            st.markdown(linko, unsafe_allow_html=True)
        
            if st.checkbox("Click here to Analyse the Usages of energy by Different Appliances"):    
                title_container2 = st.container()
                col3, col4 ,  = st.columns([0.5,8])
                from PIL import Image
                
                with title_container2:
                    
                    with col4:
                        st.markdown('<h1 style="color: Blue;">Analysis on usages of energy by Different Appliances</h1>',
                                       unsafe_allow_html=True)
                        
                new_data=refri.copy()
                
                watt_data=new_data[['Air Conditioner Central Packaged  - The estimated Watts consumed per day',
 'Air Conditioner Central Split  - The estimated Watts consumed per day',
 'Air conditioning Units Mini split  - The estimated Watts consumed per day',
 'Air conditioning Units Windows  - The estimated Watts consumed per day',
 'Portable air cooler for single room - The estimated Watts consumed per day',
 'Air Purifier Device - The estimated Watts consumed per day',
 'Electric fan - The estimated Watts consumed per day',
 'Heater - Central  - The estimated Watts consumed per day',
 'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day',
 'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day',
 'Blender/mixer/food processor  - The estimated Watts consumed per day',
 'kettle- The estimated Watts consumed per day',
 'Toaster- The estimated Watts consumed per day',
 'Range - LPG- The estimated Watts consumed per day',
 'Range - Electric- The estimated Watts consumed per day',
 'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day',
 'Oven -(LPG/Electric)- The estimated Watts consumed per day',
 'Air fryer- The estimated Watts consumed per day',
 'Coffee Maker- The estimated Watts consumed per day',
 'Water Cooler - The estimated Watts consumed per day',
 'Water Heater - Central - The estimated Watts consumed per day',
 'Water Heater - Normal - The estimated Watts consumed per day',
 'Clothes dryer - The estimated Watts consumed per day',
 'Front loaded Clothes washer automatic - The estimated Watts consumed per day',
 'Top loaded Clothes washer automatic - The estimated Watts consumed per day',
 'Clothes washer normal - The estimated Watts consumed per day',
 'Dish washer - The estimated Watts consumed per day',
 'Freezer - The estimated Watts consumed per day',
 'Refrigerator - The estimated Watts consumed per day']]
                
                usages=watt_data.T
                usages=usages.reset_index()
                usages.rename( columns={0:'Usages in Watts / day','index':'Appliances'}, inplace=True)
                if st.checkbox("click to check estimated Watts consumed per day by different appliances at your home"):
                    st.write(watt_data)
                    
                    import plotly.express as px
                    
                    fig1 = px.bar(usages, x="Appliances", y="Usages in Watts / day", title="The Estimated watt consumed per Day by different Appliances",width=800, height=600)
        
                    st.write(fig1)
                    
                    st.subheader("What Spatial comfort equipment do you have")
                    
                    if st.checkbox("Lets check the details for Spatial comfort equipment"):
                        
                        spatial=new_data[['Air Conditioner Central Packaged  - The estimated Watts consumed per day',
 'Air Conditioner Central Split  - The estimated Watts consumed per day',
 'Air conditioning Units Mini split  - The estimated Watts consumed per day',
 'Air conditioning Units Windows  - The estimated Watts consumed per day',
 'Portable air cooler for single room - The estimated Watts consumed per day',
 'Air Purifier Device - The estimated Watts consumed per day',
 'Electric fan - The estimated Watts consumed per day',
 'Heater - Central  - The estimated Watts consumed per day',
 'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day',
 'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']]
                        
                        spatial.columns=spatial.columns.str.replace('- The estimated Watts consumed per day', ' ')
                        usages_spatial=spatial.T
                        
                        usages_spatial=usages_spatial.reset_index()
                        usages_spatial.rename( columns={0:'Usages in Watts / day','index':'Appliances'}, inplace=True)
                        if st.checkbox("click to check estimated Watts consumed per day by Spatial comfort equipment at your home"):
                            st.write(spatial)
                        
                        fig2 = px.bar(usages_spatial, x="Appliances", y="Usages in Watts / day", title="The Estimated watt consumed per Day by Spatial comfort equipment",width=800, height=600)
                        st.write(fig2)
                        
                        st.subheader("Lets check the statistics of spatial comfort equipment at your home")
                        stat_spatial=usages_spatial.describe()
                        
                        stat_spatial=stat_spatial.T
                       
                       
                        statmmm_spatial=pd.DataFrame({})
                        statmmm_spatial['mean']= stat_spatial['mean']
                        statmmm_spatial['min']= stat_spatial['min']
                        statmmm_spatial['max']= stat_spatial['max']
                        statmmm_spatial=statmmm_spatial.T
                        statmmm_spatial=statmmm_spatial.reset_index()
                        
                        statmmm_spatial.rename( columns={0:'Usages in Watts / day','index':'Statistics'}, inplace=True)
                        
                        if st.checkbox("click to check Statistics of estimated Watts consumed per day by Spatial comfort equipment at your home"):
                            st.write(stat_spatial)
                        
                            fig3 = px.bar(statmmm_spatial, x="Statistics", y="Usages in Watts / day", title="stat of the Estimated watt consumed per Day by Spatial comfort equipment",width=800, height=600)
                            st.write(fig3)
                        
                        st.subheader("Check the price for energy consumption based on appliance")
                        if st.checkbox("Click to check the energy charges imposed on particular/all spatial appliances"):
                            
                            st.subheader("Predicting charges(Tariff) For all the spatial appliances")
                            
                            aspa=st.text_input("Input the per watt charge in kwd","0.02")
                            aspa = float(aspa)  
                            
                            
                            total_charge= usages_spatial['Usages in Watts / day'].sum()*aspa
                            st.write("**Total Tariff Calculated Based on Energy Usages is [ {} ]**".format(total_charge.round(2)))
                            
                            st.subheader("Predict charges(Tariff) For individual spatial appliances")
                            if st.checkbox("Click to predict the charges imposed by individual spatial equipment appliances"):
                                
                                all_columns=spatial.columns.to_list()
                                selected_columns= st.multiselect("Select Appliances to predict the Tariff charges", all_columns)

                                tarfr=st.text_input("Input the per watt charge in kwd default value is entered","0.02")
                                tarfr= float(tarfr)  
                                appeach=spatial[selected_columns]*tarfr
                                st_each=appeach.T
                                st_each=st_each.reset_index()

                                st_each.rename(columns={0:'Tariff Calculated / Day in KWD','index':'Appliances'}, inplace=True)



                                st.dataframe(st_each)
                                fig4 = px.bar(st_each, x="Appliances", y="Tariff Calculated / Day in KWD", title="Tariff Calculated / Day in (KWD) for Spatial Appliances",width=800, height=600)
                                st.write(fig4)
                            
                    st.subheader("What Cooking Equipment do you have")
                    
                    if st.checkbox("Lets check the details for Cooking Equipment"):
                        
                        cooking=new_data[['Blender/mixer/food processor  - The estimated Watts consumed per day',
 'kettle- The estimated Watts consumed per day',
 'Toaster- The estimated Watts consumed per day',
 'Range - LPG- The estimated Watts consumed per day',
 'Range - Electric- The estimated Watts consumed per day',
 'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day',
 'Oven -(LPG/Electric)- The estimated Watts consumed per day',
 'Air fryer- The estimated Watts consumed per day',
 'Coffee Maker- The estimated Watts consumed per day']]
                        
                        cooking.columns=cooking.columns.str.replace('- The estimated Watts consumed per day', ' ')
                        usages_cooking=cooking.T
                        
                        usages_cooking=usages_cooking.reset_index()
                        usages_cooking.rename( columns={0:'Usages in Watts / day','index':'Appliances'}, inplace=True)
                        if st.checkbox("click to check estimated Watts consumed per day by Cooking Equipment at your home"):
                            st.write(cooking)
                        
                        fig8 = px.bar(usages_cooking, x="Appliances", y="Usages in Watts / day", title="The Estimated watt consumed per Day by Cooking Equipment ",width=800, height=600)
                        st.write(fig8)
                        
                        st.subheader("Lets check the statistics of Cooking Equipment at your home")
                        stat_cooking=usages_cooking.describe()
                        
                        stat_cooking=stat_cooking.T
                       
                       
                        statmmm_cooking=pd.DataFrame({})
                        statmmm_cooking['mean']= stat_cooking['mean']
                        statmmm_cooking['min']= stat_cooking['min']
                        statmmm_cooking['max']= stat_cooking['max']
                        statmmm_cooking=statmmm_cooking.T
                        statmmm_cooking=statmmm_cooking.reset_index()
                        
                        statmmm_cooking.rename( columns={0:'Usages in Watts / day','index':'Statistics'}, inplace=True)
                        
                        if st.checkbox("click to check Statistics of estimated Watts consumed per day by Cooking Equipment equipment at your home"):
                            st.write(stat_cooking)
                        
                            fig6 = px.bar(statmmm_cooking, x="Statistics", y="Usages in Watts / day", title="stat of the Estimated watt consumed per Day by Cooking Equipment ",width=800, height=600)
                            st.write(fig6)
                        
                        st.subheader("Check the price for energy consumption based on appliance")
                        if st.checkbox("Click to check the energy charges imposed on particular/all cooking appliances"):
                            
                            st.subheader("Predicting charges(Tariff) For all the cooking appliances")
                            
                            aspa=st.text_input("Input the per watt charge in kwd for your Appliances","0.02")
                            aspa = float(aspa)  
                            
                            
                            total_charge= usages_cooking['Usages in Watts / day'].sum()*aspa
                            st.write("**Total Tariff Calculated Based on Energy Usages is [ {} ]**".format(total_charge.round(2)))
                            
                            st.subheader("Predict charges(Tariff) For individual cooking appliances")
                            if st.checkbox("Click to predict the Energy charges for cooking appliances"):
                                all_columns=cooking.columns.to_list()
                                selected_columns= st.multiselect("Select Appliances to predict the Tariff charges", all_columns)

                                tarfr=st.text_input("Input the per watt charge in kwd default value is 0.02","0.02")
                                tarfr= float(tarfr)  
                                appeach=cooking[selected_columns]*tarfr
                                st_each=appeach.T
                                st_each=st_each.reset_index()

                                st_each.rename(columns={0:'Tariff Calculated / Day in KWD','index':'Appliances'}, inplace=True)



                                st.dataframe(st_each)
                                fig7 = px.bar(st_each, x="Appliances", y="Tariff Calculated / Day in KWD", title="Tariff Calculated / Day in (KWD) for cooking Appliances",width=800, height=600)
                                st.write(fig7)

                            
                            
                            
                            
                            
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      

if __name__=='__main__':
    main()
