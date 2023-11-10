
# azureml-core of version 1.0.72 or higher is required
# azureml-dataprep[pandas] of version 1.1.34 or higher is required
from azureml.core import Workspace, Dataset

subscription_id = '79b61b4b-31ad-40cc-8a3d-fe4412d50036'
resource_group = 'LearningAI'
workspace_name = 'Learning_AI'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='Main_datatest')
dataset.to_pandas_dataframe()
