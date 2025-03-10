if True:
    # ignore this part in true PowerBI executions
    from pm4py.objects.log.adapters.pandas import csv_import_adapter

    dataset = csv_import_adapter.import_dataframe_from_path("C:/running-example.csv")

import pandas as pd
# this part is required because the dataframe provided by PowerBI has strings
dataset["time:timestamp"] = pd.to_datetime(dataset["time:timestamp"])

from pm4py.statistics.traces.pandas import case_statistics
from pm4py.visualization.graphs import visualizer as graphs_visualizer

x_cases, y_cases = case_statistics.get_kde_caseduration(dataset)

graph_cases = graphs_visualizer.apply(x_cases, y_cases, variant=graphs_visualizer.Variants.CASES,
                                      parameters={graphs_visualizer.Variants.CASES.value.Parameters.FORMAT: "png"})

graphs_visualizer.matplotlib_view(graph_cases)
