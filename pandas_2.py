def main():
    import pandas

    df0 = pandas.read_csv(
        'data1.csv', encoding='utf-8'
    )
    day1 = "2021/5/10"
    # col_point = df0['kion_A']
    b = len(df0)
    cnt = 0
    for cnt in range(b - 1):
        day2 = df0.loc[cnt, "day"]
        if day1 == day2:
            a = cnt
            break
    for cnt in range(b - 1):
        c = a + cnt
        if df0.loc[c, "ruiseki"] < 2000:
            df0.loc[c + 1, "nisho1"] = df0.loc[c, "nisho1"] + (df0.loc[c, "nisho"])
            if df0.loc[c, "kion_L"] > 5:
                df0.loc[c + 1, "ruiseki"] = df0.loc[c, "ruiseki"] + (df0.loc[c, "kion_A"] - 5)
                df0.loc[c + 1, "ruiseki"] = round(df0.loc[c + 1, "ruiseki"], 1)
            print(df0.loc[c + 1, "ruiseki"])
            # print(df0.loc[c + 1, "nisho1"])

        else:
            # print(df0.loc[c, "day"])
            i = (df0.loc[c, "day"])
            i_2 = (df0.loc[c, "nisho1"])
            # return i,i_2
            print(i, i_2)


if __name__ == '__main__':
    main()

# df0.to_csv('data2.csv')
