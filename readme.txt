predict_data.py是主文件，内容如下：
	1. 最外层套了一个predict(base_root,money_report_root,year_report_root,paient_information_root)函数，
	该函数有四个传入参数，分别是四个文件的路径。调用这个函数后可以直接生成预测的flag文件——result.csv。

	2.predict函数中的功能：
		2.1 调用merge_data文件实现将四个表进行预处理并连接四张表。
		2.2 做特征工程，生成新特征对应的数据
		2.3 加载verify_catboost模型，对数据进行预测
		2.4生成预测结果（生成result.csv）