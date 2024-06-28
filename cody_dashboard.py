import streamlit as st
import pandas as pd
import plotly.express as px

from utils import CONSTANTS
from data_loader import load_data
from chart_creator import create_charts

# Create the Streamlit app
st.set_page_config(page_title='Usage Dashboard', layout='wide', initial_sidebar_state='auto')
st.title('Usage Dashboard')
st.write('This dashboard displays the number of users per day.')

data = load_data()

# sort the data by date - probably not needed
data['users_per_day'].sort_values(CONSTANTS.DATE, inplace=True)
data['users_by_month'].sort_values(CONSTANTS.MONTH, inplace=True)
data['commands_per_day'].sort_values(CONSTANTS.DATE, inplace=True)
data['chats_per_day'].sort_values(CONSTANTS.DATE, inplace=True)
data['completions_per_day'].sort_values(CONSTANTS.DATE, inplace=True)

data['new_users_by_day'].sort_values(CONSTANTS.DTE, inplace=True)
data['completion_acceptance_rate_by_day'].sort_values(CONSTANTS.DATE, inplace=True)
data['average_car_by_ide'].sort_values(CONSTANTS.MONTH, inplace=True)
data['weighted_car'].sort_values(CONSTANTS.DATE, inplace=True)
data['avg_wcar_by_ide'].sort_values(CONSTANTS.MONTH, inplace=True)
data['average_completion_latency'].sort_values(CONSTANTS.DATE, inplace=True)

# find start and end date range based on users by day data. Use these dates to shape the other dataframes
start_date = data['users_per_day'][CONSTANTS.DATE].min().date()
end_date = data['users_per_day'][CONSTANTS.DATE].max().date()

with st.sidebar:
    # Create date range selector
    start_date = st.date_input('Start Date',
                               value=start_date,
                               max_value=end_date,
                               min_value=start_date,
                               key='start_date')
    end_date = st.date_input('End Date',
                             value=end_date,
                             max_value=end_date,
                             min_value=start_date,
                             key='end_date')

