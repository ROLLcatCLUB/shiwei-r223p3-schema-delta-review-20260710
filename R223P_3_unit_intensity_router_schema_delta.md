# R223P-3 unit intensity router schema delta

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: unit_router_delta_candidate_only

## 目的

不是所有美术课都应该被展开成同一种“观察-示范-小练-创作-评价”。课时需要先判断其在大单元中的位置和实践强度，再决定课堂事件展开密度。

## 候选字段

```json
{
  "unit_phase_role": "intro_understanding | technique_preparation | practice_creation | showcase_evaluation | transfer_closure | project_synthesis",
  "lesson_position_in_unit": "early | middle | late | final | standalone_unknown",
  "practice_intensity": "low | medium | high",
  "student_work_time_ratio": "low | medium | high",
  "teacher_support_density": "light | normal | heavy",
  "performance_task_link": "...",
  "stage_evidence_link": "..."
}
```

## 路由影响

| unit_phase_role | practice_intensity 建议 | 系统应加重 | 系统应减轻 |
| --- | --- | --- | --- |
| intro_understanding | low/medium | 观察、赏析、问题建立 | 大量创作支架 |
| technique_preparation | medium | 示范、小练、材料实验 | 复杂表现性任务 |
| practice_creation | high | 巡视观察、过程证据、补救策略 | 长篇导入讲解 |
| showcase_evaluation | medium | 展示评价、作品说明、二改建议 | 新技法讲授 |
| transfer_closure | low/medium | 方法总结、迁移任务 | 重创作流程 |
| project_synthesis | high | 项目进度、分工、证据链 | 单点知识讲解 |

## 与 practice_pattern_type 的关系

`unit_phase_role` 决定“本课要展开到什么程度”；`practice_pattern_type` 决定“本环节采用哪类美术课堂实践模式”。两者不能互相替代。

## P3 边界

本文件只提出 schema delta 候选，不写入正式数据库，不改 v0.1 schema，不改变现有教师稿。

