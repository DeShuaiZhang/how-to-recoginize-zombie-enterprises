import pandas as pd
import warnings
import numpy as np
warnings.filterwarnings("ignore")

# 先把两张含2015、2016、2017年份的数据合并成一行
def merge_data(base_verify_root,money_information_verify_root,year_report_verify_root,paient_information_verify_root):
    # money_information_verify1 = pd.read_csv('money_information_verify1.csv',encoding='gbk')
    money_information_verify1 = pd.read_csv(money_information_verify_root, encoding='gbk')
    # year_report_verify1 = pd.read_csv('year_report_verify1.csv',encoding='gbk')
    year_report_verify1 = pd.read_csv(year_report_verify_root,encoding='gbk')

    # money_S = money_information_verify1['year'].groupby(money_information_verify1['ID']).count()
    # year_S = year_report_verify1['year'].groupby(year_report_verify1['ID']).count()
    # # 下部分代码主要是通过两张表的年份数据相互补齐，主要补充的是在两张表中只有一个缺失值的数据，举例来说
    # # 如果ID为1的公司在money表中年份数据为N/A，2016，2017，而在year_report表中是2015，2016，2017，
    # # 那么就可以用year_report表中比money表中多出的那个年份（或者说是year表中的、与money表中不一样的年份）来填充这个缺失值。
    #
    # # 填充money表
    # pro_money_S = money_S[money_S == 2]
    # pro_ID = pro_money_S.index
    # for i in range(len(pro_ID)):
    #     years_list = year_report_verify1[year_report_verify1['ID']==pro_ID[i]]['year'].values.tolist()
    #     exist_year = money_information_verify1[money_information_verify1['ID']==pro_ID[i]][money_information_verify1['year'].notnull()]['year'].values.tolist()
    #     pro_index = money_information_verify1[money_information_verify1['ID']==pro_ID[i]][money_information_verify1['year'].isnull()].index.tolist()[0]
    #     money_information_verify1.loc[pro_index,'year'] = list(set(years_list)-set(exist_year))[0]
    # money_nopro_ID = []
    # sum_nopro_ID = money_information_verify1.loc[money_information_verify1['year'].isnull()]['ID'].values.tolist()
    # for i in range(len(pro_ID)):
    #     if pro_ID[i] in sum_nopro_ID:
    #         money_nopro_ID.append(pro_ID[i])
    # # 填充year表
    # pro_year_S = year_S[year_S == 2]
    # pro_ID = pro_year_S.index
    # for i in range(len(pro_ID)):
    #     years_list = money_information_verify1[money_information_verify1['ID']==pro_ID[i]]['year'].values.tolist()
    #     exist_year = year_report_verify1[year_report_verify1['ID']==pro_ID[i]][year_report_verify1['year'].notnull()]['year'].values.tolist()
    #     pro_index = year_report_verify1[year_report_verify1['ID']==pro_ID[i]][year_report_verify1['year'].isnull()].index.tolist()[0]
    #     year_report_verify1.loc[pro_index,'year'] = list(set(years_list)-set(exist_year))[0]
    # year_nopro_ID = []
    # sum_nopro_ID = year_report_verify1.loc[year_report_verify1['year'].isnull()]['ID'].values.tolist()
    # for i in range(len(pro_ID)):
    #     if pro_ID[i] in sum_nopro_ID:
    #         year_nopro_ID.append(pro_ID[i])
    #
    # # 此时year表已经被填充过了，用填充过了的year表做参照，填充money表
    # pro_ID = money_nopro_ID
    # for i in range(len(pro_ID)):
    #     years_list = year_report_verify1[year_report_verify1['ID']==pro_ID[i]]['year'].values.tolist()
    #     exist_year = money_information_verify1[money_information_verify1['ID']==pro_ID[i]][money_information_verify1['year'].notnull()]['year'].values.tolist()
    #     pro_index = money_information_verify1[money_information_verify1['ID']==pro_ID[i]][money_information_verify1['year'].isnull()].index.tolist()[0]
    #     money_information_verify1.loc[pro_index,'year'] = list(set(years_list)-set(exist_year))[0]
    #
    # # 用更新后的money表再更新year表
    # pro_ID = year_nopro_ID
    # for i in range(len(pro_ID)):
    #     years_list = money_information_verify1[money_information_verify1['ID']==pro_ID[i]]['year'].values.tolist()
    #     exist_year = year_report_verify1[year_report_verify1['ID']==pro_ID[i]][year_report_verify1['year'].notnull()]['year'].values.tolist()
    #     pro_index = year_report_verify1[year_report_verify1['ID']==pro_ID[i]][year_report_verify1['year'].isnull()].index.tolist()[0]
    #     year_report_verify1.loc[pro_index,'year'] = list(set(years_list)-set(exist_year))[0]

    # 根据上下文填充剩余的N/A年份（现在剩下的都是两个表中都缺失的年份数据，此部分自己用人工的方法已经试过了，发现数据排列很整齐，
    # 2015一堆、2016一堆、2017一堆，所以可以用上下文填充方法进行填充）
    money_information_verify1['year'].fillna(method='ffill',inplace=True)
    year_report_verify1['year'].fillna(method='ffill',inplace=True)

    # base_verify1 = pd.read_csv('base_verify1.csv',encoding='gbk')
    base_verify1 = pd.read_csv(base_verify_root,encoding='gbk')
    # 此时年份为空的数据全部处理完毕，开始将三年的特征整合到一行的多列里去
    money_ID = base_verify1['ID'].values.tolist()
    pro_money_dataframe = base_verify1
    feature = ['债权融资额度', '债权融资成本', '股权融资额度', '股权融资成本', '内部融资和贸易融资额度', '内部融资和贸易融资成本', '项目融资和政策融资额度', '项目融资和政策融资成本']
    year_report_feature = ['从业人数', '资产总额', '负债总额', '营业总收入', '主营业务收入', '利润总额', '净利润', '纳税总额', '所有者权益合计']
    year = [2015, 2016, 2017]
    # 先增加列名
    col_names = []
    for j in range(len(year)):
        for k in range(len(feature)):
            col_names.append('%s_%s' %(year[j], feature[k]))
        for k in range(len(year_report_feature)):
            col_names.append('%s_%s' %(year[j], year_report_feature[k]))
    start_len = len(pro_money_dataframe.columns.values.tolist())
    for i in range(len(col_names)):
        pro_money_dataframe['%s'%(col_names[i])] = ''
    lll = []
    from itertools import chain
    money_data = money_information_verify1.sort_values(by=["ID","year"])[feature].values
    year_data = year_report_verify1.sort_values(by=["ID","year"])[year_report_feature].values
    for i in range(len(money_ID)):
        # money_data = pd.DataFrame(money_information_verify1[money_information_verify1['ID']==money_ID[i]][feature]).values
        money_l = money_data[i*3:i*3+3,:].tolist()
        # year_data = pd.DataFrame(year_report_verify1[year_report_verify1['ID']==money_ID[i]][year_report_feature]).values
        year_l = year_data[i*3:i*3+3,:].tolist()
        ll = []
        for j in range(len(year)):
            ll.append(money_l[j])
            ll.append(year_l[j])
        ll = list(chain.from_iterable(ll))
        lll.append(ll)
    pro_money_dataframe.loc[0:len(money_ID), start_len:start_len + len(col_names)] = np.array(lll)
        # for j in range(len(year)):
        #     for k in range(len(feature)):
        #         # print(money_information_verify1[money_information_verify1['ID']==money_ID[i]][money_information_verify1['year']==year[j]][feature[k]].values[0])
        #         # pro_money_dataframe.loc[count,'%s_%s'%(year[j],feature[k])] = \
        #         #    money_information_verify1[money_information_verify1['ID']==money_ID[i]][money_information_verify1['year']==year[j]][feature[k]].values[0]
        #         pro_money_dataframe.loc[i, '%s_%s' % (year[j], feature[k])] = money_data[j][k]
        #     for k in range(len(year_report_feature)):
        #         # pro_money_dataframe.loc[count,'%s_%s'%(year[j],year_report_feature[k])] = \
        #         #    year_report_verify1[year_report_verify1['ID']==money_ID[i]][year_report_verify1['year']==year[j]][year_report_feature[k]].values[0]
        #         pro_money_dataframe.loc[i, '%s_%s' % (year[j], year_report_feature[k])] = year_data[j][k]


    # 这里是自己处理过的只结合三张表的情况（没有加专利的那张表，因为自己做过对比，发现专利表和base_verify表的ID顺序完全相同，
    # 自己后期是直接在excel里复制粘贴的专利表的数据，在这代码后自己用代码也实现了，但怕万一代码写错了，连前面这些跑的也失效了，
    # 故先生成一个csv保存已有数据）
    # pro_money_dataframe.to_csv('process_all_data_verify.csv')

    # 加入专利表
    # paient_information_verify1 = pd.read_csv('paient_information_verify1.csv',encoding='gbk')
    paient_information_verify1 = pd.read_csv(paient_information_verify_root,encoding='gbk')
    finally_data = pd.merge(pro_money_dataframe,paient_information_verify1,on='ID')
    # 生成最后的merge后的数据
    # finally_data.to_csv('process_all_data_verify.csv')
    return finally_data

# main函数 传参数的时候，分别按照顺序，传四个文件的路径即可，四个文件顺序不能错
# merge_data('base_verify1.csv', 'money_information_verify1.csv', 'year_report_verify1.csv', 'paient_information_verify1.csv')