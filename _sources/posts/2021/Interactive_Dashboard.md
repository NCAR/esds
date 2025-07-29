---
author: Max Grover
date: 2021-3-19
tags: dashboard, jupyter
---

# HiRes-CESM Interactive Dashboard Example

In this example, our goal is to create an interactive dashboard, using images already output on a remote server.

We are specifically interested in looking at plots created using the [HighRes-CESM-Analysis](https://github.com/marbl-ecosys/HiRes-CESM-analysis) repository.

Images created by this package can be visualized through an interactive
dashboard using [Panelify](https://github.com/andersy005/panelify)

```python
import pandas as pd
import panel as pn
import panelify

pn.extension()
```

---

## Accessing the Data (Plots)

The plots from this example are stored on the
[CGD webext machine](https://webext.cgd.ucar.edu/), specifically from
[this specific case](https://webext.cgd.ucar.edu/g.e22b05.G1850ECOIAF_JRA.TL319_g17.cocco.001/),
which we use as the path.

```python
paths = (
    "https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA_HR.TL319_t13.004/",
    "https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA_HR.TL319_t13.003/",
)
```

### Read in the CSV File Containing Metadata

We use pandas to remotely read in the data, dropping the Unnamed column, and
merging the absolute path to the directory and the relative filepaths

```python
df_list = []
for path in paths:
    df = pd.read_csv(f"{path}png_catalog.csv").drop(columns="Unnamed: 0")

    # Convert the relative filepaths to absolute filepaths
    df["absolute_filepath"] = path + df.filepath.astype(str)

    df_list.append(df)

# Merge the dataframes
df = pd.concat(df_list)
```

```python
df
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>plot_type</th>
      <th>varname</th>
      <th>casename</th>
      <th>apply_log10</th>
      <th>time_period</th>
      <th>isel_dict</th>
      <th>filepath</th>
      <th>date</th>
      <th>absolute_filepath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>histogram</td>
      <td>CaCO3_FLUX_100m</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.004</td>
      <td>False</td>
      <td>0001-01-01_0001-12-31</td>
      <td>{}</td>
      <td>histogram/CaCO3_FLUX_100m.0001-01-01_0001-12-3...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>histogram</td>
      <td>CaCO3_FLUX_100m</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.004</td>
      <td>True</td>
      <td>0001-01-01_0001-12-31</td>
      <td>{}</td>
      <td>histogram/CaCO3_FLUX_100m.0001-01-01_0001-12-3...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>histogram</td>
      <td>CaCO3_FLUX_100m</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.004</td>
      <td>False</td>
      <td>0002-01-01_0002-12-31</td>
      <td>{}</td>
      <td>histogram/CaCO3_FLUX_100m.0002-01-01_0002-12-3...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>histogram</td>
      <td>CaCO3_FLUX_100m</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.004</td>
      <td>True</td>
      <td>0002-01-01_0002-12-31</td>
      <td>{}</td>
      <td>histogram/CaCO3_FLUX_100m.0002-01-01_0002-12-3...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>histogram</td>
      <td>CaCO3_FLUX_100m</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.004</td>
      <td>False</td>
      <td>0003-01-01_0003-12-31</td>
      <td>{}</td>
      <td>histogram/CaCO3_FLUX_100m.0003-01-01_0003-12-3...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>719</th>
      <td>trend_map</td>
      <td>SiO3</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.003</td>
      <td>NaN</td>
      <td>0002-01-01_0004-12-31</td>
      <td>{'z_t': 0}</td>
      <td>trend_map/SiO3.0002-01-01_0004-12-31.z_t--3510...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>720</th>
      <td>trend_map</td>
      <td>SiO3</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.003</td>
      <td>NaN</td>
      <td>0003-01-01_0004-12-31</td>
      <td>{'basins': 0}</td>
      <td>trend_map/SiO3.0003-01-01_0004-12-31.basins--A...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>721</th>
      <td>trend_map</td>
      <td>SiO3</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.003</td>
      <td>NaN</td>
      <td>0003-01-01_0004-12-31</td>
      <td>{'basins': 0}</td>
      <td>trend_map/SiO3.0003-01-01_0004-12-31.basins--G...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>722</th>
      <td>trend_map</td>
      <td>SiO3</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.003</td>
      <td>NaN</td>
      <td>0003-01-01_0004-12-31</td>
      <td>{'basins': 0}</td>
      <td>trend_map/SiO3.0003-01-01_0004-12-31.basins--I...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
    <tr>
      <th>723</th>
      <td>trend_map</td>
      <td>SiO3</td>
      <td>g.e22.G1850ECO_JRA_HR.TL319_t13.003</td>
      <td>NaN</td>
      <td>0003-01-01_0004-12-31</td>
      <td>{'basins': 0}</td>
      <td>trend_map/SiO3.0003-01-01_0004-12-31.basins--P...</td>
      <td>NaN</td>
      <td>https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA...</td>
    </tr>
  </tbody>
</table>
<p>1969 rows × 9 columns</p>
</div>

### Dealing with Relative vs. Absolute Paths

In the previous cell, we edited the filepaths... that is because the image filepaths are relative paths, but we would ideally like absolute paths. We make use of the dataframe path to assign the new absolute filepaths. An example is given below.

```python
print("Original filepath: ", df.filepath.values[0])

# Convert the relative filepaths to absolute filepaths
df["filepath"] = path + df.filepath.astype(str)

print("New filepath ", df.filepath.values[0])
```

    Original filepath:  histogram/CaCO3_FLUX_100m.0001-01-01_0001-12-31.png
    New filepath  https://webext.cgd.ucar.edu/g.e22.G1850ECO_JRA_HR.TL319_t13.003/histogram/CaCO3_FLUX_100m.0001-01-01_0001-12-31.png

---

### Build the Dashboard

First, we check which types of plots are included in the analysis.

```python
df.plot_type.unique()
```

    array(['histogram', 'summary_map', 'time_series', 'trend_hist',
           'trend_map'], dtype=object)

Although there are five different plot types, we focus on the first three.

```python
# Since we are using https, we leave this dictionary empty
storage_options = {}

# Create the timestep dashboard
summary_map = panelify.create_dashboard(
    keys=["casename", "varname", "date", "apply_log10"],
    df=df.loc[df.plot_type == "summary_map"],
    path_column="absolute_filepath",
    storage_options=storage_options,
    column_widget_types={"date": "discrete_slider"},
)

# Create the timeseries dashboard
time_series = panelify.create_dashboard(
    keys=[
        "casename",
        "varname",
    ],
    df=df.loc[df.plot_type == "time_series"],
    path_column="absolute_filepath",
    storage_options=storage_options,
)

# Create the histogram dashboard
histogram = panelify.create_dashboard(
    keys=["casename", "varname", "time_period", "apply_log10"],
    df=df.loc[df.plot_type == "histogram"],
    path_column="absolute_filepath",
    storage_options=storage_options,
    column_widget_types={"time_period": "discrete_slider"},
)

# Bring the various dashboard components into a single canvas
canvas = panelify.Canvas(
    {
        "Summary Map": summary_map.view,
        "Time Series": time_series.view,
        "Histogram": histogram.view,
    }
)
```

### Run the Dashboard Inline

Now that we have built the dashboard, we run it within the notebook.

```python
hv_logo = '<a href="https://holoviz.org"><img src="https://holoviz.org/assets/holoviz-logo-stacked.svg" width=80></a>'
thumbnail = '<a href="https://github.com/marbl-ecosys/"><img src="https://raw.githubusercontent.com/NCAR/cesm-lens-aws/master/thumbnail.png" width=80 height=80></a>'
menu_background = "#659dbd"
menu_text = "<div><p>0.1 degree POP / CICE run with ocean BGC</p><br><br><p><a href='https://github.com/marbl-ecosys/HiRes-CESM-analysis'>HiRes-CESM analysis repo</a></p><p><a href='https://github.com/andersy005/HiRes-CESM-dashboard'>HiRes-CESM dashboard repo</a></p></div><br><br>"
menu = pn.Column(
    menu_text,
    pn.Row(
        pn.Spacer(width=10),
        pn.Pane(thumbnail),
        pn.Spacer(width=10),
        pn.Pane(hv_logo),
    ),
    background=menu_background,
)

dashboard = pn.Row(menu, canvas.show())
dashboard.servable("HiRes-CESM Diagnostics Dashboard")
```

Since these plots are not rendered directly in this notebook online, here is the ouput deployed using Dokku/Heroku

[![https://img.shields.io/badge/%E2%86%91_Deploy_to-Heroku-7056bf.svg](http://img.shields.io/badge/%E2%86%91_launch_dashboard_on-Heroku-7056bf.svg)](https://hires-cesm-analysis.dokku.projectpythia.org/Interactive_Dashboard)
