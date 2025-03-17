import pandas as pd

def stat_analysis(df):
    sDev = df.std()
    print("\nThe standard deviations are:\n", sDev)

    describe = df.describe()
    print("\nThe descriptive results are:\n", describe)

    kurt = df.kurt()
    print("\nThe kurt results are:\n", kurt)

    skew = df.skew()
    print("\nThe skew results are:\n", skew)

    quantile = df.quantile()
    print("\nThe quantile results are:\n", quantile)


def mpg_gears(df):
    mpgGears = df[['mpg', 'gear']]
    describe = mpgGears.describe()
    print("\nThe descriptive stats for mpg and gear are:\n", describe)

    sDev = mpgGears.std()
    print("\nThe standard deviations for mpg and gear are:\n", sDev)

    gear3 = mpgGears[mpgGears['gear'] == 3]
    gear4 = mpgGears[mpgGears['gear'] == 4]
    gear5 = mpgGears[mpgGears['gear'] == 5]

    # Gear3 ------------------------------------------------------------------
    describe3 = gear3['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 3 Gears are:\n", describe3)

    sDev3 = gear3['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 3 Gears are:\n", sDev3)

    # Gear4 ------------------------------------------------------------------
    describe4 = gear4['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 4 Gears are:\n", describe4)

    sDev4 = gear4['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 4 Gears are:\n", sDev4)

    # Gear5 ------------------------------------------------------------------
    describe5 = gear5['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 5 Gears are:\n", describe5)

    sDev5 = gear5['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 5 Gears are:\n", sDev5)


def mpg_carb(df):
    mpgCarb = df[['mpg', 'carb']]

    describe = mpgCarb.describe()
    print("\nThe descriptive stats for mpg and carb are:\n", describe)

    sDev = mpgCarb.std()
    print("\nThe standard deviations for mpg and carb are:\n", sDev)

    carb1 = mpgCarb[mpgCarb['carb'] == 1]
    carb2 = mpgCarb[mpgCarb['carb'] == 2]
    carb3 = mpgCarb[mpgCarb['carb'] == 3]
    carb4 = mpgCarb[mpgCarb['carb'] == 4]
    carb6 = mpgCarb[mpgCarb['carb'] == 6]
    carb8 = mpgCarb[mpgCarb['carb'] == 8]

    # Carb1 ------------------------------------------------------------------
    describe1 = carb1['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 1 Carb are:\n", describe1)

    sDev1 = carb1['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 1 Carb are:\n", sDev1)

    # Carb2 ------------------------------------------------------------------
    describe2 = carb2['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 2 Carb are:\n", describe2)

    sDev2 = carb2['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 3 Carb are:\n", sDev2)

    # Carb3 ------------------------------------------------------------------
    describe3 = carb3['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 3 Carb are:\n", describe3)

    sDev3 = carb3['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 3 Carb are:\n", sDev3)

    # Carb4 ------------------------------------------------------------------
    describe4 = carb4['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 4 Carb are:\n", describe4)

    sDev4 = carb4['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 4 Carb are:\n", sDev4)

    # Carb6 ------------------------------------------------------------------
    describe6 = carb6['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 6 Carb are:\n", describe6)

    sDev6 = carb6['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 6 Carb are:\n", sDev6)

    # Carb8 ------------------------------------------------------------------
    describe8 = carb8['mpg'].describe()
    print("\nThe descriptive MPG stats for vehicles with 8 Carb are:\n", describe8)

    sDev8 = carb8['mpg'].std()
    print("\nThe standard deviations of MPG for vehicles with 8 Carb are:\n", sDev8)

def mpg_corr(df):
    corr = df.corr()

    print(corr)
    print("The wt has the most impact on the mpg with a correlation value of -.867659")



df = pd.read_csv(r'mtcars.csv')
print(df)

stat_analysis(df)
mpg_gears(df)
mpg_carb(df)
mpg_corr(df)