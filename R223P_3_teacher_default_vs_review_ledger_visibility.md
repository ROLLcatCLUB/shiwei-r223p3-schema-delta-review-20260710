# R223P-3 teacher default vs review ledger visibility

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: visibility_policy_candidate

## 原则

教师默认稿是成熟教案文稿，不是字段墙。review ledger 是结构化审核层，负责保存模式、组件、大屏、学习单、证据、来源和规则。

## 教师默认稿禁止直接显示

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
component_trigger
component_trigger_status
screen_trigger
learning_sheet_fields
validator_rule_id
source_status
```

## 教师默认稿允许自然化呈现

| 结构字段 | 教师稿自然表达 |
| --- | --- |
| unit_phase_role | 本课在单元中承担…… |
| practice_intensity | 本节课以观察/小练/创作为主 |
| checkpoint | 巡视时重点看…… |
| process_evidence | 至少留下…… |
| aesthetic_language_focus | 引导学生关注冷暖、明暗、边缘、肌理等 |
| technique_breakthrough_point | 示范时只抓…… |
| transition_to_formal_creation | 完成小练后，再把方法用到正式作品中 |

## review ledger 必须保留

review ledger 中应完整保存：

- event_id
- practice_pattern_type
- unit_phase_role
- practice_intensity
- activated_adapter_fields
- screen_trigger
- component_trigger
- component_trigger_status
- learning_sheet_fields
- evidence_outputs
- source_anchor
- validation_rules

## 可见性判断

```text
字段能帮助老师读懂课 = 自然化进教师稿
字段只帮助系统验证/派生 = review ledger only
字段可能造成教师稿变重 = 默认隐藏
字段尚未注册为组件 = 标注状态，不执行
```

