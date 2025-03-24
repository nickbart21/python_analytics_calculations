import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
housing_df = pd.read_csv('california_housing.csv')

#housing_df_encoded.hist(figsize=(12, 10), bins=30, edgecolor="black")
#plt.subplots_adjust(hspace=0.7, wspace=0.4)
#plt.show()

sns.scatterplot(
    data=housing_df,
    x="longitude",
    y="latitude",
    size="median_house_value",
    hue="median_house_value",
    palette="viridis",
    alpha=0.5,
)
plt.legend(title="MedHouseVal", bbox_to_anchor=(1.05, 0.95), loc="upper left")
_ = plt.title("Median house value depending of\n their spatial location")
plt.tight_layout()
plt.show()
