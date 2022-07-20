"""Create pipeline files function"""
import os
import yaml


def create_pipelines_files(project_root, schedules):
    """Create pipeline files from provided schedules into project_root/plugins"""
    pipelines_dir = project_root + "/pipelines"

    if not os.path.exists(pipelines_dir):
        os.mkdir(project_root + "/pipelines")

    if schedules:
        for job in schedules.get("schedules", {}).get("job"):

            run_actions_list = job.get("job", {}).get("tasks")[0].split()

            data_components_list = []
            for action in run_actions_list:
                data_components_list.append(action.split(":")[0])

            data_components_list = list(dict.fromkeys(data_components_list))

            pipeline = {}
            pipeline["version"] = "pipelines/v0.1"
            pipeline["data_components"] = data_components_list
            pipeline["actions"] = run_actions_list
            pipeline["schedule"] = job.get("cron_interval")

            with open(
                pipelines_dir + "/" + job["name"] + ".yml", "w", encoding="utf-8"
            ) as outfile:
                yaml.dump(pipeline, outfile, default_flow_style=False, sort_keys=False)
