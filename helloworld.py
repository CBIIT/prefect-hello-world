from prefect import flow, task, get_run_logger

@task
def helloworld():
    return("Hello from Prefect.")
    

@flow(name="Hello World")
def runner():
    logger = get_run_logger()
    logger.info(helloworld())

if __name__ == "__main__":
    runner()
