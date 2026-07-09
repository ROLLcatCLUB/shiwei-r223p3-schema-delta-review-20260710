# R223P-3 component trigger status policy

stage_id: 1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA  
status: component_status_policy_only

## 为什么需要状态

R223P-2 中出现的 `component_trigger_candidates` 有些来自 R222D-P1 组件库，有些只是课堂 surface 候选。P3 不得把这些候选名默认当成可执行组件。

## 组件触发状态

| status | 含义 | 是否可执行 |
| --- | --- | --- |
| already_registered | 已在 R222D/R222D-P1 注册并审核过的课堂组件 | P3 仍不可执行，只能标注 |
| candidate_from_R222D_pool | 与 R222D 候选池相近，但命名或边界需对齐 | 不可执行 |
| new_surface_candidate | 新 surface 候选，需要后续组件库治理 | 不可执行 |
| unregistered_do_not_execute | 未注册，不得执行，不得进入 UI | 不可执行 |

## P2 候选组件状态初判

| component_trigger_candidate | status | 备注 |
| --- | --- | --- |
| circle_and_annotate | already_registered | R222D-P1 已加固 |
| compare_two_images | already_registered | R222D-P1 已加固 |
| right_wrong_compare | candidate_from_R222D_pool | 属于 compare 变体，需治理上下位关系 |
| before_after_compare | candidate_from_R222D_pool | 属于修改前后对比变体 |
| technique_step_demo | already_registered | 对应技法拆解/步骤示范 |
| gallery_walk | already_registered | 对应作品画廊/走看评价 |
| timer | candidate_from_R222D_pool | 课堂控制 surface，需确认是否作为组件 |
| observe_and_mark | new_surface_candidate | 可与圈一圈合并或作为观察标注变体 |
| artwork_annotation | new_surface_candidate | 可作为圈一圈/作品赏析变体 |
| demo_pause_card | new_surface_candidate | 示范暂停点 surface 候选 |
| micro_practice_submit | new_surface_candidate | 小练提交 surface 候选 |
| material_test_record | new_surface_candidate | 材料实验记录 surface 候选 |
| idea_cards | new_surface_candidate | 构思卡 surface 候选 |
| layout_dragger | new_surface_candidate | 版式拖拽 surface 候选 |
| midway_projection_review | new_surface_candidate | 中途投屏评议 surface 候选 |
| process_photo_capture | already_registered | 对应拍照提交/过程证据 |
| peer_review_board | new_surface_candidate | 同伴评价板候选 |
| transfer_task_prompt | new_surface_candidate | 迁移任务提示候选 |

## 禁止

- P3 不改 R222D 组件库。
- P3 不新增真实组件。
- P3 不接大屏、学习单或课堂 runtime。
- 未注册组件不得出现在教师默认稿中。

