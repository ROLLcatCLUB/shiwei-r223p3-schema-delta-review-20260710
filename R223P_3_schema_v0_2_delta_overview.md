# R223P-3 classroom_event_schema v0.2 delta overview

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: schema_delta_candidate_only  
decision: PASS_CONTINUE_TO_R223P_4_THREE_SAMPLE_REGRESSION  

## 定位

R223P-3 只提出 `classroom_event_schema v0.2` 的候选字段增量，不覆盖 R223M-P5 已锁定的 v0.1 候选标准，也不发布 v0.2。

本轮依据：

- R223M-P5 `classroom_event_schema v0.1 lock candidate`
- R223P-1 深度研究接收与缺口分析
- R223P-2 美术课堂实践模式候选注册表

## 本轮解决的问题

v0.1 已经能表达课堂事件展开、学生反应、教师追问、补救策略、大屏/组件/学习单/证据触发等基本链路。但 v0.1 对以下内容表达不足：

1. 本课在大单元中的实践强度与课时角色。
2. 美术课堂特有的观察、赏析、示范、小练、材料实验、创作推进等实践模式。
3. 示范类型、前置小练习类型、赏析支架类型、美术语言焦点等适配层字段。
4. 组件触发候选是否已注册、是否只可作为新 surface 候选。
5. 教师默认稿与 review ledger 的字段可见性边界。

## 字段分层原则

```text
general_pedagogy_core
通用教学推理底座，可在未来科学、语文、数学等学科中复用。

art_subject_adapter
美术学科实践模式适配层，只服务美术课堂展开，不等同于通用教学底座。

review_ledger_only
进入结构化审核层、回归验证和下游生成依据，不直接暴露给教师默认稿。
```

## 不发布 v0.2 的原因

这些字段会影响教师稿生成、review ledger、大屏触发、组件调用、学习单生成、评价证据链和 validator。P3 只能提出候选 delta，必须经过 P4 三样本回归后，才允许讨论 v0.2 发布。

## 当前边界

```text
schema_v0_2_published = false
R223M_P5_schema_modified = false
existing_teacher_drafts_modified = false
R222D_component_library_modified = false
formal_ui = false
R97B_modified = false
runtime_connected = false
provider_model_connected = false
prompt_modified = false
database_written = false
formal_apply = false
```

