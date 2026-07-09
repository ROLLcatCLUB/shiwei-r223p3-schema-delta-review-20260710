# R223P-3 candidate validator rules

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: candidate_validator_rules_only

## P3 validator 只验证 delta 包

本轮 validator 不验证真实教案生成质量，不验证 UI，不验证 runtime。它只检查：

1. 产物文件完整。
2. `schema_v0_2_published=false`。
3. general_pedagogy_core 与 art_subject_adapter 字段分层存在。
4. 启用规则完整。
5. teacher default 可见性边界存在。
6. component trigger status policy 存在。
7. 字段过载审查存在。
8. P4 三样本回归计划存在。

## 未来 P4 回归 validator 候选规则

P4 可在三样本回归中验证：

| rule_id | 规则 |
| --- | --- |
| P4-GEN-001 | 每个课例至少有 lesson-level `unit_phase_role` 与 `practice_intensity` 候选值 |
| P4-ART-001 | 每个课堂事件最多 1 个 primary `practice_pattern_type`，可有 secondary patterns |
| P4-ART-002 | `teacher_demonstration` 事件必须接 `micro_practice_type` 或 `transition_to_formal_creation` |
| P4-ART-003 | `micro_practice` 事件必须有 `student_practice_output` |
| P4-ART-004 | `material_experiment` 事件必须有材料结论或安全管理字段 |
| P4-VIEW-001 | 教师默认稿不得出现字段名 `practice_pattern_type` |
| P4-VIEW-002 | 教师默认稿不得出现未注册组件名 |
| P4-COMP-001 | 所有组件触发候选必须带状态 |
| P4-RISK-001 | 字段增量不得造成教师稿回到卡片墙或字段墙 |

## 决策规则

P3 本地通过后，只允许进入：

```text
PASS_CONTINUE_TO_R223P_4_THREE_SAMPLE_REGRESSION
```

P3 不能发布：

```text
R223M_STANDARD_V0_2
```

