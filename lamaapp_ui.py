# app.py
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Define the backend URL
#backend_url = 'http://localhost:8000/api'
backend_url = 'https://lama.up.railway.app/api'

def fetch_data(endpoint):
    try:
        response = requests.get(f'{backend_url}/{endpoint}/')
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            st.error("Failed to fetch data")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()

st.set_page_config(page_title="Remo Stars!!!", page_icon=":bar_chart:",layout="wide")
# Set the title of the Streamlit app
st.markdown("<h1 style='text-align: center; color: red;'>Remo Stars Performance Metrics</h1>", unsafe_allow_html=True)
#st.title('Remo Stars Performance Metrics')

# Create navigation
options = ["Team Metrics", "Physical Metrics", "Technical Metrics", "Tactical Metrics", "Physiological Metrics",
            "Player Impact Metrics", "Team Cohesion Metrics", "Psychological Metrics"]

st.sidebar.image("img/remo_stars_Logo.png", caption="Remo Stars")

choice = st.sidebar.selectbox("Choose a metrics type to visualize", options)

# Visualization for Team Metrics
if choice == "Team Metrics":
    st.header("Team Metrics Visualization")
    data = fetch_data('team-metrics')

    #Total
    total_match_played = pd.Series(data['match']).count()
    total_goals = pd.Series(data['goals_scored']).sum()
    total_assist = pd.Series(data['goal_assist']).sum()
    total_goal_conceded = pd.Series(data['goals_conceded']).sum()
    total_yellow_card = pd.Series(data['yellow_card']).sum()
    total_red_card = pd.Series(data['red_card']).sum()

    #Average
    average_goals = pd.Series(data['goals_scored']).mean()
    average_assist = pd.Series(data['goal_assist']).mean()
    average_goal_conceded = pd.Series(data['goals_conceded']).mean()
    average_yellow_card = pd.Series(data['yellow_card']).mean()
    average_red_card = pd.Series(data['red_card']).mean()
    average_possession = pd.Series(data['possession_percentage']).mean()

    #total
    total1,total2,total3,total4,total5,total6=st.columns(6,gap='small')
    with total1:
        st.info('Total Matches Played',icon="⚽")
        st.metric(label="Sum TZS",value=f"{total_match_played:,.0f}")

    with total2:
        st.info('Total Goals Scored',icon="⚽")
        st.metric(label="Sum TZS",value=f"{total_goals:,.0f}")

    with total3:
        st.info('Total Assists',icon="⚽")
        st.metric(label="Sum TZS",value=f"{total_assist:,.0f}")

    with total4:
        st.info('Total Goals Conceded',icon="⚽")
        st.metric(label="Average TZS",value=f"{total_goal_conceded:,.0f}")

    with total5:
        st.info('Total Yellow Cards',icon="🟨")
        st.metric(label="Sum TZS",value=f"{total_yellow_card:,.0f}")
    
    with total6:
        st.info('Total Red Cards',icon="🟥")
        st.metric(label="Sum TZS",value=f"{total_red_card:,.0f}")
    
    #Average
    ave1,ave2,ave3,ave4,ave5,ave6=st.columns(6,gap='small')
    with ave1:
        st.info('Average Goals Scored',icon="⚽")
        st.metric(label="Average TZS",value=f"{average_goals:,.0f}")

    with ave2:
        st.info('Average Assists',icon="⚽")
        st.metric(label="Average TZS",value=f"{average_assist:,.0f}")

    with ave3:
        st.info('Avg Goals Conceded',icon="⚽")
        st.metric(label="Average TZS",value=f"{average_goal_conceded:,.0f}")

    with ave4:
        st.info('Average Possession',icon="⚽")
        st.metric(label="Average TZS",value=f"{average_possession:,.0f}")

    with ave5:
        st.info('Average Yellow Cards',icon="🟨")
        st.metric(label="Sum TZS",value=f"{average_yellow_card:,.0f}")
    
    with ave6:
        st.info('Average Red Cards',icon="🟥")
        st.metric(label="Sum TZS",value=f"{average_red_card:,.0f}")


    col1, col2 = st.columns((2))
    if not data.empty:
        st.dataframe(data)
        
        with col1:
        # Plot Distance Covered
            # fig, ax = plt.subplots()
            # sns.histplot(data['goals_scored'], kde=True, ax=ax)
            # ax.set_title('Distribution of goals scored')
            # st.pyplot(fig)
            # Goals Scored vs Expected Goals
            st.header('Possession Analysis')
            fig_possession = px.box(data, x='team', y='possession_percentage', title='Possession Percentage by Team')
            st.plotly_chart(fig_possession)
        
        with col2:
        # Plot Top Speed
            # fig, ax = plt.subplots()
            # sns.boxplot(x='match', y='possession_percentage', data=data, ax=ax)
            # ax.set_title('Possesion by Match')
            # st.pyplot(fig)
            st.header('Goals Scored vs Expected Goals')
            fig_goals = px.scatter(data, x='goals_scored', y='expected_goals', color='team', 
                                title='Goals Scored vs Expected Goals', size='goals_scored', hover_data=['match'])
            st.plotly_chart(fig_goals)
    
    # col3, col4 = st.columns((2))
    # if not data.empty:
    #     st.dataframe(data)
        
    #     with col3:
    #     # Set-Piece Effectiveness
    #         st.header('Set-Piece Effectiveness')
    #         fig_setpiece = make_subplots(rows=1, cols=2, subplot_titles=('Corner Kicks Converted', 'Free Kicks Converted'))

    #         fig_setpiece.add_trace(go.Bar(x=data['team'], y=data['conner_kicks_converted'], name='Corner Kicks Converted'),
    #                             row=1, col=1)
    #         fig_setpiece.add_trace(go.Bar(x=data['team'], y=data['free_kicks_converted'], name='Free Kicks Converted'),
    #                             row=1, col=2)
        
        # with col4:
        # # Plot Top Speed
        #     # fig, ax = plt.subplots()
        #     # sns.boxplot(x='match', y='possession_percentage', data=data, ax=ax)
        #     # ax.set_title('Possesion by Match')
        #     # st.pyplot(fig)
        #     st.header('Goals Scored vs Expected Goals')
        #     fig_goals = px.scatter(data, x='goals_scored', y='expected_goals', color='team', 
        #                         title='Goals Scored vs Expected Goals', size='goals_scored', hover_data=['match'])
        #     st.plotly_chart(fig_goals)
        
        # # Plot Sprints
        # fig = px.bar(data, x='team', y='goals_conceded', title='Goal conceded by Team')
        # st.plotly_chart(fig)


# Visualization for Technical Metrics
if choice == "Technical Metrics":
    st.header("Technical Metrics Visualization")
    data = fetch_data('technical-metrics')
    
    if not data.empty:
        st.dataframe(data)
        
        # Plot Passing Accuracy
        fig, ax = plt.subplots()
        sns.histplot(data['passing_accuracy'], kde=True, ax=ax)
        ax.set_title('Distribution of Passing Accuracy')
        st.pyplot(fig)
        
        # Plot Shots on Target
        fig = px.bar(data, x='player', y='shots_on_target', title='Shots on Target by Player')
        st.plotly_chart(fig)

# Repeat similar blocks for other metrics...
