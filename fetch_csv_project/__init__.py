from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    sensor,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager, 
    RunRequest,
    
)


from . import assets

all_assets = load_assets_from_modules([assets])

#define a job that will materialize the assets
contract_job = define_asset_job("contract_job", selection=AssetSelection.all())

#ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
contract_schedule = ScheduleDefinition(
    job=contract_job,
    cron_schedule="0 * * * *",  # every hour
)


@sensor(
    name="contract_api_sensor",
    asset_selection=AssetSelection.all(),
    # interval=Interval(
    #     seconds=30,
    # ),
)
def contract_api_sensor():
    # """A sensor that checks for changes to the contract API assets."""
    # return RunRequest(
    #     operation_id="contract_api_sensor",
    #     assets_to_check=AssetSelection.all(),
    # )
    return RunRequest()


io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
)


defs = Definitions(
    assets=all_assets,
    jobs=[contract_job], 
    schedules=[contract_schedule],
    resources={
        "io_manager": io_manager,
    },
    sensors=[contract_api_sensor],  
)




