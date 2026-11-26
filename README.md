# pairwise-mahjong-wall-order

## 领域

游戏、图形与多媒体

## 主题

麻将牌墙摸打顺序与鸣牌改序

## 说明

摸牌指针按事件重算、鸣牌回退与重放、牌头牌尾双指针。

初始状态下 `game/mahjong_wall.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
