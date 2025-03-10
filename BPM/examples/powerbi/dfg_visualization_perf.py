if True:
    # ignore this part in true PowerBI executions
    from pm4py.objects.log.adapters.pandas import csv_import_adapter

    dataset = csv_import_adapter.import_dataframe_from_path("C:/running-example.csv")

import pandas as pd

# this part is required because the dataframe provided by PowerBI has strings
dataset["time:timestamp"] = pd.to_datetime(dataset["time:timestamp"])

from pm4py.algo.discovery.dfg.adapters.pandas import df_statistics

dfg = df_statistics.get_dfg_graph(dataset, measure="performance")

from pm4py.statistics.attributes.pandas import get as attributes_get

activities_count = attributes_get.get_attribute_values(dataset, "concept:name")

from pm4py.statistics.start_activities.pandas import get as sa_get

start_activities = sa_get.get_start_activities(dataset)
from pm4py.statistics.end_activities.pandas import get as ea_get

end_activities = ea_get.get_end_activities(dataset)

from pm4py.visualization.dfg import visualizer

gviz = visualizer.apply(dfg, activities_count=activities_count, variant=visualizer.Variants.PERFORMANCE,
                        parameters={"start_activities": start_activities, "end_activities": end_activities})
visualizer.matplotlib_view(gviz)
