#!/usr/bin/python3
def multiple_returns(sentence):
    len_sent = len(sentence)

    if (len_sent == 0):
        latest_tuple = (len_sent, None)
    else:
        latest_tuple = (len_sent, sentence[0])

    return (latest_tuple)
