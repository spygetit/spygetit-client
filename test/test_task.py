import shutil
from multiprocessing.pool import ThreadPool
from pathlib import Path
from threading import Thread
from unittest import TestCase

from client.resource import init_settings, SETTINGS
from client.task import Task, run_task


class Test(TestCase):
    def setUp(self):
        init_settings(Path(__file__).parent.joinpath('settings.ini'))
        test_dir = Path(SETTINGS['FOLDERS']['MAIN']).joinpath("Test_WF")
        if test_dir.exists():
            shutil.rmtree(test_dir)
        self.task = Task("Test_WF", "Test_Task", ['ping', '-n', '5', 'google.com'])

    def test_run_task(self):
        run_task(self.task)

    def test_run_in_thread(self):
        thread = Thread(target=run_task, args=(self.task,))
        thread.start()
        thread.join(timeout=15)

    def test_run_in_pool(self):
        task1 = Task("Test_WF", "Test_Task_1", ['ping', '-n', '5', 'google.com'])
        task2 = Task("Test_WF", "Test_Task_2", ['ping', '-n', '5', 'google.com'])
        with ThreadPool() as pool:
            pool.map(run_task, (task1, task2))

