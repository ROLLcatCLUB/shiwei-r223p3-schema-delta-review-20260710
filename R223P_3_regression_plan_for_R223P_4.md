# R223P-3 regression plan for R223P-4

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
next_stage: 1013R_R223P_4_THREE_SAMPLE_REGRESSION

## P4 目标

验证 P3 的 schema delta 是否能在三个不同课型样本中成立，并且不破坏教师默认稿阅读层。

## 必测样本

| sample | 课型侧重 | 已有依据 |
| --- | --- | --- |
| 我为文具代言 第三阶段 | 设计应用 / 生活问题解决 / 高实践密度创作 | R223M-P5 |
| 有趣的纸印 | 材料技法 / 印痕探究 / 材料实验 | R223N-P3-P1 |
| 色彩的碰撞 | 视觉语言 / 色彩感知 / 表达 | R223O-P1 |

## 必测问题

1. `unit_phase_role` 与 `practice_intensity` 是否能准确控制展开密度。
2. `practice_pattern_type` 是否能标注事件模式，而不替代教学设计。
3. 示范、小练、赏析、材料实验等条件字段是否只在需要时启用。
4. 组件触发是否都带状态，且未注册组件不进入教师默认稿。
5. 教师默认稿是否仍是成熟教案文稿，不回到字段墙。
6. review ledger 是否能完整保存模式、组件、大屏、学习单和证据链。

## P4 通过线

```text
每个样本 validator pass
每个样本教师默认稿不出现禁止字段名
每个样本 review ledger 含 primary practice_pattern_type
三样本均无文具/纸印/色彩内容互相迁移污染
至少 2/3 样本证明 unit_phase_role + practice_intensity 有实际区分度
```

## P4 决策输出

```text
A. PASS_CONTINUE_TO_R223P_5_V0_2_LOCK_CANDIDATE
B. HOLD_FOR_DELTA_REDUCTION
C. HOLD_FOR_PATTERN_REGISTRY_REWORK
```

## P4 仍然禁止

不改 UI，不改 R97B，不接 runtime/model/prompt/db，不发布 v0.2，不写回正式教案。

