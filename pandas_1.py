def main():
    import pandas

    df0 = pandas.read_csv(
        'data1.csv', encoding='utf-8'
    )
    # print(col_point.sum())

    # print(df0.loc[4, "ruiseki"])

    # print(df0.count())

    col_point = df0['kion_A']
    # print(b)

    b = len(df0)
    cnt = 0
    # day1 = input("田植え日")

    day1 = "2021/5/10"

    for cnt in range(b - 1):
        day2 = df0.loc[cnt, "day"]
        # print(day1)
        # print(day2)
        if day1 == day2:
            # print("OK")
            # print(cnt)
            a = cnt
            print(a)
            break
    print(a)

    for cnt in range(b - 1):
        c = a + cnt
        print(c)
        if df0.loc[c, "ruiseki"] < 1850:
            if df0.loc[c, "kion_A"] > 5:
                df0.loc[c + 1, "ruiseki"] = df0.loc[c, "ruiseki"] + (df0.loc[c, "kion_L"] - 5)
                df0.loc[c + 1, "ruiseki"] = round(df0.loc[c + 1, "ruiseki"], 1)
            print(df0.loc[c + 1, "ruiseki"])
        else:
            print(df0.loc[c, "day"])
            i = (df0.loc[c, "day"])
            return i

            break
    df0.to_csv('data2.csv')


if __name__ == '__main__':
    main()
