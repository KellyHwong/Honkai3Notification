
# Developing Log
## 2018-05-01 21:59:16
Find useful resources:
[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
>The purpose of PyAutoGUI is to provide a cross-platform Python module for GUI automation for human beings. The API is designed to be as simple as possible with sensible defaults.
For example, here is the complete code to move the mouse to the middle of the screen on Windows, OS X, and Linux:

# ~~Honkai3Notification~~ [Deprecated]

## ~~原理~~
~~原理很简单，屏幕监控加图像匹配。~~
~~屏幕监控不同平台用的方法不一样，Mac用python os库调用系统命令，Ubuntu同理，不过命令不同。~~
~~图像匹配用的SIFT算法，OpenCV集成了，直接用就行。~~
~~发邮件要解决的问题是认证，Gmail的话把允许不受信任的应用打开。~~
## ~~使用场景~~
~~用虚拟机游戏挂机，等别人上线做任务（主要是师徒）。此时假设你有一台空闲的电脑，虚拟机也行。
好友上线后，需要把游戏虚拟机关掉，登自己的手机玩，或者直接用虚拟机玩。这种情况下你可以一边等朋友上线一边工作。
但是我想实现的是随时可以关闭挂机虚拟机的场景，比如我去吃饭，不在挂机用的机器旁边，手机能收到邮件，但是不能登录（因为那边挂机，手机登录会提示正在游戏中）。~~
## ~~Limitations~~
~~必须手动关闭游戏虚拟机才能让手机登录，这一点比较麻烦。米忽悠这登录设定的。
（永远不会Do的）TODO：想办法手机控制电脑，关闭游戏虚拟机。~~
