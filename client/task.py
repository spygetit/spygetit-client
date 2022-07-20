import subprocess
from dataclasses import dataclass
from typing import List

from client.resource import new_task_folder


@dataclass
class Task:
    workflow_name: str
    task_name: str
    cmd: List[str]


def run_task(task: Task):
    cwd = new_task_folder(task.workflow_name, task.task_name)
    stdout = cwd.joinpath('stdout')
    stderr = cwd.joinpath('stderr')
    with open(stdout, 'w') as f_out, open(stderr, 'w') as f_err:
        res = subprocess.run(args=task.cmd, cwd=cwd, stdout=f_out, stderr=f_err)
    return res.returncode, stdout, stderr
