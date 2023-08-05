from __future__ import division
from __future__ import print_function

from topiceval.preprocessing import textcleaning
import topiceval.preprocessing.emailsprocess as emailprocess

import pandas as pd
from gensim.models import phrases

import win32com.client
import os
import logging


def extract_usermails(threaded, extrafolders):
    dirname = make_user_dir()
    items = extract(extrafolders)
    df_filename, df = makedf(items, dirname, threaded)
    # emails_dict = make_emails_dict(df)
    emailprocess.make_doc2bow(df, dirname)
    return dirname


def encodeit(s):
    if isinstance(s, str):
        return (s.encode('utf-8')).decode('utf-8')
    else:
        return s


def extract(extrafolders):
    items = []
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    folders = {"inbox": 6, "sent_items": 5}     # append "deleted_items": 3 if wanted
    for folder_type in folders:
        logging.info("Extracting emails from {0}".format(folder_type))
        folder = outlook.GetDefaultFolder(folders[folder_type])  # "6" refers to the inbox
        logging.info("Got messages...")
        messages = folder.Items
        items = extract_helper(messages=messages, folder_type=folder_type, items=items)
    extrafolders = set([folder.strip().lower() for folder in extrafolders.split(",") if folder.strip() != ""])
    if len(extrafolders) > 0:
        folders = outlook.Folders[0].Folders
        for folder in folders:
            if str(folder).lower() in extrafolders:
                logging.info("Extracting emails from {0}".format(folder))
                messages = folder.Items
                items = extract_helper(messages=messages, folder_type=folder, items=items)
    return items


def extract_helper(messages, folder_type, items):
    message = messages.GetFirst()
    while message:
        try:
            d = dict()
            d['Subject'] = encodeit(getattr(message, 'Subject', '<UNKNOWN>'))
            d['SentOn'] = encodeit(getattr(message, 'SentOn', '<UNKNOWN>'))
            d['SenderName'] = encodeit(getattr(message, 'SenderName', '<UNKNOWN>'))
            d['Size'] = encodeit(getattr(message, 'Size', '<UNKNOWN>'))
            d['CC'] = encodeit(getattr(message, 'CC', '<UNKNOWN>'))
            d['BCC'] = encodeit(getattr(message, 'BCC', '<UNKNOWN>'))
            d['To'] = encodeit(getattr(message, 'To', '<UNKNOWN>'))
            d['Body'] = encodeit(getattr(message, 'Body', '<UNKNOWN>'))
            d['ConversationID'] = encodeit(getattr(message, 'ConversationID', '<UNKNOWN>'))
            d['ConversationIndex'] = encodeit(getattr(message, 'ConversationIndex', '<UNKNOWN>'))
            d['FolderType'] = folder_type
            if d['SentOn'] != '<UNKNOWN>' and d['ConversationID'] != '<UNKNOWN>':
                items.append(d)
        except Exception as inst:
            print("Error processing mail", inst)

        message = messages.GetNext()
    return items


def make_user_dir():
    path = "./data/userdata/"
    if os.path.exists(path):
        for filename in os.listdir(path):
            os.remove(os.path.join(path, filename))
    else:
        os.makedirs(path)
    logging.info("Saving data at {0}{1}".format(os.path.dirname(os.path.abspath(__file__)), path[1:]))
    return path
    # i = 1
    # while os.path.exists("./data/user" + str(i)):
    #     i += 1
    # dirname = "./data/user" + str(i) + "/"
    # logging.info("Saving data at {0}{1}".format(os.path.dirname(os.path.abspath(__file__)), dirname[1:]))
    # os.makedirs(dirname)
    # return dirname


def makedf(items, dirname, threaded):
    items.sort(key=lambda tup: tup['SentOn'])
    keys = ["ConversationID", "ConversationIndex", "SentOn", "SenderName", "To", "CC", "BCC", "Subject", "Body",
            "FolderType"]
    df = pd.DataFrame()
    logging.debug("Making user-emails' dataframe...")
    for key in keys:
        try:
            df[key] = [str(d[key]) for d in items]
        except:
            df[key] = [d[key].encode('utf-8') for d in items]
    df.set_index(keys=["ConversationID"], inplace=True, drop=False)
    df['SentOn'] = pd.to_datetime(df['SentOn'], infer_datetime_format=True)
    logging.debug("Cleaning email bodies in dataframe...")
    names = get_names(df)
    if threaded:
        bool_list = remove_redundant_threads(df)
        df = df[bool_list]
    else:
        df['Body'] = df['Body'].apply(emailprocess.remove_threads)
    df['Body'] = df['Body'].apply(emailprocess.remove_signature)
    df['CleanBody'] = df['Body'].apply(textcleaning.clean_text)
    bigram_phraser = phrase_detection(df)
    df['CleanBody'] = df['CleanBody'].apply(textcleaning.remove_stops)
    df['CleanBody'] = df['CleanBody'].apply(phraser, args=(bigram_phraser, ))
    # df['CleanBody'] = df['CleanBody'].apply(emailprocess.replace_names, args=(names, ))
    logging.debug("Done cleaning email bodies in dataframe")
    df_filename = dirname + "emails.pkl"
    df.to_pickle(df_filename)
    logging.debug("Saved user-emails df at %s" % df_filename)
    return df_filename, df


def phraser(text, bigram):
    return ' '.join(bigram[text.split()])


def phrase_detection(df):
    sentences = [text.split() for text in df["CleanBody"]]
    phrases_ = phrases.Phrases(sentences, min_count=5, threshold=100)
    bigram = phrases.Phraser(phrases_)
    # for phr, score in phrases_.export_phrases(sentences):
    #     print(u'{0}   {1}'.format(phr, score))
    return bigram


def remove_redundant_threads(df):
    bool_list = []
    df.sort_values(by=['ConversationID', 'SentOn'], ascending=[True, True])
    for i in range(0, df.shape[0]-1):
        # print(df.irow(i)['ConversationID'])
        # print(df.irow(i + 1)['SentOn'])
        if df.iloc[i]['ConversationID'] == df.iloc[i + 1]['ConversationID']:
            bool_list.append(False)
        else:
            bool_list.append(True)
    bool_list.append(True)
    return bool_list


def get_names(df):
    return df["SenderName"].unique().tolist()


# def make_emails_dict(df):
#     emails_dict = {}
#     for elem in df.index.unique():
#         emails_dict[elem] = []
#     for idx, row in df.iterrows():
#         emails_dict[row["ConversationID"]].append((row["ConversationIndex"], row["Body"]))
#     return emails_dict
