from prefect import flow
from prefect.utilities.names import generate_slug

from project.flows.example.tasks.dummy import dummy


@flow()
def example_flow():
    items = [
        generate_slug(n_words=1) for _ in range(10)
    ]
    return dummy(items)
