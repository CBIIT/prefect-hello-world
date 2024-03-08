import dask
from prefect import flow, task, get_run_logger
from prefect_dask.task_runners import DaskTaskRunner

@task
def helloworld():
    return("Hello from Prefect.")


@flow(name="Hello World", task_runner=DaskTaskRunner(cluster_class="dask_cloudprovider.aws.FargateCluster",cluster_kwargs={"n_workers": 4, "threads_per_worker": 2}))
def runner():
    logger = get_run_logger()
    logger.info(helloworld())

if __name__ == "__main__":
    runner()
