import json
from pathlib import Path

def set_json(file_path, json_dict: dict):
    try:
        with file_path.open('r', encoding='utf-8') as f:
            data = json.load(f)

        for key, item in json_dict.items():
            data[key] = item
        
        with file_path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        print(f"an error has occured: {e}")

def set_obsidian_json(file_name, json_dict: dict):
    file_path = ".obsidian/" + file_name
    set_json(file_path, json_dict)

def set_obsidian_git_json(file_name, json_dict: dict):
    file_path = ".obsidian/plugins/obsidian-git" + file_name
    set_json(file_path, json_dict)


if __name__ == '__main__':
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
    data_setting = {
        "autoSaveInterval": 5,
        "autoPullOnBoot": True,
    }
    set_json(".obsidian/plugins/obsidian-git/data.json", data_setting)