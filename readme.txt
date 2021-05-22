predict_data.py是主文件，内容如下：
	1. 最外层套了一个predict(base_root,money_report_root,year_report_root,paient_information_root)函数，
	该函数有四个传入参数，分别是四个文件的路径。调用这个函数后可以直接生成预测的flag文件——result.csv。

	2.predict函数中的功能：
		2.1 调用merge_data文件实现将四个表进行预处理并连接四张表。
		2.2 做特征工程，生成新特征对应的数据
		2.3 加载verify_catboost模型，对数据进行预测
		2.4生成预测结果（生成result.csv）
		
第一次上传的三个文件只包含最终的数据处理方式，包括全部的数据预处理、特征工程的结果（特征经特征组合之后再特征筛选之后的结果）、训练好的CatBoost模型（可以直接调用并进行预测），并不包括如何进行的特征工程以及特征筛选，也不包括训练CatBoost模型的代码
