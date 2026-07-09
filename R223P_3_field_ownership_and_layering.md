# R223P-3 字段归属与分层

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: candidate_layering_only

## 一、general_pedagogy_core

这些字段描述“课时在单元中的责任、实践强度、过程证据、检查点和分支条件”。它们可以在未来科学、语文、数学等学科中复用，但 P3 不把它们发布为正式 required 字段。

| field_id | 作用 | required 建议 | 教师默认稿 |
| --- | --- | --- | --- |
| unit_phase_role | 标注课时属于导入理解、技法准备、实践创作、展示评价、迁移收束等角色 | lesson level recommended | 可自然写进课时定位 |
| lesson_position_in_unit | 标注 early/middle/late/final | recommended | 可写成本课在单元中的位置 |
| practice_intensity | 标注实践密度 low/medium/high | recommended | 不显字段名，只影响展开密度 |
| student_work_time_ratio | 学生实操时间占比 | optional | 不显示 |
| teacher_support_density | 教师巡视、支架、补救密度 | optional | 自然化为教师观察与辅导重点 |
| performance_task_link | 单元表现性任务链接 | conditional | 写进评价或单元位置 |
| stage_evidence_link | 阶段证据链接 | recommended | 写进评价证据 |
| process_evidence | 过程证据 | conditional | 写成“至少留下……” |
| checkpoint | 中途检查点 | conditional | 写成巡视观察点 |
| branch_to | 分支去向 | optional | 默认隐藏 |
| exit_condition | 进入下一环节条件 | recommended | 写成过渡句 |

## 二、art_subject_adapter

这些字段只属于美术学科实践模式适配层。它们不能冒充通用教学底座，也不能直接在教师默认稿中显示字段名。

| field_id | 作用 | 激活条件 | 教师默认稿 |
| --- | --- | --- | --- |
| practice_pattern_type | 标注课堂事件属于哪类美术实践模式 | 核心候选字段 | 禁止显示字段名 |
| demonstration_type | 示范类型 | teacher_demonstration | 禁止显示字段名 |
| micro_practice_type | 前置小练习类型 | micro_practice | 禁止显示字段名 |
| appreciation_scaffold_type | 赏析支架类型 | artwork_appreciation | 禁止显示字段名 |
| artwork_reference_type | 作品资源类型 | artwork_appreciation 或 comparison_judgment | 自然写作资源描述 |
| aesthetic_language_focus | 美术语言焦点 | visual/color/composition/appreciation lessons | 自然进入追问与评价 |
| technique_breakthrough_point | 技法突破点 | technique_preparation/practice_creation | 自然写作示范重点 |
| material_safety_or_management | 材料安全/管理 | material_experiment 或工具材料风险 | 写作课堂提醒 |
| student_practice_output | 学生小练输出 | micro_practice | 写作任务产物 |
| transition_to_formal_creation | 小练到正式创作的过渡 | micro_practice/teacher_demonstration | 写作过渡语 |

## 三、review_ledger_only

以下内容默认只能进入 review ledger 或生成依据层：

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
component_trigger
component_trigger_status
screen_trigger
learning_sheet_fields
source_anchor
schema_delta_reason
validator_rule_id
```

## 四、禁止事项

- 不把 art_subject_adapter 字段推成所有学科通用字段。
- 不要求 v0.1 历史事件回填全部字段。
- 不在教师默认稿中暴露字段名。
- 不因为 P2 出现候选组件名就修改 R222D 组件库。

