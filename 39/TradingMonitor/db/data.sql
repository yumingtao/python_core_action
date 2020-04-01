/*
注意直接通过pycharm查询窗口，手动插入数据，timestamp会是long型表示
这样在页面上显示的为None，所以使用sql语句插入数据，这样就没有问题
*/
INSERT INTO TradingMonitor_position (asset, timestamp, amount)
VALUES ('btc', datetime('now'), 100);
INSERT INTO TradingMonitor_position (asset, timestamp, amount)
VALUES ('btc', datetime('now'), 200);
INSERT INTO TradingMonitor_position (asset, timestamp, amount)
VALUES ('btc', datetime('now'), 300);