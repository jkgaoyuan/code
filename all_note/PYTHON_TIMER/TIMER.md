Python实现定时器
(注意啊 该实验环境 是虚拟的 需要安装 部分包请在pycharm的解释器中进行安装)
https://blog.51cto.com/cloumn/blog/1748

使用threading 实现 延时
   
   
    通过无限循环的方式实现定时计划的执行
    TIMER-Threading-Cycle.py
   
    延迟调用实现倒数计时 
    Timer-Threading-Countdown.py
    
 使用 apschedule 模块实现定时器
    pip install apscheuduler
    
    导入 datetime 模块，用于打印当前时间</p>
<p>导入调度器模块 BlockingScheduler，这是最简单的调度器，调用 start 方式阻塞当前进程，如果你的程序只用于调度，除了调度进程外没有其他后台进程，那么请用 BlockingScheduler 非常有用，此时调度进程相当于守护进程。</p>
<p>定义一个函数 tick 代表我们要调度的作业程序.</p>
<p>实例化BlockingScheduler 类，不带参数表明使用默认的作业存储器，最大的默认并发线程为10个。</p>
<p><code>scheduler.add_job</code>  用于添加一个作业 <code>tick</code>，触发器为 interval，每隔 3 秒执行一次。（另外的两个触发器分别为 date，cron。date 按特定时间点触发，cron 则按固定的时间间隔触发）。同时加入异常捕获，捕获的异常内容是什么呢？— <code>KeyboardInterrupt</code> 表示 用户终端执行（也就是我们常用的CTRL+C），<code>SystemExit</code> 表示解释器异常退出。最后 <code>pass</code> 关键字表示如有这两种异常的话，什么也不做。</p>
<p>执行结果如下：<br/><img src="https://s4.51cto.com/images/blog/202004/27/69cbd8294fc04d03ed2fb8af97e28519.png" alt="" /></p>
可以看出，每3秒会打印当前的时间。
