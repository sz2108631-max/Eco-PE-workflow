# 结果与交付契约

最低产物：研究规格、design.md、唯一执行入口、环境清单、数据审计、合并审计、样本流水、变量字典、模型清单、执行日志、主表及机器可读结果、方法诊断、run_report。没有发生合并时审计标记不适用及原因，不生成虚构记录。

模型清单每列一行：model_id、code、estimand、outcome、treatment、sample_rule、controls、FE、SE_method、cluster、weights、N、N_clusters、result_path、table_column。机器可读结果存 term、estimate、SE、CI、p、单位；不适用字段注明原因。

表格说明因变量单位、样本、FE、SE、聚类、权重和显著性阈值；主文表只放能回答研究问题的列，不强制六列递进。图有轴标签、单位、基期、CI及样本说明；保存可编辑格式与分享格式。

写作顺序：估计方向和大小 → 单位与有意义的比较 → 不确定性 → 对应识别假设 → 适用人群和外推限制。对数、交互和非线性系数按正确尺度解释，避免混淆百分比与百分点。

修稿对照表逐项记录 reviewer_request、response、code_change、evidence、manuscript_location、status。未做的请求解释原因，不声称已补分析。

## 状态

- 完成：规格内产物齐全、核心检查通过、全新运行和重复比较成功。
- 有限制完成：用户接受明确范围，识别或数据限制完整披露。
- 未验证：代码/模板已写，缺少软件、数据或执行证据。
- 阻塞：说明确切原因、受影响阶段和所需输入。

阶段完成可以报告，但不得等同整个研究完成。
