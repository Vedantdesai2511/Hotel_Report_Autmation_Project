import pandas as pd


def hotel_journal_summary_report_analysis_function(hotel_journal_summary_report):
    df1 = pd.read_csv(hotel_journal_summary_report)

    # print(df1.columns)

    # print(df1['Description (Transaction'])
    a = df1.loc[df1['Description (Transaction'] == 'Cash (CA)']
    # df2.loc[df2['Stay/C/O'] == "Stay"
    value = str(a['Postings1'])
    print(float(value[(value.find('(') + 1):value.find(')')]))

    return float(value[(value.find('(') + 1):value.find(')')])
    # print(df2)
    # print("#########################")
    # a = df2.drop(df2.loc[df2['Stay/C/O'] == "Stay"].index)
    # print(a)
    #
    # for i in room_list:
    #     df1.drop(df1.loc[df1['Room'] == i].index, inplace=True)
    #
    # print("#################################")
    # print(df1)
    # final_output = a.append(df1)
    #
    # print(final_output)
    #
    # final_output.to_csv("final_output.csv")


# root_directory = r'C:\Users\vedan\Downloads\{}'
#
# hotel_journal_summary_report_analysis_function(root_directory.format((datetime.today() + relativedelta(
# days=-1)).strftime('%m_%d_%Y') + 'hotel_journal_summary' + '.csv'))
