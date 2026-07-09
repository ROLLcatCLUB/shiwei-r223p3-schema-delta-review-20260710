import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223P_3_schema_v0_2_delta_overview.md",
    "R223P_3_classroom_event_schema_v0_2_delta.json",
    "R223P_3_field_ownership_and_layering.md",
    "R223P_3_field_activation_rules.md",
    "R223P_3_teacher_default_vs_review_ledger_visibility.md",
    "R223P_3_candidate_validator_rules.md",
    "R223P_3_component_trigger_status_policy.md",
    "R223P_3_unit_intensity_router_schema_delta.md",
    "R223P_3_risk_of_field_overload_review.md",
    "R223P_3_regression_plan_for_R223P_4.md",
    "R223P_3_decision_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]

GENERAL_FIELDS = [
    "unit_phase_role",
    "lesson_position_in_unit",
    "practice_intensity",
    "student_work_time_ratio",
    "teacher_support_density",
    "performance_task_link",
    "stage_evidence_link",
    "process_evidence",
    "checkpoint",
    "branch_to",
    "exit_condition",
]

ART_FIELDS = [
    "practice_pattern_type",
    "demonstration_type",
    "micro_practice_type",
    "appreciation_scaffold_type",
    "artwork_reference_type",
    "aesthetic_language_focus",
    "technique_breakthrough_point",
    "material_safety_or_management",
    "student_practice_output",
    "transition_to_formal_creation",
]

REQUIRED_PATTERNS = [
    "observation_discovery",
    "comparison_judgment",
    "artwork_appreciation",
    "teacher_demonstration",
    "micro_practice",
    "material_experiment",
    "idea_generation",
    "creation_progression",
    "showcase_evaluation",
    "closure_transfer",
]

FORBIDDEN_TRUE_FLAGS = [
    "schema_v0_2_published",
    "r223m_p5_schema_modified",
    "existing_teacher_drafts_modified",
    "r222d_component_library_modified",
    "formal_ui",
    "r97b_modified",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "formal_apply",
]


def load_json(name):
    with (ROOT / name).open("r", encoding="utf-8") as f:
        return json.load(f)


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def add(checks, name, passed, detail=None):
    item = {"check": name, "passed": bool(passed)}
    if detail is not None:
        item["detail"] = detail
    checks.append(item)


def main():
    checks = []

    for name in REQUIRED_FILES:
        add(checks, f"required_file:{name}", (ROOT / name).exists())

    manifest = load_json("PACKAGE_MANIFEST.json")
    delta = load_json("R223P_3_classroom_event_schema_v0_2_delta.json")

    add(checks, "manifest_stage_id", manifest.get("stage_id") == "1013R_R223P_3_CLASSROOM_EVENT_SCHEMA_V0_2_DELTA")
    add(checks, "decision", delta.get("decision") == "PASS_CONTINUE_TO_R223P_4_THREE_SAMPLE_REGRESSION")

    for flag in FORBIDDEN_TRUE_FLAGS:
        add(checks, f"boundary_false:{flag}", manifest.get(flag) is False)

    layers = delta.get("field_layers", {})
    general = layers.get("general_pedagogy_core", [])
    art = layers.get("art_subject_adapter", [])
    general_ids = {field.get("field_id") for field in general}
    art_ids = {field.get("field_id") for field in art}

    for field_id in GENERAL_FIELDS:
        add(checks, f"general_field:{field_id}", field_id in general_ids)

    for field_id in ART_FIELDS:
        add(checks, f"art_field:{field_id}", field_id in art_ids)

    practice_field = next((field for field in art if field.get("field_id") == "practice_pattern_type"), {})
    for pattern_id in REQUIRED_PATTERNS:
        add(checks, f"practice_pattern_value:{pattern_id}", pattern_id in practice_field.get("candidate_values", []))

    activation_rules = delta.get("activation_rules", [])
    for term in [
        "demonstration_type",
        "micro_practice_type",
        "appreciation_scaffold_type",
        "material_experiment",
        "practice_creation",
        "showcase_evaluation",
        "unit_phase_role",
        "practice_intensity",
    ]:
        add(checks, f"activation_rule_mentions:{term}", any(term in rule for rule in activation_rules))

    component_policy = delta.get("component_trigger_status_policy", {})
    for status in [
        "already_registered",
        "candidate_from_R222D_pool",
        "new_surface_candidate",
        "unregistered_do_not_execute",
    ]:
        add(checks, f"component_status:{status}", status in component_policy.get("allowed_statuses", []))
    add(checks, "component_formal_execution_false", component_policy.get("formal_execution_allowed") is False)

    visibility = read_text("R223P_3_teacher_default_vs_review_ledger_visibility.md")
    for hidden_term in [
        "practice_pattern_type",
        "demonstration_type",
        "micro_practice_type",
        "component_trigger",
        "review ledger",
    ]:
        add(checks, f"visibility_mentions:{hidden_term}", hidden_term in visibility)

    overload = read_text("R223P_3_risk_of_field_overload_review.md")
    for term in ["required", "optional", "review ledger", "字段墙"]:
        add(checks, f"overload_mentions:{term}", term in overload)

    regression = read_text("R223P_3_regression_plan_for_R223P_4.md")
    for sample in ["我为文具代言", "有趣的纸印", "色彩的碰撞"]:
        add(checks, f"regression_sample:{sample}", sample in regression)

    forbidden_published = read_text("R223P_3_decision_report.md")
    add(checks, "not_published_report", "NOT_PUBLISHED" in forbidden_published)

    failures = [check for check in checks if not check["passed"]]
    result = {
        "passed": not failures,
        "check_count": len(checks),
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223P_4_THREE_SAMPLE_REGRESSION" if not failures else "HOLD_FOR_SCHEMA_DELTA_HARDENING",
        "checks": checks,
    }
    (ROOT / "validate_1013R_R223P_3_schema_delta_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({k: result[k] for k in ["passed", "check_count", "failed", "decision"]}, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
