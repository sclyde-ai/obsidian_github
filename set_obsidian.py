import json
from pathlib import Path
# import subprocess

def set_json(file_path, json_dict: dict):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for key, item in json_dict.items():
            data[key] = item
        
        with open(file_path, 'r', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"an error has occured: {e}")


if __name__ == '__main__':
    # give the auth 
    # subprocess(["chmod", "700", ])

    # obsidian setting
    app_setting = {
        "newFileLocation": "current",
        "attachmentFolderPath": "_添付 attachemnts"
    }
    set_json(".obsidian/app.json", app_setting)

    core_plugin_setting = {
          "daily-notes": False,
    }
    set_json(".obsidian/core-plugins.json", core_plugin_setting)

    # obsidian git setting
    file_path = ".obsidian/plugins/obsidian-git/data.json"
    file_path_obj = Path(file_path)
    if not file_path_obj.exists():
        file_path_obj.touch()
    data_setting = {
        "autoSaveInterval": 5,
        "autoPullOnBoot": True,
    }
    set_json(file_path, data_setting)