import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import(
    MaxAbsScaler,
    MinMaxScaler,
    Normalizer,
    PowerTransformer,
    QuantileTransformer,
    RobustScaler,
    StandardScaler,
    minmax_scale)

pd.set_option('display.max_columns', None)
housing_df = pd.read_csv('california_housing.csv')
#print(housing_df.info())
#print(housing_df.describe())
df_sample = housing_df.head()
#print(df_sample)


feature_mapping = {
    "median_income": "Median income on block",
    "housing_median_age": "Median house age on block",
    "total_rooms": "Average number of total rooms in house on block",
    "total_bedrooms": "Average number of bedrooms in house on block",
    "population": "Block population",
    "households": "Number of households on block",
    "latitude": "House block latitude",
    "longitude": "House block longitude",
    "ocean_proximity": "Relative proximity to the ocean"
}
# for k, v in feature_mapping.items():
#     print(f"{k} : {v}")

#### Encoding string categorical variable ####

#print(housing_df['ocean_proximity'].unique()) # result: 5 different categories
lbl_encoder = LabelEncoder()
housing_df['ocean_encoded'] = lbl_encoder.fit_transform(housing_df['ocean_proximity'])
#print(housing_df)
housing_df_encoded = housing_df.drop(['ocean_proximity'], axis=1)
#print(housing_df_encoded.head())


X = housing_df_encoded[['median_income', 'total_rooms']]
y = housing_df_encoded.median_house_value
#print(X.head())

# These are the features that will be displayed on X and Y axes
features = ['median_income', 'total_rooms']

#Different normalizations
distributions = [
    ("Unscaled data", X),
    ("Data after standard scaling", StandardScaler().fit_transform(X)),
    ("Data after min-max scaling", MinMaxScaler().fit_transform(X)),
    ("Data after max-abs scaling", MaxAbsScaler().fit_transform(X)),
    ("Data after robust scaling", RobustScaler(quantile_range=(25, 75)).fit_transform(X)),
    ("Data after power transformation (Yeo-Johnson)",
        PowerTransformer(method="yeo-johnson").fit_transform(X)),
    ("Data after power transformation (Box-Cox)",
        PowerTransformer(method="box-cox").fit_transform(X)),
    ("Data after quantile transformation (uniform pdf)",QuantileTransformer(
            output_distribution="uniform", random_state=42).fit_transform(X)),
    ("Data after quantile transformation (gaussian pdf)", QuantileTransformer(
            output_distribution="normal", random_state=42).fit_transform(X)),
    ("Data after sample-wise L2 normalizing", Normalizer().fit_transform(X))
]

# scale the output between 0 and 1 for the colorbar
y_axis_scale = minmax_scale(y)
cmap = getattr(cm, "plasma_r", cm.hot_r)

def create_axes(title, figsize=(16, 6)):
    fig = plt.figure(figsize=figsize)
    fig.suptitle(title)

    # define the axis for the first plot
    left, width = 0.1, 0.22
    bottom, height = 0.1, 0.7
    bottom_h = height + 0.15
    left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.1]
    rect_histy = [left_h, bottom, 0.05, height]

    ax_scatter = plt.axes(rect_scatter)
    ax_histx = plt.axes(rect_histx)
    ax_histy = plt.axes(rect_histy)

    # define the axis for the zoomed-in plot
    left = width + left + 0.2
    left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.1]
    rect_histy = [left_h, bottom, 0.05, height]

    ax_scatter_zoom = plt.axes(rect_scatter)
    ax_histx_zoom = plt.axes(rect_histx)
    ax_histy_zoom = plt.axes(rect_histy)

    # define the axis for the colorbar
    left, width = width + left + 0.13, 0.01

    rect_colorbar = [left, bottom, width, height]
    ax_colorbar = plt.axes(rect_colorbar)

    return (
        (ax_scatter, ax_histy, ax_histx),
        (ax_scatter_zoom, ax_histy_zoom, ax_histx_zoom),
        ax_colorbar
    )

def plot_distribution(axes, X, y, hist_nbins=50, title="", x0_label="", x1_label=""):
    ax, hist_X1, hist_X0 = axes

    ax.set_title(title)
    ax.set_xlabel(x0_label)
    ax.set_ylabel(x1_label)

    # The scatter plot
    norm = mpl.colors.Normalize(y.min(), y.max())
    cmap1 = plt.get_cmap('plasma_r')
    ax.scatter(X[:,0], X[:,1], alpha=0.5, marker="o", s=5, lw=0, c=(norm(y)), cmap=cmap1)

    # Removing the top and the right spine for aesthetics
    # make nice axis layout
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines["left"].set_position(("outward", 10))
    ax.spines["bottom"].set_position(("outward", 10))

    # Histogram for axis X1 (feature 5)
    hist_X1.set_ylim(ax.get_ylim())
    hist_X1.hist(
        X[:, 1], bins=hist_nbins, orientation="horizontal", color="grey", ec="grey"
    )
    hist_X1.axis("off")

    # Histogram for axis X0 (feature 0)
    hist_X0.set_xlim(ax.get_xlim())
    hist_X0.hist(
        X[:, 0], bins=hist_nbins, orientation="vertical", color="grey", ec="grey"
    )
    hist_X0.axis("off")

def make_plot(item_idx):
    title, X = distributions[item_idx]
    ax_zoom_out, ax_zoom_in, ax_colorbar = create_axes(title)
    axarr = (ax_zoom_out, ax_zoom_in)
    plot_distribution(
        axarr[0],
        X,
        y,
        hist_nbins=200,
        x0_label=feature_mapping[features[0]],
        x1_label=feature_mapping[features[1]],
        title="Full data"
    )

    # zoom-in
    zoom_in_percentile_range = (0, 99)
    cutoffs_X0 = np.percentile(X[:, 0], zoom_in_percentile_range)
    cutoffs_X1 = np.percentile(X[:, 1], zoom_in_percentile_range)

    non_outliers_mask = np.all(X > [cutoffs_X0[0], cutoffs_X1[0]], axis=1) & np.all(
        X < [cutoffs_X0[1], cutoffs_X1[1]], axis=1
    )
    plot_distribution(
        axarr[1],
        X[non_outliers_mask],
        y[non_outliers_mask],
        hist_nbins=50,
        x0_label=feature_mapping[features[0]],
        x1_label=feature_mapping[features[1]],
        title="Zoom-in"
    )

    norm = plt.Normalize(y.min(), y.max())
    cmap1 = plt.get_cmap('plasma_r')
    mpl.colorbar.ColorbarBase(
        ax_colorbar,
        cmap=cmap1,
        norm=norm,
        orientation="vertical",
        label="Color mapping for values of y"
    )
    plt.show()

#make_plot(0)
make_plot(1)
make_plot(2)
make_plot(3)
make_plot(4)
make_plot(5)
make_plot(6)
make_plot(7)
make_plot(8)
make_plot(9)