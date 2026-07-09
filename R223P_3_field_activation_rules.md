# R223P-3 字段启用规则

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: candidate_activation_rules_only

## 核心启用规则

1. `practice_pattern_type` 是核心候选字段，但 v0.2 发布前不得强制所有历史事件回填。
2. 若事件包含 `demonstration_type`，则必须存在 `micro_practice_type` 或 `transition_to_formal_creation`。
3. 若事件包含 `appreciation_scaffold_type`，则必须存在 `observation_prompt` 和 `expected_student_responses`。
4. 若事件包含 `micro_practice_type`，则必须存在 `student_practice_output` 和 `transition_to_formal_creation`。
5. 若事件属于 `material_experiment`，则必须存在 `material_safety_or_management` 或 `material_test_conclusion`。
6. 若 `unit_phase_role=practice_creation`，则必须存在 `checkpoint` 或 `process_evidence`。
7. 若事件属于 `showcase_evaluation`，则必须存在 `evidence_outputs` 或 `student_art_statement`。
8. 每个 lesson-level event 应声明 `unit_phase_role` 和 `practice_intensity`，但 P3 只作为候选 delta，不正式发布。

## pattern 触发建议

| practice_pattern_type | 建议触发字段 | 不能缺少 |
| --- | --- | --- |
| observation_discovery | aesthetic_language_focus, observation_prompt | expected_student_responses |
| comparison_judgment | comparison_dimension, evidence_outputs | 判断依据 |
| artwork_appreciation | appreciation_scaffold_type, artwork_reference_type | observation_prompt |
| teacher_demonstration | demonstration_type, technique_breakthrough_point | transition_to_formal_creation 或 micro_practice_type |
| micro_practice | micro_practice_type, student_practice_output | transition_to_formal_creation |
| material_experiment | material_safety_or_management, material_test_conclusion | evidence_outputs |
| idea_generation | idea_prompt, student_practice_output | selection_reason |
| creation_progression | checkpoint, process_evidence | teacher_support_density |
| showcase_evaluation | evidence_outputs, student_art_statement | assessment_alignment |
| closure_transfer | performance_task_link, stage_evidence_link | exit_condition |

## 教师默认稿处理

启用字段只影响生成依据和 review ledger，不直接显示字段名。例如：

```text
practice_pattern_type = material_experiment
```

教师默认稿应写成：

```text
学生先用小纸片试一试材料效果，再根据试印结果选择更适合的纸材。
```

而不是写成：

```text
本环节实践模式为 material_experiment。
```

