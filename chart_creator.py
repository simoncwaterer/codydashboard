# chart_creator.py
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
from utils import CONSTANTS


def create_user_per_day_chart(user_per_day_data):
    return px.line(user_per_day_data,
                   x=CONSTANTS.DATE,
                   y=CONSTANTS.USER_BY_DAY,
                   title='Unique Users By Day',
                   labels={CONSTANTS.DATE: 'Day', CONSTANTS.USER_BY_DAY: 'Unique Users'})


def create_frequency_chart(frequency_usage_data):
    return px.bar(frequency_usage_data,
                  x=CONSTANTS.FREQUENCY_DAYS,
                  y=CONSTANTS.FREQUENCY_COUNT,
                  title='30 day Frequency Usage',
                  labels={CONSTANTS.FREQUENCY_DAYS: 'Days Used', CONSTANTS.FREQUENCY_COUNT: 'Number of Users'})


def create_new_users_chart(new_users_per_day_data):
    return px.bar(new_users_per_day_data,
                  x=CONSTANTS.DTE,
                  y=CONSTANTS.NEW_USERS,
                  title='New Users Per Day',
                  labels={CONSTANTS.DTE: 'Day', CONSTANTS.NEW_USERS: 'New Users'})


def create_users_by_month_chart(users_by_month_data):
    fig = px.bar(users_by_month_data,
           x='MONTH',
           y=CONSTANTS.USER_BY_MONTH,
           title='Users By Month',
           labels={'MONTH': 'Month', CONSTANTS.USER_BY_MONTH: 'Unique Users'})
    return fig


def create_chat_per_day_chart(chat_by_day_data):
    # Melt the DataFrame to convert columns to rows
    df_chats_melted = pd.melt(chat_by_day_data,
                              id_vars=CONSTANTS.DATE,
                              value_vars=[CONSTANTS.CHAT_EVENTS, CONSTANTS.CHAT_BY_USERS, CONSTANTS.CHAT_USERS],
                              var_name='Category',
                              value_name='Value')
    # Create the bar chart with side-by-side bars
    return px.bar(df_chats_melted,
                  x=CONSTANTS.DATE,
                  y='Value',
                  color='Category',
                  barmode='group',
                  title='Chat Events By Day',
                  labels={CONSTANTS.DATE: 'Day', 'Value': 'Chat Events'})


def create_command_per_day_chart(command_by_day_data):
    # Melt the DataFrame to convert columns to rows
    df_commands_melted = pd.melt(command_by_day_data,
                                 id_vars=CONSTANTS.DATE,
                                 value_vars=[CONSTANTS.COMMAND_EVENTS, CONSTANTS.COMMAND_BY_USERS,
                                             CONSTANTS.COMMAND_USERS],
                                 var_name='Category',
                                 value_name='Value')
    # Create the bar chart with side-by-side bars
    return px.bar(df_commands_melted,
                  x=CONSTANTS.DATE,
                  y='Value',
                  color='Category',
                  barmode='group',
                  title='Command Events By Day',
                  labels={CONSTANTS.DATE: 'Day', 'Value': 'Command Events'})


def create_top_commands(top_10_commands_data):
    return ff.create_table(top_10_commands_data, index=False)


def create_completions_per_day_chart(completions_by_day_data):
    # Melt the DataFrame to convert columns to rows
    df_completions_melted = pd.melt(completions_by_day_data,
                                    id_vars=CONSTANTS.DATE,
                                    value_vars=[CONSTANTS.TOTAL_COMPLETIONS_ACCEPTED,
                                                CONSTANTS.COMPLETIONS_ACCEPTED_VSCODE,
                                                CONSTANTS.COMPLETIONS_ACCEPTED_JETBRAINS],
                                    var_name='Category',
                                    value_name='Value')
    # Create the bar chart with side-by-side bars
    return px.bar(df_completions_melted,
                  x=CONSTANTS.DATE,
                  y='Value',
                  color='Category',
                  barmode='group',
                  title='Completions Events By Day',
                  labels={CONSTANTS.DATE: 'Day', 'Value': 'Completions'})


def create_completions_acceptance_rate_by_day_chart(completion_acceptance_rate_by_day_data):
    fig = px.line(completion_acceptance_rate_by_day_data,
                  x=CONSTANTS.DATE,
                  y=[CONSTANTS.COMPLETION_ACCEPTANCE_RATE_VSCODE, CONSTANTS.COMPLETION_ACCEPTANCE_RATE_JETBRAINS],
                  title='Completion Acceptance Rate By Day')

    return fig.update_layout(
        xaxis_title='Day',
        yaxis_title='CAR (%)')


def create_average_car_by_ide_chart(average_car_by_ide_data):
    df_car_data_melted = pd.melt(average_car_by_ide_data,
                                          id_vars='MONTH',
                                          value_vars=['vscode.cody', 'jetbrains.cody'],
                                          var_name='Category',
                                          value_name='Value')
    return px.bar(df_car_data_melted,
                  x='MONTH',
                  y='Value',
                  color='Category',
                  barmode='group',
                  title='CAR by Month',
                  labels={'MONTH': 'Month',
                          'Value': 'CAR (%)'})


def create_weighted_car_chart(weighted_car_data):
    fig = px.line(weighted_car_data,
                   x=CONSTANTS.DATE,
                   y=[CONSTANTS.WEIGHTED_CAR_VSCODE, CONSTANTS.WEIGHTED_CAR_JETBRAINS],
                   title='Weighted completion acceptance rate (wCAR) by day')

    return fig.update_layout(
        xaxis_title='Day',
        yaxis_title='wCAR (%)')


def create_avg_wcar_by_ide_chart(avg_wcar_by_ide_data):
    df_weighted_car_data_melted = pd.melt(avg_wcar_by_ide_data,
                                          id_vars='MONTH',
                                          value_vars=['vscode.cody', 'jetbrains.cody'],
                                          var_name='Category',
                                          value_name='Value')
    return px.bar(df_weighted_car_data_melted,
                  x='MONTH',
                  y='Value',
                  color='Category',
                  barmode='group',
                  title='wCAR by Month',
                  labels={'MONTH': 'Month',
                          'Value': 'wCAR (%)'})


def create_average_completion_latency_chart(average_completion_latency_data):
    return px.line(average_completion_latency_data,
                   x=CONSTANTS.DATE,
                   y=[CONSTANTS.AVG_LATENCY_VSCODE, CONSTANTS.AVG_LATENCY_JETBRAINS],
                   title='Completion Latency By Day')


def create_charts(data):
    charts = {'user_per_day': create_user_per_day_chart(data['users_per_day']),
              'frequency': create_frequency_chart(data['frequency_usage']),
              'users_by_month': create_users_by_month_chart(data['users_by_month']),
              'chat_per_day': create_chat_per_day_chart(data['chats_per_day']),
              'command_per_day': create_command_per_day_chart(data['commands_per_day']),
              'completion_per_day': create_completions_per_day_chart(data['completions_per_day']),
              'top_10_commands': create_top_commands(data['top_10_commands']),
              'new_users_per_day': create_new_users_chart(data['new_users_by_day']),
              'completion_acceptance_rate_by_day': create_completions_acceptance_rate_by_day_chart(
                  data['completion_acceptance_rate_by_day']),
              'average_car_by_ide': create_average_car_by_ide_chart(data['average_car_by_ide']),
              'weighted_car': create_weighted_car_chart(data['weighted_car']),
              'avg_wcar_by_ide': create_avg_wcar_by_ide_chart(data['avg_wcar_by_ide']),
              'average_completion_latency': create_average_completion_latency_chart(data['average_completion_latency'])}
    return charts
