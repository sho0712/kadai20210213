def main(day1):
    import pandas

    df0 = pandas.read_csv('data1.csv', encoding='utf-8')
    b = len(df0)
    for cnt in range(b - 1):
        day2 = df0.loc[cnt, "day"]
        if day1 == day2:
            a = cnt
            break

    for cnt in range(b - 1):
        c = a + cnt
        if df0.loc[c, "ruiseki"] < 2000:
            if df0.loc[c, "kion_L"] > 5:
                df0.loc[c + 1, "ruiseki"] = df0.loc[c, "ruiseki"] + (df0.loc[c, "kion_A"] - 5)
                df0.loc[c + 1, "ruiseki"] = round(df0.loc[c + 1, "ruiseki"], 1)
            print(df0.loc[c + 1, "ruiseki"])
        else:
            df0.to_csv('data2.csv')
            i = (df0.loc[c, "day"])
            return i
