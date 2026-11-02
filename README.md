# Weixuan Empirical Workflow

**从研究问题到可复现结果的经济学实证技能包。**

中文协作 · Stata 默认 · R/Python 可选 · 识别优先 · 全程追溯

这是一个可独立使用的 agent skill：研究设计、数据治理、估计、诊断、图表、写作和复现共用一份研究规格。已有项目可从任意阶段接入，无须重新跑完整流程。

## 快速开始

将整个目录复制到 Codex 的 `~/.codex/skills/weixuan-empirical-workflow/`，重启或刷新技能发现后输入：

> 使用 $weixuan-empirical-workflow，先审计我提供的项目和研究设计，再执行可行的实证步骤。中文沟通，使用 Stata；所有结果必须能从主文件复现。

也可以直接让支持文件读取的 agent 读取本目录 SKILL.md。仅支持读取 Markdown 不代表所有客户端都已验证兼容。

初始化项目（Python 3，无第三方依赖）：

```sh
python3 scripts/init_project.py /path/to/new-project
```

随后填入生成的 research-spec.json，把合法取得的数据放入 data/raw，由 agent 按技能完成具体分析。初始化器不会生成假回归结果，也不会替你选择识别策略。

## 工作流

研究问题 → 规格与识别 → 数据审计 → 分析样本 → 主估计 → 识别诊断 → 针对性扩展 → 图表与文字 → 全新会话复现。

| 模式 | 输入 | 主要交付 |
|---|---|---|
| design | 问题、政策背景、数据线索 | estimand、设计备忘录、威胁清单 |
| audit | 现有代码、数据字典、日志 | 数据和识别问题、修复优先级 |
| run | 明确规格和可用数据 | 可执行项目、估计结果、审计记录 |
| revise | 审稿意见、现有结果 | 意见—改动—证据对照表 |
| reproduce | 完整项目与运行环境 | 独立重跑、差异解释、复现报告 |

## 默认定制

中文解释、英文代码变量、Stata 优先、面向经济学论文、原始数据只读。上述是可修改初始设置；研究领域、期刊、样本口径、识别策略和计算资源均不预设。见 templates/profile.json。

## 文件导航

- [技能入口](SKILL.md)：agent 执行规则与阶段门槛。
- [方法路由](references/methods.md)：OLS/FE、DiD、IV、RDD、合成控制和实验。
- [数据与复现](references/reproducibility.md)：合并、缺失、版本、日志和复跑。
- [交付规范](references/delivery.md)：图表、文字、审计与完成判定。
- [来源及取舍](references/sources.md)：参考仓库、吸收内容、删除规则与证据范围。
- [验收案例](examples/acceptance.md)：用真实失败模式检验 agent 行为。

## 验证与边界

初始化器和技能结构经过本地检查；没有真实研究数据，因此不声称已完成 Stata/R/Python 计量端到端验证。不承诺显著结果、因果识别成立或期刊录用。运行分析需要相应软件和方法包；发现依赖缺失时报告环境需求，不能把未执行的代码描述为成功结果。

v1.0.0 · 2026-11-02。发布前应按实际研究项目补充运行证据。仓库来源仅作设计参考，本包不捆绑外部代码或数据。
