import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime as dt
from PIL import Image
from numerize import numerize

####################### PAGE CONFIGURATION #######################
st.set_page_config(page_title='Citi Bike NYC Strategy Dashboard', layout='wide')

####################### SIDEBAR - PAGE SELECTOR ##################
page = st.sidebar.selectbox('Select an aspect of the analysis',
    ["Introduction", 
     "Weather and Bike Usage",
     "Most Popular Stations",
     "Geographic Distribution",
     "Recommendations"])

####################### IMPORT DATA ##############################
df = pd.read_csv('outputs/reduced_data_to_plot.csv')
df['date'] = pd.to_datetime(df['date'])

####################### DEFINE PAGES #############################

### INTRO PAGE ###
if page == "Introduction":
    st.title("Citi Bike NYC Expansion Strategy Dashboard")
    
    st.markdown("#### Purpose")
    st.markdown("This dashboard provides data-driven insights to address Citi Bike's critical supply challenge: bikes are frequently unavailable at popular stations during peak demand periods.")
    
    st.markdown("#### Problem Statement")
    st.markdown("Customers report consistent inability to find bikes at key stations, particularly during warmer months. This analysis identifies:")
    st.markdown("- When demand peaks occur (seasonal patterns)")
    st.markdown("- Where capacity is most constrained (station-level analysis)")
    st.markdown("- How to optimize bike distribution (geographic insights)")
    
    st.markdown("#### Dashboard Structure")
    st.markdown("**Weather and Bike Usage** - Seasonal demand correlation analysis")
    st.markdown("**Most Popular Stations** - High-demand locations requiring capacity expansion")
    st.markdown("**Geographic Distribution** - Network coverage and route popularity")
    st.markdown("**Recommendations** - Strategic actions based on findings")
    
    st.markdown("#### Navigation")
    st.markdown("Use the dropdown menu on the left ('Select an aspect of the analysis') to explore different sections of this analysis.")
    
    # Optional: Add image if you have one
    # myImage = Image.open("citibike_image.jpg")
    # st.image(myImage)

### WEATHER AND BIKE USAGE PAGE ###
elif page == "Weather and Bike Usage":
    st.header("Seasonal Demand Patterns")
    
    # Create daily aggregation
    df_daily = df.groupby('date', as_index=False).agg({
        'value': 'sum',
        'avgTemp': 'first'
    })
    df_daily.rename(columns={'value': 'bike_rides_daily'}, inplace=True)
    
    # Create dual-axis line chart
    fig_2 = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_2.add_trace(
        go.Scatter(
            x=df_daily['date'],
            y=df_daily['bike_rides_daily'],
            name='Daily Bike Rides',
            marker={'color': 'blue'}
        ),
        secondary_y=False
    )
    
    fig_2.add_trace(
        go.Scatter(
            x=df_daily['date'],
            y=df_daily['avgTemp'],
            name='Daily Temperature',
            marker={'color': 'red'}
        ),
        secondary_y=True
    )
    
    fig_2.update_layout(
        title='Daily Bike Rides and Temperature Correlation - 2022',
        xaxis_title='Date',
        height=600
    )
    
    fig_2.update_yaxes(title_text='Number of Bike Rides', secondary_y=False)
    fig_2.update_yaxes(title_text='Temperature (°C)', secondary_y=True)
    
    st.plotly_chart(fig_2, use_container_width=True)
    
    st.markdown("#### Key Findings")
    st.markdown("There is a clear correlation between temperature and bike usage. As temperatures rise during spring and summer months (May-September), ridership increases dramatically. Conversely, during winter months (November-April), usage drops significantly.")
    
    st.markdown("**Implications:**")
    st.markdown("- The bike shortage problem is primarily a **warm-weather phenomenon** (May-October)")
    st.markdown("- Winter months show substantially lower demand, suggesting opportunity to reduce fleet size during this period")
    st.markdown("- Seasonal capacity planning is essential: scale up for summer, scale down for winter")
    st.markdown("- Peak demand months (June-August) require maximum bike availability at popular stations")