# Filter data based on selected date range
data['users_per_day'] = data['users_per_day'][
    (data['users_per_day'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['users_per_day'][CONSTANTS.DATE].dt.date <= end_date)]

data['chats_per_day'] = data['chats_per_day'][
    (data['chats_per_day'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['chats_per_day'][CONSTANTS.DATE].dt.date <= end_date)]

data['commands_per_day'] = data['commands_per_day'][
    (data['commands_per_day'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['commands_per_day'][CONSTANTS.DATE].dt.date <= end_date)]

data['completions_per_day'] = data['completions_per_day'][
    (data['completions_per_day'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['completions_per_day'][CONSTANTS.DATE].dt.date <= end_date)]

data['completion_acceptance_rate_by_day'] = data['completion_acceptance_rate_by_day'][
    (data['completion_acceptance_rate_by_day'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['completion_acceptance_rate_by_day'][CONSTANTS.DATE].dt.date <= end_date)]

data['weighted_car'] = data['weighted_car'][
    (data['weighted_car'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['weighted_car'][CONSTANTS.DATE].dt.date <= end_date)]

data['average_completion_latency'] = data['average_completion_latency'][
    (data['average_completion_latency'][CONSTANTS.DATE].dt.date >= start_date) &
    (data['average_completion_latency'][CONSTANTS.DATE].dt.date <= end_date)]

charts = create_charts(data)

with st.sidebar:
    show_data = st.checkbox('Show Data Table')

users, chats, commands, completions = st.tabs(["Users", "Chat", "Commands", "Completions"])

with users:
    with st.container(border=True):
        total_users_column, average_users_column, average_days_column = st.columns(3)
        total_users_column.metric("Total Users", data['total_users'])
        average_users_column.metric("Average Users", data['average_users'])
        average_days_column.metric("Average Days", data['average_days'])

    column_user_day, column_user_month = st.columns(2)

    user_day_container = st.container(border=True)

    with user_day_container:
        with column_user_day:
            st.plotly_chart(charts['user_per_day'])

        with column_user_month:
            st.plotly_chart(charts['users_by_month'])

    with st.container():
        st.plotly_chart(charts['frequency'])

    with st.container():
        st.plotly_chart(charts['new_users_per_day'])

    if show_data:
        with user_day_container:
            st.expander('User By Day')
            st.dataframe(data['users_per_day'], hide_index='true', use_container_width=True)

with chats:
    with st.container(border=True):
        total_chats_column, minutes_saved_column, hours_saved_column = st.columns(3)
        total_chats_column.metric("Total chat events", data['total_chat_events'])
        minutes_saved_column.metric("Minutes saved per chat", data['minutes_saved_by_chat'])
        hours_saved_column.metric("Hours saved by chat", data['hours_saved_by_chat'])

    chat_day_container = st.container(border=True)

    with chat_day_container:
        st.plotly_chart(charts['chat_per_day'])

    if show_data:
        with chat_day_container:
            st.expander('Chat By Day')
            st.dataframe(data['chats_per_day'], hide_index='true', use_container_width=True)

with commands:
    with st.container(border=True):
        total_commands_column, minutes_saved_column, hours_saved_column = st.columns(3)
        total_commands_column.metric("Total command events", data['total_command_events'])
        minutes_saved_column.metric("Minutes saved per command", data['minutes_saved_by_command'])
        hours_saved_column.metric("Hours saved by commands", data['hours_saved_by_command'])

    command_day_container = st.container(border=True)

    with command_day_container:
        st.plotly_chart(charts['command_per_day'])

    with st.container():
        st.plotly_chart(charts['top_10_commands'])

    if show_data:
        with command_day_container:
            st.expander('Command By Day')
            st.dataframe(data['commands_per_day'], hide_index='true', use_container_width=True)

with completions:
    with st.container(border=True):
        total_completions_column, minutes_saved_column, hours_saved_column = st.columns(3)
        total_completions_column.metric("Total accepted completions",
                                        "{:,}".format(data['total_accepted_completion']))
        minutes_saved_column.metric("Minutes saved per completion", data['minutes_saved_by_completion'])
        hours_saved_column.metric("Hours saved by completions", data['hours_saved_by_completion'])

    completion_day_container = st.container(border=True)
    completion_car_container = st.container(border=True)
    completion_wcar_container = st.container(border=True)
    completion_latency_container = st.container(border=True)

    with completion_day_container:
        st.plotly_chart(charts['completion_per_day'])

    with completion_car_container:
        column_car_day, column_car_month = st.columns(2)
        with column_car_day:
            st.plotly_chart(charts['completion_acceptance_rate_by_day'])
        with column_car_month:
            st.plotly_chart(charts['average_car_by_ide'])

    with completion_wcar_container:
        column_wcar_day, column_wcar_month = st.columns(2)
        with column_wcar_day:
            st.plotly_chart(charts['weighted_car'])
        with column_wcar_month:
            st.plotly_chart(charts['avg_wcar_by_ide'])

    with completion_latency_container:
        st.plotly_chart(charts['average_completion_latency'])

    if show_data:
        with completion_day_container:
            st.expander('Completion By Day')
            st.dataframe(data['completions_per_day'], hide_index=True, use_container_width=True)
        with completion_car_container:
            st.expander('Completion CAR By Day')
            st.dataframe(data['completion_acceptance_rate_by_day'], hide_index=True, use_container_width=True)
        with completion_wcar_container:
            st.expander('Completion wCAR By Day')
            st.dataframe(data['weighted_car'], hide_index=True, use_container_width=True)
        with completion_latency_container:
            st.expander('Completion latency By Day')
            st.dataframe(data['average_completion_latency'], hide_index=True, use_container_width=True)
