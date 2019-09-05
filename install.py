import sys
import os


def set_venv_dir():
    file_data = ""
    venv_path = os.path.join(sys.path[0], "venv")
    activate_path = os.path.join(venv_path, "Scripts") + "\\activate.bat"
    with open(file=activate_path, mode="r+", encoding="utf-8") as activate_bat:
        for line in activate_bat:
            # print(line)
            if "set \"VIRTUAL_ENV=" in line:
                line = "set \"VIRTUAL_ENV=" + venv_path + "\"\n"
            file_data += line

    with open(file=activate_path, mode="w", encoding="utf-8") as activate_bat:
        activate_bat.write(file_data)


def set_pyvenv_cfg():
    pyvenv_path = os.path.join(sys.path[0], "venv") + "\\pyvenv.cfg"
    # DO NOT RUN THIS SCRIPT AT IDE ENVIRONMENT, IT MAY CAUSE UNPREDICTABLE PROBLEM.
    python_install_path = sys.path[4]
    python_version = sys.version.split(" ")[0]
    file_data = "home = " + python_install_path + \
                "\ninclude-system-site-packages = false\nversion = " + python_version + "\n"
    with open(file=pyvenv_path, mode="w", encoding="utf-8") as pyvenv_cfg:
        pyvenv_cfg.write(file_data)


if __name__ == '__main__':
    set_venv_dir()
    set_pyvenv_cfg()
