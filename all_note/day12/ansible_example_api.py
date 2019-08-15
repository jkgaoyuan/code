#!/usr/bin/env python
###只删除了 自定义输出
###2.7 版本
##参考 https://docs.ansible.com/ansible/2.7/dev_guide/developing_api.html
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C


# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
#options 是在执行命令时, 指定的选项,这些选项大部分使用,默认值
#connection 选项指的是链接方式
#local 表示本机执行 ssh 表示 通过ssh远程链接执行 become_user应该是 指定远程登录用户 None 默认和本机登录用户一致, 若ssh链接拒绝请查看 被控制的主机上是否存在 本机登录用户
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
##dataloader 用于将yaml / json 等文件 转换成为python的数据类型
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
##用于保存各种密码
passwords = dict(vault_pass='secret')

# Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets

# create inventory, use path to host config file as source or hosts in a comma separated string
### 主机清单文件,两种表示方式
### 一种是将各个主机用, 号分开的字符串
###另一种是将 主机清单文件路径保存到列表中
inventory = InventoryManager(loader=loader, sources='localhost,')
# 定义参数
# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source =  dict(
        name = "Ansible Play",
        hosts = 'localhost',       ###在那些目标执行命令
        gather_facts = 'no',       ##执行命令前不收集目标主机信息
        tasks = [                   ###调用那个模块,添加那些参数
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
### 创建 play的实例子
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
tqm = None
###创建 任务队列管理器,用于调用play
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)