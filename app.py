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
            new['#4 Unit size in Ton - Air Conditioner Central Packaged ']=(new['#4 Unit size in Ton - Air Conditioner Central Packaged '].str.split(' ').str[-3])
            
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
            data = df['Air Conditioner Central Split - وحدات تكييف (مركزي منفصلة)'].str.split('\n',expand=True)
            acss=new.join(data)
            
            acss['#1 units owned - Air Conditioner Central Split ']=(acss[0].str.split('/').str[1])
            acss['#1 units owned - Air Conditioner Central Split ']=(acss['#1 units owned - Air Conditioner Central Split '].str.split(':').str[1])
            
            acss['#2 Average temperature (C) setting - Air Conditioner Central Split ']=(acss[1].str.split('/').str[1])
            acss['#2 Average temperature (C) setting - Air Conditioner Central Split ']=(acss['#2 Average temperature (C) setting - Air Conditioner Central Split '].str.split(':').str[1])
            
            acss['#3 Operating in hours per day - Air Conditioner Central Split ']=(acss[2].str.split('/').str[1])
            acss['#3 Operating in hours per day - Air Conditioner Central Split ']=(acss['#3 Operating in hours per day - Air Conditioner Central Split '].str.split(':').str[1])
            
            acss['#4 Unit size in Ton - Air Conditioner Central Split ']=(acss[3].str.split('/').str[1])
            acss['#4 Unit size in Ton - Air Conditioner Central Split ']=(acss['#4 Unit size in Ton - Air Conditioner Central Split '].str.split(':').str[1])
            acss['#4 Unit size in Ton - Air Conditioner Central Split ']=(acss['#4 Unit size in Ton - Air Conditioner Central Split '].str.split(' ').str[-3])
            
            import re
            acss['Air Conditioner Central Split  - The estimated Watts consumed per day'] =pd.to_numeric(acss[5].str.replace('[^\d.]', ''), errors='coerce')
            
            acss=acss.drop([0,1,2,3,4,5], axis=1)
            
            col2=acss.columns.get_loc('Air Conditioner Central Split - وحدات تكييف (مركزي منفصلة)')
            
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
            data = df['Air conditioning Units Mini split - وحدة تكييف (مركزي منفصلة)'].str.split('\n',expand=True)
            acum=acss.join(data)
            
            acum['#1 units owned - Air conditioning Units Mini split ']=(acum[0].str.split('/').str[1])
            acum['#1 units owned - Air conditioning Units Mini split ']=(acum['#1 units owned - Air conditioning Units Mini split '].str.split(':').str[1])
            
            acum['#2 Average temperature (C) setting - Air conditioning Units Mini split ']=(acum[1].str.split('/').str[1])
            acum['#2 Average temperature (C) setting - Air conditioning Units Mini split ']=(acum['#2 Average temperature (C) setting - Air conditioning Units Mini split '].str.split(':').str[1])
            
            acum['#3 Operating in hours per day - Air conditioning Units Mini split ']=(acum[2].str.split('/').str[1])
            acum['#3 Operating in hours per day - Air conditioning Units Mini split ']=(acum['#3 Operating in hours per day - Air conditioning Units Mini split '].str.split(':').str[1])
            
            acum['#4 Unit size in Ton - Air conditioning Units Mini split ']=(acum[3].str.split('/').str[1])
            acum['#4 Unit size in Ton - Air conditioning Units Mini split ']=(acum['#4 Unit size in Ton - Air conditioning Units Mini split '].str.split(':').str[1])
            acum['#4 Unit size in Ton - Air conditioning Units Mini split ']=(acum['#4 Unit size in Ton - Air conditioning Units Mini split '].str.split(' ').str[-3])
            
            import re
            acum['Air conditioning Units Mini split  - The estimated Watts consumed per day'] =pd.to_numeric(acum[5].str.replace('[^\d.]', ''), errors='coerce')
            
            acum=acum.drop([0,1,2,3,4,5], axis=1)
            
            col3=acum.columns.get_loc('Air conditioning Units Mini split - وحدة تكييف (مركزي منفصلة)')
            
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
            data = df['Air conditioning Units Windows -  وحدات التكييف (نوافذ)'].str.split('\n',expand=True)
            acuw=acum.join(data)
            
            acuw['#1 units owned - Air conditioning Units Windows ']=(acuw[0].str.split('/').str[1])
            acuw['#1 units owned - Air conditioning Units Windows ']=(acuw['#1 units owned - Air conditioning Units Windows '].str.split(':').str[1])
            
            acuw['#2 Average temperature (C) setting - Air conditioning Units Windows ']=(acuw[1].str.split('/').str[1])
            acuw['#2 Average temperature (C) setting - Air conditioning Units Windows ']=(acuw['#2 Average temperature (C) setting - Air conditioning Units Windows '].str.split(':').str[1])
            
            acuw['#3 Operating in hours per day - Air conditioning Units Windows ']=(acuw[2].str.split('/').str[1])
            acuw['#3 Operating in hours per day - Air conditioning Units Windows ']=(acuw['#3 Operating in hours per day - Air conditioning Units Windows '].str.split(':').str[1])
            
            acuw['#4 Unit size in Ton - Air conditioning Units Windows ']=(acuw[3].str.split('/').str[1])
            acuw['#4 Unit size in Ton - Air conditioning Units Windows ']=(acuw['#4 Unit size in Ton - Air conditioning Units Windows '].str.split(':').str[1])
            acuw['#4 Unit size in Ton - Air conditioning Units Windows ']=(acuw['#4 Unit size in Ton - Air conditioning Units Windows '].str.split(' ').str[-3])
            
            import re
            acuw['Air conditioning Units Windows  - The estimated Watts consumed per day'] =pd.to_numeric(acuw[5].str.replace('[^\d.]', ''), errors='coerce')
            
            acuw=acuw.drop([0,1,2,3,4,5], axis=1)
            
            col4=acuw.columns.get_loc('Air conditioning Units Windows -  وحدات التكييف (نوافذ)')
            
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
            data = df['Blender/mixer/food processor - الخلاط//طاحن الطعام حلة أرز / حلة ضغط / مقلاة هوائية'].str.split('\n',expand=True)
            mbm=hso.join(data)
            mbm['#1 units owned - Blender/mixer/food processor ']=(mbm[0].str.split('/').str[1])
            mbm['#1 units owned - Blender/mixer/food processor ']=(mbm['#1 units owned - Blender/mixer/food processor '].str.split(':').str[1])
            
            
            
            mbm['#2 Operating in minutes per day - Blender/mixer/food processor ']=(mbm[1].str.split('/').str[1])
            mbm['#2 Operating in minutes per day - Blender/mixer/food processor ']=(mbm['#2 Operating in minutes per day - Blender/mixer/food processor '].str.split(':').str[1])
            
            
            import re
            mbm['Blender/mixer/food processor  - The estimated Watts consumed per day'] =pd.to_numeric(mbm[3].str.replace('[^\d.]', ''), errors='coerce')
            
            mbm=mbm.drop([0,1,2,3], axis=1)
            
            col11=mbm.columns.get_loc('Blender/mixer/food processor - الخلاط//طاحن الطعام حلة أرز / حلة ضغط / مقلاة هوائية')
            
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
            data = df['Range - LPG - موقد للطبخ - غاز البترول المسال (يشمل غاز البترول المسال بالفرن ، غاز البترول المسال بالكهرباء)'].str.split('\n',expand=True)
            lpg=toast.join(data)
            lpg['#1 units owned - Range - LPG ']=(lpg[0].str.split('/').str[1])
            lpg['#1 units owned - Range - LPG ']=(lpg['#1 units owned - Range - LPG '].str.split(':').str[1])
            
            
            
            lpg['#2 Operating in minutes per day - Range - LPG ']=(lpg[1].str.split('/').str[1])
            lpg['#2 Operating in minutes per day - Range - LPG ']=(lpg['#2 Operating in minutes per day - Range - LPG '].str.split(':').str[1])
            
            
            import re
            lpg['Range - LPG- The estimated Watts consumed per day'] =pd.to_numeric(lpg[3].str.replace('[^\d.]', ''), errors='coerce')
            
            lpg=lpg.drop([0,1,2,3], axis=1)
            
            col14=lpg.columns.get_loc('Range - LPG - موقد للطبخ - غاز البترول المسال (يشمل غاز البترول المسال بالفرن ، غاز البترول المسال بالكهرباء)')
            
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
            data = df['Oven -(LPG/Electric) - فرن كهربائي للطبخ متنقل'].str.split('\n',expand=True)
            ole=celi.join(data)
            ole['#1 units owned - Oven -(LPG/Electric) ']=(ole[0].str.split('/').str[1])
            ole['#1 units owned - Oven -(LPG/Electric) ']=(ole['#1 units owned - Oven -(LPG/Electric) '].str.split(':').str[1])
            
            
            
            ole['#2 Operating in minutes per day - Oven -(LPG/Electric) ']=(ole[1].str.split('/').str[1])
            ole['#2 Operating in minutes per day - Oven -(LPG/Electric) ']=(ole['#2 Operating in minutes per day - Oven -(LPG/Electric) '].str.split(':').str[1])
            
            
            import re
            ole['Oven -(LPG/Electric)- The estimated Watts consumed per day'] =pd.to_numeric(ole[3].str.replace('[^\d.]', ''), errors='coerce')
            
            ole=ole.drop([0,1,2,3], axis=1)
            
            col17=ole.columns.get_loc('Oven -(LPG/Electric) - فرن كهربائي للطبخ متنقل')
            
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
            data = df['Water Heater - Normal -  مستقل سخان المياه -عادي'].str.split('\n',expand=True)
            whn=whc.join(data)
            whn['#1 units owned - Water Heater - Normal  ']=(whn[0].str.split('/').str[1])
            whn['#1 units owned - Water Heater - Normal  ']=(whn['#1 units owned - Water Heater - Normal  '].str.split(':').str[1])
            
            
            
            whn['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']=(whn[1].str.split('/').str[1])
            whn['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']=(whn['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal'].str.split(':').str[1])
            
            
            import re
            whn['Water Heater - Normal - The estimated Watts consumed per day'] =pd.to_numeric(whn[3].str.replace('[^\d.]', ''), errors='coerce')
            
            whn=whn.drop([0,1,2,3], axis=1)
            
            col22=whn.columns.get_loc('Water Heater - Normal -  مستقل سخان المياه -عادي')
            
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

            ffff['#2 What is the capacity?']=(ffff[1].str.split('/').str[1])
            ffff['#2 What is the capacity?']=(ffff['#2 What is the capacity?'].str.split(':').str[1])
            ffff['#2 What is the capacity?']=(ffff['#2 What is the capacity?'].str.split('(').str[0])
            import re
            ffff['Freezer - The estimated Watts consumed per day'] =pd.to_numeric(ffff[3].str.replace('[^\d.]', ''), errors='coerce')
            
            ffff=ffff.drop([0,1,2,3], axis=1)

            col28=ffff.columns.get_loc('Freezer - الفريزر')

            first_ffffumn = ffff.pop('#1 units owned - Freezer  ')


            second_ffffumn=ffff.pop('#2 What is the capacity?')

            fifth_ffffumn=ffff.pop('Freezer - The estimated Watts consumed per day')

            ffff.insert(col28+1, '#1 units owned - Freezer  ', first_ffffumn)
            ffff.insert(col28+2, '#2 What is the capacity? - Freezer', second_ffffumn)
            ffff.insert(col28+3, 'Freezer - The estimated Watts consumed per day', fifth_ffffumn)

            
            #column 29th
            data=[]
            data = df['Refrigerator - ثلاجة'].str.split('\n',expand=True)

            refri=ffff.join(data)
            refri['#1 units owned - Refrigerator  ']=(refri[0].str.split('/').str[1])
            refri['#1 units owned - Refrigerator  ']=(refri['#1 units owned - Refrigerator  '].str.split(':').str[1])

            refri['#2 What is the capacity?']=(refri[1].str.split('/').str[1])
            refri['#2 What is the capacity?']=(refri['#2 What is the capacity?'].str.split(':').str[1])
            refri['#2 What is the capacity?']=(refri['#2 What is the capacity?'].str.split('(').str[0])
            import re
            refri['Refrigerator - The estimated Watts consumed per day'] =pd.to_numeric(refri[3].str.replace('[^\d.]', ''), errors='coerce')

            refri=refri.drop([0,1,2,3], axis=1)

            col29=refri.columns.get_loc('Refrigerator - ثلاجة')

            first_refriumn = refri.pop('#1 units owned - Refrigerator  ')


            second_refriumn=refri.pop('#2 What is the capacity?')

            fifth_refriumn=refri.pop('Refrigerator - The estimated Watts consumed per day')

            refri.insert(col29+1, '#1 units owned - Refrigerator  ', first_refriumn)

            refri.insert(col29+2, '#3 What is the capacity? - Refrigerator', second_refriumn)
            refri.insert(col29+3, 'Refrigerator - The estimated Watts consumed per day', fifth_refriumn)

            if st.checkbox("click to see the data with new features"):
                st.write(refri)
            
            

            refri=refri.apply(pd.to_numeric,errors='ignore')
            
            import base64
            import io
            towrite = io.BytesIO()
            downloaded_file = refri.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
            towrite.seek(0)  # reset pointer
            b64 = base64.b64encode(towrite.read()).decode() 
            linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="Energy_consumption.xlsx">Download excel file</a>'
            st.markdown(linko, unsafe_allow_html=True)
        
            #if st.checkbox("Click here to Analyse the Usages of energy by Different Appliances"):    
            title_container2 = st.container()
            col3, col4 ,  = st.columns([0.5,8])
            from PIL import Image
            
            with title_container2:
                
                with col4:
                    st.markdown('<h1 style="color: Blue;">Analysis on usages of energy by Different Appliances</h1>',
                                   unsafe_allow_html=True)
                        
                new_data=refri.copy()
                
                watt_data=new_data[[
 'Air Conditioner Central Packaged  - The estimated Watts consumed per day',
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
            st.subheader("Demographic Variables")
            
            demo=refri.copy()
            demo['الفئة العمرية لمجيب الاستبيان']= demo['الفئة العمرية لمجيب الاستبيان'].replace({'اقل من ٢٦ سنة': 'Less than 26 years old', 'من ٢٦ لي ٣٥ سنة': 'From 26 to 35 years old', 'من ٣٦ لي ٤٥ سنة': 'From 36 to 45 years old', 'من ٤٦ لي ٥٥ سنة': 'From 46 to 55 years old','من ٥٦ لي ٦٥':'From 56 to 65 year old','اكبر من ٦٥ سنة':'More than 65 years old'})   
            st.markdown('**Category**')
            #st.markdown("**Age group**")
            age = demo['الفئة العمرية لمجيب الاستبيان']
            counts = age.value_counts()
             
            percent100 = age.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            age=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #age.reset_index(inplace = True)
             #age.rename(columns={'index':'Age Group'},inplace=True)
           
            #st.table(data=age)
             
            #st.markdown("**Family Size**")
            demo['حجم الأسرة مع العمالة المنزلية']= demo['حجم الأسرة مع العمالة المنزلية'].replace({'اقل من ٣ اشخاص': 'Less than 3 persons', 'من ٣ لي ٥ اشخاص': 'From 3 to 5 people', 'من ٦ لي ٨ اشخاص': 'From 6 to 8 people', 'من ٩ لي ١١ شخص': 'From 9 to 11 people','اكثر من ١١ شخص':'More than 11 people'})  
            family=demo['حجم الأسرة مع العمالة المنزلية']
            counts = family.value_counts()
             
            percent100 = family.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            family=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #family.reset_index(inplace = True)
             #family.rename(columns={'index':'Family Size'},inplace=True)
           
           # st.table(data=family)
             
            #st.markdown("**Educational qualification**")
             
            demo['اعلى مؤهل دراسي لرب الأسرة']= demo['اعلى مؤهل دراسي لرب الأسرة'].replace({'ثانوي او مايعادل': 'secondary or equivalent', 'دبلوم': 'diploma', 'جامعي': 'collegiate', 'ماجستير': 'Master','دكتوراه':'PHD'})  
            # demo['اعلى مؤهل دراسي لرب الأسرة']=demo['اعلى مؤهل دراسي لرب الأسرة'].map(lambda x: translator.translate(x, dest="en").text)
             
            Education=demo['اعلى مؤهل دراسي لرب الأسرة']
            counts = Education.value_counts()
             
            percent100 = Education.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            Education=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #Education.reset_index(inplace = True)
             #Education.rename(columns={'index':'Educational qualification'},inplace=True)
             
            #st.table(data=Education)
             
            #st.markdown("**Functional Status**")
             
            demo['الحالة الوظيفية']= demo['الحالة الوظيفية'].replace({'موظف في قطاع حكومي': 'An employee in the government sector', 'موظف في قطاع خاص': 'An employee in the Private sector', 'اعمال حره': 'Business owner', 'متقاعد': 'Retired'})  
            function=demo['الحالة الوظيفية']
            counts = function.value_counts()
             
            percent100 = function.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            function=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #function.reset_index(inplace = True)
             #function.rename(columns={'index':'Functional Status'},inplace=True)
             
            #st.table(data=function)
             
            #st.markdown("**Governorate**")
             
            demo['المحافظة تبعا للسكن']= demo['المحافظة تبعا للسكن'].replace({'الأحمدي': 'Al-Ahmadi', 'الجهراء': 'Al-Jahra', 'الفروانية': 'Al-Farwaniyah', 'حولي': 'Hawally','العاصمة':'Al-Asimah','مبارك الكبير':'Mubarak Al-Kabeer'})  
            goveranate=demo['المحافظة تبعا للسكن']
            counts = goveranate.value_counts()
             
            percent100 = goveranate.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            goveranate=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #goveranate.reset_index(inplace = True)
             #goveranate.rename(columns={'index':'Governorate'},inplace=True)
            #st.table(data=goveranate)
             
            #st.markdown("**Household income**")
            demo['إجمالي دخل الأسرة شهريًا بالدينار الكويتي']= demo['إجمالي دخل الأسرة شهريًا بالدينار الكويتي'].replace({'اقل من او يساوي ١٠٠٠ د.ك.': 'Less than or equal to 1000 KD', 'من ١٠٠١ لي ٢٠٠٠ د.ك.': 'From 1001 to 2000 KD', 'من ٢٠٠١ لي ٣٠٠٠ د.ك.': 'From 2001 to 3000 KD', 'من ٣٠٠١ لي ٤٠٠٠ د.ك.': 'From 3001 to 4000 KD','من ٤٠٠١ لي ٥٠٠٠ د.ك.':'From 4001 to 5000 KD','اكثر من ٥٠٠٠ د.ك.':'More than 5000 KD'})  
            income=demo['إجمالي دخل الأسرة شهريًا بالدينار الكويتي']
            counts = income.value_counts()
             
            percent100 = income.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            income=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #income.reset_index(inplace = True)
             #income.rename(columns={'index':'Household income'},inplace=True)
            #st.table(data=income)
             
            #st.markdown("**Type of housing unit**")
            demo['نوع الوحدة السكنية']= demo['نوع الوحدة السكنية'].replace({'شقة صغيرة (عدد 3 غرف أو أقل)': 'Small apartment (3 rooms or less)','منزل من طابق واحد أو شقة كبيرة (أكثر من 3 غرف)': 'Bungalow or large apartment (more than 3 rooms)', 'منزل من طابقين': 'Two-story house', 'منزل من طابقين و سرداب': 'Two-storey house and basement','منزل من ثلاثة طوابق':'Three-storey house','منزل من ثلاثة طوابق و سرداب':'Three storey house and basement'})  
            typ=demo['نوع الوحدة السكنية']
            counts = typ.value_counts()
             
            percent100 = typ.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            typ=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #typ.reset_index(inplace = True)
             #typ.rename(columns={'index':'Type of housing unit'},inplace=True)
            #st.table(data=typ)
             
            #st.markdown("**Solar Panel**")
            demo['هل لديك الواح شمسية تستخدمها لتوليد الطاقة الكهربائية لديك في المنزل؟']= demo['هل لديك الواح شمسية تستخدمها لتوليد الطاقة الكهربائية لديك في المنزل؟'].replace({'نعم': 'Yes','لا': 'No'})  
            sol=demo['هل لديك الواح شمسية تستخدمها لتوليد الطاقة الكهربائية لديك في المنزل؟']
            counts = sol.value_counts()
             
            percent100 = sol.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            sol=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #sol.reset_index(inplace = True)
             #sol.rename(columns={'index':'Solar'},inplace=True)
            #st.table(data=sol)
             
            #st.markdown("**Smart home system**")
            demo['هل تستخدم نظام المنزل الذكي؟']= demo['هل تستخدم نظام المنزل الذكي؟'].replace({'نعم': 'Yes','لا': 'No'})  
            shs=demo['هل تستخدم نظام المنزل الذكي؟']
            counts = shs.value_counts()
             
            percent100 = shs.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            shs=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #shs.reset_index(inplace = True)
             #shs.rename(columns={'index':'Smart Home System'},inplace=True)
            #st.table(data=shs)
             
            #st.markdown("**Light occupancy sensors**")
            demo['هل لديك مستشعرات إشغال الضوء؟']= demo['هل لديك مستشعرات إشغال الضوء؟'].replace({'نعم': 'Yes','لا': 'No'})  
            los=demo['هل لديك مستشعرات إشغال الضوء؟']
            counts = los.value_counts()
             
            percent100 = los.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
            n=counts.sum()
            los=pd.DataFrame({"Overall (N={})".format(n): counts, '%': percent100})
             #los.reset_index(inplace = True)
             #los.rename(columns={'index':'Light occupancy sensors'},inplace=True)
             
            #st.table(data=los)
             
            #st.markdown("**Average operating hours during summer**")
            aos=demo['في تقديرك، متوسط ساعات التشغيل لأجهزة التكييف في اليوم (مثل مكيفات الهواء والوحدات المركزية) خلال فصل الصيف']
            aos_d=aos.describe()
             
            aos_m=pd.DataFrame({"Overall (N={})".format(n): aos_d['mean'].round(2).astype(str)+'({})'.format(aos_d['std'].round(2))},index=['Mean(SD)'])
            aos_mi=pd.DataFrame({"Overall (N={})".format(n): aos_d['min'].round(2).astype(str)+' - {}'.format(aos_d['max'].round(2))},index=['Range'])
            aos=aos_m.append(aos_mi)
             
             
             
            #st.table(data=aos)
             
            #st.markdown("**Average operating hours during winter**")
            aos_w=demo['في تقديرك ، متوسط ساعات تشغيل لأجهزة التكييف يوميًا (مثل مكيفات الهواء والوحدات المركزية) خلال فصل الشتاء']
            aos_d=aos_w.describe()
             
            aos_m=pd.DataFrame({"Overall (N={})".format(n): aos_d['mean'].round(2).astype(str)+'({})'.format(aos_d['std'].round(2))},index=['Mean(SD)'])
            aos_mi=pd.DataFrame({"Overall (N={})".format(n): aos_d['min'].round(2).astype(str)+' - {}'.format(aos_d['max'].round(2))},index=['Range'])
            aos_w=aos_m.append(aos_mi)
             
             #frames = [age, family, Education,function,goveranate,income,typ,sol,shs,los,aos,aos_w]
             #ff=[age,family]
    
             #result = pd.concat(ff, ignore_index=True,axis=0)
             #st.write(result)
             
            #st.table(data=aos_w)
             
            new=demo.copy() 
            
            col5='المحافظة تبعا للسكن'
            
            
            new.rename(columns={col5:'Governorate'}, inplace=True)
            
            new=new.apply(pd.to_numeric,errors='ignore')
            
            
                
            if st.checkbox("Table 1: Demographic variables"):
                st.markdown("**Age group**")
                st.table(data=age)
                st.markdown("**Family Size**")
                st.table(data=family)
                st.markdown("**Educational qualification**")
                st.table(data=Education)
                st.markdown("**Functional Status**")
                st.table(data=function)
                st.markdown("**Governorate**")
                st.table(data=goveranate)
                st.markdown("**Household income**")
                st.table(data=income)
                st.markdown("**Type of housing unit**")
                st.table(data=typ)
                st.markdown("**Solar Panel**")
                st.table(data=sol)
                st.markdown("**Smart home system**")
                st.table(data=shs)
                st.markdown("**Light occupancy sensors**")
                st.table(data=los)
                st.markdown("**Average operating hours during summer**")
                st.table(data=aos)
                st.markdown("**Average operating hours during winter**")
                st.table(data=aos_w)
            st.subheader("Analysis on different Spatial -Thermal comfort equipment (Air- conditioners)")    
            if st.checkbox("➡️ Analysis and statistics on different Spatial -Thermal comfort equipment (Air- conditioners)"):  
                st.markdown("**Air Conditioner**")
                if st.checkbox("Click here for Air conditioner device"):
                    st.markdown("**Units owned of Air Conditioner**")
                    if st.checkbox("Table 2. Descriptive Statistics - Units owned of Air Conditioner"):
                            
                        col5='المحافظة تبعا للسكن'
                        col2='#1 units owned - Air Conditioner Central Packaged '
                        acp=new.groupby('Governorate')['#1 units owned - Air Conditioner Central Packaged '].describe()
                        acp.reset_index(inplace = True)
                        acp.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Units owned - AC Central Packaged**")
                        st.table(acp)
                        
                        
                        acs=new.groupby('Governorate')['#1 units owned - Air Conditioner Central Split '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Units owned - AC Central Split**")
                        st.table(acs)
                            
                        acm=new.groupby('Governorate')['#1 units owned - Air conditioning Units Mini split '].describe()
                        acm.reset_index(inplace = True)
                        acm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Units owned - AC Mini split**")
                        st.table(acm)   
                        
                        acw=new.groupby('Governorate')['#1 units owned - Air conditioning Units Windows '].describe()
                        acw.reset_index(inplace = True)
                        acw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Units owned - AC Units Windows**")
                        st.table(acw)
                        
                    if st.checkbox("Table 3. Association of Air Conditioner (Units Owned) with Governorate"):
                        #1   
                        dd=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Packaged ']].std()
                        dd=dd.T
                        dd.reset_index(inplace=True)
                        dd.rename(columns={'index':'Units owned - AC Central Packaged'},inplace=True)
                        dd['Units owned - AC Central Packaged'] = dd['Units owned - AC Central Packaged'].replace({'#1 units owned - Air Conditioner Central Packaged ': 'Std'})
                         
                        acpp=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Packaged ']].mean()
                        acpp=acpp.T
                        acpp.reset_index(inplace = True)
                         
                        acpp.rename(columns={'index':'Units owned - AC Central Packaged'},inplace=True)
                        acpp['Units owned - AC Central Packaged'] = acpp['Units owned - AC Central Packaged'].replace({'#1 units owned - Air Conditioner Central Packaged ': 'Mean(SD)'})
                        acpp['Al-Ahmadi']=acpp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(dd['Al-Ahmadi'][0].round(2))
                        acpp['Al-Asimah']=acpp['Al-Asimah'].round(2).astype(str)+'({})'.format(dd['Al-Asimah'][0].round(2))
                        acpp['Al-Farwaniyah']=acpp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(dd['Al-Farwaniyah'][0].round(2))
                        acpp['Al-Jahra']=acpp['Al-Jahra'].round(2).astype(str)+'({})'.format(dd['Al-Jahra'][0].round(2))
                        acpp['Hawally']=acpp['Hawally'].round(2).astype(str)+'({})'.format(dd['Hawally'][0].round(2))
                        acpp['Mubarak Al-Kabeer']=acpp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(dd['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        rang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Packaged ']].min()
                        rang_m=rang_m.T
                         
                        rang_m.reset_index(inplace=True)
                        rang_m.rename(columns={'index':'Units owned - AC Central Packaged'},inplace=True)
                        rang_m['Units owned - AC Central Packaged'] = rang_m['Units owned - AC Central Packaged'].replace({'#1 units owned - Air Conditioner Central Packaged ': 'min'})
                        
                        rang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Packaged ']].max()
                        rang_mx=rang_mx.T
                        rang_mx.reset_index(inplace=True)
                        rang_mx.rename(columns={'index':'Units owned - AC Central Packaged'},inplace=True)
                        rang_mx['Units owned - AC Central Packaged'] = rang_mx['Units owned - AC Central Packaged'].replace({'#1 units owned - Air Conditioner Central Packaged ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Packaged ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Units owned - AC Central Packaged'},inplace=True)
                        vc['Units owned - AC Central Packaged'] = vc['Units owned - AC Central Packaged'].replace({'#1 units owned - Air Conditioner Central Packaged ': 'count'})
                        
                        rang_mx['Al-Ahmadi']=rang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Ahmadi'][0].round(2))
                        rang_mx['Al-Asimah']=rang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Asimah'][0].round(2))
                        rang_mx['Al-Farwaniyah']=rang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Farwaniyah'][0].round(2))
                        rang_mx['Al-Jahra']=rang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Jahra'][0].round(2))
                        rang_mx['Hawally']=rang_m['Hawally'].round(2).astype(str)+' - {}'.format(rang_mx['Hawally'][0].round(2))
                        rang_mx['Mubarak Al-Kabeer']=rang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(rang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_res = acpp.append(rang_mx)
                        df_res=df_res.reset_index(drop=True)
                        
                        df_res['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_res['Al-Ahmadi']
                        del df_res['Al-Ahmadi']
                        
                        df_res['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_res['Al-Asimah']
                        del df_res['Al-Asimah']
                        
                        df_res['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_res['Al-Farwaniyah']
                        del df_res['Al-Farwaniyah']
                        
                        df_res['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_res['Al-Jahra']
                        del df_res['Al-Jahra']
                         
                        df_res['Hawally (N={})'.format(vc['Hawally'][0])]=df_res['Hawally']
                        del df_res['Hawally']
                         
                        df_res['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_res['Mubarak Al-Kabeer']
                        del df_res['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Units owned - AC Central Packaged**")
                        st.write(df_res)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Split ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Units owned - AC Central Split'},inplace=True)
                        cs['Units owned - AC Central Split'] = cs['Units owned - AC Central Split'].replace({'#1 units owned - Air Conditioner Central Split ': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Split ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Units owned - AC Central Split'},inplace=True)
                        acsp['Units owned - AC Central Split'] = acsp['Units owned - AC Central Split'].replace({'#1 units owned - Air Conditioner Central Split ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        rang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Split ']].min()
                        rang_m=rang_m.T
                        
                        rang_m.reset_index(inplace=True)
                        rang_m.rename(columns={'index':'Units owned - AC Central Split'},inplace=True)
                        rang_m['Units owned - AC Central Split'] = rang_m['Units owned - AC Central Split'].replace({'#1 units owned - Air Conditioner Central Split ': 'min'})
                         
                        rang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Split ']].max()
                        rang_mx=rang_mx.T
                        rang_mx.reset_index(inplace=True)
                        rang_mx.rename(columns={'index':'Units owned - AC Central Split'},inplace=True)
                        rang_mx['Units owned - AC Central Split'] = rang_mx['Units owned - AC Central Split'].replace({'#1 units owned - Air Conditioner Central Split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Units owned - AC Central Split'},inplace=True)
                        vc['Units owned - AC Central Split'] = vc['Units owned - AC Central Split'].replace({'#1 units owned - Air Conditioner Central Split ': 'count'})
                        
                        rang_mx['Al-Ahmadi']=rang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Ahmadi'][0].round(2))
                        rang_mx['Al-Asimah']=rang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Asimah'][0].round(2))
                        rang_mx['Al-Farwaniyah']=rang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Farwaniyah'][0].round(2))
                        rang_mx['Al-Jahra']=rang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Jahra'][0].round(2))
                        rang_mx['Hawally']=rang_m['Hawally'].round(2).astype(str)+' - {}'.format(rang_mx['Hawally'][0].round(2))
                        rang_mx['Mubarak Al-Kabeer']=rang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(rang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(rang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Units owned - AC Central Split**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Mini split ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Units owned - AC Mini split'},inplace=True)
                        ms['Units owned - AC Mini split'] = ms['Units owned - AC Mini split'].replace({'#1 units owned - Air conditioning Units Mini split ': 'Std'})
                         
                        acms=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Mini split ']].mean()
                        acms=acms.T
                        acms.reset_index(inplace = True)
                         
                        acms.rename(columns={'index':'Units owned - AC Mini split'},inplace=True)
                        acms['Units owned - AC Mini split'] = acms['Units owned - AC Mini split'].replace({'#1 units owned - Air conditioning Units Mini split ': 'Mean(SD)'})
                        acms['Al-Ahmadi']=acms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        acms['Al-Asimah']=acms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        acms['Al-Farwaniyah']=acms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        acms['Al-Jahra']=acms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        acms['Hawally']=acms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        acms['Mubarak Al-Kabeer']=acms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        rang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Mini split ']].min()
                        rang_m=rang_m.T
                        
                        rang_m.reset_index(inplace=True)
                        rang_m.rename(columns={'index':'Units owned - AC Mini split'},inplace=True)
                        rang_m['Units owned - AC Mini split'] = rang_m['Units owned - AC Mini split'].replace({'#1 units owned - Air conditioning Units Mini split ': 'min'})
                         
                        rang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Mini split ']].max()
                        rang_mx=rang_mx.T
                        rang_mx.reset_index(inplace=True)
                        rang_mx.rename(columns={'index':'Units owned - AC Mini split'},inplace=True)
                        rang_mx['Units owned - AC Mini split'] = rang_mx['Units owned - AC Mini split'].replace({'#1 units owned - Air conditioning Units Mini split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Mini split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Units owned - AC Mini split'},inplace=True)
                        vc['Units owned - AC Mini split'] = vc['Units owned - AC Mini split'].replace({'#1 units owned - Air conditioning Units Mini split ': 'count'})
                        
                        rang_mx['Al-Ahmadi']=rang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Ahmadi'][0].round(2))
                        rang_mx['Al-Asimah']=rang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Asimah'][0].round(2))
                        rang_mx['Al-Farwaniyah']=rang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Farwaniyah'][0].round(2))
                        rang_mx['Al-Jahra']=rang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Jahra'][0].round(2))
                        rang_mx['Hawally']=rang_m['Hawally'].round(2).astype(str)+' - {}'.format(rang_mx['Hawally'][0].round(2))
                        rang_mx['Mubarak Al-Kabeer']=rang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(rang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = acms.append(rang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Units owned - AC Mini split**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Windows ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Units owned - AC Units Windows'},inplace=True)
                        uw['Units owned - AC Units Windows'] = uw['Units owned - AC Units Windows'].replace({'#1 units owned - Air conditioning Units Windows ': 'Std'})
                        
                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Windows ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)
                        
                        acuw.rename(columns={'index':'Units owned - AC Units Windows'},inplace=True)
                        acuw['Units owned - AC Units Windows'] = acuw['Units owned - AC Units Windows'].replace({'#1 units owned - Air conditioning Units Windows ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        rang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Windows ']].min()
                        rang_m=rang_m.T
                        
                        rang_m.reset_index(inplace=True)
                        rang_m.rename(columns={'index':'Units owned - AC Units Windows'},inplace=True)
                        rang_m['Units owned - AC Units Windows'] = rang_m['Units owned - AC Units Windows'].replace({'#1 units owned - Air conditioning Units Windows ': 'min'})
                        
                        rang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Windows ']].max()
                        rang_mx=rang_mx.T
                        rang_mx.reset_index(inplace=True)
                        rang_mx.rename(columns={'index':'Units owned - AC Units Windows'},inplace=True)
                        rang_mx['Units owned - AC Units Windows'] = rang_mx['Units owned - AC Units Windows'].replace({'#1 units owned - Air conditioning Units Windows ': 'Range'})
                        
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Windows ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Units owned - AC Units Windows'},inplace=True)
                        vc['Units owned - AC Units Windows'] = vc['Units owned - AC Units Windows'].replace({'#1 units owned - Air conditioning Units Windows ': 'count'})
                        
                        rang_mx['Al-Ahmadi']=rang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Ahmadi'][0].round(2))
                        rang_mx['Al-Asimah']=rang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Asimah'][0].round(2))
                        rang_mx['Al-Farwaniyah']=rang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Farwaniyah'][0].round(2))
                        rang_mx['Al-Jahra']=rang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(rang_mx['Al-Jahra'][0].round(2))
                        rang_mx['Hawally']=rang_m['Hawally'].round(2).astype(str)+' - {}'.format(rang_mx['Hawally'][0].round(2))
                        rang_mx['Mubarak Al-Kabeer']=rang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(rang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        df_auw = acuw.append(rang_mx)
                        df_auw=df_auw.reset_index(drop=True)
                         
                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']
                         
                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']
                         
                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']
                        
                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']
                         
                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']
                         
                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Units owned - AC Units Windows**")
                        st.write(df_auw)
                         
                         
                        #graph
                         
                        gacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Packaged ']].sum()
                        gacp.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Conditioner Central Split ']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Mini split ']].sum()
                        gams.reset_index(inplace=True)
                        
                        gauw=new.groupby('Governorate',as_index=True)[['#1 units owned - Air conditioning Units Windows ']].sum()
                        gauw.reset_index(inplace=True)
                        
                        import plotly.express as px
                        st.markdown("**Figure1. Distribution of Air Conditioner units owned under different Governorate**")
                        import plotly.graph_objects as go
                        fig = go.Figure(data=[
                            go.Bar(name='AC central packaged', x=gacp['Governorate'], y=gacp['#1 units owned - Air Conditioner Central Packaged ']),
                             go.Bar(name='AC central split', x=gacs['Governorate'], y=gacs['#1 units owned - Air Conditioner Central Split ']),
                             go.Bar(name='AC mini split', x=gams['Governorate'], y=gams['#1 units owned - Air conditioning Units Mini split ']),
                             go.Bar(name='AC unit windows', x=gauw['Governorate'], y=gauw['#1 units owned - Air conditioning Units Windows ']),
                        ])
                        # Change the bar mode
                        fig.update_layout(barmode='stack')
                        #fig.show()
                        
                        st.write(fig)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure2. Air Conditioners Units owned by participants under different Governorate**")
                        fig6 = px.bar(gacp, x="Governorate", y='#1 units owned - Air Conditioner Central Packaged ', color="Governorate")
                        fig7 = px.bar(gacs, x="Governorate", y='#1 units owned - Air Conditioner Central Split ', color="Governorate")
                        fig8 = px.bar(gams, x="Governorate", y='#1 units owned - Air conditioning Units Mini split ', color="Governorate")
                        fig9 = px.bar(gauw, x="Governorate", y='#1 units owned - Air conditioning Units Windows ', color="Governorate")
                        st.write(fig6)
                        st.write(fig7)
                        st.write(fig8)
                        st.write(fig9)
                    # temperature
                    
                    st.markdown("**Temperature of Air Conditioner**")
                    if st.checkbox("Table4. Descriptive Statistics- Temperature of Air Conditioner"):
                            
                        
                        atp=new.groupby('Governorate')['#2 Average temperature (C) setting - Air Conditioner Central Packaged '].describe()
                        atp.reset_index(inplace = True)
                        atp.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Average temperature  - AC Central Packaged**")
                        st.table(atp)
                        
                        
                        acs=new.groupby('Governorate')['#2 Average temperature (C) setting - Air Conditioner Central Split '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Average temperature  - AC Central Split**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['#2 Average temperature (C) setting - Air conditioning Units Mini split '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Average temperature  - AC Mini split**")
                        st.table(atm)   
                        
                        atw=new.groupby('Governorate')['#2 Average temperature (C) setting - Air conditioning Units Windows '].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Average temperature  - AC Units Windows**")
                        st.table(atw)
                        
                    if st.checkbox("Table5. Association of Air Conditioner Average Temperature with Governorate"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Average temperature  - AC Central Packaged'},inplace=True)
                        td['Average temperature  - AC Central Packaged'] = td['Average temperature  - AC Central Packaged'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Packaged ': 'Std'})
                         
                        atpp=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']].mean()
                        atpp=atpp.T
                        atpp.reset_index(inplace = True)
                         
                        atpp.rename(columns={'index':'Average temperature  - AC Central Packaged'},inplace=True)
                        atpp['Average temperature  - AC Central Packaged'] = atpp['Average temperature  - AC Central Packaged'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Packaged ': 'Mean(SD)'})
                        atpp['Al-Ahmadi']=atpp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        atpp['Al-Asimah']=atpp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        atpp['Al-Farwaniyah']=atpp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        atpp['Al-Jahra']=atpp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        atpp['Hawally']=atpp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        atpp['Mubarak Al-Kabeer']=atpp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Average temperature  - AC Central Packaged'},inplace=True)
                        tang_m['Average temperature  - AC Central Packaged'] = tang_m['Average temperature  - AC Central Packaged'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Packaged ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Average temperature  - AC Central Packaged'},inplace=True)
                        tang_mx['Average temperature  - AC Central Packaged'] = tang_mx['Average temperature  - AC Central Packaged'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Packaged ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Average temperature  - AC Central Packaged'},inplace=True)
                        vc['Average temperature  - AC Central Packaged'] = vc['Average temperature  - AC Central Packaged'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Packaged ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = atpp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Average temperature  - AC Central Packaged**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Split ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Average temperature  - AC Central Split'},inplace=True)
                        cs['Average temperature  - AC Central Split'] = cs['Average temperature  - AC Central Split'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Split ': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Split ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Average temperature  - AC Central Split'},inplace=True)
                        acsp['Average temperature  - AC Central Split'] = acsp['Average temperature  - AC Central Split'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Split ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Split ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Average temperature  - AC Central Split'},inplace=True)
                        tang_m['Average temperature  - AC Central Split'] = tang_m['Average temperature  - AC Central Split'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Split ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Split ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Average temperature  - AC Central Split'},inplace=True)
                        tang_mx['Average temperature  - AC Central Split'] = tang_mx['Average temperature  - AC Central Split'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Average temperature  - AC Central Split'},inplace=True)
                        vc['Average temperature  - AC Central Split'] = vc['Average temperature  - AC Central Split'].replace({'#2 Average temperature (C) setting - Air Conditioner Central Split ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Average temperature  - AC Central Split**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Mini split ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Average temperature  - AC Mini split'},inplace=True)
                        ms['Average temperature  - AC Mini split'] = ms['Average temperature  - AC Mini split'].replace({'#2 Average temperature (C) setting - Air conditioning Units Mini split ': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Mini split ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'Average temperature  - AC Mini split'},inplace=True)
                        atms['Average temperature  - AC Mini split'] = atms['Average temperature  - AC Mini split'].replace({'#2 Average temperature (C) setting - Air conditioning Units Mini split ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Mini split ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Average temperature  - AC Mini split'},inplace=True)
                        tang_m['Average temperature  - AC Mini split'] = tang_m['Average temperature  - AC Mini split'].replace({'#2 Average temperature (C) setting - Air conditioning Units Mini split ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Mini split ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Average temperature  - AC Mini split'},inplace=True)
                        tang_mx['Average temperature  - AC Mini split'] = tang_mx['Average temperature  - AC Mini split'].replace({'#2 Average temperature (C) setting - Air conditioning Units Mini split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Mini split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Average temperature  - AC Mini split'},inplace=True)
                        vc['Average temperature  - AC Mini split'] = vc['Average temperature  - AC Mini split'].replace({'#2 Average temperature (C) setting - Air conditioning Units Mini split ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Average temperature  - AC Mini split**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Windows ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Average temperature  - AC Units Windows'},inplace=True)
                        uw['Average temperature  - AC Units Windows'] = uw['Average temperature  - AC Units Windows'].replace({'#2 Average temperature (C) setting - Air conditioning Units Windows ': 'Std'})
                        
                        acuw=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Windows ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)
                        
                        acuw.rename(columns={'index':'Average temperature  - AC Units Windows'},inplace=True)
                        acuw['Average temperature  - AC Units Windows'] = acuw['Average temperature  - AC Units Windows'].replace({'#2 Average temperature (C) setting - Air conditioning Units Windows ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Windows ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Average temperature  - AC Units Windows'},inplace=True)
                        tang_m['Average temperature  - AC Units Windows'] = tang_m['Average temperature  - AC Units Windows'].replace({'#2 Average temperature (C) setting - Air conditioning Units Windows ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Windows ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Average temperature  - AC Units Windows'},inplace=True)
                        tang_mx['Average temperature  - AC Units Windows'] = tang_mx['Average temperature  - AC Units Windows'].replace({'#2 Average temperature (C) setting - Air conditioning Units Windows ': 'Range'})
                        
                        vc=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Windows ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Average temperature  - AC Units Windows'},inplace=True)
                        vc['Average temperature  - AC Units Windows'] = vc['Average temperature  - AC Units Windows'].replace({'#2 Average temperature (C) setting - Air conditioning Units Windows ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)
                         
                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']
                         
                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']
                         
                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']
                        
                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']
                         
                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']
                         
                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Average temperature  - AC Units Windows**")
                        st.write(df_auw)
                         
                         
                        #graph
                         
                        gatp=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']].mean()
                        gatp.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air Conditioner Central Split ']].mean()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Mini split ']].mean()
                        gams.reset_index(inplace=True)
                        
                        gauw=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Air conditioning Units Windows ']].mean()
                        gauw.reset_index(inplace=True)
                        
                        import plotly.express as px
                        st.markdown("**Figure3. Comparison of mean temperature of Air Conditioners under different Governorate**")
                        import plotly.graph_objects as go
                        fig1 = go.Figure(data=[
                            go.Bar(name='AC central packaged', x=gatp['Governorate'], y=gatp['#2 Average temperature (C) setting - Air Conditioner Central Packaged ']),
                             go.Bar(name='AC central split', x=gacs['Governorate'], y=gacs['#2 Average temperature (C) setting - Air Conditioner Central Split ']),
                             go.Bar(name='AC mini split', x=gams['Governorate'], y=gams['#2 Average temperature (C) setting - Air conditioning Units Mini split ']),
                             go.Bar(name='AC unit windows', x=gauw['Governorate'], y=gauw['#2 Average temperature (C) setting - Air conditioning Units Windows ']),
                        ])
                        # Change the bar mode
                        fig1.update_layout(barmode='group')
                        #fig.show()
                        
                        st.write(fig1)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure4. Air Conditioners average temperature under different Governorate**")
                        fig10 = px.bar(gatp, x="Governorate", y='#2 Average temperature (C) setting - Air Conditioner Central Packaged ', color="Governorate")
                        fig11 = px.bar(gacs, x="Governorate", y='#2 Average temperature (C) setting - Air Conditioner Central Split ', color="Governorate")
                        fig12 = px.bar(gams, x="Governorate", y='#2 Average temperature (C) setting - Air conditioning Units Mini split ', color="Governorate")
                        fig13= px.bar(gauw, x="Governorate", y='#2 Average temperature (C) setting - Air conditioning Units Windows ', color="Governorate")
                        st.write(fig10)
                        st.write(fig11)
                        st.write(fig12)
                        st.write(fig13)
                #operating hours        
                    st.markdown("**Operating Hours of Air Conditioner**")
                    if st.checkbox("Table 6. Descriptive Statistics- Operating Hours of Air Conditioner"):
                            
                        
                        otp=new.groupby('Governorate')['#3 Operating in hours per day - Air Conditioner Central Packaged '].describe()
                        otp.reset_index(inplace = True)
                        otp.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating hours  - AC Central Packaged**")
                        st.table(otp)
                        
                        
                        acs=new.groupby('Governorate')['#3 Operating in hours per day - Air Conditioner Central Split '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating hours  - AC Central Split**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['#3 Operating in hours per day - Air conditioning Units Mini split '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating hours  - AC Mini split**")
                        st.table(atm)   
                        
                        atw=new.groupby('Governorate')['#3 Operating in hours per day - Air conditioning Units Windows '].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating hours  - AC Units Windows**")
                        st.table(atw)
                        
                    if st.checkbox("Table 7. Association of Air Conditioner operating hours with Governorate"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Packaged ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Operating hours  - AC Central Packaged'},inplace=True)
                        td['Operating hours  - AC Central Packaged'] = td['Operating hours  - AC Central Packaged'].replace({'#3 Operating in hours per day - Air Conditioner Central Packaged ': 'Std'})
                         
                        otpp=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Packaged ']].mean()
                        otpp=otpp.T
                        otpp.reset_index(inplace = True)
                         
                        otpp.rename(columns={'index':'Operating hours  - AC Central Packaged'},inplace=True)
                        otpp['Operating hours  - AC Central Packaged'] = otpp['Operating hours  - AC Central Packaged'].replace({'#3 Operating in hours per day - Air Conditioner Central Packaged ': 'Mean(SD)'})
                        otpp['Al-Ahmadi']=otpp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        otpp['Al-Asimah']=otpp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        otpp['Al-Farwaniyah']=otpp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        otpp['Al-Jahra']=otpp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        otpp['Hawally']=otpp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        otpp['Mubarak Al-Kabeer']=otpp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Packaged ']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating hours  - AC Central Packaged'},inplace=True)
                        tang_m['Operating hours  - AC Central Packaged'] = tang_m['Operating hours  - AC Central Packaged'].replace({'#3 Operating in hours per day - Air Conditioner Central Packaged ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Packaged ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating hours  - AC Central Packaged'},inplace=True)
                        tang_mx['Operating hours  - AC Central Packaged'] = tang_mx['Operating hours  - AC Central Packaged'].replace({'#3 Operating in hours per day - Air Conditioner Central Packaged ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Packaged ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating hours  - AC Central Packaged'},inplace=True)
                        vc['Operating hours  - AC Central Packaged'] = vc['Operating hours  - AC Central Packaged'].replace({'#3 Operating in hours per day - Air Conditioner Central Packaged ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = otpp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating hours  - AC Central Packaged**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Split ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Operating hours  - AC Central Split'},inplace=True)
                        cs['Operating hours  - AC Central Split'] = cs['Operating hours  - AC Central Split'].replace({'#3 Operating in hours per day - Air Conditioner Central Split ': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Split ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Operating hours  - AC Central Split'},inplace=True)
                        acsp['Operating hours  - AC Central Split'] = acsp['Operating hours  - AC Central Split'].replace({'#3 Operating in hours per day - Air Conditioner Central Split ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Split ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating hours  - AC Central Split'},inplace=True)
                        tang_m['Operating hours  - AC Central Split'] = tang_m['Operating hours  - AC Central Split'].replace({'#3 Operating in hours per day - Air Conditioner Central Split ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Split ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating hours  - AC Central Split'},inplace=True)
                        tang_mx['Operating hours  - AC Central Split'] = tang_mx['Operating hours  - AC Central Split'].replace({'#3 Operating in hours per day - Air Conditioner Central Split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating hours  - AC Central Split'},inplace=True)
                        vc['Operating hours  - AC Central Split'] = vc['Operating hours  - AC Central Split'].replace({'#3 Operating in hours per day - Air Conditioner Central Split ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating hours  - AC Central Split**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Mini split ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Operating hours  - AC Mini split'},inplace=True)
                        ms['Operating hours  - AC Mini split'] = ms['Operating hours  - AC Mini split'].replace({'#3 Operating in hours per day - Air conditioning Units Mini split ': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Mini split ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'Operating hours  - AC Mini split'},inplace=True)
                        atms['Operating hours  - AC Mini split'] = atms['Operating hours  - AC Mini split'].replace({'#3 Operating in hours per day - Air conditioning Units Mini split ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Mini split ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating hours  - AC Mini split'},inplace=True)
                        tang_m['Operating hours  - AC Mini split'] = tang_m['Operating hours  - AC Mini split'].replace({'#3 Operating in hours per day - Air conditioning Units Mini split ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Mini split ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating hours  - AC Mini split'},inplace=True)
                        tang_mx['Operating hours  - AC Mini split'] = tang_mx['Operating hours  - AC Mini split'].replace({'#3 Operating in hours per day - Air conditioning Units Mini split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Mini split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating hours  - AC Mini split'},inplace=True)
                        vc['Operating hours  - AC Mini split'] = vc['Operating hours  - AC Mini split'].replace({'#3 Operating in hours per day - Air conditioning Units Mini split ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating hours  - AC Mini split**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Windows ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating hours  - AC Units Windows'},inplace=True)
                        uw['Operating hours  - AC Units Windows'] = uw['Operating hours  - AC Units Windows'].replace({'#3 Operating in hours per day - Air conditioning Units Windows ': 'Std'})
                        
                        acuw=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Windows ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)
                        
                        acuw.rename(columns={'index':'Operating hours  - AC Units Windows'},inplace=True)
                        acuw['Operating hours  - AC Units Windows'] = acuw['Operating hours  - AC Units Windows'].replace({'#3 Operating in hours per day - Air conditioning Units Windows ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Windows ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating hours  - AC Units Windows'},inplace=True)
                        tang_m['Operating hours  - AC Units Windows'] = tang_m['Operating hours  - AC Units Windows'].replace({'#3 Operating in hours per day - Air conditioning Units Windows ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Windows ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating hours  - AC Units Windows'},inplace=True)
                        tang_mx['Operating hours  - AC Units Windows'] = tang_mx['Operating hours  - AC Units Windows'].replace({'#3 Operating in hours per day - Air conditioning Units Windows ': 'Range'})
                        
                        vc=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Windows ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating hours  - AC Units Windows'},inplace=True)
                        vc['Operating hours  - AC Units Windows'] = vc['Operating hours  - AC Units Windows'].replace({'#3 Operating in hours per day - Air conditioning Units Windows ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)
                         
                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']
                         
                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']
                         
                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']
                        
                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']
                         
                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']
                         
                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating hours  - AC Units Windows**")
                        st.write(df_auw)
                         
                         
                        #graph
                         
                        gotp=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Packaged ']].sum()
                        gotp.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air Conditioner Central Split ']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Mini split ']].sum()
                        gams.reset_index(inplace=True)
                        
                        gauw=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Air conditioning Units Windows ']].sum()
                        gauw.reset_index(inplace=True)
                        
                        import plotly.express as px
                        st.markdown("**Figure 5. Comparison of operating hours of Air Conditioners under different Governorate**")
                        import plotly.graph_objects as go
                        fig2 = go.Figure(data=[
                            go.Bar(name='AC central packaged', x=gotp['Governorate'], y=gotp['#3 Operating in hours per day - Air Conditioner Central Packaged ']),
                             go.Bar(name='AC central split', x=gacs['Governorate'], y=gacs['#3 Operating in hours per day - Air Conditioner Central Split ']),
                             go.Bar(name='AC mini split', x=gams['Governorate'], y=gams['#3 Operating in hours per day - Air conditioning Units Mini split ']),
                             go.Bar(name='AC unit windows', x=gauw['Governorate'], y=gauw['#3 Operating in hours per day - Air conditioning Units Windows ']),
                        ])
                        # Change the bar mode
                        fig2.update_layout(barmode='stack')
                        #fig.show()
                        
                        st.write(fig2)
                        
                        
                        st.markdown("**Figure 6. Air Conditioners operating hours under different Governorate**")
                        fig14 = px.bar(gotp, x="Governorate", y='#3 Operating in hours per day - Air Conditioner Central Packaged ', color="Governorate")
                        fig15 = px.bar(gacs, x="Governorate", y='#3 Operating in hours per day - Air Conditioner Central Split ', color="Governorate")
                        fig16 = px.bar(gams, x="Governorate", y='#3 Operating in hours per day - Air conditioning Units Mini split ', color="Governorate")
                        fig17= px.bar(gauw, x="Governorate", y='#3 Operating in hours per day - Air conditioning Units Windows ', color="Governorate")
                        st.write(fig14)
                        st.write(fig15)
                        st.write(fig16)
                        st.write(fig17)
                    # unit size
                    
                    st.markdown("**Unit size of Air Conditioner**")
                    if st.checkbox("Table 8. Descriptive Statistics- Unit size of Air Conditioner"):
                            
                        
                        aus=new.groupby('Governorate')['#4 Unit size in Ton - Air Conditioner Central Packaged '].describe()
                        aus.reset_index(inplace = True)
                        aus.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Unit size  - AC Central Packaged**")
                        st.table(aus)
                        
                        
                        acs=new.groupby('Governorate')['#4 Unit size in Ton - Air Conditioner Central Split '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Unit size  - AC Central Split**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['#4 Unit size in Ton - Air conditioning Units Mini split '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Unit size  - AC Mini split**")
                        st.table(atm)   
                        
                        atw=new.groupby('Governorate')['#4 Unit size in Ton - Air conditioning Units Windows '].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Unit size  - AC Units Windows**")
                        st.table(atw)
                        
                    if st.checkbox("Table 9. Association of Air Conditioner unit size with Governorate"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Packaged ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Unit size  - AC Central Packaged'},inplace=True)
                        td['Unit size  - AC Central Packaged'] = td['Unit size  - AC Central Packaged'].replace({'#4 Unit size in Ton - Air Conditioner Central Packaged ': 'Std'})
                         
                        ausp=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Packaged ']].mean()
                        ausp=ausp.T
                        ausp.reset_index(inplace = True)
                         
                        ausp.rename(columns={'index':'Unit size  - AC Central Packaged'},inplace=True)
                        ausp['Unit size  - AC Central Packaged'] = ausp['Unit size  - AC Central Packaged'].replace({'#4 Unit size in Ton - Air Conditioner Central Packaged ': 'Mean(SD)'})
                        ausp['Al-Ahmadi']=ausp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        ausp['Al-Asimah']=ausp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        ausp['Al-Farwaniyah']=ausp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        ausp['Al-Jahra']=ausp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        ausp['Hawally']=ausp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        ausp['Mubarak Al-Kabeer']=ausp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Packaged ']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Unit size  - AC Central Packaged'},inplace=True)
                        tang_m['Unit size  - AC Central Packaged'] = tang_m['Unit size  - AC Central Packaged'].replace({'#4 Unit size in Ton - Air Conditioner Central Packaged ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Packaged ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Unit size  - AC Central Packaged'},inplace=True)
                        tang_mx['Unit size  - AC Central Packaged'] = tang_mx['Unit size  - AC Central Packaged'].replace({'#4 Unit size in Ton - Air Conditioner Central Packaged ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Packaged ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Unit size  - AC Central Packaged'},inplace=True)
                        vc['Unit size  - AC Central Packaged'] = vc['Unit size  - AC Central Packaged'].replace({'#4 Unit size in Ton - Air Conditioner Central Packaged ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = ausp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Unit size  - AC Central Packaged**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Split ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Unit size  - AC Central Split'},inplace=True)
                        cs['Unit size  - AC Central Split'] = cs['Unit size  - AC Central Split'].replace({'#4 Unit size in Ton - Air Conditioner Central Split ': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Split ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Unit size  - AC Central Split'},inplace=True)
                        acsp['Unit size  - AC Central Split'] = acsp['Unit size  - AC Central Split'].replace({'#4 Unit size in Ton - Air Conditioner Central Split ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Split ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Unit size  - AC Central Split'},inplace=True)
                        tang_m['Unit size  - AC Central Split'] = tang_m['Unit size  - AC Central Split'].replace({'#4 Unit size in Ton - Air Conditioner Central Split ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Split ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Unit size  - AC Central Split'},inplace=True)
                        tang_mx['Unit size  - AC Central Split'] = tang_mx['Unit size  - AC Central Split'].replace({'#4 Unit size in Ton - Air Conditioner Central Split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Unit size  - AC Central Split'},inplace=True)
                        vc['Unit size  - AC Central Split'] = vc['Unit size  - AC Central Split'].replace({'#4 Unit size in Ton - Air Conditioner Central Split ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                     
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Unit size  - AC Central Split**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Mini split ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Unit size  - AC Mini split'},inplace=True)
                        ms['Unit size  - AC Mini split'] = ms['Unit size  - AC Mini split'].replace({'#4 Unit size in Ton - Air conditioning Units Mini split ': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Mini split ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'Unit size  - AC Mini split'},inplace=True)
                        atms['Unit size  - AC Mini split'] = atms['Unit size  - AC Mini split'].replace({'#4 Unit size in Ton - Air conditioning Units Mini split ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Mini split ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Unit size  - AC Mini split'},inplace=True)
                        tang_m['Unit size  - AC Mini split'] = tang_m['Unit size  - AC Mini split'].replace({'#4 Unit size in Ton - Air conditioning Units Mini split ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Mini split ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Unit size  - AC Mini split'},inplace=True)
                        tang_mx['Unit size  - AC Mini split'] = tang_mx['Unit size  - AC Mini split'].replace({'#4 Unit size in Ton - Air conditioning Units Mini split ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Mini split ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Unit size  - AC Mini split'},inplace=True)
                        vc['Unit size  - AC Mini split'] = vc['Unit size  - AC Mini split'].replace({'#4 Unit size in Ton - Air conditioning Units Mini split ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Unit size  - AC Mini split**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Windows ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Unit size  - AC Units Windows'},inplace=True)
                        uw['Unit size  - AC Units Windows'] = uw['Unit size  - AC Units Windows'].replace({'#4 Unit size in Ton - Air conditioning Units Windows ': 'Std'})
                        
                        acuw=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Windows ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)
                        
                        acuw.rename(columns={'index':'Unit size  - AC Units Windows'},inplace=True)
                        acuw['Unit size  - AC Units Windows'] = acuw['Unit size  - AC Units Windows'].replace({'#4 Unit size in Ton - Air conditioning Units Windows ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Windows ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Unit size  - AC Units Windows'},inplace=True)
                        tang_m['Unit size  - AC Units Windows'] = tang_m['Unit size  - AC Units Windows'].replace({'#4 Unit size in Ton - Air conditioning Units Windows ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Windows ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Unit size  - AC Units Windows'},inplace=True)
                        tang_mx['Unit size  - AC Units Windows'] = tang_mx['Unit size  - AC Units Windows'].replace({'#4 Unit size in Ton - Air conditioning Units Windows ': 'Range'})
                        
                        vc=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Windows ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Unit size  - AC Units Windows'},inplace=True)
                        vc['Unit size  - AC Units Windows'] = vc['Unit size  - AC Units Windows'].replace({'#4 Unit size in Ton - Air conditioning Units Windows ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)
                         
                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']
                         
                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']
                         
                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']
                        
                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']
                         
                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']
                         
                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Unit size  - AC Units Windows**")
                        st.write(df_auw)
                         
                         
                        #graph
                         
                        gaus=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Packaged ']].sum()
                        gaus.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air Conditioner Central Split ']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Mini split ']].sum()
                        gams.reset_index(inplace=True)
                        
                        gauw=new.groupby('Governorate',as_index=True)[['#4 Unit size in Ton - Air conditioning Units Windows ']].sum()
                        gauw.reset_index(inplace=True)
                        
                        import plotly.express as px
                        st.markdown("**Figure7. Comparison of unit size of Air Conditioners under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='AC central packaged', x=gaus['Governorate'], y=gaus['#4 Unit size in Ton - Air Conditioner Central Packaged ']),
                             go.Bar(name='AC central split', x=gacs['Governorate'], y=gacs['#4 Unit size in Ton - Air Conditioner Central Split ']),
                             go.Bar(name='AC mini split', x=gams['Governorate'], y=gams['#4 Unit size in Ton - Air conditioning Units Mini split ']),
                             go.Bar(name='AC unit windows', x=gauw['Governorate'], y=gauw['#4 Unit size in Ton - Air conditioning Units Windows ']),
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='group')
                        #fig.show()
                        
                        st.write(fig3)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure 8. Air Conditioners unit size under different Governorate**")
                        fig18 = px.bar(gaus, x="Governorate", y='#4 Unit size in Ton - Air Conditioner Central Packaged ', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='#4 Unit size in Ton - Air Conditioner Central Split ', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='#4 Unit size in Ton - Air conditioning Units Mini split ', color="Governorate")
                        fig21= px.bar(gauw, x="Governorate", y='#4 Unit size in Ton - Air conditioning Units Windows ', color="Governorate")
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        st.write(fig21)
                    #watt consumed
                    
                    st.markdown("**Watt consumed by Air Conditioner**")
                    if st.checkbox("Table 10. Descriptive Statistics- Watt consumed by Air Conditioner"):
                            
                        
                        wac=new.groupby('Governorate')['Air Conditioner Central Packaged  - The estimated Watts consumed per day'].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watt consumed  - AC Central Packaged**")
                        st.table(wac)
                        
                        
                        acs=new.groupby('Governorate')['Air Conditioner Central Split  - The estimated Watts consumed per day'].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watt consumed  - AC Central Split**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['Air conditioning Units Mini split  - The estimated Watts consumed per day'].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watt consumed  - AC Mini split**")
                        st.table(atm)   
                        
                        atw=new.groupby('Governorate')['Air conditioning Units Windows  - The estimated Watts consumed per day'].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watt consumed  - AC Units Windows**")
                        st.table(atw)
                        
                    if st.checkbox("Table 11. Association of watt consumed by Air Conditioner with Governorate"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Packaged  - The estimated Watts consumed per day']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Watt consumed  - AC Central Packaged'},inplace=True)
                        td['Watt consumed  - AC Central Packaged'] = td['Watt consumed  - AC Central Packaged'].replace({'Air Conditioner Central Packaged  - The estimated Watts consumed per day': 'Std'})
                         
                        wacp=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Packaged  - The estimated Watts consumed per day']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)
                         
                        wacp.rename(columns={'index':'Watt consumed  - AC Central Packaged'},inplace=True)
                        wacp['Watt consumed  - AC Central Packaged'] = wacp['Watt consumed  - AC Central Packaged'].replace({'Air Conditioner Central Packaged  - The estimated Watts consumed per day': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Packaged  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watt consumed  - AC Central Packaged'},inplace=True)
                        tang_m['Watt consumed  - AC Central Packaged'] = tang_m['Watt consumed  - AC Central Packaged'].replace({'Air Conditioner Central Packaged  - The estimated Watts consumed per day': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Packaged  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watt consumed  - AC Central Packaged'},inplace=True)
                        tang_mx['Watt consumed  - AC Central Packaged'] = tang_mx['Watt consumed  - AC Central Packaged'].replace({'Air Conditioner Central Packaged  - The estimated Watts consumed per day': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Packaged  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watt consumed  - AC Central Packaged'},inplace=True)
                        vc['Watt consumed  - AC Central Packaged'] = vc['Watt consumed  - AC Central Packaged'].replace({'Air Conditioner Central Packaged  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watt consumed  - AC Central Packaged**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Split  - The estimated Watts consumed per day']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Watt consumed  - AC Central Split'},inplace=True)
                        cs['Watt consumed  - AC Central Split'] = cs['Watt consumed  - AC Central Split'].replace({'Air Conditioner Central Split  - The estimated Watts consumed per day': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Split  - The estimated Watts consumed per day']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Watt consumed  - AC Central Split'},inplace=True)
                        acsp['Watt consumed  - AC Central Split'] = acsp['Watt consumed  - AC Central Split'].replace({'Air Conditioner Central Split  - The estimated Watts consumed per day': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Split  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watt consumed  - AC Central Split'},inplace=True)
                        tang_m['Watt consumed  - AC Central Split'] = tang_m['Watt consumed  - AC Central Split'].replace({'Air Conditioner Central Split  - The estimated Watts consumed per day': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Split  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watt consumed  - AC Central Split'},inplace=True)
                        tang_mx['Watt consumed  - AC Central Split'] = tang_mx['Watt consumed  - AC Central Split'].replace({'Air Conditioner Central Split  - The estimated Watts consumed per day': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Split  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watt consumed  - AC Central Split'},inplace=True)
                        vc['Watt consumed  - AC Central Split'] = vc['Watt consumed  - AC Central Split'].replace({'Air Conditioner Central Split  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watt consumed  - AC Central Split**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['Air conditioning Units Mini split  - The estimated Watts consumed per day']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Watt consumed  - AC Mini split'},inplace=True)
                        ms['Watt consumed  - AC Mini split'] = ms['Watt consumed  - AC Mini split'].replace({'Air conditioning Units Mini split  - The estimated Watts consumed per day': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['Air conditioning Units Mini split  - The estimated Watts consumed per day']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'Watt consumed  - AC Mini split'},inplace=True)
                        atms['Watt consumed  - AC Mini split'] = atms['Watt consumed  - AC Mini split'].replace({'Air conditioning Units Mini split  - The estimated Watts consumed per day': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Air conditioning Units Mini split  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watt consumed  - AC Mini split'},inplace=True)
                        tang_m['Watt consumed  - AC Mini split'] = tang_m['Watt consumed  - AC Mini split'].replace({'Air conditioning Units Mini split  - The estimated Watts consumed per day': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['Air conditioning Units Mini split  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watt consumed  - AC Mini split'},inplace=True)
                        tang_mx['Watt consumed  - AC Mini split'] = tang_mx['Watt consumed  - AC Mini split'].replace({'Air conditioning Units Mini split  - The estimated Watts consumed per day': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['Air conditioning Units Mini split  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watt consumed  - AC Mini split'},inplace=True)
                        vc['Watt consumed  - AC Mini split'] = vc['Watt consumed  - AC Mini split'].replace({'Air conditioning Units Mini split  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watt consumed  - AC Mini split**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['Air conditioning Units Windows  - The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Watt consumed  - AC Units Windows'},inplace=True)
                        uw['Watt consumed  - AC Units Windows'] = uw['Watt consumed  - AC Units Windows'].replace({'Air conditioning Units Windows  - The estimated Watts consumed per day': 'Std'})
                        
                        acuw=new.groupby('Governorate',as_index=True)[['Air conditioning Units Windows  - The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)
                        
                        acuw.rename(columns={'index':'Watt consumed  - AC Units Windows'},inplace=True)
                        acuw['Watt consumed  - AC Units Windows'] = acuw['Watt consumed  - AC Units Windows'].replace({'Air conditioning Units Windows  - The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Air conditioning Units Windows  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watt consumed  - AC Units Windows'},inplace=True)
                        tang_m['Watt consumed  - AC Units Windows'] = tang_m['Watt consumed  - AC Units Windows'].replace({'Air conditioning Units Windows  - The estimated Watts consumed per day': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['Air conditioning Units Windows  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watt consumed  - AC Units Windows'},inplace=True)
                        tang_mx['Watt consumed  - AC Units Windows'] = tang_mx['Watt consumed  - AC Units Windows'].replace({'Air conditioning Units Windows  - The estimated Watts consumed per day': 'Range'})
                        
                        vc=new.groupby('Governorate',as_index=True)[['Air conditioning Units Windows  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watt consumed  - AC Units Windows'},inplace=True)
                        vc['Watt consumed  - AC Units Windows'] = vc['Watt consumed  - AC Units Windows'].replace({'Air conditioning Units Windows  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                         
                        
                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)
                         
                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']
                         
                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']
                         
                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']
                        
                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']
                         
                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']
                         
                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watt consumed  - AC Units Windows**")
                        st.write(df_auw)
                         
                         
                        #graph
                         
                        gwac=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Packaged  - The estimated Watts consumed per day']].sum()
                        gwac.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['Air Conditioner Central Split  - The estimated Watts consumed per day']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['Air conditioning Units Mini split  - The estimated Watts consumed per day']].sum()
                        gams.reset_index(inplace=True)
                        
                        gauw=new.groupby('Governorate',as_index=True)[['Air conditioning Units Windows  - The estimated Watts consumed per day']].sum()
                        gauw.reset_index(inplace=True)
                        
                        import plotly.express as px
                        st.markdown("**Figure 9. Comparison of watt consumed by Air Conditioners under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='AC central packaged', x=gwac['Governorate'], y=gwac['Air Conditioner Central Packaged  - The estimated Watts consumed per day']),
                             go.Bar(name='AC central split', x=gacs['Governorate'], y=gacs['Air Conditioner Central Split  - The estimated Watts consumed per day']),
                             go.Bar(name='AC mini split', x=gams['Governorate'], y=gams['Air conditioning Units Mini split  - The estimated Watts consumed per day']),
                             go.Bar(name='AC unit windows', x=gauw['Governorate'], y=gauw['Air conditioning Units Windows  - The estimated Watts consumed per day']),
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='stack')
                        #fig.show()
                        
                        st.write(fig3)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure 10. Watts consumed by Air Conditioners under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='Air Conditioner Central Packaged  - The estimated Watts consumed per day', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='Air Conditioner Central Split  - The estimated Watts consumed per day', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='Air conditioning Units Mini split  - The estimated Watts consumed per day', color="Governorate")
                        fig21= px.bar(gauw, x="Governorate", y='Air conditioning Units Windows  - The estimated Watts consumed per day', color="Governorate")
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        st.write(fig21)
                    
                # poratble air cooler
                st.markdown("**Portable air cooler for single room**")
                if st.checkbox("Table 12. Descriptive Statistics- Portable air cooler for single room"):
                        
                    
                    wac=new.groupby('Governorate')['#1 units owned - Portable air cooler for single room'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Portable air cooler for single room**")
                    st.table(wac)
                    
                    acs=new.groupby('Governorate')['#2 Average temperature (C) setting - Portable air cooler for single room'].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Average temperature - Portable air cooler for single room**")
                    st.table(acs)
                        
                    atm=new.groupby('Governorate')['#3 Operating in hours per day - Portable air cooler for single room'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Operating hours - Portable air cooler for single room**")
                    st.table(atm)   
                    
                    atw=new.groupby('Governorate')['Portable air cooler for single room - The estimated Watts consumed per day'].describe()
                    atw.reset_index(inplace = True)
                    atw.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Portable air cooler for single room**")
                    st.table(atw)
                    
                if st.checkbox("Table 13. Association of consumption by Portable air cooler for single room"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#1 units owned - Portable air cooler for single room']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'units owned  - Portable air cooler for single room'},inplace=True)
                    td['units owned  - Portable air cooler for single room'] = td['units owned  - Portable air cooler for single room'].replace({'#1 units owned - Portable air cooler for single room': 'Std'})
                     
                    wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Portable air cooler for single room']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)
                     
                    wacp.rename(columns={'index':'units owned  - Portable air cooler for single room'},inplace=True)
                    wacp['units owned  - Portable air cooler for single room'] = wacp['units owned  - Portable air cooler for single room'].replace({'#1 units owned - Portable air cooler for single room': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Portable air cooler for single room']].min()
                    tang_m=tang_m.T
                     
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned  - Portable air cooler for single room'},inplace=True)
                    tang_m['units owned  - Portable air cooler for single room'] = tang_m['units owned  - Portable air cooler for single room'].replace({'#1 units owned - Portable air cooler for single room': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Portable air cooler for single room']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned  - Portable air cooler for single room'},inplace=True)
                    tang_mx['units owned  - Portable air cooler for single room'] = tang_mx['units owned  - Portable air cooler for single room'].replace({'#1 units owned - Portable air cooler for single room': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Portable air cooler for single room']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned  - Portable air cooler for single room'},inplace=True)
                    vc['units owned  - Portable air cooler for single room'] = vc['units owned  - Portable air cooler for single room'].replace({'#1 units owned - Portable air cooler for single room': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                    
                    
                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)
                    
                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']
                    
                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']
                    
                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']
                    
                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']
                     
                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']
                     
                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**units owned  - Portable air cooler for single room**")
                    st.write(df_atc)
                    
                    #2     
                    cs=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Portable air cooler for single room']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'Average temperature - Portable air cooler for single room'},inplace=True)
                    cs['Average temperature - Portable air cooler for single room'] = cs['Average temperature - Portable air cooler for single room'].replace({'#2 Average temperature (C) setting - Portable air cooler for single room': 'Std'})
                     
                    acsp=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Portable air cooler for single room']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)
                     
                    acsp.rename(columns={'index':'Average temperature - Portable air cooler for single room'},inplace=True)
                    acsp['Average temperature - Portable air cooler for single room'] = acsp['Average temperature - Portable air cooler for single room'].replace({'#2 Average temperature (C) setting - Portable air cooler for single room': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Portable air cooler for single room']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Average temperature - Portable air cooler for single room'},inplace=True)
                    tang_m['Average temperature - Portable air cooler for single room'] = tang_m['Average temperature - Portable air cooler for single room'].replace({'#2 Average temperature (C) setting - Portable air cooler for single room': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Portable air cooler for single room']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Average temperature - Portable air cooler for single room'},inplace=True)
                    tang_mx['Average temperature - Portable air cooler for single room'] = tang_mx['Average temperature - Portable air cooler for single room'].replace({'#2 Average temperature (C) setting - Portable air cooler for single room': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Portable air cooler for single room']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Average temperature - Portable air cooler for single room'},inplace=True)
                    vc['Average temperature - Portable air cooler for single room'] = vc['Average temperature - Portable air cooler for single room'].replace({'#2 Average temperature (C) setting - Portable air cooler for single room': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)
                     
                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']
                    
                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']
                     
                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']
                    
                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']
                     
                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']
                     
                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Average temperature - Portable air cooler for single room**")
                    st.write(df_acs)
                    
                    #3
                     
                    ms=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Portable air cooler for single room']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'Operating hours - Portable air cooler for single room'},inplace=True)
                    ms['Operating hours - Portable air cooler for single room'] = ms['Operating hours - Portable air cooler for single room'].replace({'#3 Operating in hours per day - Portable air cooler for single room': 'Std'})
                     
                    atms=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Portable air cooler for single room']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)
                     
                    atms.rename(columns={'index':'Operating hours - Portable air cooler for single room'},inplace=True)
                    atms['Operating hours - Portable air cooler for single room'] = atms['Operating hours - Portable air cooler for single room'].replace({'#3 Operating in hours per day - Portable air cooler for single room': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Portable air cooler for single room']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Operating hours - Portable air cooler for single room'},inplace=True)
                    tang_m['Operating hours - Portable air cooler for single room'] = tang_m['Operating hours - Portable air cooler for single room'].replace({'#3 Operating in hours per day - Portable air cooler for single room': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Portable air cooler for single room']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Operating hours - Portable air cooler for single room'},inplace=True)
                    tang_mx['Operating hours - Portable air cooler for single room'] = tang_mx['Operating hours - Portable air cooler for single room'].replace({'#3 Operating in hours per day - Portable air cooler for single room': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Portable air cooler for single room']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Operating hours - Portable air cooler for single room'},inplace=True)
                    vc['Operating hours - Portable air cooler for single room'] = vc['Operating hours - Portable air cooler for single room'].replace({'#3 Operating in hours per day - Portable air cooler for single room': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)
                     
                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']
                     
                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']
                     
                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']
                     
                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']
                     
                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']
                     
                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Operating hours - Portable air cooler for single room**")
                    st.write(df_ams)
                    
                    #4
                    uw=new.groupby('Governorate',as_index=True)[['Portable air cooler for single room - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Portable air cooler for single room'},inplace=True)
                    uw['Watts consumed - Portable air cooler for single room'] = uw['Watts consumed - Portable air cooler for single room'].replace({'Portable air cooler for single room - The estimated Watts consumed per day': 'Std'})
                    
                    acuw=new.groupby('Governorate',as_index=True)[['Portable air cooler for single room - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)
                    
                    acuw.rename(columns={'index':'Watts consumed - Portable air cooler for single room'},inplace=True)
                    acuw['Watts consumed - Portable air cooler for single room'] = acuw['Watts consumed - Portable air cooler for single room'].replace({'Portable air cooler for single room - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['Portable air cooler for single room - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Portable air cooler for single room'},inplace=True)
                    tang_m['Watts consumed - Portable air cooler for single room'] = tang_m['Watts consumed - Portable air cooler for single room'].replace({'Portable air cooler for single room - The estimated Watts consumed per day': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['Portable air cooler for single room - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Portable air cooler for single room'},inplace=True)
                    tang_mx['Watts consumed - Portable air cooler for single room'] = tang_mx['Watts consumed - Portable air cooler for single room'].replace({'Portable air cooler for single room - The estimated Watts consumed per day': 'Range'})
                    
                    vc=new.groupby('Governorate',as_index=True)[['Portable air cooler for single room - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Portable air cooler for single room'},inplace=True)
                    vc['Watts consumed - Portable air cooler for single room'] = vc['Watts consumed - Portable air cooler for single room'].replace({'Portable air cooler for single room - The estimated Watts consumed per day': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                     
                    
                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)
                     
                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']
                     
                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']
                     
                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']
                    
                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']
                     
                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']
                     
                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Watts consumed - Portable air cooler for single room**")
                    st.write(df_auw)
                    
                    #graph
                     
                    gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Portable air cooler for single room']].sum()
                    gwac.reset_index(inplace=True)
                     
                    gacs=new.groupby('Governorate',as_index=True)[['#2 Average temperature (C) setting - Portable air cooler for single room']].sum()
                    gacs.reset_index(inplace=True)
                    
                    gams=new.groupby('Governorate',as_index=True)[['#3 Operating in hours per day - Portable air cooler for single room']].sum()
                    gams.reset_index(inplace=True)
                    
                    gauw=new.groupby('Governorate',as_index=True)[['Portable air cooler for single room - The estimated Watts consumed per day']].sum()
                    gauw.reset_index(inplace=True)
                    
                    import plotly.express as px
                    
                    st.markdown("**Figure 11. Comparison of different parameters for portable air cooler under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Portable air cooler for single room', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='#2 Average temperature (C) setting - Portable air cooler for single room', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='#3 Operating in hours per day - Portable air cooler for single room', color="Governorate")
                    fig21= px.bar(gauw, x="Governorate", y='Portable air cooler for single room - The estimated Watts consumed per day', color="Governorate")
                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                    st.write(fig21)
                    
                    #air purifier
                    
                st.markdown("**Air Purifier Device**")
                if st.checkbox("Table 14. Descriptive Statistics- Air Purifier Device"):
                        
                    
                    wac=new.groupby('Governorate')['#1 units owned - Air Purifier Device'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Air Purifier Device**")
                    st.table(wac)
                        
                    atm=new.groupby('Governorate')['#2 Operating in hours per day - Air Purifier Device'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Operating hours - Air Purifier Device**")
                    st.table(atm)   
                    
                    atw=new.groupby('Governorate')['Air Purifier Device - The estimated Watts consumed per day'].describe()
                    atw.reset_index(inplace = True)
                    atw.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Air Purifier Device**")
                    st.table(atw)
                    
                if st.checkbox("Table 15. Association of consumption by Air Purifier Device"):
                    
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Purifier Device']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'units owned  - Air Purifier Device'},inplace=True)
                    td['units owned  - Air Purifier Device'] = td['units owned  - Air Purifier Device'].replace({'#1 units owned - Air Purifier Device': 'Std'})
                     
                    wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Purifier Device']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)
                     
                    wacp.rename(columns={'index':'units owned  - Air Purifier Device'},inplace=True)
                    wacp['units owned  - Air Purifier Device'] = wacp['units owned  - Air Purifier Device'].replace({'#1 units owned - Air Purifier Device': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Purifier Device']].min()
                    tang_m=tang_m.T
                     
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned  - Air Purifier Device'},inplace=True)
                    tang_m['units owned  - Air Purifier Device'] = tang_m['units owned  - Air Purifier Device'].replace({'#1 units owned - Air Purifier Device': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Purifier Device']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned  - Air Purifier Device'},inplace=True)
                    tang_mx['units owned  - Air Purifier Device'] = tang_mx['units owned  - Air Purifier Device'].replace({'#1 units owned - Air Purifier Device': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Purifier Device']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned  - Air Purifier Device'},inplace=True)
                    vc['units owned  - Air Purifier Device'] = vc['units owned  - Air Purifier Device'].replace({'#1 units owned - Air Purifier Device': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                    
                    
                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)
                    
                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']
                    
                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']
                    
                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']
                    
                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']
                     
                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']
                     
                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**units owned  - Air Purifier Device**")
                    st.write(df_atc)
                    
                    #3
                     
                    ms=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Air Purifier Device']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'Operating hours - Air Purifier Device'},inplace=True)
                    ms['Operating hours - Air Purifier Device'] = ms['Operating hours - Air Purifier Device'].replace({'#2 Operating in hours per day - Air Purifier Device': 'Std'})
                     
                    atms=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Air Purifier Device']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)
                     
                    atms.rename(columns={'index':'Operating hours - Air Purifier Device'},inplace=True)
                    atms['Operating hours - Air Purifier Device'] = atms['Operating hours - Air Purifier Device'].replace({'#2 Operating in hours per day - Air Purifier Device': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Air Purifier Device']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Operating hours - Air Purifier Device'},inplace=True)
                    tang_m['Operating hours - Air Purifier Device'] = tang_m['Operating hours - Air Purifier Device'].replace({'#2 Operating in hours per day - Air Purifier Device': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Air Purifier Device']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Operating hours - Air Purifier Device'},inplace=True)
                    tang_mx['Operating hours - Air Purifier Device'] = tang_mx['Operating hours - Air Purifier Device'].replace({'#2 Operating in hours per day - Air Purifier Device': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Air Purifier Device']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Operating hours - Air Purifier Device'},inplace=True)
                    vc['Operating hours - Air Purifier Device'] = vc['Operating hours - Air Purifier Device'].replace({'#2 Operating in hours per day - Air Purifier Device': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)
                     
                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']
                     
                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']
                     
                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']
                     
                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']
                     
                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']
                     
                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Operating hours - Air Purifier Device**")
                    st.write(df_ams)
                    
                    #4
                    uw=new.groupby('Governorate',as_index=True)[['Air Purifier Device - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Air Purifier Device'},inplace=True)
                    uw['Watts consumed - Air Purifier Device'] = uw['Watts consumed - Air Purifier Device'].replace({'Air Purifier Device - The estimated Watts consumed per day': 'Std'})
                    
                    acuw=new.groupby('Governorate',as_index=True)[['Air Purifier Device - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)
                    
                    acuw.rename(columns={'index':'Watts consumed - Air Purifier Device'},inplace=True)
                    acuw['Watts consumed - Air Purifier Device'] = acuw['Watts consumed - Air Purifier Device'].replace({'Air Purifier Device - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['Air Purifier Device - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Air Purifier Device'},inplace=True)
                    tang_m['Watts consumed - Air Purifier Device'] = tang_m['Watts consumed - Air Purifier Device'].replace({'Air Purifier Device - The estimated Watts consumed per day': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['Air Purifier Device - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Air Purifier Device'},inplace=True)
                    tang_mx['Watts consumed - Air Purifier Device'] = tang_mx['Watts consumed - Air Purifier Device'].replace({'Air Purifier Device - The estimated Watts consumed per day': 'Range'})
                    
                    vc=new.groupby('Governorate',as_index=True)[['Air Purifier Device - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Air Purifier Device'},inplace=True)
                    vc['Watts consumed - Air Purifier Device'] = vc['Watts consumed - Air Purifier Device'].replace({'Air Purifier Device - The estimated Watts consumed per day': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                     
                    
                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)
                     
                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']
                     
                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']
                     
                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']
                    
                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']
                     
                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']
                     
                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Watts consumed - Air Purifier Device**")
                    st.write(df_auw)
                    
                    #graph
                     
                    gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Air Purifier Device']].sum()
                    gwac.reset_index(inplace=True)
                    
                    gams=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Air Purifier Device']].sum()
                    gams.reset_index(inplace=True)
                    
                    gauw=new.groupby('Governorate',as_index=True)[['Air Purifier Device - The estimated Watts consumed per day']].sum()
                    gauw.reset_index(inplace=True)
                    
                    import plotly.express as px
                    
                    st.markdown("**Figure 12. Comparison of different parameters for air purifier device under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Air Purifier Device', color="Governorate")
                    
                    fig20 = px.bar(gams, x="Governorate", y='#2 Operating in hours per day - Air Purifier Device', color="Governorate")
                    fig21= px.bar(gauw, x="Governorate", y='Air Purifier Device - The estimated Watts consumed per day', color="Governorate")
                    st.write(fig18)
                    
                    st.write(fig20)
                    st.write(fig21)
                    
                #electric fan
                
                st.markdown("**Electric fan**")
                if st.checkbox("Table 16. Descriptive Statistics- Electric fan"):
                        
                    
                    wac=new.groupby('Governorate')['#1 units owned - Electric fan'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Electric fan**")
                    st.table(wac)
                        
                    atm=new.groupby('Governorate')['#2 Operating in hours per day - Electric fan'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Operating hours - Electric fan**")
                    st.table(atm)   
                    
                    atw=new.groupby('Governorate')['Electric fan - The estimated Watts consumed per day'].describe()
                    atw.reset_index(inplace = True)
                    atw.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Electric fan**")
                    st.table(atw)
                    
                if st.checkbox("Table 17. Association of consumtion by Electric fan"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#1 units owned - Electric fan']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'units owned  - Electric fan'},inplace=True)
                    td['units owned  - Electric fan'] = td['units owned  - Electric fan'].replace({'#1 units owned - Electric fan': 'Std'})
                     
                    wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Electric fan']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)
                     
                    wacp.rename(columns={'index':'units owned  - Electric fan'},inplace=True)
                    wacp['units owned  - Electric fan'] = wacp['units owned  - Electric fan'].replace({'#1 units owned - Electric fan': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Electric fan']].min()
                    tang_m=tang_m.T
                     
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned  - Electric fan'},inplace=True)
                    tang_m['units owned  - Electric fan'] = tang_m['units owned  - Electric fan'].replace({'#1 units owned - Electric fan': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Electric fan']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned  - Electric fan'},inplace=True)
                    tang_mx['units owned  - Electric fan'] = tang_mx['units owned  - Electric fan'].replace({'#1 units owned - Electric fan': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Electric fan']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned  - Electric fan'},inplace=True)
                    vc['units owned  - Electric fan'] = vc['units owned  - Electric fan'].replace({'#1 units owned - Electric fan': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                    
                    
                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)
                    
                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']
                    
                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']
                    
                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']
                    
                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']
                     
                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']
                     
                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**units owned  - Electric fan**")
                    st.write(df_atc)
                    
                    #3
                     
                    ms=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Electric fan']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'Operating hours - Electric fan'},inplace=True)
                    ms['Operating hours - Electric fan'] = ms['Operating hours - Electric fan'].replace({'#2 Operating in hours per day - Electric fan': 'Std'})
                     
                    atms=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Electric fan']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)
                     
                    atms.rename(columns={'index':'Operating hours - Electric fan'},inplace=True)
                    atms['Operating hours - Electric fan'] = atms['Operating hours - Electric fan'].replace({'#2 Operating in hours per day - Electric fan': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Electric fan']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Operating hours - Electric fan'},inplace=True)
                    tang_m['Operating hours - Electric fan'] = tang_m['Operating hours - Electric fan'].replace({'#2 Operating in hours per day - Electric fan': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Electric fan']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Operating hours - Electric fan'},inplace=True)
                    tang_mx['Operating hours - Electric fan'] = tang_mx['Operating hours - Electric fan'].replace({'#2 Operating in hours per day - Electric fan': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Electric fan']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Operating hours - Electric fan'},inplace=True)
                    vc['Operating hours - Electric fan'] = vc['Operating hours - Electric fan'].replace({'#2 Operating in hours per day - Electric fan': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)
                     
                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']
                     
                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']
                     
                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']
                     
                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']
                     
                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']
                     
                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Operating hours - Electric fan**")
                    st.write(df_ams)
                    
                    #4
                    uw=new.groupby('Governorate',as_index=True)[['Electric fan - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Electric fan'},inplace=True)
                    uw['Watts consumed - Electric fan'] = uw['Watts consumed - Electric fan'].replace({'Electric fan - The estimated Watts consumed per day': 'Std'})
                    
                    acuw=new.groupby('Governorate',as_index=True)[['Electric fan - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)
                    
                    acuw.rename(columns={'index':'Watts consumed - Electric fan'},inplace=True)
                    acuw['Watts consumed - Electric fan'] = acuw['Watts consumed - Electric fan'].replace({'Electric fan - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['Electric fan - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Electric fan'},inplace=True)
                    tang_m['Watts consumed - Electric fan'] = tang_m['Watts consumed - Electric fan'].replace({'Electric fan - The estimated Watts consumed per day': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['Electric fan - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Electric fan'},inplace=True)
                    tang_mx['Watts consumed - Electric fan'] = tang_mx['Watts consumed - Electric fan'].replace({'Electric fan - The estimated Watts consumed per day': 'Range'})
                    
                    vc=new.groupby('Governorate',as_index=True)[['Electric fan - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Electric fan'},inplace=True)
                    vc['Watts consumed - Electric fan'] = vc['Watts consumed - Electric fan'].replace({'Electric fan - The estimated Watts consumed per day': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                     
                    
                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)
                     
                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']
                     
                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']
                     
                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']
                    
                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']
                     
                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']
                     
                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**Watts consumed - Electric fan**")
                    st.write(df_auw)
                    
                    #graph
                     
                    gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Electric fan']].sum()
                    gwac.reset_index(inplace=True)
                    
                    gams=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Electric fan']].sum()
                    gams.reset_index(inplace=True)
                    
                    gauw=new.groupby('Governorate',as_index=True)[['Electric fan - The estimated Watts consumed per day']].sum()
                    gauw.reset_index(inplace=True)
                    
                    import plotly.express as px
                    
                    st.markdown("**Figure13. Comparison of different parameters for electric fan under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Electric fan', color="Governorate")
                    
                    fig20 = px.bar(gams, x="Governorate", y='#2 Operating in hours per day - Electric fan', color="Governorate")
                    fig21= px.bar(gauw, x="Governorate", y='Electric fan - The estimated Watts consumed per day', color="Governorate")
                    st.write(fig18)
                    
                    st.write(fig20)
                    st.write(fig21)
                
                st.markdown("**Heater Equipments**")    
                if st.checkbox("Click here for Heater Equipments"):
                    st.markdown("**Units owned by (Heater)**")
                    if st.checkbox("Table18. Descriptive Statistics- Units owned (Heater)"):
                            
                        
                        wac=new.groupby('Governorate')['#1 units owned - Heater - Central '].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Heater - Central**")
                        st.table(wac)
                        
                        
                        acs=new.groupby('Governorate')['#1 units owned - Heater - Space Heater (Portable, Electric) '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Heater - Space Heater (Portable, Electric)**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['#1 units owned - Heater - Space Heater (Portable, Oil) '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Heater - Space Heater (Portable, Oil)**")
                        st.table(atm)   
                        
                        
                        
                    if st.checkbox("Table 19. Association of units owned by (Heater)"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Central ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'units owned - Heater - Central'},inplace=True)
                        td['units owned - Heater - Central'] = td['units owned - Heater - Central'].replace({'#1 units owned - Heater - Central ': 'Std'})
                         
                        wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Central ']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)
                         
                        wacp.rename(columns={'index':'units owned - Heater - Central'},inplace=True)
                        wacp['units owned - Heater - Central'] = wacp['units owned - Heater - Central'].replace({'#1 units owned - Heater - Central ': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Central ']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Heater - Central'},inplace=True)
                        tang_m['units owned - Heater - Central'] = tang_m['units owned - Heater - Central'].replace({'#1 units owned - Heater - Central ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Central ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Heater - Central'},inplace=True)
                        tang_mx['units owned - Heater - Central'] = tang_mx['units owned - Heater - Central'].replace({'#1 units owned - Heater - Central ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Central ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Heater - Central'},inplace=True)
                        vc['units owned - Heater - Central'] = vc['units owned - Heater - Central'].replace({'#1 units owned - Heater - Central ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**units owned - Heater - Central**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Electric) ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        cs['units owned - Heater - Space Heater (Portable, Electric)'] = cs['units owned - Heater - Space Heater (Portable, Electric)'].replace({'#1 units owned - Heater - Space Heater (Portable, Electric) ': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Electric) ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        acsp['units owned - Heater - Space Heater (Portable, Electric)'] = acsp['units owned - Heater - Space Heater (Portable, Electric)'].replace({'#1 units owned - Heater - Space Heater (Portable, Electric) ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Electric) ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        tang_m['units owned - Heater - Space Heater (Portable, Electric)'] = tang_m['units owned - Heater - Space Heater (Portable, Electric)'].replace({'#1 units owned - Heater - Space Heater (Portable, Electric) ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Electric) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        tang_mx['units owned - Heater - Space Heater (Portable, Electric)'] = tang_mx['units owned - Heater - Space Heater (Portable, Electric)'].replace({'#1 units owned - Heater - Space Heater (Portable, Electric) ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Electric) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        vc['units owned - Heater - Space Heater (Portable, Electric)'] = vc['units owned - Heater - Space Heater (Portable, Electric)'].replace({'#1 units owned - Heater - Space Heater (Portable, Electric) ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**units owned - Heater - Space Heater (Portable, Electric)**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Oil) ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        ms['units owned - Heater - Space Heater (Portable, Oil)'] = ms['units owned - Heater - Space Heater (Portable, Oil)'].replace({'#1 units owned - Heater - Space Heater (Portable, Oil) ': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Oil) ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        atms['units owned - Heater - Space Heater (Portable, Oil)'] = atms['units owned - Heater - Space Heater (Portable, Oil)'].replace({'#1 units owned - Heater - Space Heater (Portable, Oil) ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Oil) ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        tang_m['units owned - Heater - Space Heater (Portable, Oil)'] = tang_m['units owned - Heater - Space Heater (Portable, Oil)'].replace({'#1 units owned - Heater - Space Heater (Portable, Oil) ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Oil) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        tang_mx['units owned - Heater - Space Heater (Portable, Oil)'] = tang_mx['units owned - Heater - Space Heater (Portable, Oil)'].replace({'#1 units owned - Heater - Space Heater (Portable, Oil) ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Oil) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        vc['units owned - Heater - Space Heater (Portable, Oil)'] = vc['units owned - Heater - Space Heater (Portable, Oil)'].replace({'#1 units owned - Heater - Space Heater (Portable, Oil) ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**units owned - Heater - Space Heater (Portable, Oil)**")
                        st.write(df_ams)
                     
                         
                        #graph
                         
                        gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Central ']].sum()
                        gwac.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Electric) ']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['#1 units owned - Heater - Space Heater (Portable, Oil) ']].sum()
                        gams.reset_index(inplace=True)
                        
                       
                        
                        import plotly.express as px
                        st.markdown("**Figure 14. Comparison of units owned of Heaters under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='Heater - Central', x=gwac['Governorate'], y=gwac['#1 units owned - Heater - Central ']),
                             go.Bar(name='Heater - Space Heater (Portable, Electric)', x=gacs['Governorate'], y=gacs['#1 units owned - Heater - Space Heater (Portable, Electric) ']),
                             go.Bar(name='Heater - Space Heater (Portable, Oil)', x=gams['Governorate'], y=gams['#1 units owned - Heater - Space Heater (Portable, Oil) ']),
                             
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='group')
                        #fig.show()
                        
                        st.write(fig3)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure 15. Distribution of units owned of Heaters under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Heater - Central ', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='#1 units owned - Heater - Space Heater (Portable, Electric) ', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='#1 units owned - Heater - Space Heater (Portable, Oil) ', color="Governorate")
                        
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        
                    st.markdown("**Operating hours by (Heater)**")
                    if st.checkbox("Table 20. Descriptive Statistics- Operating hours (Heater)"):
                            
                        
                        wac=new.groupby('Governorate')['#2 Operating in hours per day - Heater - Central '].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in hours per day - Heater - Central**")
                        st.table(wac)
                        
                        
                        acs=new.groupby('Governorate')['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in hours per day - Heater - Space Heater (Portable, Electric)**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in hours per day - Heater - Space Heater (Portable, Oil)**")
                        st.table(atm)   
                        
                        
                        
                    if st.checkbox("Table 21. Association of Operating in hours per day by (Heater)"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Central ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Operating in hours per day - Heater - Central'},inplace=True)
                        td['Operating in hours per day - Heater - Central'] = td['Operating in hours per day - Heater - Central'].replace({'#2 Operating in hours per day - Heater - Central ': 'Std'})
                         
                        wacp=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Central ']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)
                         
                        wacp.rename(columns={'index':'Operating in hours per day - Heater - Central'},inplace=True)
                        wacp['Operating in hours per day - Heater - Central'] = wacp['Operating in hours per day - Heater - Central'].replace({'#2 Operating in hours per day - Heater - Central ': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Central ']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in hours per day - Heater - Central'},inplace=True)
                        tang_m['Operating in hours per day - Heater - Central'] = tang_m['Operating in hours per day - Heater - Central'].replace({'#2 Operating in hours per day - Heater - Central ': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Central ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in hours per day - Heater - Central'},inplace=True)
                        tang_mx['Operating in hours per day - Heater - Central'] = tang_mx['Operating in hours per day - Heater - Central'].replace({'#2 Operating in hours per day - Heater - Central ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Central ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in hours per day - Heater - Central'},inplace=True)
                        vc['Operating in hours per day - Heater - Central'] = vc['Operating in hours per day - Heater - Central'].replace({'#2 Operating in hours per day - Heater - Central ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating in hours per day - Heater - Central**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        cs['Operating in hours per day - Heater - Space Heater (Portable, Electric)'] = cs['Operating in hours per day - Heater - Space Heater (Portable, Electric)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        acsp['Operating in hours per day - Heater - Space Heater (Portable, Electric)'] = acsp['Operating in hours per day - Heater - Space Heater (Portable, Electric)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        tang_m['Operating in hours per day - Heater - Space Heater (Portable, Electric)'] = tang_m['Operating in hours per day - Heater - Space Heater (Portable, Electric)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        tang_mx['Operating in hours per day - Heater - Space Heater (Portable, Electric)'] = tang_mx['Operating in hours per day - Heater - Space Heater (Portable, Electric)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        vc['Operating in hours per day - Heater - Space Heater (Portable, Electric)'] = vc['Operating in hours per day - Heater - Space Heater (Portable, Electric)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating in hours per day - Heater - Space Heater (Portable, Electric)**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        ms['Operating in hours per day - Heater - Space Heater (Portable, Oil)'] = ms['Operating in hours per day - Heater - Space Heater (Portable, Oil)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        atms['Operating in hours per day - Heater - Space Heater (Portable, Oil)'] = atms['Operating in hours per day - Heater - Space Heater (Portable, Oil)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        tang_m['Operating in hours per day - Heater - Space Heater (Portable, Oil)'] = tang_m['Operating in hours per day - Heater - Space Heater (Portable, Oil)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        tang_mx['Operating in hours per day - Heater - Space Heater (Portable, Oil)'] = tang_mx['Operating in hours per day - Heater - Space Heater (Portable, Oil)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in hours per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        vc['Operating in hours per day - Heater - Space Heater (Portable, Oil)'] = vc['Operating in hours per day - Heater - Space Heater (Portable, Oil)'].replace({'#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Operating in hours per day - Heater - Space Heater (Portable, Oil)**")
                        st.write(df_ams)
                     
                         
                        #graph
                         
                        gwac=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Central ']].sum()
                        gwac.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']].sum()
                        gams.reset_index(inplace=True)
                        
                       
                        
                        import plotly.express as px
                        st.markdown("**Figure 14. Distribution of Operating hours of Heaters under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='Heater - Central', x=gwac['Governorate'], y=gwac['#2 Operating in hours per day - Heater - Central ']),
                             go.Bar(name='Heater - Space Heater (Portable, Electric)', x=gacs['Governorate'], y=gacs['#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ']),
                             go.Bar(name='Heater - Space Heater (Portable, Oil)', x=gams['Governorate'], y=gams['#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ']),
                             
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='stack')
                        #fig.show()
                        
                        st.write(fig3)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure 15. Comparison of Operating hours of Heaters under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='#2 Operating in hours per day - Heater - Central ', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='#2 Operating in hours per day - Heater - Space Heater (Portable, Electric) ', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='#2 Operating in hours per day - Heater - Space Heater (Portable, Oil) ', color="Governorate")
                        
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                    
                    #watt
                    st.markdown("**Watts consumed by (Heater)**")
                    if st.checkbox("Table 22. Descriptive Statistics- Watts consumed per day by (Heater)"):
                        wac=new.groupby('Governorate')['Heater - Central  - The estimated Watts consumed per day'].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watts consumed per day - Heater - Central**")
                        st.table(wac)
                        
                        
                        acs=new.groupby('Governorate')['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day'].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watts consumed per day - Heater - Space Heater (Portable, Electric)**")
                        st.table(acs)
                            
                        atm=new.groupby('Governorate')['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day'].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Watts consumed per day - Heater - Space Heater (Portable, Oil)**")
                        st.table(atm)   
                        
                        
                        
                    if st.checkbox("Table 23. Association of Watts consumed per day by (Heater)"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['Heater - Central  - The estimated Watts consumed per day']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Watts consumed per day - Heater - Central'},inplace=True)
                        td['Watts consumed per day - Heater - Central'] = td['Watts consumed per day - Heater - Central'].replace({'Heater - Central  - The estimated Watts consumed per day': 'Std'})
                         
                        wacp=new.groupby('Governorate',as_index=True)[['Heater - Central  - The estimated Watts consumed per day']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)
                         
                        wacp.rename(columns={'index':'Watts consumed per day - Heater - Central'},inplace=True)
                        wacp['Watts consumed per day - Heater - Central'] = wacp['Watts consumed per day - Heater - Central'].replace({'Heater - Central  - The estimated Watts consumed per day': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Heater - Central  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                         
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watts consumed per day - Heater - Central'},inplace=True)
                        tang_m['Watts consumed per day - Heater - Central'] = tang_m['Watts consumed per day - Heater - Central'].replace({'Heater - Central  - The estimated Watts consumed per day': 'min'})
                        
                        tang_mx=new.groupby('Governorate',as_index=True)[['Heater - Central  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watts consumed per day - Heater - Central'},inplace=True)
                        tang_mx['Watts consumed per day - Heater - Central'] = tang_mx['Watts consumed per day - Heater - Central'].replace({'Heater - Central  - The estimated Watts consumed per day': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['Heater - Central  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watts consumed per day - Heater - Central'},inplace=True)
                        vc['Watts consumed per day - Heater - Central'] = vc['Watts consumed per day - Heater - Central'].replace({'Heater - Central  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                        
                        
                        
                        
                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)
                        
                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']
                        
                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']
                        
                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']
                        
                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']
                         
                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']
                         
                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watts consumed per day - Heater - Central**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        cs['Watts consumed per day - Heater - Space Heater (Portable, Electric)'] = cs['Watts consumed per day - Heater - Space Heater (Portable, Electric)'].replace({'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day': 'Std'})
                         
                        acsp=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)
                         
                        acsp.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        acsp['Watts consumed per day - Heater - Space Heater (Portable, Electric)'] = acsp['Watts consumed per day - Heater - Space Heater (Portable, Electric)'].replace({'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        tang_m['Watts consumed per day - Heater - Space Heater (Portable, Electric)'] = tang_m['Watts consumed per day - Heater - Space Heater (Portable, Electric)'].replace({'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        tang_mx['Watts consumed per day - Heater - Space Heater (Portable, Electric)'] = tang_mx['Watts consumed per day - Heater - Space Heater (Portable, Electric)'].replace({'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Electric)'},inplace=True)
                        vc['Watts consumed per day - Heater - Space Heater (Portable, Electric)'] = vc['Watts consumed per day - Heater - Space Heater (Portable, Electric)'].replace({'Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)
                         
                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']
                        
                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']
                         
                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']
                        
                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']
                         
                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']
                         
                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watts consumed per day - Heater - Space Heater (Portable, Electric)**")
                        st.write(df_acs)
                         
                        ms=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        ms['Watts consumed per day - Heater - Space Heater (Portable, Oil)'] = ms['Watts consumed per day - Heater - Space Heater (Portable, Oil)'].replace({'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day': 'Std'})
                         
                        atms=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)
                         
                        atms.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        atms['Watts consumed per day - Heater - Space Heater (Portable, Oil)'] = atms['Watts consumed per day - Heater - Space Heater (Portable, Oil)'].replace({'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                        
                         
                         
                        
                        tang_m=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T
                        
                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        tang_m['Watts consumed per day - Heater - Space Heater (Portable, Oil)'] = tang_m['Watts consumed per day - Heater - Space Heater (Portable, Oil)'].replace({'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day': 'min'})
                         
                        tang_mx=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        tang_mx['Watts consumed per day - Heater - Space Heater (Portable, Oil)'] = tang_mx['Watts consumed per day - Heater - Space Heater (Portable, Oil)'].replace({'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day': 'Range'})
                         
                        vc=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Watts consumed per day - Heater - Space Heater (Portable, Oil)'},inplace=True)
                        vc['Watts consumed per day - Heater - Space Heater (Portable, Oil)'] = vc['Watts consumed per day - Heater - Space Heater (Portable, Oil)'].replace({'Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day': 'count'})
                        
                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                         
                         
                         
                         
                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)
                         
                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']
                         
                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']
                         
                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']
                         
                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']
                         
                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']
                         
                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']
                         
                     
                        st.markdown("**Watts consumed per day - Heater - Space Heater (Portable, Oil)**")
                        st.write(df_ams)
                     
                         
                        #graph
                         
                        gwac=new.groupby('Governorate',as_index=True)[['Heater - Central  - The estimated Watts consumed per day']].sum()
                        gwac.reset_index(inplace=True)
                         
                        gacs=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']].sum()
                        gacs.reset_index(inplace=True)
                        
                        gams=new.groupby('Governorate',as_index=True)[['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']].sum()
                        gams.reset_index(inplace=True)
                        
                       
                        
                        import plotly.express as px
                        st.markdown("**Figure 18. Distribution of watts consumed by Heaters under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='Heater - Central', x=gwac['Governorate'], y=gwac['Heater - Central  - The estimated Watts consumed per day']),
                             go.Bar(name='Heater - Space Heater (Portable, Electric)', x=gacs['Governorate'], y=gacs['Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day']),
                             go.Bar(name='Heater - Space Heater (Portable, Oil)', x=gams['Governorate'], y=gams['Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day']),
                             
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='stack')
                        #fig.show()
                        
                        st.write(fig3)
                        
                        
                        
                        
                        
                        
                        
                        
                        st.markdown("**Figure 19. Comparison of watts consumed by Heaters under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='Heater - Central  - The estimated Watts consumed per day', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='Heater - Space Heater (Portable, Electric)  - The estimated Watts consumed per day', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='Heater - Space Heater (Portable, Oil)  - The estimated Watts consumed per day', color="Governorate")
                        
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        
            st.subheader("Analysis on different Cooking Equipments / Kitchen Equipments")    
            if st.checkbox("➡️ Analysis and statistics on different Cooking Equipments / Kitchen Equipments"):
                
                st.markdown("**Cooking / Kitchen Equipments**")
                if st.checkbox("Click here for Cooking / Kitchen Equipments"):
                    st.markdown("**Units owned by Kitchen items**")
                    if st.checkbox("Table 24. Descriptive Statistics- Kitchen items (Units owned)"):


                        wac=new.groupby('Governorate')['#1 units owned - Blender/mixer/food processor '].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Blender/mixer/food processor**")
                        st.table(wac)


                        acs=new.groupby('Governorate')['#1 units owned - kettle '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - kettle**")
                        st.table(acs)

                        atm=new.groupby('Governorate')['#1 units owned - Toaster '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Toaster**")
                        st.table(atm)   

                        atw=new.groupby('Governorate')['#1 units owned - Range - LPG '].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Range - LPG**")
                        st.table(atw)

                        atre=new.groupby('Governorate')['#1 units owned - Range - Electric '].describe()
                        atre.reset_index(inplace = True)
                        atre.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Range - Electric**")
                        st.table(atre)

                        acook=new.groupby('Governorate')['#1 units owned - Cooktop - (LPG/Electric/Induction) '].describe()
                        acook.reset_index(inplace = True)
                        acook.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Cooktop - (LPG/Electric/Induction)**")
                        st.table(acook)

                        ale=new.groupby('Governorate')['#1 units owned - Oven -(LPG/Electric) '].describe()
                        ale.reset_index(inplace = True)
                        ale.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Oven -(LPG/Electric)**")
                        st.table(ale)

                        af=new.groupby('Governorate')['#1 units owned - Air fryer '].describe()
                        af.reset_index(inplace = True)
                        af.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Air fryer**")
                        st.table(af)

                        cm=new.groupby('Governorate')['#1 units owned - Coffee Maker '].describe()
                        cm.reset_index(inplace = True)
                        cm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**units owned - Coffee Maker**")
                        st.table(cm)



                    if st.checkbox("Table 25. Association of units owned by Kitchen items"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#1 units owned - Blender/mixer/food processor ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'units owned - Blender/mixer/food processor'},inplace=True)
                        td['units owned - Blender/mixer/food processor'] = td['units owned - Blender/mixer/food processor'].replace({'#1 units owned - Blender/mixer/food processor ': 'Std'})

                        wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Blender/mixer/food processor ']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)

                        wacp.rename(columns={'index':'units owned - Blender/mixer/food processor'},inplace=True)
                        wacp['units owned - Blender/mixer/food processor'] = wacp['units owned - Blender/mixer/food processor'].replace({'#1 units owned - Blender/mixer/food processor ': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Blender/mixer/food processor ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Blender/mixer/food processor'},inplace=True)
                        tang_m['units owned - Blender/mixer/food processor'] = tang_m['units owned - Blender/mixer/food processor'].replace({'#1 units owned - Blender/mixer/food processor ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Blender/mixer/food processor ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Blender/mixer/food processor'},inplace=True)
                        tang_mx['units owned - Blender/mixer/food processor'] = tang_mx['units owned - Blender/mixer/food processor'].replace({'#1 units owned - Blender/mixer/food processor ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Blender/mixer/food processor ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Blender/mixer/food processor'},inplace=True)
                        vc['units owned - Blender/mixer/food processor'] = vc['units owned - Blender/mixer/food processor'].replace({'#1 units owned - Blender/mixer/food processor ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)

                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']

                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']

                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']

                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']

                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']

                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Blender/mixer/food processor**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#1 units owned - kettle ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'units owned - kettle'},inplace=True)
                        cs['units owned - kettle'] = cs['units owned - kettle'].replace({'#1 units owned - kettle ': 'Std'})

                        acsp=new.groupby('Governorate',as_index=True)[['#1 units owned - kettle ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)

                        acsp.rename(columns={'index':'units owned - kettle'},inplace=True)
                        acsp['units owned - kettle'] = acsp['units owned - kettle'].replace({'#1 units owned - kettle ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - kettle ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - kettle'},inplace=True)
                        tang_m['units owned - kettle'] = tang_m['units owned - kettle'].replace({'#1 units owned - kettle ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - kettle ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - kettle'},inplace=True)
                        tang_mx['units owned - kettle'] = tang_mx['units owned - kettle'].replace({'#1 units owned - kettle ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - kettle ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - kettle'},inplace=True)
                        vc['units owned - kettle'] = vc['units owned - kettle'].replace({'#1 units owned - kettle ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)

                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']

                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']

                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']

                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']

                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']

                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']


                        st.markdown("**units owned - kettle**")
                        st.write(df_acs)

                        ms=new.groupby('Governorate',as_index=True)[['#1 units owned - Toaster ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'units owned - Toaster'},inplace=True)
                        ms['units owned - Toaster'] = ms['units owned - Toaster'].replace({'#1 units owned - Toaster ': 'Std'})

                        atms=new.groupby('Governorate',as_index=True)[['#1 units owned - Toaster ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)

                        atms.rename(columns={'index':'units owned - Toaster'},inplace=True)
                        atms['units owned - Toaster'] = atms['units owned - Toaster'].replace({'#1 units owned - Toaster ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Toaster ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Toaster'},inplace=True)
                        tang_m['units owned - Toaster'] = tang_m['units owned - Toaster'].replace({'#1 units owned - Toaster ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Toaster ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Toaster'},inplace=True)
                        tang_mx['units owned - Toaster'] = tang_mx['units owned - Toaster'].replace({'#1 units owned - Toaster ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Toaster ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Toaster'},inplace=True)
                        vc['units owned - Toaster'] = vc['units owned - Toaster'].replace({'#1 units owned - Toaster ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)

                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']

                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']

                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']

                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']

                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']

                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Toaster**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - LPG ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'units owned - Range - LPG'},inplace=True)
                        uw['units owned - Range - LPG'] = uw['units owned - Range - LPG'].replace({'#1 units owned - Range - LPG ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - LPG ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'units owned - Range - LPG'},inplace=True)
                        acuw['units owned - Range - LPG'] = acuw['units owned - Range - LPG'].replace({'#1 units owned - Range - LPG ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - LPG ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Range - LPG'},inplace=True)
                        tang_m['units owned - Range - LPG'] = tang_m['units owned - Range - LPG'].replace({'#1 units owned - Range - LPG ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - LPG ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Range - LPG'},inplace=True)
                        tang_mx['units owned - Range - LPG'] = tang_mx['units owned - Range - LPG'].replace({'#1 units owned - Range - LPG ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - LPG ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Range - LPG'},inplace=True)
                        vc['units owned - Range - LPG'] = vc['units owned - Range - LPG'].replace({'#1 units owned - Range - LPG ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)

                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']

                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']

                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']

                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']

                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']

                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Range - LPG**")
                        st.write(df_auw)
                      #5  

                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - Electric ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'units owned - Range - Electric'},inplace=True)
                        uw['units owned - Range - Electric'] = uw['units owned - Range - Electric'].replace({'#1 units owned - Range - Electric ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - Electric ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'units owned - Range - Electric'},inplace=True)
                        acuw['units owned - Range - Electric'] = acuw['units owned - Range - Electric'].replace({'#1 units owned - Range - Electric ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - Electric ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Range - Electric'},inplace=True)
                        tang_m['units owned - Range - Electric'] = tang_m['units owned - Range - Electric'].replace({'#1 units owned - Range - Electric ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - Electric ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Range - Electric'},inplace=True)
                        tang_mx['units owned - Range - Electric'] = tang_mx['units owned - Range - Electric'].replace({'#1 units owned - Range - Electric ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - Electric ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Range - Electric'},inplace=True)
                        vc['units owned - Range - Electric'] = vc['units owned - Range - Electric'].replace({'#1 units owned - Range - Electric ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)

                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']

                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']

                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']

                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']

                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']

                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Range - Electric**")
                        st.write(df_auw)

                      #6  

                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Cooktop - (LPG/Electric/Induction) ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'units owned - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        uw['units owned - Cooktop - (LPG/Electric/Induction)'] = uw['units owned - Cooktop - (LPG/Electric/Induction)'].replace({'#1 units owned - Cooktop - (LPG/Electric/Induction) ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Cooktop - (LPG/Electric/Induction) ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'units owned - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        acuw['units owned - Cooktop - (LPG/Electric/Induction)'] = acuw['units owned - Cooktop - (LPG/Electric/Induction)'].replace({'#1 units owned - Cooktop - (LPG/Electric/Induction) ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Cooktop - (LPG/Electric/Induction) ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        tang_m['units owned - Cooktop - (LPG/Electric/Induction)'] = tang_m['units owned - Cooktop - (LPG/Electric/Induction)'].replace({'#1 units owned - Cooktop - (LPG/Electric/Induction) ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Cooktop - (LPG/Electric/Induction) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        tang_mx['units owned - Cooktop - (LPG/Electric/Induction)'] = tang_mx['units owned - Cooktop - (LPG/Electric/Induction)'].replace({'#1 units owned - Cooktop - (LPG/Electric/Induction) ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Cooktop - (LPG/Electric/Induction) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        vc['units owned - Cooktop - (LPG/Electric/Induction)'] = vc['units owned - Cooktop - (LPG/Electric/Induction)'].replace({'#1 units owned - Cooktop - (LPG/Electric/Induction) ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_cokt = acuw.append(tang_mx)
                        df_cokt=df_cokt.reset_index(drop=True)

                        df_cokt['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cokt['Al-Ahmadi']
                        del df_cokt['Al-Ahmadi']

                        df_cokt['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cokt['Al-Asimah']
                        del df_cokt['Al-Asimah']

                        df_cokt['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cokt['Al-Farwaniyah']
                        del df_cokt['Al-Farwaniyah']

                        df_cokt['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cokt['Al-Jahra']
                        del df_cokt['Al-Jahra']

                        df_cokt['Hawally (N={})'.format(vc['Hawally'][0])]=df_cokt['Hawally']
                        del df_cokt['Hawally']

                        df_cokt['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cokt['Mubarak Al-Kabeer']
                        del df_cokt['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Cooktop - (LPG/Electric/Induction)**")
                        st.write(df_cokt)

                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Oven -(LPG/Electric) ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'units owned - Oven -(LPG/Electric)'},inplace=True)
                        uw['units owned - Oven -(LPG/Electric)'] = uw['units owned - Oven -(LPG/Electric)'].replace({'#1 units owned - Oven -(LPG/Electric) ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Oven -(LPG/Electric) ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'units owned - Oven -(LPG/Electric)'},inplace=True)
                        acuw['units owned - Oven -(LPG/Electric)'] = acuw['units owned - Oven -(LPG/Electric)'].replace({'#1 units owned - Oven -(LPG/Electric) ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Oven -(LPG/Electric) ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Oven -(LPG/Electric)'},inplace=True)
                        tang_m['units owned - Oven -(LPG/Electric)'] = tang_m['units owned - Oven -(LPG/Electric)'].replace({'#1 units owned - Oven -(LPG/Electric) ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Oven -(LPG/Electric) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Oven -(LPG/Electric)'},inplace=True)
                        tang_mx['units owned - Oven -(LPG/Electric)'] = tang_mx['units owned - Oven -(LPG/Electric)'].replace({'#1 units owned - Oven -(LPG/Electric) ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Oven -(LPG/Electric) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Oven -(LPG/Electric)'},inplace=True)
                        vc['units owned - Oven -(LPG/Electric)'] = vc['units owned - Oven -(LPG/Electric)'].replace({'#1 units owned - Oven -(LPG/Electric) ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_lpg = acuw.append(tang_mx)
                        df_lpg=df_lpg.reset_index(drop=True)

                        df_lpg['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_lpg['Al-Ahmadi']
                        del df_lpg['Al-Ahmadi']

                        df_lpg['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_lpg['Al-Asimah']
                        del df_lpg['Al-Asimah']

                        df_lpg['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_lpg['Al-Farwaniyah']
                        del df_lpg['Al-Farwaniyah']

                        df_lpg['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_lpg['Al-Jahra']
                        del df_lpg['Al-Jahra']

                        df_lpg['Hawally (N={})'.format(vc['Hawally'][0])]=df_lpg['Hawally']
                        del df_lpg['Hawally']

                        df_lpg['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_lpg['Mubarak Al-Kabeer']
                        del df_lpg['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Oven -(LPG/Electric)**")
                        st.write(df_lpg)
                        #7
                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Air fryer ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'units owned - Air fryer'},inplace=True)
                        uw['units owned - Air fryer'] = uw['units owned - Air fryer'].replace({'#1 units owned - Air fryer ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Air fryer ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'units owned - Air fryer'},inplace=True)
                        acuw['units owned - Air fryer'] = acuw['units owned - Air fryer'].replace({'#1 units owned - Air fryer ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Air fryer ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Air fryer'},inplace=True)
                        tang_m['units owned - Air fryer'] = tang_m['units owned - Air fryer'].replace({'#1 units owned - Air fryer ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Air fryer ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Air fryer'},inplace=True)
                        tang_mx['units owned - Air fryer'] = tang_mx['units owned - Air fryer'].replace({'#1 units owned - Air fryer ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Air fryer ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Air fryer'},inplace=True)
                        vc['units owned - Air fryer'] = vc['units owned - Air fryer'].replace({'#1 units owned - Air fryer ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_af = acuw.append(tang_mx)
                        df_af=df_af.reset_index(drop=True)

                        df_af['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_af['Al-Ahmadi']
                        del df_af['Al-Ahmadi']

                        df_af['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_af['Al-Asimah']
                        del df_af['Al-Asimah']

                        df_af['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_af['Al-Farwaniyah']
                        del df_af['Al-Farwaniyah']

                        df_af['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_af['Al-Jahra']
                        del df_af['Al-Jahra']

                        df_af['Hawally (N={})'.format(vc['Hawally'][0])]=df_af['Hawally']
                        del df_af['Hawally']

                        df_af['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_af['Mubarak Al-Kabeer']
                        del df_af['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Air fryer**")
                        st.write(df_af)

                        #8
                        uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Coffee Maker ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'units owned - Coffee Maker'},inplace=True)
                        uw['units owned - Coffee Maker'] = uw['units owned - Coffee Maker'].replace({'#1 units owned - Coffee Maker ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Coffee Maker ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'units owned - Coffee Maker'},inplace=True)
                        acuw['units owned - Coffee Maker'] = acuw['units owned - Coffee Maker'].replace({'#1 units owned - Coffee Maker ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Coffee Maker ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'units owned - Coffee Maker'},inplace=True)
                        tang_m['units owned - Coffee Maker'] = tang_m['units owned - Coffee Maker'].replace({'#1 units owned - Coffee Maker ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Coffee Maker ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'units owned - Coffee Maker'},inplace=True)
                        tang_mx['units owned - Coffee Maker'] = tang_mx['units owned - Coffee Maker'].replace({'#1 units owned - Coffee Maker ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Coffee Maker ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'units owned - Coffee Maker'},inplace=True)
                        vc['units owned - Coffee Maker'] = vc['units owned - Coffee Maker'].replace({'#1 units owned - Coffee Maker ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_cm = acuw.append(tang_mx)
                        df_cm=df_cm.reset_index(drop=True)

                        df_cm['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cm['Al-Ahmadi']
                        del df_cm['Al-Ahmadi']

                        df_cm['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cm['Al-Asimah']
                        del df_cm['Al-Asimah']

                        df_cm['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cm['Al-Farwaniyah']
                        del df_cm['Al-Farwaniyah']

                        df_cm['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cm['Al-Jahra']
                        del df_cm['Al-Jahra']

                        df_cm['Hawally (N={})'.format(vc['Hawally'][0])]=df_cm['Hawally']
                        del df_cm['Hawally']

                        df_cm['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cm['Mubarak Al-Kabeer']
                        del df_cm['Mubarak Al-Kabeer']


                        st.markdown("**units owned - Coffee Maker**")
                        st.write(df_cm)








                        #graph

                        gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Blender/mixer/food processor ']].sum()
                        gwac.reset_index(inplace=True)

                        gacs=new.groupby('Governorate',as_index=True)[['#1 units owned - kettle ']].sum()
                        gacs.reset_index(inplace=True)

                        gams=new.groupby('Governorate',as_index=True)[['#1 units owned - Toaster ']].sum()
                        gams.reset_index(inplace=True)

                        gauw=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - LPG ']].sum()
                        gauw.reset_index(inplace=True)

                        gact=new.groupby('Governorate',as_index=True)[['#1 units owned - Range - Electric ']].sum()
                        gact.reset_index(inplace=True)

                        gael=new.groupby('Governorate',as_index=True)[['#1 units owned - Cooktop - (LPG/Electric/Induction) ']].sum()
                        gael.reset_index(inplace=True)

                        gaoel=new.groupby('Governorate',as_index=True)[['#1 units owned - Oven -(LPG/Electric) ']].sum()
                        gaoel.reset_index(inplace=True)

                        gaaf=new.groupby('Governorate',as_index=True)[['#1 units owned - Air fryer ']].sum()
                        gaaf.reset_index(inplace=True)

                        gacf=new.groupby('Governorate',as_index=True)[['#1 units owned - Coffee Maker ']].sum()
                        gacf.reset_index(inplace=True)


                        import plotly.express as px
                        st.markdown("**Figure 20. Distribution of units owned (Kitchen appliances) under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='Blender/mixer/food processor', x=gwac['Governorate'], y=gwac['#1 units owned - Blender/mixer/food processor ']),
                             go.Bar(name='kettle', x=gacs['Governorate'], y=gacs['#1 units owned - kettle ']),
                             go.Bar(name='Toaster', x=gams['Governorate'], y=gams['#1 units owned - Toaster ']),
                             go.Bar(name='Range - LPG', x=gauw['Governorate'], y=gauw['#1 units owned - Range - LPG ']),
                            go.Bar(name='Range - Electric', x=gact['Governorate'], y=gact['#1 units owned - Range - Electric ']),
                            go.Bar(name='Cooktop - (LPG/Electric/Induction)', x=gael['Governorate'], y=gael['#1 units owned - Cooktop - (LPG/Electric/Induction) ']),
                            go.Bar(name='Oven -(LPG/Electric)', x=gaoel['Governorate'], y=gaoel['#1 units owned - Oven -(LPG/Electric) ']),
                            go.Bar(name='Air fryer', x=gaaf['Governorate'], y=gaaf['#1 units owned - Air fryer ']),
                            go.Bar(name='Coffee Maker', x=gacf['Governorate'], y=gacf['#1 units owned - Coffee Maker ']),
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='group')
                        #fig.show()

                        st.write(fig3)








                        st.markdown("**Figure 21. Comparison of units owned (Kitchen appliances) under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Blender/mixer/food processor ', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='#1 units owned - kettle ', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='#1 units owned - Toaster ', color="Governorate")
                        fig21= px.bar(gauw, x="Governorate", y='#1 units owned - Range - LPG ', color="Governorate")
                        fig22= px.bar(gact, x="Governorate", y='#1 units owned - Range - Electric ', color="Governorate")
                        fig23= px.bar(gael, x="Governorate", y='#1 units owned - Cooktop - (LPG/Electric/Induction) ', color="Governorate")
                        fig24= px.bar(gaoel, x="Governorate", y='#1 units owned - Oven -(LPG/Electric) ', color="Governorate")
                        fig25= px.bar(gaaf, x="Governorate", y='#1 units owned - Air fryer ', color="Governorate")
                        fig26= px.bar(gacf, x="Governorate", y='#1 units owned - Coffee Maker ', color="Governorate")
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        st.write(fig21)
                        st.write(fig22)
                        st.write(fig23)
                        st.write(fig24)
                        st.write(fig25)
                        st.write(fig26)
                        
                        #operiting time
                    st.markdown("**Operating in minutes per day by Kitchen items**")
                    if st.checkbox("Table 26. Descriptive Statistics- Kitchen items (Operating in minutes per day)"):


                        wac=new.groupby('Governorate')['#2 Operating in minutes per day - Blender/mixer/food processor '].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Blender/mixer/food processor**")
                        st.table(wac)


                        acs=new.groupby('Governorate')['#2 Operating in minutes per day - kettle '].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - kettle**")
                        st.table(acs)

                        atm=new.groupby('Governorate')['#2 Operating in minutes per day - Toaster '].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Toaster**")
                        st.table(atm)   

                        atw=new.groupby('Governorate')['#2 Operating in minutes per day - Range - LPG '].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Range - LPG**")
                        st.table(atw)

                        atre=new.groupby('Governorate')['#2 Operating in minutes per day - Range - Electric '].describe()
                        atre.reset_index(inplace = True)
                        atre.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Range - Electric**")
                        st.table(atre)

                        acook=new.groupby('Governorate')['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) '].describe()
                        acook.reset_index(inplace = True)
                        acook.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Cooktop - (LPG/Electric/Induction)**")
                        st.table(acook)

                        ale=new.groupby('Governorate')['#2 Operating in minutes per day - Oven -(LPG/Electric) '].describe()
                        ale.reset_index(inplace = True)
                        ale.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Oven -(LPG/Electric)**")
                        st.table(ale)

                        af=new.groupby('Governorate')['#2 Operating in minutes per day - Air fryer '].describe()
                        af.reset_index(inplace = True)
                        af.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Air fryer**")
                        st.table(af)

                        cm=new.groupby('Governorate')['#2 Operating in minutes per day - Coffee Maker '].describe()
                        cm.reset_index(inplace = True)
                        cm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**Operating in minutes per day - Coffee Maker**")
                        st.table(cm)



                    if st.checkbox("Table 27. Association of Operating in minutes per day of Kitchen items"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Blender/mixer/food processor ']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'Operating in minutes per day - Blender/mixer/food processor'},inplace=True)
                        td['Operating in minutes per day - Blender/mixer/food processor'] = td['Operating in minutes per day - Blender/mixer/food processor'].replace({'#2 Operating in minutes per day - Blender/mixer/food processor ': 'Std'})

                        wacp=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Blender/mixer/food processor ']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)

                        wacp.rename(columns={'index':'Operating in minutes per day - Blender/mixer/food processor'},inplace=True)
                        wacp['Operating in minutes per day - Blender/mixer/food processor'] = wacp['Operating in minutes per day - Blender/mixer/food processor'].replace({'#2 Operating in minutes per day - Blender/mixer/food processor ': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Blender/mixer/food processor ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Blender/mixer/food processor'},inplace=True)
                        tang_m['Operating in minutes per day - Blender/mixer/food processor'] = tang_m['Operating in minutes per day - Blender/mixer/food processor'].replace({'#2 Operating in minutes per day - Blender/mixer/food processor ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Blender/mixer/food processor ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Blender/mixer/food processor'},inplace=True)
                        tang_mx['Operating in minutes per day - Blender/mixer/food processor'] = tang_mx['Operating in minutes per day - Blender/mixer/food processor'].replace({'#2 Operating in minutes per day - Blender/mixer/food processor ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Blender/mixer/food processor ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Blender/mixer/food processor'},inplace=True)
                        vc['Operating in minutes per day - Blender/mixer/food processor'] = vc['Operating in minutes per day - Blender/mixer/food processor'].replace({'#2 Operating in minutes per day - Blender/mixer/food processor ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)

                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']

                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']

                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']

                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']

                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']

                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Blender/mixer/food processor**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - kettle ']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'Operating in minutes per day - kettle'},inplace=True)
                        cs['Operating in minutes per day - kettle'] = cs['Operating in minutes per day - kettle'].replace({'#2 Operating in minutes per day - kettle ': 'Std'})

                        acsp=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - kettle ']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)

                        acsp.rename(columns={'index':'Operating in minutes per day - kettle'},inplace=True)
                        acsp['Operating in minutes per day - kettle'] = acsp['Operating in minutes per day - kettle'].replace({'#2 Operating in minutes per day - kettle ': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - kettle ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - kettle'},inplace=True)
                        tang_m['Operating in minutes per day - kettle'] = tang_m['Operating in minutes per day - kettle'].replace({'#2 Operating in minutes per day - kettle ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - kettle ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - kettle'},inplace=True)
                        tang_mx['Operating in minutes per day - kettle'] = tang_mx['Operating in minutes per day - kettle'].replace({'#2 Operating in minutes per day - kettle ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - kettle ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - kettle'},inplace=True)
                        vc['Operating in minutes per day - kettle'] = vc['Operating in minutes per day - kettle'].replace({'#2 Operating in minutes per day - kettle ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)

                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']

                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']

                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']

                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']

                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']

                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - kettle**")
                        st.write(df_acs)

                        ms=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Toaster ']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'Operating in minutes per day - Toaster'},inplace=True)
                        ms['Operating in minutes per day - Toaster'] = ms['Operating in minutes per day - Toaster'].replace({'#2 Operating in minutes per day - Toaster ': 'Std'})

                        atms=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Toaster ']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)

                        atms.rename(columns={'index':'Operating in minutes per day - Toaster'},inplace=True)
                        atms['Operating in minutes per day - Toaster'] = atms['Operating in minutes per day - Toaster'].replace({'#2 Operating in minutes per day - Toaster ': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Toaster ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Toaster'},inplace=True)
                        tang_m['Operating in minutes per day - Toaster'] = tang_m['Operating in minutes per day - Toaster'].replace({'#2 Operating in minutes per day - Toaster ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Toaster ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Toaster'},inplace=True)
                        tang_mx['Operating in minutes per day - Toaster'] = tang_mx['Operating in minutes per day - Toaster'].replace({'#2 Operating in minutes per day - Toaster ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Toaster ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Toaster'},inplace=True)
                        vc['Operating in minutes per day - Toaster'] = vc['Operating in minutes per day - Toaster'].replace({'#2 Operating in minutes per day - Toaster ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)

                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']

                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']

                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']

                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']

                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']

                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Toaster**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - LPG ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating in minutes per day - Range - LPG'},inplace=True)
                        uw['Operating in minutes per day - Range - LPG'] = uw['Operating in minutes per day - Range - LPG'].replace({'#2 Operating in minutes per day - Range - LPG ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - LPG ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'Operating in minutes per day - Range - LPG'},inplace=True)
                        acuw['Operating in minutes per day - Range - LPG'] = acuw['Operating in minutes per day - Range - LPG'].replace({'#2 Operating in minutes per day - Range - LPG ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - LPG ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Range - LPG'},inplace=True)
                        tang_m['Operating in minutes per day - Range - LPG'] = tang_m['Operating in minutes per day - Range - LPG'].replace({'#2 Operating in minutes per day - Range - LPG ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - LPG ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Range - LPG'},inplace=True)
                        tang_mx['Operating in minutes per day - Range - LPG'] = tang_mx['Operating in minutes per day - Range - LPG'].replace({'#2 Operating in minutes per day - Range - LPG ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - LPG ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Range - LPG'},inplace=True)
                        vc['Operating in minutes per day - Range - LPG'] = vc['Operating in minutes per day - Range - LPG'].replace({'#2 Operating in minutes per day - Range - LPG ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)

                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']

                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']

                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']

                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']

                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']

                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Range - LPG**")
                        st.write(df_auw)
                      #5  

                        uw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - Electric ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating in minutes per day - Range - Electric'},inplace=True)
                        uw['Operating in minutes per day - Range - Electric'] = uw['Operating in minutes per day - Range - Electric'].replace({'#2 Operating in minutes per day - Range - Electric ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - Electric ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'Operating in minutes per day - Range - Electric'},inplace=True)
                        acuw['Operating in minutes per day - Range - Electric'] = acuw['Operating in minutes per day - Range - Electric'].replace({'#2 Operating in minutes per day - Range - Electric ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - Electric ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Range - Electric'},inplace=True)
                        tang_m['Operating in minutes per day - Range - Electric'] = tang_m['Operating in minutes per day - Range - Electric'].replace({'#2 Operating in minutes per day - Range - Electric ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - Electric ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Range - Electric'},inplace=True)
                        tang_mx['Operating in minutes per day - Range - Electric'] = tang_mx['Operating in minutes per day - Range - Electric'].replace({'#2 Operating in minutes per day - Range - Electric ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - Electric ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Range - Electric'},inplace=True)
                        vc['Operating in minutes per day - Range - Electric'] = vc['Operating in minutes per day - Range - Electric'].replace({'#2 Operating in minutes per day - Range - Electric ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)

                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']

                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']

                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']

                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']

                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']

                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Range - Electric**")
                        st.write(df_auw)

                      #6  

                        uw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        uw['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'] = uw['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'].replace({'#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        acuw['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'] = acuw['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'].replace({'#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        tang_m['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'] = tang_m['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'].replace({'#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        tang_mx['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'] = tang_mx['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'].replace({'#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        vc['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'] = vc['Operating in minutes per day - Cooktop - (LPG/Electric/Induction)'].replace({'#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_cokt = acuw.append(tang_mx)
                        df_cokt=df_cokt.reset_index(drop=True)

                        df_cokt['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cokt['Al-Ahmadi']
                        del df_cokt['Al-Ahmadi']

                        df_cokt['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cokt['Al-Asimah']
                        del df_cokt['Al-Asimah']

                        df_cokt['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cokt['Al-Farwaniyah']
                        del df_cokt['Al-Farwaniyah']

                        df_cokt['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cokt['Al-Jahra']
                        del df_cokt['Al-Jahra']

                        df_cokt['Hawally (N={})'.format(vc['Hawally'][0])]=df_cokt['Hawally']
                        del df_cokt['Hawally']

                        df_cokt['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cokt['Mubarak Al-Kabeer']
                        del df_cokt['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Cooktop - (LPG/Electric/Induction)**")
                        st.write(df_cokt)

                        uw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Oven -(LPG/Electric) ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating in minutes per day - Oven -(LPG/Electric)'},inplace=True)
                        uw['Operating in minutes per day - Oven -(LPG/Electric)'] = uw['Operating in minutes per day - Oven -(LPG/Electric)'].replace({'#2 Operating in minutes per day - Oven -(LPG/Electric) ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Oven -(LPG/Electric) ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'Operating in minutes per day - Oven -(LPG/Electric)'},inplace=True)
                        acuw['Operating in minutes per day - Oven -(LPG/Electric)'] = acuw['Operating in minutes per day - Oven -(LPG/Electric)'].replace({'#2 Operating in minutes per day - Oven -(LPG/Electric) ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Oven -(LPG/Electric) ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Oven -(LPG/Electric)'},inplace=True)
                        tang_m['Operating in minutes per day - Oven -(LPG/Electric)'] = tang_m['Operating in minutes per day - Oven -(LPG/Electric)'].replace({'#2 Operating in minutes per day - Oven -(LPG/Electric) ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Oven -(LPG/Electric) ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Oven -(LPG/Electric)'},inplace=True)
                        tang_mx['Operating in minutes per day - Oven -(LPG/Electric)'] = tang_mx['Operating in minutes per day - Oven -(LPG/Electric)'].replace({'#2 Operating in minutes per day - Oven -(LPG/Electric) ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Oven -(LPG/Electric) ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Oven -(LPG/Electric)'},inplace=True)
                        vc['Operating in minutes per day - Oven -(LPG/Electric)'] = vc['Operating in minutes per day - Oven -(LPG/Electric)'].replace({'#2 Operating in minutes per day - Oven -(LPG/Electric) ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_lpg = acuw.append(tang_mx)
                        df_lpg=df_lpg.reset_index(drop=True)

                        df_lpg['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_lpg['Al-Ahmadi']
                        del df_lpg['Al-Ahmadi']

                        df_lpg['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_lpg['Al-Asimah']
                        del df_lpg['Al-Asimah']

                        df_lpg['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_lpg['Al-Farwaniyah']
                        del df_lpg['Al-Farwaniyah']

                        df_lpg['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_lpg['Al-Jahra']
                        del df_lpg['Al-Jahra']

                        df_lpg['Hawally (N={})'.format(vc['Hawally'][0])]=df_lpg['Hawally']
                        del df_lpg['Hawally']

                        df_lpg['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_lpg['Mubarak Al-Kabeer']
                        del df_lpg['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Oven -(LPG/Electric)**")
                        st.write(df_lpg)
                        #7
                        uw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Air fryer ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating in minutes per day - Air fryer'},inplace=True)
                        uw['Operating in minutes per day - Air fryer'] = uw['Operating in minutes per day - Air fryer'].replace({'#2 Operating in minutes per day - Air fryer ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Air fryer ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'Operating in minutes per day - Air fryer'},inplace=True)
                        acuw['Operating in minutes per day - Air fryer'] = acuw['Operating in minutes per day - Air fryer'].replace({'#2 Operating in minutes per day - Air fryer ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Air fryer ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Air fryer'},inplace=True)
                        tang_m['Operating in minutes per day - Air fryer'] = tang_m['Operating in minutes per day - Air fryer'].replace({'#2 Operating in minutes per day - Air fryer ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Air fryer ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Air fryer'},inplace=True)
                        tang_mx['Operating in minutes per day - Air fryer'] = tang_mx['Operating in minutes per day - Air fryer'].replace({'#2 Operating in minutes per day - Air fryer ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Air fryer ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Air fryer'},inplace=True)
                        vc['Operating in minutes per day - Air fryer'] = vc['Operating in minutes per day - Air fryer'].replace({'#2 Operating in minutes per day - Air fryer ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_af = acuw.append(tang_mx)
                        df_af=df_af.reset_index(drop=True)

                        df_af['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_af['Al-Ahmadi']
                        del df_af['Al-Ahmadi']

                        df_af['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_af['Al-Asimah']
                        del df_af['Al-Asimah']

                        df_af['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_af['Al-Farwaniyah']
                        del df_af['Al-Farwaniyah']

                        df_af['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_af['Al-Jahra']
                        del df_af['Al-Jahra']

                        df_af['Hawally (N={})'.format(vc['Hawally'][0])]=df_af['Hawally']
                        del df_af['Hawally']

                        df_af['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_af['Mubarak Al-Kabeer']
                        del df_af['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Air fryer**")
                        st.write(df_af)

                        #8
                        uw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Coffee Maker ']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'Operating in minutes per day - Coffee Maker'},inplace=True)
                        uw['Operating in minutes per day - Coffee Maker'] = uw['Operating in minutes per day - Coffee Maker'].replace({'#2 Operating in minutes per day - Coffee Maker ': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Coffee Maker ']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'Operating in minutes per day - Coffee Maker'},inplace=True)
                        acuw['Operating in minutes per day - Coffee Maker'] = acuw['Operating in minutes per day - Coffee Maker'].replace({'#2 Operating in minutes per day - Coffee Maker ': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Coffee Maker ']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'Operating in minutes per day - Coffee Maker'},inplace=True)
                        tang_m['Operating in minutes per day - Coffee Maker'] = tang_m['Operating in minutes per day - Coffee Maker'].replace({'#2 Operating in minutes per day - Coffee Maker ': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Coffee Maker ']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'Operating in minutes per day - Coffee Maker'},inplace=True)
                        tang_mx['Operating in minutes per day - Coffee Maker'] = tang_mx['Operating in minutes per day - Coffee Maker'].replace({'#2 Operating in minutes per day - Coffee Maker ': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Coffee Maker ']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'Operating in minutes per day - Coffee Maker'},inplace=True)
                        vc['Operating in minutes per day - Coffee Maker'] = vc['Operating in minutes per day - Coffee Maker'].replace({'#2 Operating in minutes per day - Coffee Maker ': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_cm = acuw.append(tang_mx)
                        df_cm=df_cm.reset_index(drop=True)

                        df_cm['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cm['Al-Ahmadi']
                        del df_cm['Al-Ahmadi']

                        df_cm['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cm['Al-Asimah']
                        del df_cm['Al-Asimah']

                        df_cm['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cm['Al-Farwaniyah']
                        del df_cm['Al-Farwaniyah']

                        df_cm['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cm['Al-Jahra']
                        del df_cm['Al-Jahra']

                        df_cm['Hawally (N={})'.format(vc['Hawally'][0])]=df_cm['Hawally']
                        del df_cm['Hawally']

                        df_cm['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cm['Mubarak Al-Kabeer']
                        del df_cm['Mubarak Al-Kabeer']


                        st.markdown("**Operating in minutes per day - Coffee Maker**")
                        st.write(df_cm)








                        #graph

                        gwac=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Blender/mixer/food processor ']].sum()
                        gwac.reset_index(inplace=True)

                        gacs=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - kettle ']].sum()
                        gacs.reset_index(inplace=True)

                        gams=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Toaster ']].sum()
                        gams.reset_index(inplace=True)

                        gauw=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - LPG ']].sum()
                        gauw.reset_index(inplace=True)

                        gact=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Range - Electric ']].sum()
                        gact.reset_index(inplace=True)

                        gael=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']].sum()
                        gael.reset_index(inplace=True)

                        gaoel=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Oven -(LPG/Electric) ']].sum()
                        gaoel.reset_index(inplace=True)

                        gaaf=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Air fryer ']].sum()
                        gaaf.reset_index(inplace=True)

                        gacf=new.groupby('Governorate',as_index=True)[['#2 Operating in minutes per day - Coffee Maker ']].sum()
                        gacf.reset_index(inplace=True)


                        import plotly.express as px
                        st.markdown("**Figure 22. Operating time of various kitchen appliances under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='Blender/mixer/food processor', x=gwac['Governorate'], y=gwac['#2 Operating in minutes per day - Blender/mixer/food processor ']),
                             go.Bar(name='kettle', x=gacs['Governorate'], y=gacs['#2 Operating in minutes per day - kettle ']),
                             go.Bar(name='Toaster', x=gams['Governorate'], y=gams['#2 Operating in minutes per day - Toaster ']),
                             go.Bar(name='Range - LPG', x=gauw['Governorate'], y=gauw['#2 Operating in minutes per day - Range - LPG ']),
                            go.Bar(name='Range - Electric', x=gact['Governorate'], y=gact['#2 Operating in minutes per day - Range - Electric ']),
                            go.Bar(name='Cooktop - (LPG/Electric/Induction)', x=gael['Governorate'], y=gael['#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ']),
                            go.Bar(name='Oven -(LPG/Electric)', x=gaoel['Governorate'], y=gaoel['#2 Operating in minutes per day - Oven -(LPG/Electric) ']),
                            go.Bar(name='Air fryer', x=gaaf['Governorate'], y=gaaf['#2 Operating in minutes per day - Air fryer ']),
                            go.Bar(name='Coffee Maker', x=gacf['Governorate'], y=gacf['#2 Operating in minutes per day - Coffee Maker ']),
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='group')
                        #fig.show()

                        st.write(fig3)








                        st.markdown("**Figure 23. Comparison of operating time (Kitchen appliances) under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='#2 Operating in minutes per day - Blender/mixer/food processor ', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='#2 Operating in minutes per day - kettle ', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='#2 Operating in minutes per day - Toaster ', color="Governorate")
                        fig21= px.bar(gauw, x="Governorate", y='#2 Operating in minutes per day - Range - LPG ', color="Governorate")
                        fig22= px.bar(gact, x="Governorate", y='#2 Operating in minutes per day - Range - Electric ', color="Governorate")
                        fig23= px.bar(gael, x="Governorate", y='#2 Operating in minutes per day - Cooktop - (LPG/Electric/Induction) ', color="Governorate")
                        fig24= px.bar(gaoel, x="Governorate", y='#2 Operating in minutes per day - Oven -(LPG/Electric) ', color="Governorate")
                        fig25= px.bar(gaaf, x="Governorate", y='#2 Operating in minutes per day - Air fryer ', color="Governorate")
                        fig26= px.bar(gacf, x="Governorate", y='#2 Operating in minutes per day - Coffee Maker ', color="Governorate")
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        st.write(fig21)
                        st.write(fig22)
                        st.write(fig23)
                        st.write(fig24)
                        st.write(fig25)
                        st.write(fig26)
                        
                        #watt
                    st.markdown("**The estimated Watts consumed per day by Kitchen items**")
                    if st.checkbox("Table 28. Descriptive Statistics- Kitchen items (The estimated Watts consumed per day)"):


                        wac=new.groupby('Governorate')['Blender/mixer/food processor  - The estimated Watts consumed per day'].describe()
                        wac.reset_index(inplace = True)
                        wac.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Blender/mixer/food processor**")
                        st.table(wac)


                        acs=new.groupby('Governorate')['kettle- The estimated Watts consumed per day'].describe()
                        acs.reset_index(inplace = True)
                        acs.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - kettle**")
                        st.table(acs)

                        atm=new.groupby('Governorate')['Toaster- The estimated Watts consumed per day'].describe()
                        atm.reset_index(inplace = True)
                        atm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Toaster**")
                        st.table(atm)   

                        atw=new.groupby('Governorate')['Range - LPG- The estimated Watts consumed per day'].describe()
                        atw.reset_index(inplace = True)
                        atw.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Range - LPG**")
                        st.table(atw)

                        atre=new.groupby('Governorate')['Range - Electric- The estimated Watts consumed per day'].describe()
                        atre.reset_index(inplace = True)
                        atre.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Range - Electric**")
                        st.table(atre)

                        acook=new.groupby('Governorate')['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day'].describe()
                        acook.reset_index(inplace = True)
                        acook.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)**")
                        st.table(acook)

                        ale=new.groupby('Governorate')['Oven -(LPG/Electric)- The estimated Watts consumed per day'].describe()
                        ale.reset_index(inplace = True)
                        ale.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Oven -(LPG/Electric)**")
                        st.table(ale)

                        af=new.groupby('Governorate')['Air fryer- The estimated Watts consumed per day'].describe()
                        af.reset_index(inplace = True)
                        af.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Air fryer**")
                        st.table(af)

                        cm=new.groupby('Governorate')['Coffee Maker- The estimated Watts consumed per day'].describe()
                        cm.reset_index(inplace = True)
                        cm.rename(columns={'index':'Governorate'},inplace=True)
                        st.markdown("**The estimated Watts consumed per day - Coffee Maker**")
                        st.table(cm)



                    if st.checkbox("Table 29. Association of The estimated Watts consumed per day of Kitchen items"):
                        #1   
                        td=new.groupby('Governorate',as_index=True)[['Blender/mixer/food processor  - The estimated Watts consumed per day']].std()
                        td=td.T
                        td.reset_index(inplace=True)
                        td.rename(columns={'index':'The estimated Watts consumed per day - Blender/mixer/food processor'},inplace=True)
                        td['The estimated Watts consumed per day - Blender/mixer/food processor'] = td['The estimated Watts consumed per day - Blender/mixer/food processor'].replace({'Blender/mixer/food processor  - The estimated Watts consumed per day': 'Std'})

                        wacp=new.groupby('Governorate',as_index=True)[['Blender/mixer/food processor  - The estimated Watts consumed per day']].mean()
                        wacp=wacp.T
                        wacp.reset_index(inplace = True)

                        wacp.rename(columns={'index':'The estimated Watts consumed per day - Blender/mixer/food processor'},inplace=True)
                        wacp['The estimated Watts consumed per day - Blender/mixer/food processor'] = wacp['The estimated Watts consumed per day - Blender/mixer/food processor'].replace({'Blender/mixer/food processor  - The estimated Watts consumed per day': 'Mean(SD)'})
                        wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                        wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                        wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                        wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                        wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                        wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Blender/mixer/food processor  - The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Blender/mixer/food processor'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Blender/mixer/food processor'] = tang_m['The estimated Watts consumed per day - Blender/mixer/food processor'].replace({'Blender/mixer/food processor  - The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Blender/mixer/food processor  - The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Blender/mixer/food processor'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Blender/mixer/food processor'] = tang_mx['The estimated Watts consumed per day - Blender/mixer/food processor'].replace({'Blender/mixer/food processor  - The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Blender/mixer/food processor  - The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Blender/mixer/food processor'},inplace=True)
                        vc['The estimated Watts consumed per day - Blender/mixer/food processor'] = vc['The estimated Watts consumed per day - Blender/mixer/food processor'].replace({'Blender/mixer/food processor  - The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_atc = wacp.append(tang_mx)
                        df_atc=df_atc.reset_index(drop=True)

                        df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                        del df_atc['Al-Ahmadi']

                        df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                        del df_atc['Al-Asimah']

                        df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                        del df_atc['Al-Farwaniyah']

                        df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                        del df_atc['Al-Jahra']

                        df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                        del df_atc['Hawally']

                        df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                        del df_atc['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Blender/mixer/food processor**")
                        st.write(df_atc)
                    #2     
                        cs=new.groupby('Governorate',as_index=True)[['kettle- The estimated Watts consumed per day']].std()
                        cs=cs.T
                        cs.reset_index(inplace=True)
                        cs.rename(columns={'index':'The estimated Watts consumed per day - kettle'},inplace=True)
                        cs['The estimated Watts consumed per day - kettle'] = cs['The estimated Watts consumed per day - kettle'].replace({'kettle- The estimated Watts consumed per day': 'Std'})

                        acsp=new.groupby('Governorate',as_index=True)[['kettle- The estimated Watts consumed per day']].mean()
                        acsp=acsp.T
                        acsp.reset_index(inplace = True)

                        acsp.rename(columns={'index':'The estimated Watts consumed per day - kettle'},inplace=True)
                        acsp['The estimated Watts consumed per day - kettle'] = acsp['The estimated Watts consumed per day - kettle'].replace({'kettle- The estimated Watts consumed per day': 'Mean(SD)'})
                        acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                        acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                        acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                        acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                        acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                        acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['kettle- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - kettle'},inplace=True)
                        tang_m['The estimated Watts consumed per day - kettle'] = tang_m['The estimated Watts consumed per day - kettle'].replace({'kettle- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['kettle- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - kettle'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - kettle'] = tang_mx['The estimated Watts consumed per day - kettle'].replace({'kettle- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['kettle- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - kettle'},inplace=True)
                        vc['The estimated Watts consumed per day - kettle'] = vc['The estimated Watts consumed per day - kettle'].replace({'kettle- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_acs = acsp.append(tang_mx)
                        df_acs=df_acs.reset_index(drop=True)

                        df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                        del df_acs['Al-Ahmadi']

                        df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                        del df_acs['Al-Asimah']

                        df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                        del df_acs['Al-Farwaniyah']

                        df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                        del df_acs['Al-Jahra']

                        df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                        del df_acs['Hawally']

                        df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                        del df_acs['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - kettle**")
                        st.write(df_acs)

                        ms=new.groupby('Governorate',as_index=True)[['Toaster- The estimated Watts consumed per day']].std()
                        ms=ms.T
                        ms.reset_index(inplace=True)
                        ms.rename(columns={'index':'The estimated Watts consumed per day - Toaster'},inplace=True)
                        ms['The estimated Watts consumed per day - Toaster'] = ms['The estimated Watts consumed per day - Toaster'].replace({'Toaster- The estimated Watts consumed per day': 'Std'})

                        atms=new.groupby('Governorate',as_index=True)[['Toaster- The estimated Watts consumed per day']].mean()
                        atms=atms.T
                        atms.reset_index(inplace = True)

                        atms.rename(columns={'index':'The estimated Watts consumed per day - Toaster'},inplace=True)
                        atms['The estimated Watts consumed per day - Toaster'] = atms['The estimated Watts consumed per day - Toaster'].replace({'Toaster- The estimated Watts consumed per day': 'Mean(SD)'})
                        atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                        atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                        atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                        atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                        atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                        atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Toaster- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Toaster'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Toaster'] = tang_m['The estimated Watts consumed per day - Toaster'].replace({'Toaster- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Toaster- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Toaster'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Toaster'] = tang_mx['The estimated Watts consumed per day - Toaster'].replace({'Toaster- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Toaster- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Toaster'},inplace=True)
                        vc['The estimated Watts consumed per day - Toaster'] = vc['The estimated Watts consumed per day - Toaster'].replace({'Toaster- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_ams = atms.append(tang_mx)
                        df_ams=df_ams.reset_index(drop=True)

                        df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                        del df_ams['Al-Ahmadi']

                        df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                        del df_ams['Al-Asimah']

                        df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                        del df_ams['Al-Farwaniyah']

                        df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                        del df_ams['Al-Jahra']

                        df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                        del df_ams['Hawally']

                        df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                        del df_ams['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Toaster**")
                        st.write(df_ams)
                     #4
                        uw=new.groupby('Governorate',as_index=True)[['Range - LPG- The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'The estimated Watts consumed per day - Range - LPG'},inplace=True)
                        uw['The estimated Watts consumed per day - Range - LPG'] = uw['The estimated Watts consumed per day - Range - LPG'].replace({'Range - LPG- The estimated Watts consumed per day': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['Range - LPG- The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'The estimated Watts consumed per day - Range - LPG'},inplace=True)
                        acuw['The estimated Watts consumed per day - Range - LPG'] = acuw['The estimated Watts consumed per day - Range - LPG'].replace({'Range - LPG- The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Range - LPG- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Range - LPG'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Range - LPG'] = tang_m['The estimated Watts consumed per day - Range - LPG'].replace({'Range - LPG- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Range - LPG- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Range - LPG'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Range - LPG'] = tang_mx['The estimated Watts consumed per day - Range - LPG'].replace({'Range - LPG- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Range - LPG- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Range - LPG'},inplace=True)
                        vc['The estimated Watts consumed per day - Range - LPG'] = vc['The estimated Watts consumed per day - Range - LPG'].replace({'Range - LPG- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)

                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']

                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']

                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']

                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']

                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']

                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Range - LPG**")
                        st.write(df_auw)
                      #5  

                        uw=new.groupby('Governorate',as_index=True)[['Range - Electric- The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'The estimated Watts consumed per day - Range - Electric'},inplace=True)
                        uw['The estimated Watts consumed per day - Range - Electric'] = uw['The estimated Watts consumed per day - Range - Electric'].replace({'Range - Electric- The estimated Watts consumed per day': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['Range - Electric- The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'The estimated Watts consumed per day - Range - Electric'},inplace=True)
                        acuw['The estimated Watts consumed per day - Range - Electric'] = acuw['The estimated Watts consumed per day - Range - Electric'].replace({'Range - Electric- The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Range - Electric- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Range - Electric'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Range - Electric'] = tang_m['The estimated Watts consumed per day - Range - Electric'].replace({'Range - Electric- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Range - Electric- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Range - Electric'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Range - Electric'] = tang_mx['The estimated Watts consumed per day - Range - Electric'].replace({'Range - Electric- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Range - Electric- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Range - Electric'},inplace=True)
                        vc['The estimated Watts consumed per day - Range - Electric'] = vc['The estimated Watts consumed per day - Range - Electric'].replace({'Range - Electric- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_auw = acuw.append(tang_mx)
                        df_auw=df_auw.reset_index(drop=True)

                        df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                        del df_auw['Al-Ahmadi']

                        df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                        del df_auw['Al-Asimah']

                        df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                        del df_auw['Al-Farwaniyah']

                        df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                        del df_auw['Al-Jahra']

                        df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                        del df_auw['Hawally']

                        df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                        del df_auw['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Range - Electric**")
                        st.write(df_auw)

                      #6  

                        uw=new.groupby('Governorate',as_index=True)[['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        uw['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'] = uw['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'].replace({'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        acuw['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'] = acuw['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'].replace({'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'] = tang_m['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'].replace({'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'] = tang_mx['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'].replace({'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'},inplace=True)
                        vc['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'] = vc['The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)'].replace({'Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_cokt = acuw.append(tang_mx)
                        df_cokt=df_cokt.reset_index(drop=True)

                        df_cokt['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cokt['Al-Ahmadi']
                        del df_cokt['Al-Ahmadi']

                        df_cokt['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cokt['Al-Asimah']
                        del df_cokt['Al-Asimah']

                        df_cokt['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cokt['Al-Farwaniyah']
                        del df_cokt['Al-Farwaniyah']

                        df_cokt['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cokt['Al-Jahra']
                        del df_cokt['Al-Jahra']

                        df_cokt['Hawally (N={})'.format(vc['Hawally'][0])]=df_cokt['Hawally']
                        del df_cokt['Hawally']

                        df_cokt['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cokt['Mubarak Al-Kabeer']
                        del df_cokt['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Cooktop - (LPG/Electric/Induction)**")
                        st.write(df_cokt)

                        uw=new.groupby('Governorate',as_index=True)[['Oven -(LPG/Electric)- The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'The estimated Watts consumed per day - Oven -(LPG/Electric)'},inplace=True)
                        uw['The estimated Watts consumed per day - Oven -(LPG/Electric)'] = uw['The estimated Watts consumed per day - Oven -(LPG/Electric)'].replace({'Oven -(LPG/Electric)- The estimated Watts consumed per day': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['Oven -(LPG/Electric)- The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'The estimated Watts consumed per day - Oven -(LPG/Electric)'},inplace=True)
                        acuw['The estimated Watts consumed per day - Oven -(LPG/Electric)'] = acuw['The estimated Watts consumed per day - Oven -(LPG/Electric)'].replace({'Oven -(LPG/Electric)- The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Oven -(LPG/Electric)- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Oven -(LPG/Electric)'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Oven -(LPG/Electric)'] = tang_m['The estimated Watts consumed per day - Oven -(LPG/Electric)'].replace({'Oven -(LPG/Electric)- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Oven -(LPG/Electric)- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Oven -(LPG/Electric)'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Oven -(LPG/Electric)'] = tang_mx['The estimated Watts consumed per day - Oven -(LPG/Electric)'].replace({'Oven -(LPG/Electric)- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Oven -(LPG/Electric)- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Oven -(LPG/Electric)'},inplace=True)
                        vc['The estimated Watts consumed per day - Oven -(LPG/Electric)'] = vc['The estimated Watts consumed per day - Oven -(LPG/Electric)'].replace({'Oven -(LPG/Electric)- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_lpg = acuw.append(tang_mx)
                        df_lpg=df_lpg.reset_index(drop=True)

                        df_lpg['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_lpg['Al-Ahmadi']
                        del df_lpg['Al-Ahmadi']

                        df_lpg['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_lpg['Al-Asimah']
                        del df_lpg['Al-Asimah']

                        df_lpg['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_lpg['Al-Farwaniyah']
                        del df_lpg['Al-Farwaniyah']

                        df_lpg['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_lpg['Al-Jahra']
                        del df_lpg['Al-Jahra']

                        df_lpg['Hawally (N={})'.format(vc['Hawally'][0])]=df_lpg['Hawally']
                        del df_lpg['Hawally']

                        df_lpg['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_lpg['Mubarak Al-Kabeer']
                        del df_lpg['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Oven -(LPG/Electric)**")
                        st.write(df_lpg)
                        #7
                        uw=new.groupby('Governorate',as_index=True)[['Air fryer- The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'The estimated Watts consumed per day - Air fryer'},inplace=True)
                        uw['The estimated Watts consumed per day - Air fryer'] = uw['The estimated Watts consumed per day - Air fryer'].replace({'Air fryer- The estimated Watts consumed per day': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['Air fryer- The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'The estimated Watts consumed per day - Air fryer'},inplace=True)
                        acuw['The estimated Watts consumed per day - Air fryer'] = acuw['The estimated Watts consumed per day - Air fryer'].replace({'Air fryer- The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Air fryer- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Air fryer'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Air fryer'] = tang_m['The estimated Watts consumed per day - Air fryer'].replace({'Air fryer- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Air fryer- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Air fryer'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Air fryer'] = tang_mx['The estimated Watts consumed per day - Air fryer'].replace({'Air fryer- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Air fryer- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Air fryer'},inplace=True)
                        vc['The estimated Watts consumed per day - Air fryer'] = vc['The estimated Watts consumed per day - Air fryer'].replace({'Air fryer- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_af = acuw.append(tang_mx)
                        df_af=df_af.reset_index(drop=True)

                        df_af['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_af['Al-Ahmadi']
                        del df_af['Al-Ahmadi']

                        df_af['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_af['Al-Asimah']
                        del df_af['Al-Asimah']

                        df_af['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_af['Al-Farwaniyah']
                        del df_af['Al-Farwaniyah']

                        df_af['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_af['Al-Jahra']
                        del df_af['Al-Jahra']

                        df_af['Hawally (N={})'.format(vc['Hawally'][0])]=df_af['Hawally']
                        del df_af['Hawally']

                        df_af['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_af['Mubarak Al-Kabeer']
                        del df_af['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Air fryer**")
                        st.write(df_af)

                        #8
                        uw=new.groupby('Governorate',as_index=True)[['Coffee Maker- The estimated Watts consumed per day']].std()
                        uw=uw.T
                        uw.reset_index(inplace=True)
                        uw.rename(columns={'index':'The estimated Watts consumed per day - Coffee Maker'},inplace=True)
                        uw['The estimated Watts consumed per day - Coffee Maker'] = uw['The estimated Watts consumed per day - Coffee Maker'].replace({'Coffee Maker- The estimated Watts consumed per day': 'Std'})

                        acuw=new.groupby('Governorate',as_index=True)[['Coffee Maker- The estimated Watts consumed per day']].mean()
                        acuw=acuw.T
                        acuw.reset_index(inplace = True)

                        acuw.rename(columns={'index':'The estimated Watts consumed per day - Coffee Maker'},inplace=True)
                        acuw['The estimated Watts consumed per day - Coffee Maker'] = acuw['The estimated Watts consumed per day - Coffee Maker'].replace({'Coffee Maker- The estimated Watts consumed per day': 'Mean(SD)'})
                        acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                        acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                        acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                        acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                        acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                        acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                        tang_m=new.groupby('Governorate',as_index=True)[['Coffee Maker- The estimated Watts consumed per day']].min()
                        tang_m=tang_m.T

                        tang_m.reset_index(inplace=True)
                        tang_m.rename(columns={'index':'The estimated Watts consumed per day - Coffee Maker'},inplace=True)
                        tang_m['The estimated Watts consumed per day - Coffee Maker'] = tang_m['The estimated Watts consumed per day - Coffee Maker'].replace({'Coffee Maker- The estimated Watts consumed per day': 'min'})

                        tang_mx=new.groupby('Governorate',as_index=True)[['Coffee Maker- The estimated Watts consumed per day']].max()
                        tang_mx=tang_mx.T
                        tang_mx.reset_index(inplace=True)
                        tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Coffee Maker'},inplace=True)
                        tang_mx['The estimated Watts consumed per day - Coffee Maker'] = tang_mx['The estimated Watts consumed per day - Coffee Maker'].replace({'Coffee Maker- The estimated Watts consumed per day': 'Range'})

                        vc=new.groupby('Governorate',as_index=True)[['Coffee Maker- The estimated Watts consumed per day']].count()
                        vc=vc.T
                        vc.reset_index(inplace=True)
                        vc.rename(columns={'index':'The estimated Watts consumed per day - Coffee Maker'},inplace=True)
                        vc['The estimated Watts consumed per day - Coffee Maker'] = vc['The estimated Watts consumed per day - Coffee Maker'].replace({'Coffee Maker- The estimated Watts consumed per day': 'count'})

                        tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                        tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                        tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                        tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                        tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                        tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                        df_cm = acuw.append(tang_mx)
                        df_cm=df_cm.reset_index(drop=True)

                        df_cm['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cm['Al-Ahmadi']
                        del df_cm['Al-Ahmadi']

                        df_cm['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cm['Al-Asimah']
                        del df_cm['Al-Asimah']

                        df_cm['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cm['Al-Farwaniyah']
                        del df_cm['Al-Farwaniyah']

                        df_cm['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cm['Al-Jahra']
                        del df_cm['Al-Jahra']

                        df_cm['Hawally (N={})'.format(vc['Hawally'][0])]=df_cm['Hawally']
                        del df_cm['Hawally']

                        df_cm['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cm['Mubarak Al-Kabeer']
                        del df_cm['Mubarak Al-Kabeer']


                        st.markdown("**The estimated Watts consumed per day - Coffee Maker**")
                        st.write(df_cm)








                        #graph

                        gwac=new.groupby('Governorate',as_index=True)[['Blender/mixer/food processor  - The estimated Watts consumed per day']].sum()
                        gwac.reset_index(inplace=True)

                        gacs=new.groupby('Governorate',as_index=True)[['kettle- The estimated Watts consumed per day']].sum()
                        gacs.reset_index(inplace=True)

                        gams=new.groupby('Governorate',as_index=True)[['Toaster- The estimated Watts consumed per day']].sum()
                        gams.reset_index(inplace=True)

                        gauw=new.groupby('Governorate',as_index=True)[['Range - LPG- The estimated Watts consumed per day']].sum()
                        gauw.reset_index(inplace=True)

                        gact=new.groupby('Governorate',as_index=True)[['Range - Electric- The estimated Watts consumed per day']].sum()
                        gact.reset_index(inplace=True)

                        gael=new.groupby('Governorate',as_index=True)[['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']].sum()
                        gael.reset_index(inplace=True)

                        gaoel=new.groupby('Governorate',as_index=True)[['Oven -(LPG/Electric)- The estimated Watts consumed per day']].sum()
                        gaoel.reset_index(inplace=True)

                        gaaf=new.groupby('Governorate',as_index=True)[['Air fryer- The estimated Watts consumed per day']].sum()
                        gaaf.reset_index(inplace=True)

                        gacf=new.groupby('Governorate',as_index=True)[['Coffee Maker- The estimated Watts consumed per day']].sum()
                        gacf.reset_index(inplace=True)


                        import plotly.express as px
                        st.markdown("**Figure 24. Watts consumed by various kitchen appliances under different Governorate**")
                        import plotly.graph_objects as go
                        fig3 = go.Figure(data=[
                            go.Bar(name='Blender/mixer/food processor', x=gwac['Governorate'], y=gwac['Blender/mixer/food processor  - The estimated Watts consumed per day']),
                             go.Bar(name='kettle', x=gacs['Governorate'], y=gacs['kettle- The estimated Watts consumed per day']),
                             go.Bar(name='Toaster', x=gams['Governorate'], y=gams['Toaster- The estimated Watts consumed per day']),
                             go.Bar(name='Range - LPG', x=gauw['Governorate'], y=gauw['Range - LPG- The estimated Watts consumed per day']),
                            go.Bar(name='Range - Electric', x=gact['Governorate'], y=gact['Range - Electric- The estimated Watts consumed per day']),
                            go.Bar(name='Cooktop - (LPG/Electric/Induction)', x=gael['Governorate'], y=gael['Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day']),
                            go.Bar(name='Oven -(LPG/Electric)', x=gaoel['Governorate'], y=gaoel['Oven -(LPG/Electric)- The estimated Watts consumed per day']),
                            go.Bar(name='Air fryer', x=gaaf['Governorate'], y=gaaf['Air fryer- The estimated Watts consumed per day']),
                            go.Bar(name='Coffee Maker', x=gacf['Governorate'], y=gacf['Coffee Maker- The estimated Watts consumed per day']),
                        ])
                        # Change the bar mode
                        fig3.update_layout(barmode='group')
                        #fig.show()

                        st.write(fig3)








                        st.markdown("**Figure 25. Comparison of watt consumed by Kitchen appliances under different Governorate**")
                        fig18 = px.bar(gwac, x="Governorate", y='Blender/mixer/food processor  - The estimated Watts consumed per day', color="Governorate")
                        fig19 = px.bar(gacs, x="Governorate", y='kettle- The estimated Watts consumed per day', color="Governorate")
                        fig20 = px.bar(gams, x="Governorate", y='Toaster- The estimated Watts consumed per day', color="Governorate")
                        fig21= px.bar(gauw, x="Governorate", y='Range - LPG- The estimated Watts consumed per day', color="Governorate")
                        fig22= px.bar(gact, x="Governorate", y='Range - Electric- The estimated Watts consumed per day', color="Governorate")
                        fig23= px.bar(gael, x="Governorate", y='Cooktop - (LPG/Electric/Induction)- The estimated Watts consumed per day', color="Governorate")
                        fig24= px.bar(gaoel, x="Governorate", y='Oven -(LPG/Electric)- The estimated Watts consumed per day', color="Governorate")
                        fig25= px.bar(gaaf, x="Governorate", y='Air fryer- The estimated Watts consumed per day', color="Governorate")
                        fig26= px.bar(gacf, x="Governorate", y='Coffee Maker- The estimated Watts consumed per day', color="Governorate")
                        st.write(fig18)
                        st.write(fig19)
                        st.write(fig20)
                        st.write(fig21)
                        st.write(fig22)
                        st.write(fig23)
                        st.write(fig24)
                        st.write(fig25)
                        st.write(fig26)
            st.subheader("Analysis on different Water equipment")
            if st.checkbox("➡️ Analysis and statistics on different Water equipment"):
                
                st.markdown("**Units owned by (Water equipment)**")
                if st.checkbox("Table 30. Descriptive Statistics- Units owned (Water equipment)"):
                    wac=new.groupby('Governorate')['#1 units owned - Water Cooler  '].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Water Cooler**")
                    st.table(wac)
                    
                    
                    acs=new.groupby('Governorate')['#1 units owned - Water Heater - Central  '].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Water Heater - Central**")
                    st.table(acs)
                        
                    atm=new.groupby('Governorate')['#1 units owned - Water Heater - Normal  '].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Water Heater - Normal**")
                    st.table(atm)   
                    
                    
                    
                if st.checkbox("Table 31. Association of Units owned (Water equipment)"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Cooler  ']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'units owned - Water Cooler'},inplace=True)
                    td['units owned - Water Cooler'] = td['units owned - Water Cooler'].replace({'#1 units owned - Water Cooler  ': 'Std'})
                     
                    wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Cooler  ']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)
                     
                    wacp.rename(columns={'index':'units owned - Water Cooler'},inplace=True)
                    wacp['units owned - Water Cooler'] = wacp['units owned - Water Cooler'].replace({'#1 units owned - Water Cooler  ': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Cooler  ']].min()
                    tang_m=tang_m.T
                     
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Water Cooler'},inplace=True)
                    tang_m['units owned - Water Cooler'] = tang_m['units owned - Water Cooler'].replace({'#1 units owned - Water Cooler  ': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Cooler  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Water Cooler'},inplace=True)
                    tang_mx['units owned - Water Cooler'] = tang_mx['units owned - Water Cooler'].replace({'#1 units owned - Water Cooler  ': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Cooler  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Water Cooler'},inplace=True)
                    vc['units owned - Water Cooler'] = vc['units owned - Water Cooler'].replace({'#1 units owned - Water Cooler  ': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                    
                    
                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)
                    
                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']
                    
                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']
                    
                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']
                    
                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']
                     
                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']
                     
                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**units owned - Water Cooler**")
                    st.write(df_atc)
                #2     
                    cs=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Central  ']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'units owned - Water Heater - Central'},inplace=True)
                    cs['units owned - Water Heater - Central'] = cs['units owned - Water Heater - Central'].replace({'#1 units owned - Water Heater - Central  ': 'Std'})
                     
                    acsp=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Central  ']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)
                     
                    acsp.rename(columns={'index':'units owned - Water Heater - Central'},inplace=True)
                    acsp['units owned - Water Heater - Central'] = acsp['units owned - Water Heater - Central'].replace({'#1 units owned - Water Heater - Central  ': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Central  ']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Water Heater - Central'},inplace=True)
                    tang_m['units owned - Water Heater - Central'] = tang_m['units owned - Water Heater - Central'].replace({'#1 units owned - Water Heater - Central  ': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Central  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Water Heater - Central'},inplace=True)
                    tang_mx['units owned - Water Heater - Central'] = tang_mx['units owned - Water Heater - Central'].replace({'#1 units owned - Water Heater - Central  ': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Central  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Water Heater - Central'},inplace=True)
                    vc['units owned - Water Heater - Central'] = vc['units owned - Water Heater - Central'].replace({'#1 units owned - Water Heater - Central  ': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)
                     
                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']
                    
                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']
                     
                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']
                    
                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']
                     
                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']
                     
                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**units owned - Water Heater - Central**")
                    st.write(df_acs)
                     
                    ms=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Normal  ']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'units owned - Water Heater - Normal'},inplace=True)
                    ms['units owned - Water Heater - Normal'] = ms['units owned - Water Heater - Normal'].replace({'#1 units owned - Water Heater - Normal  ': 'Std'})
                     
                    atms=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Normal  ']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)
                     
                    atms.rename(columns={'index':'units owned - Water Heater - Normal'},inplace=True)
                    atms['units owned - Water Heater - Normal'] = atms['units owned - Water Heater - Normal'].replace({'#1 units owned - Water Heater - Normal  ': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Normal  ']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Water Heater - Normal'},inplace=True)
                    tang_m['units owned - Water Heater - Normal'] = tang_m['units owned - Water Heater - Normal'].replace({'#1 units owned - Water Heater - Normal  ': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Normal  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Water Heater - Normal'},inplace=True)
                    tang_mx['units owned - Water Heater - Normal'] = tang_mx['units owned - Water Heater - Normal'].replace({'#1 units owned - Water Heater - Normal  ': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Normal  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Water Heater - Normal'},inplace=True)
                    vc['units owned - Water Heater - Normal'] = vc['units owned - Water Heater - Normal'].replace({'#1 units owned - Water Heater - Normal  ': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)
                     
                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']
                     
                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']
                     
                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']
                     
                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']
                     
                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']
                     
                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**units owned - Water Heater - Normal**")
                    st.write(df_ams)
                 
                     
                    #graph
                     
                    gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Cooler  ']].sum()
                    gwac.reset_index(inplace=True)
                     
                    gacs=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Central  ']].sum()
                    gacs.reset_index(inplace=True)
                    
                    gams=new.groupby('Governorate',as_index=True)[['#1 units owned - Water Heater - Normal  ']].sum()
                    gams.reset_index(inplace=True)
                    
                   
                    
                    import plotly.express as px
                    st.markdown("**Figure 26. Distribution of units owned (water equipment) under different Governorate**")
                    import plotly.graph_objects as go
                    fig3 = go.Figure(data=[
                        go.Bar(name='Water Cooler', x=gwac['Governorate'], y=gwac['#1 units owned - Water Cooler  ']),
                         go.Bar(name='Water Heater - Central', x=gacs['Governorate'], y=gacs['#1 units owned - Water Heater - Central  ']),
                         go.Bar(name='Water Heater - Normal', x=gams['Governorate'], y=gams['#1 units owned - Water Heater - Normal  ']),
                         
                    ])
                    # Change the bar mode
                    fig3.update_layout(barmode='stack')
                    #fig.show()
                    
                    st.write(fig3)
                    
                    
                    
                    
                    
                    
                    
                    
                    st.markdown("**Figure 27. Comparison of units owned (water equipment) under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Water Cooler  ', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='#1 units owned - Water Heater - Central  ', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='#1 units owned - Water Heater - Normal  ', color="Governorate")
                    
                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                    
                    
                st.markdown("**size of the equipment by (Water)**")
                if st.checkbox("Table 32. Descriptive Statistics- size of the equipment (Water)"):
                    wac=new.groupby('Governorate')['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**size of the equipment - Water Cooler**")
                    st.table(wac)
                    
                    
                    acs=new.groupby('Governorate')['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central'].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**size of the equipment - Water Heater - Central**")
                    st.table(acs)
                        
                    atm=new.groupby('Governorate')['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**size of the equipment - Water Heater - Normal**")
                    st.table(atm)   
                    
                    
                    
                if st.checkbox("Table 33. Association of size of the equipment (Water)"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'size of the equipment - Water Cooler'},inplace=True)
                    td['size of the equipment - Water Cooler'] = td['size of the equipment - Water Cooler'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler': 'Std'})
                     
                    wacp=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)
                     
                    wacp.rename(columns={'index':'size of the equipment - Water Cooler'},inplace=True)
                    wacp['size of the equipment - Water Cooler'] = wacp['size of the equipment - Water Cooler'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']].min()
                    tang_m=tang_m.T
                     
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'size of the equipment - Water Cooler'},inplace=True)
                    tang_m['size of the equipment - Water Cooler'] = tang_m['size of the equipment - Water Cooler'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'size of the equipment - Water Cooler'},inplace=True)
                    tang_mx['size of the equipment - Water Cooler'] = tang_mx['size of the equipment - Water Cooler'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'size of the equipment - Water Cooler'},inplace=True)
                    vc['size of the equipment - Water Cooler'] = vc['size of the equipment - Water Cooler'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                    
                    
                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)
                    
                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']
                    
                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']
                    
                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']
                    
                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']
                     
                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']
                     
                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**size of the equipment - Water Cooler**")
                    st.write(df_atc)
                #2     
                    cs=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'size of the equipment - Water Heater - Central'},inplace=True)
                    cs['size of the equipment - Water Heater - Central'] = cs['size of the equipment - Water Heater - Central'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central': 'Std'})
                     
                    acsp=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)
                     
                    acsp.rename(columns={'index':'size of the equipment - Water Heater - Central'},inplace=True)
                    acsp['size of the equipment - Water Heater - Central'] = acsp['size of the equipment - Water Heater - Central'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'size of the equipment - Water Heater - Central'},inplace=True)
                    tang_m['size of the equipment - Water Heater - Central'] = tang_m['size of the equipment - Water Heater - Central'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'size of the equipment - Water Heater - Central'},inplace=True)
                    tang_mx['size of the equipment - Water Heater - Central'] = tang_mx['size of the equipment - Water Heater - Central'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'size of the equipment - Water Heater - Central'},inplace=True)
                    vc['size of the equipment - Water Heater - Central'] = vc['size of the equipment - Water Heater - Central'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)
                     
                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']
                    
                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']
                     
                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']
                    
                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']
                     
                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']
                     
                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**size of the equipment - Water Heater - Central**")
                    st.write(df_acs)
                     
                    ms=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'size of the equipment - Water Heater - Normal'},inplace=True)
                    ms['size of the equipment - Water Heater - Normal'] = ms['size of the equipment - Water Heater - Normal'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal': 'Std'})
                     
                    atms=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)
                     
                    atms.rename(columns={'index':'size of the equipment - Water Heater - Normal'},inplace=True)
                    atms['size of the equipment - Water Heater - Normal'] = atms['size of the equipment - Water Heater - Normal'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'size of the equipment - Water Heater - Normal'},inplace=True)
                    tang_m['size of the equipment - Water Heater - Normal'] = tang_m['size of the equipment - Water Heater - Normal'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'size of the equipment - Water Heater - Normal'},inplace=True)
                    tang_mx['size of the equipment - Water Heater - Normal'] = tang_mx['size of the equipment - Water Heater - Normal'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'size of the equipment - Water Heater - Normal'},inplace=True)
                    vc['size of the equipment - Water Heater - Normal'] = vc['size of the equipment - Water Heater - Normal'].replace({'#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)
                     
                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']
                     
                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']
                     
                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']
                     
                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']
                     
                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']
                     
                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**size of the equipment - Water Heater - Normal**")
                    st.write(df_ams)
                 
                     
                    #graph
                     
                    gwac=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']].sum()
                    gwac.reset_index(inplace=True)
                     
                    gacs=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']].sum()
                    gacs.reset_index(inplace=True)
                    
                    gams=new.groupby('Governorate',as_index=True)[['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']].sum()
                    gams.reset_index(inplace=True)
                    
                   
                    
                    import plotly.express as px
                    st.markdown("**Figure 28. Distribution of size of the equipment (water equipment) under different Governorate**")
                    import plotly.graph_objects as go
                    fig3 = go.Figure(data=[
                        go.Bar(name='Water Cooler', x=gwac['Governorate'], y=gwac['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler']),
                         go.Bar(name='Water Heater - Central', x=gacs['Governorate'], y=gacs['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central']),
                         go.Bar(name='Water Heater - Norma', x=gams['Governorate'], y=gams['#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal']),
                         
                    ])
                    # Change the bar mode
                    fig3.update_layout(barmode='stack')
                    #fig.show()
                    
                    st.write(fig3)
                    
                    
                    
                    
                    
                    
                    
                    
                    st.markdown("**Figure29. Comparison of Size of the equipment (water equipment) under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Cooler', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Central', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='#2 What is the size of the equipment? (e.g. 10 litres, 15 litres) - Water Heater - Normal', color="Governorate")
                    
                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                
                #watts
                st.markdown("**The estimated Watts consumed per day by (Water)**")
                if st.checkbox("Table 34. Descriptive Statistics- The estimated Watts consumed per day (Water)"):
                    wac=new.groupby('Governorate')['Water Cooler - The estimated Watts consumed per day'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**The estimated Watts consumed per day - Water Cooler**")
                    st.table(wac)
                    
                    
                    acs=new.groupby('Governorate')['Water Heater - Central - The estimated Watts consumed per day'].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**The estimated Watts consumed per day - Water Heater - Central**")
                    st.table(acs)
                        
                    atm=new.groupby('Governorate')['Water Heater - Normal - The estimated Watts consumed per day'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**The estimated Watts consumed per day - Water Heater - Normal**")
                    st.table(atm)   
                    
                    
                    
                if st.checkbox("Table 35. Association of The estimated Watts consumed per day (Water)"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['Water Cooler - The estimated Watts consumed per day']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'The estimated Watts consumed per day - Water Cooler'},inplace=True)
                    td['The estimated Watts consumed per day - Water Cooler'] = td['The estimated Watts consumed per day - Water Cooler'].replace({'Water Cooler - The estimated Watts consumed per day': 'Std'})
                     
                    wacp=new.groupby('Governorate',as_index=True)[['Water Cooler - The estimated Watts consumed per day']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)
                     
                    wacp.rename(columns={'index':'The estimated Watts consumed per day - Water Cooler'},inplace=True)
                    wacp['The estimated Watts consumed per day - Water Cooler'] = wacp['The estimated Watts consumed per day - Water Cooler'].replace({'Water Cooler - The estimated Watts consumed per day': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['Water Cooler - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T
                     
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'The estimated Watts consumed per day - Water Cooler'},inplace=True)
                    tang_m['The estimated Watts consumed per day - Water Cooler'] = tang_m['The estimated Watts consumed per day - Water Cooler'].replace({'Water Cooler - The estimated Watts consumed per day': 'min'})
                    
                    tang_mx=new.groupby('Governorate',as_index=True)[['Water Cooler - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Water Cooler'},inplace=True)
                    tang_mx['The estimated Watts consumed per day - Water Cooler'] = tang_mx['The estimated Watts consumed per day - Water Cooler'].replace({'Water Cooler - The estimated Watts consumed per day': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['Water Cooler - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'The estimated Watts consumed per day - Water Cooler'},inplace=True)
                    vc['The estimated Watts consumed per day - Water Cooler'] = vc['The estimated Watts consumed per day - Water Cooler'].replace({'Water Cooler - The estimated Watts consumed per day': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                    
                    
                    
                    
                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)
                    
                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']
                    
                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']
                    
                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']
                    
                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']
                     
                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']
                     
                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**The estimated Watts consumed per day - Water Cooler**")
                    st.write(df_atc)
                #2     
                    cs=new.groupby('Governorate',as_index=True)[['Water Heater - Central - The estimated Watts consumed per day']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Central'},inplace=True)
                    cs['The estimated Watts consumed per day - Water Heater - Central'] = cs['The estimated Watts consumed per day - Water Heater - Central'].replace({'Water Heater - Central - The estimated Watts consumed per day': 'Std'})
                     
                    acsp=new.groupby('Governorate',as_index=True)[['Water Heater - Central - The estimated Watts consumed per day']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)
                     
                    acsp.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Central'},inplace=True)
                    acsp['The estimated Watts consumed per day - Water Heater - Central'] = acsp['The estimated Watts consumed per day - Water Heater - Central'].replace({'Water Heater - Central - The estimated Watts consumed per day': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['Water Heater - Central - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Central'},inplace=True)
                    tang_m['The estimated Watts consumed per day - Water Heater - Central'] = tang_m['The estimated Watts consumed per day - Water Heater - Central'].replace({'Water Heater - Central - The estimated Watts consumed per day': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['Water Heater - Central - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Central'},inplace=True)
                    tang_mx['The estimated Watts consumed per day - Water Heater - Central'] = tang_mx['The estimated Watts consumed per day - Water Heater - Central'].replace({'Water Heater - Central - The estimated Watts consumed per day': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['Water Heater - Central - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Central'},inplace=True)
                    vc['The estimated Watts consumed per day - Water Heater - Central'] = vc['The estimated Watts consumed per day - Water Heater - Central'].replace({'Water Heater - Central - The estimated Watts consumed per day': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)
                     
                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']
                    
                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']
                     
                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']
                    
                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']
                     
                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']
                     
                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**The estimated Watts consumed per day - Water Heater - Central**")
                    st.write(df_acs)
                     
                    ms=new.groupby('Governorate',as_index=True)[['Water Heater - Normal - The estimated Watts consumed per day']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Normal'},inplace=True)
                    ms['The estimated Watts consumed per day - Water Heater - Normal'] = ms['The estimated Watts consumed per day - Water Heater - Normal'].replace({'Water Heater - Normal - The estimated Watts consumed per day': 'Std'})
                     
                    atms=new.groupby('Governorate',as_index=True)[['Water Heater - Normal - The estimated Watts consumed per day']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)
                     
                    atms.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Normal'},inplace=True)
                    atms['The estimated Watts consumed per day - Water Heater - Normal'] = atms['The estimated Watts consumed per day - Water Heater - Normal'].replace({'Water Heater - Normal - The estimated Watts consumed per day': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))
                    
                     
                     
                    
                    tang_m=new.groupby('Governorate',as_index=True)[['Water Heater - Normal - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T
                    
                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Normal'},inplace=True)
                    tang_m['The estimated Watts consumed per day - Water Heater - Normal'] = tang_m['The estimated Watts consumed per day - Water Heater - Normal'].replace({'Water Heater - Normal - The estimated Watts consumed per day': 'min'})
                     
                    tang_mx=new.groupby('Governorate',as_index=True)[['Water Heater - Normal - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Normal'},inplace=True)
                    tang_mx['The estimated Watts consumed per day - Water Heater - Normal'] = tang_mx['The estimated Watts consumed per day - Water Heater - Normal'].replace({'Water Heater - Normal - The estimated Watts consumed per day': 'Range'})
                     
                    vc=new.groupby('Governorate',as_index=True)[['Water Heater - Normal - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'The estimated Watts consumed per day - Water Heater - Normal'},inplace=True)
                    vc['The estimated Watts consumed per day - Water Heater - Normal'] = vc['The estimated Watts consumed per day - Water Heater - Normal'].replace({'Water Heater - Normal - The estimated Watts consumed per day': 'count'})
                    
                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))
                     
                     
                     
                     
                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)
                     
                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']
                     
                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']
                     
                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']
                     
                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']
                     
                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']
                     
                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']
                     
                 
                    st.markdown("**The estimated Watts consumed per day - Water Heater - Normal**")
                    st.write(df_ams)
                 
                     
                    #graph
                     
                    gwac=new.groupby('Governorate',as_index=True)[['Water Cooler - The estimated Watts consumed per day']].sum()
                    gwac.reset_index(inplace=True)
                     
                    gacs=new.groupby('Governorate',as_index=True)[['Water Heater - Central - The estimated Watts consumed per day']].sum()
                    gacs.reset_index(inplace=True)
                    
                    gams=new.groupby('Governorate',as_index=True)[['Water Heater - Normal - The estimated Watts consumed per day']].sum()
                    gams.reset_index(inplace=True)
                    
                   
                    
                    import plotly.express as px
                    st.markdown("**Figure 30. Distribution of The estimated Watts consumed per day (water equipment) under different Governorate**")
                    import plotly.graph_objects as go
                    fig3 = go.Figure(data=[
                        go.Bar(name='Water Cooler', x=gwac['Governorate'], y=gwac['Water Cooler - The estimated Watts consumed per day']),
                         go.Bar(name='Water Heater - Central', x=gacs['Governorate'], y=gacs['Water Heater - Central - The estimated Watts consumed per day']),
                         go.Bar(name='Water Heater - Norma', x=gams['Governorate'], y=gams['Water Heater - Normal - The estimated Watts consumed per day']),
                         
                    ])
                    # Change the bar mode
                    fig3.update_layout(barmode='group')
                    #fig.show()
                    
                    st.write(fig3)
                    
                    
                    
                    
                    
                    
                    
                    
                    st.markdown("**Figure 31. Comparison of The estimated Watts consumed per day (water equipment) under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='Water Cooler - The estimated Watts consumed per day', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='Water Heater - Central - The estimated Watts consumed per day', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='Water Heater - Normal - The estimated Watts consumed per day', color="Governorate")
                    
                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                    
            st.subheader("Analysis on Miscellaneous equipment")
            if st.checkbox("➡️ Analysis and statistics on Miscellaneous equipment"):
                
                st.markdown("**Units owned (Miscellaneous equipment)**")
                if st.checkbox("Table 36. Descriptive Statistics- Units owned (Miscellaneous equipment)"):


                    wac=new.groupby('Governorate')['#1 units owned - Clothes dryer  '].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Clothes dryer**")
                    st.table(wac)


                    acs=new.groupby('Governorate')['#1 units owned - Front loaded Clothes washer automatic  '].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Front loaded Clothes washer automatic**")
                    st.table(acs)

                    atm=new.groupby('Governorate')['#1 units owned - Top loaded Clothes washer automatic  '].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Top loaded Clothes washer automatic**")
                    st.table(atm)   

                    atw=new.groupby('Governorate')['#1 units owned - Clothes washer normal  '].describe()
                    atw.reset_index(inplace = True)
                    atw.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Clothes washer normal**")
                    st.table(atw)

                    atre=new.groupby('Governorate')['#1 units owned - Dish washer  '].describe()
                    atre.reset_index(inplace = True)
                    atre.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Dish washer**")
                    st.table(atre)

                    acook=new.groupby('Governorate')['#1 units owned - Freezer  '].describe()
                    acook.reset_index(inplace = True)
                    acook.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Freezer**")
                    st.table(acook)

                    ale=new.groupby('Governorate')['#1 units owned - Refrigerator  '].describe()
                    ale.reset_index(inplace = True)
                    ale.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**units owned - Refrigerator**")
                    st.table(ale)


                if st.checkbox("Table 37. Association of units owned of (Miscellaneous equipment)"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes dryer  ']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'units owned - Clothes dryer'},inplace=True)
                    td['units owned - Clothes dryer'] = td['units owned - Clothes dryer'].replace({'#1 units owned - Clothes dryer  ': 'Std'})

                    wacp=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes dryer  ']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)

                    wacp.rename(columns={'index':'units owned - Clothes dryer'},inplace=True)
                    wacp['units owned - Clothes dryer'] = wacp['units owned - Clothes dryer'].replace({'#1 units owned - Clothes dryer  ': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes dryer  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Clothes dryer'},inplace=True)
                    tang_m['units owned - Clothes dryer'] = tang_m['units owned - Clothes dryer'].replace({'#1 units owned - Clothes dryer  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes dryer  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Clothes dryer'},inplace=True)
                    tang_mx['units owned - Clothes dryer'] = tang_mx['units owned - Clothes dryer'].replace({'#1 units owned - Clothes dryer  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes dryer  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Clothes dryer'},inplace=True)
                    vc['units owned - Clothes dryer'] = vc['units owned - Clothes dryer'].replace({'#1 units owned - Clothes dryer  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)

                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']

                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']

                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']

                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']

                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']

                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Blender/mixer/food processor**")
                    st.write(df_atc)
                #2     
                    cs=new.groupby('Governorate',as_index=True)[['#1 units owned - Front loaded Clothes washer automatic  ']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'units owned - Front loaded Clothes washer automatic'},inplace=True)
                    cs['units owned - Front loaded Clothes washer automatic'] = cs['units owned - Front loaded Clothes washer automatic'].replace({'#1 units owned - Front loaded Clothes washer automatic  ': 'Std'})

                    acsp=new.groupby('Governorate',as_index=True)[['#1 units owned - Front loaded Clothes washer automatic  ']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)

                    acsp.rename(columns={'index':'units owned - Front loaded Clothes washer automatic'},inplace=True)
                    acsp['units owned - Front loaded Clothes washer automatic'] = acsp['units owned - Front loaded Clothes washer automatic'].replace({'#1 units owned - Front loaded Clothes washer automatic  ': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Front loaded Clothes washer automatic  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Front loaded Clothes washer automatic'},inplace=True)
                    tang_m['units owned - Front loaded Clothes washer automatic'] = tang_m['units owned - Front loaded Clothes washer automatic'].replace({'#1 units owned - Front loaded Clothes washer automatic  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Front loaded Clothes washer automatic  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Front loaded Clothes washer automatic'},inplace=True)
                    tang_mx['units owned - Front loaded Clothes washer automatic'] = tang_mx['units owned - Front loaded Clothes washer automatic'].replace({'#1 units owned - Front loaded Clothes washer automatic  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Front loaded Clothes washer automatic  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Front loaded Clothes washer automatic'},inplace=True)
                    vc['units owned - Front loaded Clothes washer automatic'] = vc['units owned - Front loaded Clothes washer automatic'].replace({'#1 units owned - Front loaded Clothes washer automatic  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)

                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']

                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']

                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']

                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']

                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']

                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Front loaded Clothes washer automatic**")
                    st.write(df_acs)
    #3
                    ms=new.groupby('Governorate',as_index=True)[['#1 units owned - Top loaded Clothes washer automatic  ']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'units owned - Top loaded Clothes washer automatic'},inplace=True)
                    ms['units owned - Top loaded Clothes washer automatic'] = ms['units owned - Top loaded Clothes washer automatic'].replace({'#1 units owned - Top loaded Clothes washer automatic  ': 'Std'})

                    atms=new.groupby('Governorate',as_index=True)[['#1 units owned - Top loaded Clothes washer automatic  ']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)

                    atms.rename(columns={'index':'units owned - Top loaded Clothes washer automatic'},inplace=True)
                    atms['units owned - Top loaded Clothes washer automatic'] = atms['units owned - Top loaded Clothes washer automatic'].replace({'#1 units owned - Top loaded Clothes washer automatic  ': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Top loaded Clothes washer automatic  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Top loaded Clothes washer automatic'},inplace=True)
                    tang_m['units owned - Top loaded Clothes washer automatic'] = tang_m['units owned - Top loaded Clothes washer automatic'].replace({'#1 units owned - Top loaded Clothes washer automatic  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Top loaded Clothes washer automatic  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Top loaded Clothes washer automatic'},inplace=True)
                    tang_mx['units owned - Top loaded Clothes washer automatic'] = tang_mx['units owned - Top loaded Clothes washer automatic'].replace({'#1 units owned - Top loaded Clothes washer automatic  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Top loaded Clothes washer automatic  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Top loaded Clothes washer automatic'},inplace=True)
                    vc['units owned - Top loaded Clothes washer automatic'] = vc['units owned - Top loaded Clothes washer automatic'].replace({'#1 units owned - Top loaded Clothes washer automatic  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)

                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']

                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']

                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']

                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']

                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']

                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Top loaded Clothes washer automatic**")
                    st.write(df_ams)
                 #4
                    uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes washer normal  ']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'units owned - Clothes washer normal'},inplace=True)
                    uw['units owned - Clothes washer normal'] = uw['units owned - Clothes washer normal'].replace({'#1 units owned - Clothes washer normal  ': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes washer normal  ']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'units owned - Clothes washer normal'},inplace=True)
                    acuw['units owned - Clothes washer normal'] = acuw['units owned - Clothes washer normal'].replace({'#1 units owned - Clothes washer normal  ': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes washer normal  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Clothes washer normal'},inplace=True)
                    tang_m['units owned - Clothes washer normal'] = tang_m['units owned - Clothes washer normal'].replace({'#1 units owned - Clothes washer normal  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes washer normal  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Clothes washer normal'},inplace=True)
                    tang_mx['units owned - Clothes washer normal'] = tang_mx['units owned - Clothes washer normal'].replace({'#1 units owned - Clothes washer normal  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes washer normal  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Clothes washer normal'},inplace=True)
                    vc['units owned - Clothes washer normal'] = vc['units owned - Clothes washer normal'].replace({'#1 units owned - Clothes washer normal  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)

                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']

                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']

                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']

                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']

                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']

                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Clothes washer normal**")
                    st.write(df_auw)
                  #5  

                    uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Dish washer  ']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'units owned - Dish washer'},inplace=True)
                    uw['units owned - Dish washer'] = uw['units owned - Dish washer'].replace({'#1 units owned - Dish washer  ': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Dish washer  ']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'units owned - Dish washer'},inplace=True)
                    acuw['units owned - Dish washer'] = acuw['units owned - Dish washer'].replace({'#1 units owned - Dish washer  ': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Dish washer  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Dish washer'},inplace=True)
                    tang_m['units owned - Dish washer'] = tang_m['units owned - Dish washer'].replace({'#1 units owned - Dish washer  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Dish washer  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Dish washer'},inplace=True)
                    tang_mx['units owned - Dish washer'] = tang_mx['units owned - Dish washer'].replace({'#1 units owned - Dish washer  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Dish washer  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Dish washer'},inplace=True)
                    vc['units owned - Dish washer'] = vc['units owned - Dish washer'].replace({'#1 units owned - Dish washer  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)

                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']

                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']

                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']

                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']

                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']

                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Dish washer**")
                    st.write(df_auw)

                  #6  

                    uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Freezer  ']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'units owned - Freezer'},inplace=True)
                    uw['units owned - Freezer'] = uw['units owned - Freezer'].replace({'#1 units owned - Freezer  ': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Freezer  ']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'units owned - Freezer'},inplace=True)
                    acuw['units owned - Freezer'] = acuw['units owned - Freezer'].replace({'#1 units owned - Freezer  ': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Freezer  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Freezer'},inplace=True)
                    tang_m['units owned - Freezer'] = tang_m['units owned - Freezer'].replace({'#1 units owned - Freezer  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Freezer  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Freezer'},inplace=True)
                    tang_mx['units owned - Freezer'] = tang_mx['units owned - Freezer'].replace({'#1 units owned - Freezer  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Freezer  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Freezer'},inplace=True)
                    vc['units owned - Freezer'] = vc['units owned - Freezer'].replace({'#1 units owned - Freezer  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_cokt = acuw.append(tang_mx)
                    df_cokt=df_cokt.reset_index(drop=True)

                    df_cokt['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cokt['Al-Ahmadi']
                    del df_cokt['Al-Ahmadi']

                    df_cokt['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cokt['Al-Asimah']
                    del df_cokt['Al-Asimah']

                    df_cokt['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cokt['Al-Farwaniyah']
                    del df_cokt['Al-Farwaniyah']

                    df_cokt['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cokt['Al-Jahra']
                    del df_cokt['Al-Jahra']

                    df_cokt['Hawally (N={})'.format(vc['Hawally'][0])]=df_cokt['Hawally']
                    del df_cokt['Hawally']

                    df_cokt['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cokt['Mubarak Al-Kabeer']
                    del df_cokt['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Freezer**")
                    st.write(df_cokt)
    #7
                    uw=new.groupby('Governorate',as_index=True)[['#1 units owned - Refrigerator  ']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'units owned - Refrigerator'},inplace=True)
                    uw['units owned - Refrigerator'] = uw['units owned - Refrigerator'].replace({'#1 units owned - Refrigerator  ': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['#1 units owned - Refrigerator  ']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'units owned - Refrigerator'},inplace=True)
                    acuw['units owned - Refrigerator'] = acuw['units owned - Refrigerator'].replace({'#1 units owned - Refrigerator  ': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#1 units owned - Refrigerator  ']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'units owned - Refrigerator'},inplace=True)
                    tang_m['units owned - Refrigerator'] = tang_m['units owned - Refrigerator'].replace({'#1 units owned - Refrigerator  ': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#1 units owned - Refrigerator  ']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'units owned - Refrigerator'},inplace=True)
                    tang_mx['units owned - Refrigerator'] = tang_mx['units owned - Refrigerator'].replace({'#1 units owned - Refrigerator  ': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#1 units owned - Refrigerator  ']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'units owned - Refrigerator'},inplace=True)
                    vc['units owned - Refrigerator'] = vc['units owned - Refrigerator'].replace({'#1 units owned - Refrigerator  ': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_lpg = acuw.append(tang_mx)
                    df_lpg=df_lpg.reset_index(drop=True)

                    df_lpg['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_lpg['Al-Ahmadi']
                    del df_lpg['Al-Ahmadi']

                    df_lpg['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_lpg['Al-Asimah']
                    del df_lpg['Al-Asimah']

                    df_lpg['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_lpg['Al-Farwaniyah']
                    del df_lpg['Al-Farwaniyah']

                    df_lpg['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_lpg['Al-Jahra']
                    del df_lpg['Al-Jahra']

                    df_lpg['Hawally (N={})'.format(vc['Hawally'][0])]=df_lpg['Hawally']
                    del df_lpg['Hawally']

                    df_lpg['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_lpg['Mubarak Al-Kabeer']
                    del df_lpg['Mubarak Al-Kabeer']


                    st.markdown("**units owned - Refrigerator**")
                    st.write(df_lpg)









                    #graph

                    gwac=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes dryer  ']].sum()
                    gwac.reset_index(inplace=True)

                    gacs=new.groupby('Governorate',as_index=True)[['#1 units owned - Front loaded Clothes washer automatic  ']].sum()
                    gacs.reset_index(inplace=True)

                    gams=new.groupby('Governorate',as_index=True)[['#1 units owned - Top loaded Clothes washer automatic  ']].sum()
                    gams.reset_index(inplace=True)

                    gauw=new.groupby('Governorate',as_index=True)[['#1 units owned - Clothes washer normal  ']].sum()
                    gauw.reset_index(inplace=True)

                    gact=new.groupby('Governorate',as_index=True)[['#1 units owned - Dish washer  ']].sum()
                    gact.reset_index(inplace=True)

                    gael=new.groupby('Governorate',as_index=True)[['#1 units owned - Freezer  ']].sum()
                    gael.reset_index(inplace=True)

                    gaoel=new.groupby('Governorate',as_index=True)[['#1 units owned - Refrigerator  ']].sum()
                    gaoel.reset_index(inplace=True)

                    


                    import plotly.express as px
                    st.markdown("**Figure 32. Distribution of Units owned (Miscellaneous equipment) under different Governorate**")
                    import plotly.graph_objects as go
                    fig3 = go.Figure(data=[
                        go.Bar(name='Clothes dryer', x=gwac['Governorate'], y=gwac['#1 units owned - Clothes dryer  ']),
                         go.Bar(name='Front loaded Clothes washer automatic', x=gacs['Governorate'], y=gacs['#1 units owned - Front loaded Clothes washer automatic  ']),
                         go.Bar(name='Top loaded Clothes washer automatic', x=gams['Governorate'], y=gams['#1 units owned - Top loaded Clothes washer automatic  ']),
                         go.Bar(name='Clothes washer normal', x=gauw['Governorate'], y=gauw['#1 units owned - Clothes washer normal  ']),
                        go.Bar(name='Dish washer', x=gact['Governorate'], y=gact['#1 units owned - Dish washer  ']),
                        go.Bar(name='Freezer', x=gael['Governorate'], y=gael['#1 units owned - Freezer  ']),
                        go.Bar(name='Refrigerator', x=gaoel['Governorate'], y=gaoel['#1 units owned - Refrigerator  ']),

                    ])
                    # Change the bar mode
                    fig3.update_layout(barmode='group')
                    #fig.show()

                    st.write(fig3)

                    st.markdown("**Figure 33. Comparison of Units owned (Miscellaneous equipment) under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#1 units owned - Clothes dryer  ', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='#1 units owned - Front loaded Clothes washer automatic  ', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='#1 units owned - Top loaded Clothes washer automatic  ', color="Governorate")
                    fig21= px.bar(gauw, x="Governorate", y='#1 units owned - Clothes washer normal  ', color="Governorate")
                    fig22= px.bar(gact, x="Governorate", y='#1 units owned - Dish washer  ', color="Governorate")
                    fig23= px.bar(gael, x="Governorate", y='#1 units owned - Freezer  ', color="Governorate")
                    fig24= px.bar(gaoel, x="Governorate", y='#1 units owned - Refrigerator  ', color="Governorate")

                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                    st.write(fig21)
                    st.write(fig22)
                    st.write(fig23)
                    st.write(fig24)
                
                #no of time
                st.markdown("**No of times appliance used in a week (Miscellaneous equipment)**")
                if st.checkbox("Table 38. Descriptive Statistics- No of times appliance used in a week (Miscellaneous equipment)"):


                    wac=new.groupby('Governorate')['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**No of times appliance used in a week - Clothes dryer**")
                    st.table(wac)


                    acs=new.groupby('Governorate')['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic'].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**No of times appliance used in a week - Front loaded Clothes washer automatic**")
                    st.table(acs)

                    atm=new.groupby('Governorate')['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**No of times appliance used in a week - Top loaded Clothes washer automatic**")
                    st.table(atm)   

                    atw=new.groupby('Governorate')['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal'].describe()
                    atw.reset_index(inplace = True)
                    atw.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**No of times appliance used in a week - Clothes washer normal**")
                    st.table(atw)

                    atre=new.groupby('Governorate')['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer'].describe()
                    atre.reset_index(inplace = True)
                    atre.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**No of times appliance used in a week - Dish washer**")
                    st.table(atre)

                    


                if st.checkbox("Table 39. Association of No of times appliance used in a week of (Miscellaneous equipment)"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'No of times appliance used in a week - Clothes dryer'},inplace=True)
                    td['No of times appliance used in a week - Clothes dryer'] = td['No of times appliance used in a week - Clothes dryer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer': 'Std'})

                    wacp=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)

                    wacp.rename(columns={'index':'No of times appliance used in a week - Clothes dryer'},inplace=True)
                    wacp['No of times appliance used in a week - Clothes dryer'] = wacp['No of times appliance used in a week - Clothes dryer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'No of times appliance used in a week - Clothes dryer'},inplace=True)
                    tang_m['No of times appliance used in a week - Clothes dryer'] = tang_m['No of times appliance used in a week - Clothes dryer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'No of times appliance used in a week - Clothes dryer'},inplace=True)
                    tang_mx['No of times appliance used in a week - Clothes dryer'] = tang_mx['No of times appliance used in a week - Clothes dryer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'No of times appliance used in a week - Clothes dryer'},inplace=True)
                    vc['No of times appliance used in a week - Clothes dryer'] = vc['No of times appliance used in a week - Clothes dryer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)

                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']

                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']

                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']

                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']

                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']

                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']


                    st.markdown("**No of times appliance used in a week - Blender/mixer/food processor**")
                    st.write(df_atc)
                #2     
                    cs=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'No of times appliance used in a week - Front loaded Clothes washer automatic'},inplace=True)
                    cs['No of times appliance used in a week - Front loaded Clothes washer automatic'] = cs['No of times appliance used in a week - Front loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic': 'Std'})

                    acsp=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)

                    acsp.rename(columns={'index':'No of times appliance used in a week - Front loaded Clothes washer automatic'},inplace=True)
                    acsp['No of times appliance used in a week - Front loaded Clothes washer automatic'] = acsp['No of times appliance used in a week - Front loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'No of times appliance used in a week - Front loaded Clothes washer automatic'},inplace=True)
                    tang_m['No of times appliance used in a week - Front loaded Clothes washer automatic'] = tang_m['No of times appliance used in a week - Front loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'No of times appliance used in a week - Front loaded Clothes washer automatic'},inplace=True)
                    tang_mx['No of times appliance used in a week - Front loaded Clothes washer automatic'] = tang_mx['No of times appliance used in a week - Front loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'No of times appliance used in a week - Front loaded Clothes washer automatic'},inplace=True)
                    vc['No of times appliance used in a week - Front loaded Clothes washer automatic'] = vc['No of times appliance used in a week - Front loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)

                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']

                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']

                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']

                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']

                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']

                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']


                    st.markdown("**No of times appliance used in a week - Front loaded Clothes washer automatic**")
                    st.write(df_acs)
    #3
                    ms=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'No of times appliance used in a week - Top loaded Clothes washer automatic'},inplace=True)
                    ms['No of times appliance used in a week - Top loaded Clothes washer automatic'] = ms['No of times appliance used in a week - Top loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic': 'Std'})

                    atms=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)

                    atms.rename(columns={'index':'No of times appliance used in a week - Top loaded Clothes washer automatic'},inplace=True)
                    atms['No of times appliance used in a week - Top loaded Clothes washer automatic'] = atms['No of times appliance used in a week - Top loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'No of times appliance used in a week - Top loaded Clothes washer automatic'},inplace=True)
                    tang_m['No of times appliance used in a week - Top loaded Clothes washer automatic'] = tang_m['No of times appliance used in a week - Top loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'No of times appliance used in a week - Top loaded Clothes washer automatic'},inplace=True)
                    tang_mx['No of times appliance used in a week - Top loaded Clothes washer automatic'] = tang_mx['No of times appliance used in a week - Top loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'No of times appliance used in a week - Top loaded Clothes washer automatic'},inplace=True)
                    vc['No of times appliance used in a week - Top loaded Clothes washer automatic'] = vc['No of times appliance used in a week - Top loaded Clothes washer automatic'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)

                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']

                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']

                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']

                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']

                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']

                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']


                    st.markdown("**No of times appliance used in a week - Top loaded Clothes washer automatic**")
                    st.write(df_ams)
                 #4
                    uw=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'No of times appliance used in a week - Clothes washer normal'},inplace=True)
                    uw['No of times appliance used in a week - Clothes washer normal'] = uw['No of times appliance used in a week - Clothes washer normal'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'No of times appliance used in a week - Clothes washer normal'},inplace=True)
                    acuw['No of times appliance used in a week - Clothes washer normal'] = acuw['No of times appliance used in a week - Clothes washer normal'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'No of times appliance used in a week - Clothes washer normal'},inplace=True)
                    tang_m['No of times appliance used in a week - Clothes washer normal'] = tang_m['No of times appliance used in a week - Clothes washer normal'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'No of times appliance used in a week - Clothes washer normal'},inplace=True)
                    tang_mx['No of times appliance used in a week - Clothes washer normal'] = tang_mx['No of times appliance used in a week - Clothes washer normal'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'No of times appliance used in a week - Clothes washer normal'},inplace=True)
                    vc['No of times appliance used in a week - Clothes washer normal'] = vc['No of times appliance used in a week - Clothes washer normal'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)

                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']

                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']

                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']

                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']

                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']

                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']


                    st.markdown("**No of times appliance used in a week - Clothes washer normal**")
                    st.write(df_auw)
                  #5  

                    uw=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'No of times appliance used in a week - Dish washer'},inplace=True)
                    uw['No of times appliance used in a week - Dish washer'] = uw['No of times appliance used in a week - Dish washer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'No of times appliance used in a week - Dish washer'},inplace=True)
                    acuw['No of times appliance used in a week - Dish washer'] = acuw['No of times appliance used in a week - Dish washer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'No of times appliance used in a week - Dish washer'},inplace=True)
                    tang_m['No of times appliance used in a week - Dish washer'] = tang_m['No of times appliance used in a week - Dish washer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'No of times appliance used in a week - Dish washer'},inplace=True)
                    tang_mx['No of times appliance used in a week - Dish washer'] = tang_mx['No of times appliance used in a week - Dish washer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'No of times appliance used in a week - Dish washer'},inplace=True)
                    vc['No of times appliance used in a week - Dish washer'] = vc['No of times appliance used in a week - Dish washer'].replace({'#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)

                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']

                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']

                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']

                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']

                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']

                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']


                    st.markdown("**No of times appliance used in a week - Dish washer**")
                    st.write(df_auw)


                    #graph

                    gwac=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']].sum()
                    gwac.reset_index(inplace=True)

                    gacs=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']].sum()
                    gacs.reset_index(inplace=True)

                    gams=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']].sum()
                    gams.reset_index(inplace=True)

                    gauw=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']].sum()
                    gauw.reset_index(inplace=True)

                    gact=new.groupby('Governorate',as_index=True)[['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']].sum()
                    gact.reset_index(inplace=True)

                    


                    import plotly.express as px
                    st.markdown("**Figure 34. Distribution of No of times appliance used in a week (Miscellaneous equipment) under different Governorate**")
                    import plotly.graph_objects as go
                    fig3 = go.Figure(data=[
                        go.Bar(name='Clothes dryer', x=gwac['Governorate'], y=gwac['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer']),
                         go.Bar(name='Front loaded Clothes washer automatic', x=gacs['Governorate'], y=gacs['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic']),
                         go.Bar(name='Top loaded Clothes washer automatic', x=gams['Governorate'], y=gams['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic']),
                         go.Bar(name='Clothes washer normal', x=gauw['Governorate'], y=gauw['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal']),
                        go.Bar(name='Dish washer', x=gact['Governorate'], y=gact['#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer']),
                        

                    ])
                    # Change the bar mode
                    fig3.update_layout(barmode='stack')
                    #fig.show()

                    st.write(fig3)

                    st.markdown("**Figure 35. Comparison of No of times appliance used (Miscellaneous equipment) under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes dryer', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Front loaded Clothes washer automatic', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Top loaded Clothes washer automatic', color="Governorate")
                    fig21= px.bar(gauw, x="Governorate", y='#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Clothes washer normal', color="Governorate")
                    fig22= px.bar(gact, x="Governorate", y='#2 How many times do you use this appliance in a week? (5 times, 6 times or daily) - Dish washer', color="Governorate")
                   

                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                    st.write(fig21)
                    st.write(fig22)
                #watts final
                st.markdown("**Watts consumed (Miscellaneous equipment)**")
                if st.checkbox("Table 40. Descriptive Statistics- Watts consumed (Miscellaneous equipment)"):


                    wac=new.groupby('Governorate')['Clothes dryer - The estimated Watts consumed per day'].describe()
                    wac.reset_index(inplace = True)
                    wac.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Clothes dryer**")
                    st.table(wac)


                    acs=new.groupby('Governorate')['Front loaded Clothes washer automatic - The estimated Watts consumed per day'].describe()
                    acs.reset_index(inplace = True)
                    acs.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Front loaded Clothes washer automatic**")
                    st.table(acs)

                    atm=new.groupby('Governorate')['Top loaded Clothes washer automatic - The estimated Watts consumed per day'].describe()
                    atm.reset_index(inplace = True)
                    atm.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Top loaded Clothes washer automatic**")
                    st.table(atm)   

                    atw=new.groupby('Governorate')['Clothes washer normal - The estimated Watts consumed per day'].describe()
                    atw.reset_index(inplace = True)
                    atw.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Clothes washer normal**")
                    st.table(atw)

                    atre=new.groupby('Governorate')['Dish washer - The estimated Watts consumed per day'].describe()
                    atre.reset_index(inplace = True)
                    atre.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Dish washer**")
                    st.table(atre)

                    acook=new.groupby('Governorate')['Freezer - The estimated Watts consumed per day'].describe()
                    acook.reset_index(inplace = True)
                    acook.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Freezer**")
                    st.table(acook)

                    ale=new.groupby('Governorate')['Refrigerator - The estimated Watts consumed per day'].describe()
                    ale.reset_index(inplace = True)
                    ale.rename(columns={'index':'Governorate'},inplace=True)
                    st.markdown("**Watts consumed - Refrigerator**")
                    st.table(ale)


                if st.checkbox("Table 41. Association of Watts consumed of (Miscellaneous equipment)"):
                    #1   
                    td=new.groupby('Governorate',as_index=True)[['Clothes dryer - The estimated Watts consumed per day']].std()
                    td=td.T
                    td.reset_index(inplace=True)
                    td.rename(columns={'index':'Watts consumed - Clothes dryer'},inplace=True)
                    td['Watts consumed - Clothes dryer'] = td['Watts consumed - Clothes dryer'].replace({'Clothes dryer - The estimated Watts consumed per day': 'Std'})

                    wacp=new.groupby('Governorate',as_index=True)[['Clothes dryer - The estimated Watts consumed per day']].mean()
                    wacp=wacp.T
                    wacp.reset_index(inplace = True)

                    wacp.rename(columns={'index':'Watts consumed - Clothes dryer'},inplace=True)
                    wacp['Watts consumed - Clothes dryer'] = wacp['Watts consumed - Clothes dryer'].replace({'Clothes dryer - The estimated Watts consumed per day': 'Mean(SD)'})
                    wacp['Al-Ahmadi']=wacp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(td['Al-Ahmadi'][0].round(2))
                    wacp['Al-Asimah']=wacp['Al-Asimah'].round(2).astype(str)+'({})'.format(td['Al-Asimah'][0].round(2))
                    wacp['Al-Farwaniyah']=wacp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(td['Al-Farwaniyah'][0].round(2))
                    wacp['Al-Jahra']=wacp['Al-Jahra'].round(2).astype(str)+'({})'.format(td['Al-Jahra'][0].round(2))
                    wacp['Hawally']=wacp['Hawally'].round(2).astype(str)+'({})'.format(td['Hawally'][0].round(2))
                    wacp['Mubarak Al-Kabeer']=wacp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(td['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Clothes dryer - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Clothes dryer'},inplace=True)
                    tang_m['Watts consumed - Clothes dryer'] = tang_m['Watts consumed - Clothes dryer'].replace({'Clothes dryer - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Clothes dryer - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Clothes dryer'},inplace=True)
                    tang_mx['Watts consumed - Clothes dryer'] = tang_mx['Watts consumed - Clothes dryer'].replace({'Clothes dryer - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Clothes dryer - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Clothes dryer'},inplace=True)
                    vc['Watts consumed - Clothes dryer'] = vc['Watts consumed - Clothes dryer'].replace({'Clothes dryer - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_atc = wacp.append(tang_mx)
                    df_atc=df_atc.reset_index(drop=True)

                    df_atc['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_atc['Al-Ahmadi']
                    del df_atc['Al-Ahmadi']

                    df_atc['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_atc['Al-Asimah']
                    del df_atc['Al-Asimah']

                    df_atc['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_atc['Al-Farwaniyah']
                    del df_atc['Al-Farwaniyah']

                    df_atc['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_atc['Al-Jahra']
                    del df_atc['Al-Jahra']

                    df_atc['Hawally (N={})'.format(vc['Hawally'][0])]=df_atc['Hawally']
                    del df_atc['Hawally']

                    df_atc['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_atc['Mubarak Al-Kabeer']
                    del df_atc['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Blender/mixer/food processor**")
                    st.write(df_atc)
                #2     
                    cs=new.groupby('Governorate',as_index=True)[['Front loaded Clothes washer automatic - The estimated Watts consumed per day']].std()
                    cs=cs.T
                    cs.reset_index(inplace=True)
                    cs.rename(columns={'index':'Watts consumed - Front loaded Clothes washer automatic'},inplace=True)
                    cs['Watts consumed - Front loaded Clothes washer automatic'] = cs['Watts consumed - Front loaded Clothes washer automatic'].replace({'Front loaded Clothes washer automatic - The estimated Watts consumed per day': 'Std'})

                    acsp=new.groupby('Governorate',as_index=True)[['Front loaded Clothes washer automatic - The estimated Watts consumed per day']].mean()
                    acsp=acsp.T
                    acsp.reset_index(inplace = True)

                    acsp.rename(columns={'index':'Watts consumed - Front loaded Clothes washer automatic'},inplace=True)
                    acsp['Watts consumed - Front loaded Clothes washer automatic'] = acsp['Watts consumed - Front loaded Clothes washer automatic'].replace({'Front loaded Clothes washer automatic - The estimated Watts consumed per day': 'Mean(SD)'})
                    acsp['Al-Ahmadi']=acsp['Al-Ahmadi'].round(2).astype(str)+'({})'.format(cs['Al-Ahmadi'][0].round(2))
                    acsp['Al-Asimah']=acsp['Al-Asimah'].round(2).astype(str)+'({})'.format(cs['Al-Asimah'][0].round(2))
                    acsp['Al-Farwaniyah']=acsp['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(cs['Al-Farwaniyah'][0].round(2))
                    acsp['Al-Jahra']=acsp['Al-Jahra'].round(2).astype(str)+'({})'.format(cs['Al-Jahra'][0].round(2))
                    acsp['Hawally']=acsp['Hawally'].round(2).astype(str)+'({})'.format(cs['Hawally'][0].round(2))
                    acsp['Mubarak Al-Kabeer']=acsp['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(cs['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Front loaded Clothes washer automatic - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Front loaded Clothes washer automatic'},inplace=True)
                    tang_m['Watts consumed - Front loaded Clothes washer automatic'] = tang_m['Watts consumed - Front loaded Clothes washer automatic'].replace({'Front loaded Clothes washer automatic - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Front loaded Clothes washer automatic - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Front loaded Clothes washer automatic'},inplace=True)
                    tang_mx['Watts consumed - Front loaded Clothes washer automatic'] = tang_mx['Watts consumed - Front loaded Clothes washer automatic'].replace({'Front loaded Clothes washer automatic - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Front loaded Clothes washer automatic - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Front loaded Clothes washer automatic'},inplace=True)
                    vc['Watts consumed - Front loaded Clothes washer automatic'] = vc['Watts consumed - Front loaded Clothes washer automatic'].replace({'Front loaded Clothes washer automatic - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_acs = acsp.append(tang_mx)
                    df_acs=df_acs.reset_index(drop=True)

                    df_acs['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_acs['Al-Ahmadi']
                    del df_acs['Al-Ahmadi']

                    df_acs['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_acs['Al-Asimah']
                    del df_acs['Al-Asimah']

                    df_acs['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_acs['Al-Farwaniyah']
                    del df_acs['Al-Farwaniyah']

                    df_acs['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_acs['Al-Jahra']
                    del df_acs['Al-Jahra']

                    df_acs['Hawally (N={})'.format(vc['Hawally'][0])]=df_acs['Hawally']
                    del df_acs['Hawally']

                    df_acs['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_acs['Mubarak Al-Kabeer']
                    del df_acs['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Front loaded Clothes washer automatic**")
                    st.write(df_acs)
    #3
                    ms=new.groupby('Governorate',as_index=True)[['Top loaded Clothes washer automatic - The estimated Watts consumed per day']].std()
                    ms=ms.T
                    ms.reset_index(inplace=True)
                    ms.rename(columns={'index':'Watts consumed - Top loaded Clothes washer automatic'},inplace=True)
                    ms['Watts consumed - Top loaded Clothes washer automatic'] = ms['Watts consumed - Top loaded Clothes washer automatic'].replace({'Top loaded Clothes washer automatic - The estimated Watts consumed per day': 'Std'})

                    atms=new.groupby('Governorate',as_index=True)[['Top loaded Clothes washer automatic - The estimated Watts consumed per day']].mean()
                    atms=atms.T
                    atms.reset_index(inplace = True)

                    atms.rename(columns={'index':'Watts consumed - Top loaded Clothes washer automatic'},inplace=True)
                    atms['Watts consumed - Top loaded Clothes washer automatic'] = atms['Watts consumed - Top loaded Clothes washer automatic'].replace({'Top loaded Clothes washer automatic - The estimated Watts consumed per day': 'Mean(SD)'})
                    atms['Al-Ahmadi']=atms['Al-Ahmadi'].round(2).astype(str)+'({})'.format(ms['Al-Ahmadi'][0].round(2))
                    atms['Al-Asimah']=atms['Al-Asimah'].round(2).astype(str)+'({})'.format(ms['Al-Asimah'][0].round(2))
                    atms['Al-Farwaniyah']=atms['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(ms['Al-Farwaniyah'][0].round(2))
                    atms['Al-Jahra']=atms['Al-Jahra'].round(2).astype(str)+'({})'.format(ms['Al-Jahra'][0].round(2))
                    atms['Hawally']=atms['Hawally'].round(2).astype(str)+'({})'.format(ms['Hawally'][0].round(2))
                    atms['Mubarak Al-Kabeer']=atms['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(ms['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Top loaded Clothes washer automatic - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Top loaded Clothes washer automatic'},inplace=True)
                    tang_m['Watts consumed - Top loaded Clothes washer automatic'] = tang_m['Watts consumed - Top loaded Clothes washer automatic'].replace({'Top loaded Clothes washer automatic - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Top loaded Clothes washer automatic - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Top loaded Clothes washer automatic'},inplace=True)
                    tang_mx['Watts consumed - Top loaded Clothes washer automatic'] = tang_mx['Watts consumed - Top loaded Clothes washer automatic'].replace({'Top loaded Clothes washer automatic - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Top loaded Clothes washer automatic - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Top loaded Clothes washer automatic'},inplace=True)
                    vc['Watts consumed - Top loaded Clothes washer automatic'] = vc['Watts consumed - Top loaded Clothes washer automatic'].replace({'Top loaded Clothes washer automatic - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_ams = atms.append(tang_mx)
                    df_ams=df_ams.reset_index(drop=True)

                    df_ams['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_ams['Al-Ahmadi']
                    del df_ams['Al-Ahmadi']

                    df_ams['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_ams['Al-Asimah']
                    del df_ams['Al-Asimah']

                    df_ams['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_ams['Al-Farwaniyah']
                    del df_ams['Al-Farwaniyah']

                    df_ams['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_ams['Al-Jahra']
                    del df_ams['Al-Jahra']

                    df_ams['Hawally (N={})'.format(vc['Hawally'][0])]=df_ams['Hawally']
                    del df_ams['Hawally']

                    df_ams['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_ams['Mubarak Al-Kabeer']
                    del df_ams['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Top loaded Clothes washer automatic**")
                    st.write(df_ams)
                 #4
                    uw=new.groupby('Governorate',as_index=True)[['Clothes washer normal - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Clothes washer normal'},inplace=True)
                    uw['Watts consumed - Clothes washer normal'] = uw['Watts consumed - Clothes washer normal'].replace({'Clothes washer normal - The estimated Watts consumed per day': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['Clothes washer normal - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'Watts consumed - Clothes washer normal'},inplace=True)
                    acuw['Watts consumed - Clothes washer normal'] = acuw['Watts consumed - Clothes washer normal'].replace({'Clothes washer normal - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Clothes washer normal - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Clothes washer normal'},inplace=True)
                    tang_m['Watts consumed - Clothes washer normal'] = tang_m['Watts consumed - Clothes washer normal'].replace({'Clothes washer normal - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Clothes washer normal - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Clothes washer normal'},inplace=True)
                    tang_mx['Watts consumed - Clothes washer normal'] = tang_mx['Watts consumed - Clothes washer normal'].replace({'Clothes washer normal - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Clothes washer normal - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Clothes washer normal'},inplace=True)
                    vc['Watts consumed - Clothes washer normal'] = vc['Watts consumed - Clothes washer normal'].replace({'Clothes washer normal - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)

                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']

                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']

                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']

                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']

                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']

                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Clothes washer normal**")
                    st.write(df_auw)
                  #5  

                    uw=new.groupby('Governorate',as_index=True)[['Dish washer - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Dish washer'},inplace=True)
                    uw['Watts consumed - Dish washer'] = uw['Watts consumed - Dish washer'].replace({'Dish washer - The estimated Watts consumed per day': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['Dish washer - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'Watts consumed - Dish washer'},inplace=True)
                    acuw['Watts consumed - Dish washer'] = acuw['Watts consumed - Dish washer'].replace({'Dish washer - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Dish washer - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Dish washer'},inplace=True)
                    tang_m['Watts consumed - Dish washer'] = tang_m['Watts consumed - Dish washer'].replace({'Dish washer - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Dish washer - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Dish washer'},inplace=True)
                    tang_mx['Watts consumed - Dish washer'] = tang_mx['Watts consumed - Dish washer'].replace({'Dish washer - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Dish washer - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Dish washer'},inplace=True)
                    vc['Watts consumed - Dish washer'] = vc['Watts consumed - Dish washer'].replace({'Dish washer - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_auw = acuw.append(tang_mx)
                    df_auw=df_auw.reset_index(drop=True)

                    df_auw['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_auw['Al-Ahmadi']
                    del df_auw['Al-Ahmadi']

                    df_auw['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_auw['Al-Asimah']
                    del df_auw['Al-Asimah']

                    df_auw['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_auw['Al-Farwaniyah']
                    del df_auw['Al-Farwaniyah']

                    df_auw['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_auw['Al-Jahra']
                    del df_auw['Al-Jahra']

                    df_auw['Hawally (N={})'.format(vc['Hawally'][0])]=df_auw['Hawally']
                    del df_auw['Hawally']

                    df_auw['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_auw['Mubarak Al-Kabeer']
                    del df_auw['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Dish washer**")
                    st.write(df_auw)

                  #6  

                    uw=new.groupby('Governorate',as_index=True)[['Freezer - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Freezer'},inplace=True)
                    uw['Watts consumed - Freezer'] = uw['Watts consumed - Freezer'].replace({'Freezer - The estimated Watts consumed per day': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['Freezer - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'Watts consumed - Freezer'},inplace=True)
                    acuw['Watts consumed - Freezer'] = acuw['Watts consumed - Freezer'].replace({'Freezer - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Freezer - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Freezer'},inplace=True)
                    tang_m['Watts consumed - Freezer'] = tang_m['Watts consumed - Freezer'].replace({'Freezer - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Freezer - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Freezer'},inplace=True)
                    tang_mx['Watts consumed - Freezer'] = tang_mx['Watts consumed - Freezer'].replace({'Freezer - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Freezer - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Freezer'},inplace=True)
                    vc['Watts consumed - Freezer'] = vc['Watts consumed - Freezer'].replace({'Freezer - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_cokt = acuw.append(tang_mx)
                    df_cokt=df_cokt.reset_index(drop=True)

                    df_cokt['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_cokt['Al-Ahmadi']
                    del df_cokt['Al-Ahmadi']

                    df_cokt['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_cokt['Al-Asimah']
                    del df_cokt['Al-Asimah']

                    df_cokt['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_cokt['Al-Farwaniyah']
                    del df_cokt['Al-Farwaniyah']

                    df_cokt['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_cokt['Al-Jahra']
                    del df_cokt['Al-Jahra']

                    df_cokt['Hawally (N={})'.format(vc['Hawally'][0])]=df_cokt['Hawally']
                    del df_cokt['Hawally']

                    df_cokt['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_cokt['Mubarak Al-Kabeer']
                    del df_cokt['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Freezer**")
                    st.write(df_cokt)
    #7
                    uw=new.groupby('Governorate',as_index=True)[['Refrigerator - The estimated Watts consumed per day']].std()
                    uw=uw.T
                    uw.reset_index(inplace=True)
                    uw.rename(columns={'index':'Watts consumed - Refrigerator'},inplace=True)
                    uw['Watts consumed - Refrigerator'] = uw['Watts consumed - Refrigerator'].replace({'Refrigerator - The estimated Watts consumed per day': 'Std'})

                    acuw=new.groupby('Governorate',as_index=True)[['Refrigerator - The estimated Watts consumed per day']].mean()
                    acuw=acuw.T
                    acuw.reset_index(inplace = True)

                    acuw.rename(columns={'index':'Watts consumed - Refrigerator'},inplace=True)
                    acuw['Watts consumed - Refrigerator'] = acuw['Watts consumed - Refrigerator'].replace({'Refrigerator - The estimated Watts consumed per day': 'Mean(SD)'})
                    acuw['Al-Ahmadi']=acuw['Al-Ahmadi'].round(2).astype(str)+'({})'.format(uw['Al-Ahmadi'][0].round(2))
                    acuw['Al-Asimah']=acuw['Al-Asimah'].round(2).astype(str)+'({})'.format(uw['Al-Asimah'][0].round(2))
                    acuw['Al-Farwaniyah']=acuw['Al-Farwaniyah'].round(2).astype(str)+'({})'.format(uw['Al-Farwaniyah'][0].round(2))
                    acuw['Al-Jahra']=acuw['Al-Jahra'].round(2).astype(str)+'({})'.format(uw['Al-Jahra'][0].round(2))
                    acuw['Hawally']=acuw['Hawally'].round(2).astype(str)+'({})'.format(uw['Hawally'][0].round(2))
                    acuw['Mubarak Al-Kabeer']=acuw['Mubarak Al-Kabeer'].round(2).astype(str)+'({})'.format(uw['Mubarak Al-Kabeer'][0].round(2))




                    tang_m=new.groupby('Governorate',as_index=True)[['Refrigerator - The estimated Watts consumed per day']].min()
                    tang_m=tang_m.T

                    tang_m.reset_index(inplace=True)
                    tang_m.rename(columns={'index':'Watts consumed - Refrigerator'},inplace=True)
                    tang_m['Watts consumed - Refrigerator'] = tang_m['Watts consumed - Refrigerator'].replace({'Refrigerator - The estimated Watts consumed per day': 'min'})

                    tang_mx=new.groupby('Governorate',as_index=True)[['Refrigerator - The estimated Watts consumed per day']].max()
                    tang_mx=tang_mx.T
                    tang_mx.reset_index(inplace=True)
                    tang_mx.rename(columns={'index':'Watts consumed - Refrigerator'},inplace=True)
                    tang_mx['Watts consumed - Refrigerator'] = tang_mx['Watts consumed - Refrigerator'].replace({'Refrigerator - The estimated Watts consumed per day': 'Range'})

                    vc=new.groupby('Governorate',as_index=True)[['Refrigerator - The estimated Watts consumed per day']].count()
                    vc=vc.T
                    vc.reset_index(inplace=True)
                    vc.rename(columns={'index':'Watts consumed - Refrigerator'},inplace=True)
                    vc['Watts consumed - Refrigerator'] = vc['Watts consumed - Refrigerator'].replace({'Refrigerator - The estimated Watts consumed per day': 'count'})

                    tang_mx['Al-Ahmadi']=tang_m['Al-Ahmadi'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Ahmadi'][0].round(2))
                    tang_mx['Al-Asimah']=tang_m['Al-Asimah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Asimah'][0].round(2))
                    tang_mx['Al-Farwaniyah']=tang_m['Al-Farwaniyah'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Farwaniyah'][0].round(2))
                    tang_mx['Al-Jahra']=tang_m['Al-Jahra'].round(2).astype(str)+' - {}'.format(tang_mx['Al-Jahra'][0].round(2))
                    tang_mx['Hawally']=tang_m['Hawally'].round(2).astype(str)+' - {}'.format(tang_mx['Hawally'][0].round(2))
                    tang_mx['Mubarak Al-Kabeer']=tang_m['Mubarak Al-Kabeer'].round(2).astype(str)+' - {}'.format(tang_mx['Mubarak Al-Kabeer'][0].round(2))




                    df_lpg = acuw.append(tang_mx)
                    df_lpg=df_lpg.reset_index(drop=True)

                    df_lpg['Al-Ahmadi (N={})'.format(vc['Al-Ahmadi'][0])]=df_lpg['Al-Ahmadi']
                    del df_lpg['Al-Ahmadi']

                    df_lpg['Al-Asimah (N={})'.format(vc['Al-Asimah'][0])]=df_lpg['Al-Asimah']
                    del df_lpg['Al-Asimah']

                    df_lpg['Al-Farwaniyah (N={})'.format(vc['Al-Farwaniyah'][0])]=df_lpg['Al-Farwaniyah']
                    del df_lpg['Al-Farwaniyah']

                    df_lpg['Al-Jahra (N={})'.format(vc['Al-Jahra'][0])]=df_lpg['Al-Jahra']
                    del df_lpg['Al-Jahra']

                    df_lpg['Hawally (N={})'.format(vc['Hawally'][0])]=df_lpg['Hawally']
                    del df_lpg['Hawally']

                    df_lpg['Mubarak Al-Kabeer (N={})'.format(vc['Mubarak Al-Kabeer'][0])]=df_lpg['Mubarak Al-Kabeer']
                    del df_lpg['Mubarak Al-Kabeer']


                    st.markdown("**Watts consumed - Refrigerator**")
                    st.write(df_lpg)









                    #graph

                    gwac=new.groupby('Governorate',as_index=True)[['Clothes dryer - The estimated Watts consumed per day']].sum()
                    gwac.reset_index(inplace=True)

                    gacs=new.groupby('Governorate',as_index=True)[['Front loaded Clothes washer automatic - The estimated Watts consumed per day']].sum()
                    gacs.reset_index(inplace=True)

                    gams=new.groupby('Governorate',as_index=True)[['Top loaded Clothes washer automatic - The estimated Watts consumed per day']].sum()
                    gams.reset_index(inplace=True)

                    gauw=new.groupby('Governorate',as_index=True)[['Clothes washer normal - The estimated Watts consumed per day']].sum()
                    gauw.reset_index(inplace=True)

                    gact=new.groupby('Governorate',as_index=True)[['Dish washer - The estimated Watts consumed per day']].sum()
                    gact.reset_index(inplace=True)

                    gael=new.groupby('Governorate',as_index=True)[['Freezer - The estimated Watts consumed per day']].sum()
                    gael.reset_index(inplace=True)

                    gaoel=new.groupby('Governorate',as_index=True)[['Refrigerator - The estimated Watts consumed per day']].sum()
                    gaoel.reset_index(inplace=True)

                    


                    import plotly.express as px
                    st.markdown("**Figure 36. Distribution of Watts consumed (Miscellaneous equipment) under different Governorate**")
                    import plotly.graph_objects as go
                    fig3 = go.Figure(data=[
                        go.Bar(name='Clothes dryer', x=gwac['Governorate'], y=gwac['Clothes dryer - The estimated Watts consumed per day']),
                         go.Bar(name='Front loaded Clothes washer automatic', x=gacs['Governorate'], y=gacs['Front loaded Clothes washer automatic - The estimated Watts consumed per day']),
                         go.Bar(name='Top loaded Clothes washer automatic', x=gams['Governorate'], y=gams['Top loaded Clothes washer automatic - The estimated Watts consumed per day']),
                         go.Bar(name='Clothes washer normal', x=gauw['Governorate'], y=gauw['Clothes washer normal - The estimated Watts consumed per day']),
                        go.Bar(name='Dish washer', x=gact['Governorate'], y=gact['Dish washer - The estimated Watts consumed per day']),
                        go.Bar(name='Freezer', x=gael['Governorate'], y=gael['Freezer - The estimated Watts consumed per day']),
                        go.Bar(name='Refrigerator', x=gaoel['Governorate'], y=gaoel['Refrigerator - The estimated Watts consumed per day']),

                    ])
                    # Change the bar mode
                    fig3.update_layout(barmode='group')
                    #fig.show()

                    st.write(fig3)

                    st.markdown("**Figure 37. Comparison of Watts consumed (Miscellaneous equipment) under different Governorate**")
                    fig18 = px.bar(gwac, x="Governorate", y='Clothes dryer - The estimated Watts consumed per day', color="Governorate")
                    fig19 = px.bar(gacs, x="Governorate", y='Front loaded Clothes washer automatic - The estimated Watts consumed per day', color="Governorate")
                    fig20 = px.bar(gams, x="Governorate", y='Top loaded Clothes washer automatic - The estimated Watts consumed per day', color="Governorate")
                    fig21= px.bar(gauw, x="Governorate", y='Clothes washer normal - The estimated Watts consumed per day', color="Governorate")
                    fig22= px.bar(gact, x="Governorate", y='Dish washer - The estimated Watts consumed per day', color="Governorate")
                    fig23= px.bar(gael, x="Governorate", y='Freezer - The estimated Watts consumed per day', color="Governorate")
                    fig24= px.bar(gaoel, x="Governorate", y='Refrigerator - The estimated Watts consumed per day', color="Governorate")

                    st.write(fig18)
                    st.write(fig19)
                    st.write(fig20)
                    st.write(fig21)
                    st.write(fig22)
                    st.write(fig23)
                    st.write(fig24)

                
                    



                
                    
                
                
                
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                
                    
                    
                    
                
                
                
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                            
                            
                            
                            
                            
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      

if __name__=='__main__':
    main()
