# 来源、筛选与原创边界

检索日期：2026-11-02。使用 GitHub 仓库公开页面和搜索摘要进行定向筛选，另检查本地 stata-empirical-workflow 与 r-econometrics 的技能内容。未做全GitHub普查、逐仓库代码审计、固定commit归档或外部技能运行对比。以下是架构参考，不构成质量背书。

| 公开来源 | 本包吸收的设计方向 | 本包的取舍 |
|---|---|---|
| [EconAgentSkills](https://github.com/JonasWeinert/EconAgentSkills) | 数据—分析—写作贯通及方法分流 | 独立组织方法说明，不依赖整套外部skills |
| [econ-research-workflow](https://github.com/tsdfs930514/econ-research-workflow) | 可复现项目与质量检查 | 保留阶段门槛，不默认多agent或强制跨语言重复估计 |
| [applied-micro-skills](https://github.com/kennethkhoocy/applied-micro-skills) | 复现审计与事件研究关注点 | 根据研究问题启用模块，不堆叠平台依赖 |
| [stata-skill](https://github.com/dylantmoore/stata-skill) | 软件语法与领域方法分离 | 运行时检查具体帮助，不把命令名当识别策略 |
| [Skills-research](https://github.com/graceveryear/Skills-research) | 端到端产物意识 | 不强制固定列数、机制或异质性分析 |

本地技能对照发现的改进点：不把第一阶段F>10当通用充分条件；不一律聚类到单一层级；不因少量研究规格缺失就停止一切独立工作；把依赖检查和已授权安装区分开。

## 方法权威资料入口

执行时按问题阅读原文或官方文档，不仅依赖技能摘要：

- [DIME Analytics](https://worldbank.github.io/dime-data-handbook/)：数据管理与可复现研究。
- [did 官方文档](https://bcallaway11.github.io/did/)：分期处理和group-time ATT。
- [fixest 官方文档](https://lrberge.github.io/fixest/)：固定效应、推断和事件研究实现。
- [RD Packages](https://rdpackages.github.io/)：RD估计与诊断软件。

所有说明为独立编写，没有复制或捆绑上述仓库源码。未来引入第三方代码须逐文件核对许可证、保留声明并固定来源版本；当前不擅自替用户选择对外开源许可证。
