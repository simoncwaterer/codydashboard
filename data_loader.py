import pandas as pd
import streamlit as st
from utils import CONSTANTS


@st.cache_data
def load_users_per_day(data_source):
    # Create a dataframe from the CSV file.
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.USER_BY_DAY_CSV}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    return usage_data


@st.cache_data
def load_commands_per_day(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.COMMANDS_BY_DAY_CSV}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    usage_data[CONSTANTS.COMMAND_EVENTS] = usage_data[CONSTANTS.COMMAND_EVENTS]
    return usage_data


@st.cache_data
def load_chat_per_day(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.CHAT_BY_DAY_CSV}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    usage_data[CONSTANTS.CHAT_EVENTS] = usage_data[CONSTANTS.CHAT_EVENTS].str.replace(',', '').astype(int)
    return usage_data


@st.cache_data
def load_completions_per_day(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.COMPLETIONS_BY_DAY_CSV}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    usage_data[CONSTANTS.COMPLETIONS_ACCEPTED_JETBRAINS] = (
        usage_data[CONSTANTS.COMPLETIONS_ACCEPTED_JETBRAINS].str.replace(',', '').astype(int))
    usage_data[CONSTANTS.COMPLETIONS_ACCEPTED_VSCODE] = (
        usage_data[CONSTANTS.COMPLETIONS_ACCEPTED_VSCODE].str.replace(',', '').astype(int))
    usage_data[CONSTANTS.TOTAL_COMPLETIONS_ACCEPTED] = (usage_data[CONSTANTS.COMPLETIONS_ACCEPTED_JETBRAINS] +
                                                        usage_data[CONSTANTS.COMPLETIONS_ACCEPTED_VSCODE])
    return usage_data


@st.cache_data
def load_user_frequency(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.FREQUENCY_USAGE}', data_source)
    return usage_data


@st.cache_data
def load_user_by_month(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.MONTHLY_USAGE}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.MONTH] = pd.to_datetime(usage_data[CONSTANTS.MONTH])
    usage_data['MONTH'] = usage_data[CONSTANTS.MONTH].dt.strftime('%B')
    usage_data[CONSTANTS.USER_BY_MONTH] = usage_data[CONSTANTS.USER_BY_MONTH].str.replace(',', '').astype(int)
    return usage_data


@st.cache_data
def load_total_users(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.TOTAL_USERS}', data_source)
    return usage_data.loc[0, CONSTANTS.DISTINCT_USERS]


@st.cache_data
def load_average_users(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.AVERAGE_USERS}', data_source)
    return usage_data.loc[0, CONSTANTS.AVERAGE_DAUS]


@st.cache_data
def load_average_number_days(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.AVERAGE_NUMBER_DAYS}', data_source)
    return usage_data.loc[0, 'Avg days used (of last 30)']


@st.cache_data
def load_top_10_commands(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.TOP_10_COMMANDS}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    return usage_data


@st.cache_data
def load_total_command_events(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.TOTAL_COMMAND_EVENTS}', data_source)
    return usage_data.loc[0, CONSTANTS.COMMAND_EVENTS]


@st.cache_data
def load_minutes_saved_commands(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.MINUTES_SAVED_PER_COMMAND}', data_source)
    return usage_data.loc[0, CONSTANTS.MINUTES_SAVED_PER_COMMANDS]


@st.cache_data
def load_hours_saved_commands(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.HOURS_SAVED_BY_COMMAND}', data_source)
    return usage_data.loc[0, CONSTANTS.HOURS_SAVED_BY_COMMANDS]


@st.cache_data
def load_total_chat_events(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.TOTAL_CHAT_EVENTS}', data_source)
    return usage_data.loc[0, CONSTANTS.CHAT_EVENTS]


@st.cache_data
def load_minutes_saved_chats(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.MINUTES_SAVED_PER_CHAT}', data_source)
    return usage_data.loc[0, CONSTANTS.MINUTES_SAVED_PER_CHATS]


@st.cache_data
def load_hours_saved_chats(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.HOURS_SAVED_BY_CHAT}', data_source)
    return usage_data.loc[0, CONSTANTS.HOURS_SAVED_BY_CHATS]


@st.cache_data
def load_total_accepted_completions(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.TOTAL_ACCEPTED_COMPLETIONS}', data_source)
    return usage_data.loc[0, CONSTANTS.TOTAL_ACCEPTED_COMPLETION]


@st.cache_data
def load_minutes_saved_completions(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.MINUTES_SAVED_PER_COMPLETION}', data_source)
    return usage_data.loc[0, CONSTANTS.MINUTES_SAVED_PER_COMPLETIONS]


@st.cache_data
def load_hours_saved_completions(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.HOURS_SAVED_BY_COMPLETION}', data_source)
    return usage_data.loc[0, CONSTANTS.HOURS_SAVED_BY_COMPLETIONS]


