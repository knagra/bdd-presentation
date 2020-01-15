import subprocess


def before_scenario(context, scenario):
    p = subprocess.Popen(["rm", "data_store.txt"])
    p.wait()
