# R223P-3 字段过载风险审查

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: overload_review

## 最大风险

P2 模式库很有价值，但如果 P3 把所有字段都变成 required，教师稿会重新退化成字段墙，validator 也会鼓励生成器“填满字段”而不是“生成好课”。

## required / optional / ledger-only 建议

| field_id | 建议 |
| --- | --- |
| practice_pattern_type | core candidate, P4 回归时可要求每个事件有 primary pattern |
| unit_phase_role | lesson level recommended, event level optional |
| practice_intensity | lesson level recommended |
| demonstration_type | conditional optional，仅 teacher_demonstration 激活 |
| micro_practice_type | conditional optional，仅 micro_practice 激活 |
| appreciation_scaffold_type | conditional optional，仅 artwork_appreciation 激活 |
| aesthetic_language_focus | recommended for visual language lessons |
| technique_breakthrough_point | recommended when demonstration/technique preparation exists |
| material_safety_or_management | required when material/tool/safety risk exists |
| checkpoint | required when practice_creation is high intensity |
| process_evidence | required when practice_creation or micro_practice exists |
| component_trigger_status | review ledger only |
| screen_trigger | review ledger by default, naturalized in teacher稿 |
| learning_sheet_fields | review ledger by default, naturalized in evidence section |

## 只适合 review ledger 的字段

```text
component_trigger_status
validator_rule_id
source_status
activated_adapter_fields
primary_pattern
secondary_patterns
```

## 可能未来跨学科复用的字段

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
process_evidence
checkpoint
branch_to
exit_condition
```

## 只属于美术适配层的字段

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
artwork_reference_type
aesthetic_language_focus
technique_breakthrough_point
material_safety_or_management
student_practice_output
transition_to_formal_creation
```

## 控制策略

1. P3 只做 delta，不发布。
2. P4 必须用《我为文具代言》《有趣的纸印》《色彩的碰撞》回归。
3. 回归时同时看 review ledger 和教师默认稿。
4. 若教师默认稿出现字段名或组件货架，字段进入 v0.2 的资格暂停。