@st.cache_data
def load_new_users_by_day(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.NEW_USERS_BY_DAY}', data_source)
    usage_data[CONSTANTS.DTE] = pd.to_datetime(usage_data[CONSTANTS.DTE])
    return usage_data


def load_completions_acceptance_rate_by_day(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.COMPLETION_ACCEPTANCE_RATE}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    return usage_data


def load_average_car_by_ide(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.AVERAGE_CAR_BY_IDE}', data_source, skiprows=1)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data.rename(columns={usage_data.columns[1]: 'jetbrains.cody'}, inplace=True)
    usage_data.rename(columns={usage_data.columns[2]: 'vscode.cody'}, inplace=True)
    usage_data[CONSTANTS.MONTH] = pd.to_datetime(usage_data[CONSTANTS.MONTH])
    usage_data['MONTH'] = usage_data[CONSTANTS.MONTH].dt.strftime('%B')
    return usage_data


def load_weighted_car(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.WEIGHTED_CAR}', data_source)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    return usage_data


def load_avg_wcar_by_ide(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.AVG_WCAR_BY_IDE}', data_source, skiprows=1)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    usage_data.rename(columns={usage_data.columns[1]: 'jetbrains.cody'}, inplace=True)
    usage_data.rename(columns={usage_data.columns[2]: 'vscode.cody'}, inplace=True)
    usage_data[CONSTANTS.MONTH] = pd.to_datetime(usage_data[CONSTANTS.MONTH])
    usage_data['MONTH'] = usage_data[CONSTANTS.MONTH].dt.strftime('%B')
    return usage_data


def load_average_completion_latency(data_source):
    usage_data = read_csv(f'{CONSTANTS.CSV_ROOT}/{CONSTANTS.AVERAGE_COMPLETION_LATENCY}', data_source, skiprows=1)
    usage_data = usage_data.drop('Unnamed: 0', axis=1)
    # drop columns 3 and 4
    usage_data = usage_data.drop(usage_data.columns[7], axis=1)
    usage_data = usage_data.drop(usage_data.columns[5], axis=1)
    usage_data = usage_data.drop(usage_data.columns[4], axis=1)
    usage_data = usage_data.drop(usage_data.columns[3], axis=1)
    usage_data = usage_data.drop(usage_data.columns[1], axis=1)
    usage_data.rename(columns={usage_data.columns[1]: CONSTANTS.AVG_LATENCY_VSCODE}, inplace=True)
    usage_data.rename(columns={usage_data.columns[2]: CONSTANTS.AVG_LATENCY_JETBRAINS}, inplace=True)
    usage_data[CONSTANTS.DATE] = pd.to_datetime(usage_data[CONSTANTS.DATE])
    return usage_data


def load_data(data_source):
    data = {'users_per_day': load_users_per_day(data_source),
            'commands_per_day': load_commands_per_day(data_source),
            'chats_per_day': load_chat_per_day(data_source),
            'completions_per_day': load_completions_per_day(data_source),
            'frequency_usage': load_user_frequency(data_source),
            'users_by_month': load_user_by_month(data_source),
            'total_users': load_total_users(data_source),
            'average_users': load_average_users(data_source),
            'average_days': load_average_number_days(data_source),
            'top_10_commands': load_top_10_commands(data_source),
            'total_command_events': load_total_command_events(data_source),
            'minutes_saved_by_command': load_minutes_saved_commands(data_source),
            'hours_saved_by_command': load_hours_saved_commands(data_source),
            'total_chat_events': load_total_chat_events(data_source),
            'minutes_saved_by_chat': load_minutes_saved_chats(data_source),
            'hours_saved_by_chat': load_hours_saved_chats(data_source),
            'total_accepted_completion': load_total_accepted_completions(data_source),
            'minutes_saved_by_completion': load_minutes_saved_completions(data_source),
            'hours_saved_by_completion': load_hours_saved_completions(data_source),
            'new_users_by_day': load_new_users_by_day(data_source),
            'completion_acceptance_rate_by_day': load_completions_acceptance_rate_by_day(data_source),
            'average_car_by_ide': load_average_car_by_ide(data_source),
            'weighted_car': load_weighted_car(data_source),
            'avg_wcar_by_ide': load_avg_wcar_by_ide(data_source),
            'average_completion_latency': load_average_completion_latency(data_source)}
    return data


def read_csv(file_path, data_source, skiprows=0):
    if data_source == "s3":
        return pd.read_csv(f"s3://{CONSTANTS.S3_BUCKET}/{file_path}",
                           storage_options={"anon": False}, skiprows=skiprows)
    else:
        return pd.read_csv(f'{file_path}', skiprows=skiprows)
