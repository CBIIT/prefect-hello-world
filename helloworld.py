from prefect import flow, task, get_run_logger
from prefect.run_configs import ECSRun

@task
def helloworld():
    return("Hello from Prefect.")


@flow(name="Hello World", run_config=ECSRun(cpu="2 vcpu", memory="4 GB"))
def runner():
    logger = get_run_logger()
    logger.info(helloworld())

if __name__ == "__main__":
    runner()
