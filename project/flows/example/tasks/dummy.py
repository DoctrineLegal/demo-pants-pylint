from prefect import task


@task()
def dummy(items: list[str]) -> list[str]:
    for item in items:
        print(item)
    return items