### MOST POPULAR STATIONS PAGE ###
elif page == "Most Popular Stations":
    st.header("High-Demand Station Analysis")
    
    # Seasonal filter
    with st.sidebar:
        st.markdown("---")
        season_filter = st.multiselect(
            label='Filter by Season',
            options=df['season'].unique(),
            default=df['season'].unique()
        )
    
    # Apply filter
    df1 = df.query('season == @season_filter')
    
    # Total rides metric
    total_rides = float(df1['value'].sum())
    st.metric(label='Total Bike Rides', value=numerize(total_rides))
    
    # Create bar chart
    df_groupby_bar = df1.groupby('start_station_name', as_index=False).agg({'value': 'sum'})
    top20 = df_groupby_bar.nlargest(20, 'value')
    
    fig = go.Figure(go.Bar(
        x=top20['value'],
        y=top20['start_station_name'],
        orientation='h',
        marker={'color': top20['value'], 'colorscale': 'Blues'}
    ))
    
    fig.update_layout(
        title='Top 20 Most Popular Starting Stations',
        xaxis_title='Number of Trips',
        yaxis_title='Station Name',
        height=700
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("#### Key Findings")
    st.markdown("The data reveals significant variation in station popularity. The top stations show substantially higher usage than lower-ranked stations, indicating concentrated demand at specific locations.")
    
    st.markdown("**Top Station Characteristics:**")
    st.markdown("- Concentrated in Lower Manhattan and waterfront areas")
    st.markdown("- Near major transit hubs, tourist attractions, and office districts")
    st.markdown("- Show consistent high demand across seasons (use filter to verify)")
    
    st.markdown("**Implications:**")
    st.markdown("- These high-traffic stations require immediate capacity expansion")
    st.markdown("- Priority for real-time monitoring and dynamic bike redistribution")
    st.markdown("- Consider larger dock capacity at these locations")
    st.markdown("- Ensure consistent bike availability during peak hours (7-9 AM, 5-7 PM)")

### GEOGRAPHIC DISTRIBUTION PAGE ###
elif page == "Geographic Distribution":
    st.header("Network Coverage and Trip Patterns")
    st.markdown("Interactive map showing popular routes and identifying network gaps for strategic expansion.")
    
    # Path to HTML map
    path_to_html = "outputs/citibike_trips_map.html"
    
    try:
        with open(path_to_html, 'r') as f:
            html_data = f.read()
        
        st.components.v1.html(html_data, height=1000)
        
        st.markdown("#### Key Findings")
        st.markdown("**High-Traffic Corridors:**")
        st.markdown("- Hudson River waterfront shows concentrated route activity")
        st.markdown("- Strong commuter patterns between Lower Manhattan and Brooklyn")
        st.markdown("- Midtown transit hubs (Penn Station, Grand Central) serve as key connectors")
        
        st.markdown("**Network Gaps:**")
        st.markdown("- **Queens**: Minimal coverage despite large population")
        st.markdown("- **Upper Manhattan**: Sparse station density above Central Park")
        st.markdown("- **Outer Brooklyn**: Limited integration with core network")
        
        st.markdown("**Implications:**")
        st.markdown("- Expansion into Queens represents largest growth opportunity")
        st.markdown("- Cross-river connections need strengthening (more stations near bridges)")
        st.markdown("- Waterfront stations require capacity increases due to recreational and commuter demand")
        
    except FileNotFoundError:
        st.warning("⚠️ Map file not found.")
        st.info("The interactive map can be regenerated by running Exercise 2.5 notebook. For now, key geographic insights:")
        
        st.markdown("**High-Demand Areas:**")
        st.markdown("- Financial District (FiDi): Morning inbound, evening outbound commuter patterns")
        st.markdown("- Waterfront corridor: Mixed recreational and commuter usage")
        st.markdown("- Brooklyn Bridge area: Heavy cross-river traffic")
        
        st.markdown("**Expansion Opportunities:**")
        st.markdown("- **Queens**: 2.3M residents, minimal current coverage")
        st.markdown("- **Williamsburg**: Growing demand, limited cross-river connections")
        st.markdown("- **Upper Manhattan**: Dense residential areas underserved")

### RECOMMENDATIONS PAGE ###
else:  # Recommendations
    st.header("Strategic Recommendations")
    
    # Optional: Add image
    # bikes_image = Image.open("recommendations_image.jpg")
    # st.image(bikes_image)
    
    st.markdown("### Executive Summary")
    st.markdown("Our analysis reveals that Citi Bike's supply challenges are driven by:")
    st.markdown("1. **Seasonal demand fluctuations** (3-4x variation summer vs. winter)")
    st.markdown("2. **Geographic concentration** at specific high-traffic stations")
    st.markdown("3. **Network gaps** in high-population outer boroughs")
    
    st.markdown("### Immediate Actions (0-3 months)")
    
    st.markdown("#### 1. Capacity Expansion at High-Demand Stations")
    st.markdown("**Target:** Top 20 stations identified in analysis")
    st.markdown("- Increase docking capacity by 30-50% at peak stations")
    st.markdown("- Install real-time occupancy monitoring")
    st.markdown("- Implement dynamic pricing during peak periods")
    
    st.markdown("#### 2. Optimize Seasonal Fleet Management")
    st.markdown("**November-April period:**")
    st.markdown("- Reduce active fleet by 40-50% during winter months")
    st.markdown("- Focus bikes at core commuter stations (Lower Manhattan, transit hubs)")
    st.markdown("- Shift excess bikes to maintenance/storage")
    st.markdown("- **Cost savings:** Reduced redistribution logistics, maintenance scheduling efficiency")
    
    st.markdown("#### 3. Enhanced Bike Redistribution")
    st.markdown("**Peak demand stations require:**")
    st.markdown("- Morning restocking (6-8 AM) at commuter destinations (FiDi, Midtown)")
    st.markdown("- Evening restocking (4-6 PM) at residential areas (Williamsburg, Brooklyn Heights)")
    st.markdown("- Automated alerts when stations reach 90% full/10% empty")
    
    st.markdown("### Medium-Term Strategy (3-12 months)")
    
    st.markdown("#### 4. Waterfront Corridor Enhancement")
    st.markdown("**Methodology:** Analyze current high-demand waterfront stations, calculate capacity shortfall")
    st.markdown("- **Data needed:** Peak hour usage rates, current dock capacity, queue/wait data")
    st.markdown("- **Approach:** Add stations every 500m along gaps in Hudson River Greenway")
    st.markdown("- **Priority locations:** Between existing high-traffic stations with >2km gaps")
    
    st.markdown("#### 5. Cross-River Expansion")
    st.markdown("- Add stations within 200m of Manhattan and Brooklyn Bridge bike paths")
    st.markdown("- Target commuter routes showing high demand but limited current coverage")
    st.markdown("- Pilot program: 5-10 new stations near bridge access points")
    
    st.markdown("### Long-Term Growth (1-2 years)")
    
    st.markdown("#### 6. Outer Borough Network Development")
    st.markdown("**Queens Expansion (Priority 1):**")
    st.markdown("- Phase 1: Astoria, Long Island City (near Manhattan connections)")
    st.markdown("- Phase 2: Flushing, Jackson Heights (dense residential areas)")
    st.markdown("- Target: 50-75 new stations over 18 months")
    
    st.markdown("**Upper Manhattan:**")
    st.markdown("- Harlem, Washington Heights station network")
    st.markdown("- Connect to existing Midtown infrastructure")
    
    st.markdown("### Key Metrics for Success")
    st.markdown("- **Bike availability:** >95% of searches result in available bike within 2 blocks")
    st.markdown("- **Station capacity:** <5% of trips encounter full docking stations")
    st.markdown("- **Seasonal efficiency:** Winter operational costs reduced by 30-40%")
    st.markdown("- **Network coverage:** 80% of NYC population within 10-minute walk of station")
    
    st.markdown("### Next Steps")
    st.markdown("1. **Data collection:** Implement real-time monitoring at top 20 stations")
    st.markdown("2. **Pilot testing:** Trial enhanced redistribution at 5 high-demand stations")
    st.markdown("3. **Stakeholder alignment:** Present findings to operations and expansion teams")
    st.markdown("4. **Budget planning:** Develop ROI models for Queens expansion phase")

####################### FOOTER ###############################
st.sidebar.markdown("---")
st.sidebar.markdown("**Citi Bike NYC Expansion Analysis**")
st.sidebar.markdown("Data Visualization in Python - Achievement 2")
